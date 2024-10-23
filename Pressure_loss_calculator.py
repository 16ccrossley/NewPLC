import streamlit as st
import math

st.title("Hot Runner Pressure Loss Calculator (Cross-WLF Model)")

# Input parameters for the user
nozzle_diameter = st.number_input("Nozzle Flow Bore Diameter (mm)", value=4.0, step=0.1)
fill_time = st.number_input("Fill Time (s)", value=2.0, step=0.1)
shot_weight = st.number_input("Shot Weight (g)", value=50.0, step=1.0)
gate_diameter = st.number_input("Gate Diameter (mm)", value=2.0, step=0.1)
nozzle_length = st.number_input("Nozzle Length (mm)", value=50.0, step=1.0)
mold_temp = st.number_input("Mold Temperature (°C)", value=60.0, min_value=0.0, max_value=500.0, step=1.0)
cycle_time = st.number_input("Cycle Time (s)", value=30.0, step=1.0)
melt_temp = st.number_input("Melt Temperature (°C)", value=230.0, min_value=0.0, max_value=500.0, step=1.0)

# Material constants for Cross-WLF model (example for HDPE)
D1 = st.number_input("D1 (Material Constant)", value=6.0)
D2 = st.number_input("D2 (Material Constant)", value=200.0)
D3 = st.number_input("D3 (Material Constant)", value=0.025)
T_ref = st.number_input("Reference Temperature (°C)", value=100.0)
n = st.number_input("Shear-Thinning Index", value=0.4)
gamma_dot_0 = st.number_input("Reference Shear Rate (1/s)", value=1.0)

# Calculate the zero-shear viscosity using the Cross-WLF model
def calculate_zero_shear_viscosity(T, P, D1, D2, D3, T_ref):
    log_eta_0 = D1 + (D2 / (T - T_ref + D3 * P))
    eta_0 = 10 ** log_eta_0  # Zero-shear viscosity in Pa.s
    return eta_0

# Calculate viscosity using Cross-WLF
def calculate_viscosity(T, P, shear_rate, D1, D2, D3, T_ref, n, gamma_dot_0):
    eta_0 = calculate_zero_shear_viscosity(T, P, D1, D2, D3, T_ref)
    viscosity = eta_0 / (1 + (shear_rate / gamma_dot_0) ** (1 - n))
    return viscosity

# Shear rate calculation (simplified)
radius = nozzle_diameter / 2 / 1000  # Convert diameter to meters
volume_flow_rate = shot_weight / (fill_time * 1000)  # Flow rate in m^3/s
shear_rate = (4 * volume_flow_rate) / (math.pi * radius ** 3)  # Shear rate in 1/s

# Calculate pressure loss using viscosity
def calculate_pressure_loss(eta, nozzle_diameter, fill_time, shot_weight, gate_diameter, nozzle_length, mold_temp, cycle_time):
    radius = nozzle_diameter / 2 / 1000  # Convert to meters
    volume_flow_rate = shot_weight / (fill_time * 1000)  # Volume flow rate in m^3/s
    pressure_loss_pa = (8 * eta * volume_flow_rate * nozzle_length / 1000) / (math.pi * radius ** 4)  # Pressure loss in Pascals
    return pressure_loss_pa

# Get pressure (initial guess or set by user)
P = st.number_input("Pressure (Pa)", value=100000.0)  # Example value for pressure in Pa

if st.button("Calculate Pressure Loss"):
    viscosity = calculate_viscosity(melt_temp, P, shear_rate, D1, D2, D3, T_ref, n, gamma_dot_0)
    pressure_loss_pa = calculate_pressure_loss(viscosity, nozzle_diameter, fill_time, shot_weight, gate_diameter, nozzle_length, mold_temp, cycle_time)
    pressure_loss_psi = pressure_loss_pa * 0.000145038  # Convert Pascals to PSI
    st.write(f"Calculated Pressure Loss: {pressure_loss_psi:.2f} PSI")
