
import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("ev_battery_model.pkl","rb"))

st.title("EV Battery Quality Prediction")

Ambient_Temp_C = st.number_input("Ambient Temperature")
Anode_Overhang_mm = st.number_input("Anode Overhang")
Electrolyte_Volume_ml = st.number_input("Electrolyte Volume")
Internal_Resistance_mOhm = st.number_input("Internal Resistance")
Capacity_mAh = st.number_input("Capacity")
Retention_50Cycle_Pct = st.number_input("Retention")

Production_Line = st.number_input("Production Line")
Shift = st.number_input("Shift")
Supplier_ID = st.number_input("Supplier_ID")

if st.button("Predict"):

    features = np.array([[Ambient_Temp_C,
                          Anode_Overhang_mm,
                          Electrolyte_Volume_ml,
                          Internal_Resistance_mOhm,
                          Capacity_mAh,
                          Retention_50Cycle_Pct,
                          Production_Line,
                          Shift,
                          Supplier]])

    prediction = model.predict(features)[0]

    grade_map = {
    0: "Grade A",
    1: "Grade B",
    2: "Scrap"
}

prediction = model.predict(features)[0]

st.success(f"Predicted QC Grade: {grade_map[prediction]}")

