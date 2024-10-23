import streamlit as st
import math

st.title("Hot Runner Pressure Loss Calculator")

# Display a key for average MFR values for common materials
st.subheader("Average MFR Values for Common Materials (g/10 min)")

mfr_data = {
    "HDPE": "0.5 - 10",
    "LDPE": "1 - 25",
    "PC (Polycarbonate)": "6 - 25",
    "ABS": "2 - 30",
    "PC-ABS": "10 - 20",
    "POM (Acetal)": "9 - 30",
    "PA 6 (Nylon 6)": "3 - 20",
    "PA 6/6 (Nylon 66)": "1 - 15",
    "PP (Polypropylene)": "3 - 30"
}

# Display the table of MFR values
for material, mfr_value in mfr_data.items():
    st.write(f"**{material}:** {mfr_value}")

st.subheader("Input Parameters")

# User inputs for the calculator
nozzle_diameter = st.number_input("Nozzle Flow Bore Diameter (mm)", value=4.0, step=0.1)
fill_time = st.number_input("Fill Time (s)", value=2.0, step=0.1)
shot_weight = st.number_input("Shot Weight (g)", value=50.0, step=1.0)
gate_diameter = st.number_input("Gate Diameter (mm)", value=2.0, step=0.1)
nozzle_length = st.number_input("Nozzle Length (mm)", value=50.0, step=1.0)
mold_temp = st.number_input("Mold Temperature (°C)", value=60.0, min_value=0.0, max_value=500.0, step=1.0)
cycle_time = st.number_input("Cycle Time (s)", value=30.0, step=1.0)
melt_temp = st.number_input("Melt Temperature (°C)", value=230.0, min_value=0.0, max_value=500.0, step=1.0)

# User inputs MFR directly
mfr_value = st.number_input("Enter the Material's MFR (g/10 min)", value=10.0, step=0.1)

# Calculate viscosity from MFR (empirical relationship)
n = 1  # This can be adjusted based on material properties (generally around 0.8-1.2)
k = 1000  # Constant (can be fine-tuned)
viscosity = k / (mfr_value ** n)

# Pressure loss calculation based on viscosity
def calculate_pressure_loss(eta, nozzle_diameter, fill_time, shot_weight, gate_diameter, nozzle_length, mold_temp, cycle_time):
    # Simplified pressure loss calculation (can be refined)
    radius = nozzle_diameter / 2 / 1000  # Convert to meters
    volume_flow_rate = shot_weight / (fill_time * 1000)  # Volume flow rate in m^3/s
    pressure_loss = (8 * eta * volume_flow_rate * nozzle_length / 1000) / (math.pi * radius ** 4)
    return pressure_loss

if st.button("Calculate Pressure Loss"):
    pressure_loss = calculate_pressure_loss(viscosity, nozzle_diameter, fill_time, shot_weight, gate_diameter, nozzle_length, mold_temp, cycle_time)
    st.write(f"Calculated Pressure Loss: {pressure_loss:.2f} Pa")
