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
    "Acetal (POM)": {"eta0":
