import streamlit as st

# Function to convert between units
def convert_units(value, unit_from, unit_to):
    # Dictionary to store conversion factors and functions
    conversions = {
        # Length conversions
        "meters_kilometers": 0.001, 
        "kilometers_meters": 1000,
        "meters_feet": 3.28084,
        "feet_meters": 0.3048,
        "inches_centimeters": 2.54,
        "centimeters_inches": 0.393701,
        
        # Weight conversions
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
        "pounds_kilograms": 0.453592,
        "kilograms_pounds": 2.20462,
        "ounces_grams": 28.3495,
        "grams_ounces": 0.035274,
        
        # Temperature conversions (using lambda functions)
        "celsius_fahrenheit": lambda c: (c * 9/5) + 32,
        "fahrenheit_celsius": lambda f: (f - 32) * 5/9,
    }
    
    key = f"{unit_from}_{unit_to}"  # Generate a key for lookup
    
    if key in conversions:
        conversion = conversions[key]
        return conversion(value) if callable(conversion) else value * conversion  # Apply conversion
    elif unit_from == unit_to:
        return value  # If same units, return original value
    else:
        return None  # Return None for unsupported conversions

# Streamlit UI
st.title("Assignment 1: Unit Converter App")

# Category selection
category = st.selectbox("Select a category:", ["Length", "Weight", "Temperature"])

# Define unit options based on category
unit_options = {
    "Length": ["meters", "kilometers", "feet", "inches", "centimeters"],
    "Weight": ["grams", "kilograms", "pounds", "ounces"],
    "Temperature": ["celsius", "fahrenheit"],
}

# User input for value
value = st.number_input("Enter the value to convert:", min_value=0.0, step=0.1)

# Dropdowns for unit selection
unit_from = st.selectbox("Convert from:", unit_options[category])
unit_to = st.selectbox("Convert to:", unit_options[category])

# Convert button
display_result = st.button("Convert")

if display_result:
    result = convert_units(value, unit_from, unit_to)
    
    if result is not None:
        st.success(f"✅ {value} {unit_from} = {result:.4f} {unit_to}")  # Format to 4 decimal places
    else:
        st.error("⚠️ Conversion not supported.")
