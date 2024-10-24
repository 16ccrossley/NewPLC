import streamlit as st
import pandas as pd
import math

# Load material data from Excel file
@st.cache
def load_material_data(file_path):
    return pd.read_excel(file_path)

# Load the material database (upload your Excel file)
file_path = 'material_data.xlsx'  # Replace with your Excel file path
material_data = load_material_data(file_path)

# Title of the app
st.title("Pressure Loss Calculator with Material Database")

# Dropdown to select material
material = st.selectbox("Select Material", material_data['Material'].unique())

# Get selected material's properties from the database
selected_material = material_data[material_data['Material'] == material].iloc[0]
power_law_constant = selected_material['Power_Law_Constant']
power_law_index = selected_material['Power_Law_Index']
specific_gravity = selected_material['Specific_Gravity']

# Display the material properties
st.write(f"Power Law Constant: {power_law_constant}")
st.write(f"Power Law Index: {power_law_index}")
st.write(f"Specific Gravity: {specific_gravity}")

# Input fields for other parameters
melt_temp = st.number_input("Melt Temperature (°C)", value=230.0, min_value=0.0, max_value=500.0, step=1.0)
fill_time = st.number_input("Fill Time (s)", value=2.0, step=0.1)
flow_length = st.number_input("Flow Length (mm)", value=100.0, step=1.0)
flow_bore_size = st.number_input("Flow Bore Size (mm)", value=4.0, step=0.1)

# Calculate shear rate (simplified)
def calculate_shear_rate(flow_bore_size, fill_time, flow_length):
    radius = flow_bore_size / 2 / 1000  # Convert bore size to meters
    volume_flow_rate = (flow_length / fill_time) * specific_gravity / 1000  # Volume flow rate in m^3/s
    shear_rate = (4 * volume_flow_rate) / (math.pi * radius ** 3)  # Shear rate in 1/s
    return shear_rate

# Calculate viscosity using Power Law model
def calculate_viscosity(shear_rate, power_law_index, power_law_constant):
    viscosity = power_law_constant * (shear_rate ** (power_law_index - 1))
    return viscosity

# Calculate pressure loss
def calculate_pressure_loss(viscosity, flow_bore_size, fill_time, flow_length):
    radius = flow_bore_size / 2 / 1000  # Convert bore size to meters
    volume_flow_rate = (flow_length / fill_time) * specific_gravity / 1000  # Volume flow rate in m^3/s
    pressure_loss_pa = (8 * viscosity * volume_flow_rate * flow_length / 1000) / (math.pi * radius ** 4)  # Pressure loss in Pascals
    return pressure_loss_pa

# Perform calculations when the user clicks the button
if st.button("Calculate Pressure Loss"):
    shear_rate = calculate_shear_rate(flow_bore_size, fill_time, flow_length)
    viscosity = calculate_viscosity(shear_rate, power_law_index, power_law_constant)
    pressure_loss_pa = calculate_pressure_loss(viscosity, flow_bore_size, fill_time, flow_length)
    pressure_loss_psi = pressure_loss_pa * 0.000145038  # Convert Pascals to PSI
    st.write(f"Calculated Pressure Loss: {pressure_loss_psi:.2f} PSI")


