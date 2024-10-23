import streamlit as st

def calculate_pressure_loss(eta0, b, T_ref, nozzle_diameter, fill_time, shot_weight, gate_diameter, nozzle_length, mold_temp, cycle_time):
    # Calculate viscosity at the injection temperature
    T_injection = T_ref + (fill_time * 0.1)  # Example adjustment for fill time
    eta = eta0 * (1 + b * (T_injection - T_ref))

    # Pressure loss calculations (simplified for demonstration)
    pressure_loss = (shot_weight * eta) / (nozzle_diameter ** 4)  # Example formula
    return pressure_loss

# Define materials and their characteristics
materials = {
    "ABS": {"eta0": 3000, "b": 0.02, "T_ref": 230},
    "ABS Glass-Filled": {"eta0": 2200, "b": 0.018, "T_ref": 230},
    "HDPE": {"eta0": 800, "b": 0.015, "T_ref": 130},
    "HDPE Glass-Filled": {"eta0": 600, "b": 0.013, "T_ref": 130},
    "LLDPE": {"eta0": 700, "b": 0.014, "T_ref": 120},
    "LLDPE Glass-Filled": {"eta0": 500, "b": 0.012, "T_ref": 120},
    "LDPE": {"eta0": 600, "b": 0.016, "T_ref": 110},
    "LDPE Glass-Filled": {"eta0": 400, "b": 0.014, "T_ref": 110},
    "Nylon (PA)": {"eta0": 1200, "b": 0.025, "T_ref": 250},
    "Nylon (PA) Glass-Filled": {"eta0": 900, "b": 0.022, "T_ref": 250},
    "Polycarbonate (PC)": {"eta0": 3500, "b": 0.03, "T_ref": 270},
    "PC Glass-Filled": {"eta0": 2800, "b": 0.028, "T_ref": 270},
    "PET": {"eta0": 2000, "b": 0.02, "T_ref": 260},
    "PET Glass-Filled": {"eta0": 1500, "b": 0.018, "T_ref": 260},
    "Polystyrene (PS)": {"eta0": 1500, "b": 0.015, "T_ref": 200},
    "PS Glass-Filled": {"eta0": 1200, "b": 0.014, "T_ref": 200},
    "Acetal (POM)": {"eta0": 1800, "b": 0.025, "T_ref": 180},
    "POM Glass-Filled": {"eta0": 1400, "b": 0.022, "T_ref": 180},
    "PBT": {"eta0": 1200, "b": 0.025, "T_ref": 220},
    "PBT Glass-Filled": {"eta0": 900, "b": 0.022, "T_ref": 220},
    "Co-Polyester": {"eta0": 2000, "b": 0.02, "T_ref": 240},
    "Co-Polyester Glass-Filled": {"eta0": 1600, "b": 0.018, "T_ref": 240},
    "Thermoplastic Elastomer": {"eta0": 1500, "b": 0.02, "T_ref": 210},
    "Thermoplastic Elastomer Glass-Filled": {"eta0": 1200, "b": 0.018, "T_ref": 210},
}

st.title("Pressure Loss Calculator for Hot Runners")

# Material selection dropdown
selected_material = st.selectbox("Select Material", list(materials.keys()))

# Get material properties based on selection
material_properties = materials[selected_material]
eta0 = material_properties["eta0"]
b = material_properties["b"]
T_ref = material_properties["T_ref"]

# Input fields for other parameters
st.header("Injection Molding Parameters")

nozzle_diameter = st.number_input("Nozzle Flow Bore Diameter (mm)", value=4.0, step=0.1)
fill_time = st.number_input("Fill Time (s)", value=2.0, step=0.1)  # Changed from injection speed to fill time
shot_weight = st.number_input("Shot Weight (g)", value=50.0, step=1.0)
gate_diameter = st.number_input("Gate Diameter (mm)", value=2.0, step=0.1)
nozzle_length = st.number_input("Nozzle Length (mm)", value=50.0, step=1.0)

# Maximum temperature inputs with validation
mold_temp = st.number_input("Mold Temperature (°C)", value=60.0, min_value=0.0, max_value=500.0, step=1.0)
cycle_time = st.number_input("Cycle Time (s)", value=30.0, step=1.0)

# Maximum melt temperature input with validation
melt_temp = st.number_input("Melt Temperature (°C)", value=230.0, min_value=0.0, max_value=500.0, step=1.0)

if st.button("Calculate Pressure Loss"):
    pressure_loss = calculate_pressure_loss(eta0, b, melt_temp, nozzle_diameter / 1000, fill_time, shot_weight, gate_diameter / 1000, nozzle_length / 1000, mold_temp, cycle_time)
    st.write(f"Calculated Pressure Loss: {pressure_loss:.2f} Pa")
