import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001, 
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
    }

    key = f"{unit_from}_{unit_to}"  # Generate a unique key based on the input & output

    if key in conversions:
        conversion = conversions[key]  # Use correct conversion factor
        return value * conversion  # Multiply with conversion factor
    elif unit_from == unit_to:
        return value  # If same units, return original value
    else:
        return "Conversion not supported"

# Streamlit App
st.title("Unit Converter")

value = st.number_input("Enter the value to convert:", min_value=1.0, step=1.0)

unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])  # Fixed typo: "kilogram" -> "kilograms"

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    
    if isinstance(result, (int, float)):
        st.success(f"✅ {value} {unit_from} = {result} {unit_to}")
    else:
        st.error("⚠️ Conversion not supported.")
