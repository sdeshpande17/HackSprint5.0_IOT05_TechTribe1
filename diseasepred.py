import streamlit as st

def main():
    st.title("Plant Disease and possible threat Prediction")
    st.title("Appropriate step needed to reolve it  ")
    # Take user input for temperature, humidity, moisture, and chemical levels
    temperature = st.number_input("Enter temperature:", min_value=1, max_value=100, step=1)
    add_buttons("temperature", temperature)

    humidity = st.number_input("Enter humidity:", min_value=1, max_value=100, step=1)
    add_buttons("humidity", humidity)

    moisture = st.number_input("Enter moisture:", min_value=1, max_value=100, step=1)
    add_buttons("moisture", moisture)

    chemical = st.number_input("Enter chemical level:", min_value=1, max_value=100, step=1)
    add_buttons("chemical", chemical)

    if st.button("Predict"):
        predict_disease(temperature, humidity, moisture, chemical)

def add_buttons(label, value):
    st.write(f"Select range for {label}:")
    button_values = [(0, 25), (25, 50), (50, 75), (75, 100)]
    for min_val, max_val in button_values:
        if st.button(f"{min_val}-{max_val}", key=f"{label}_{min_val}_{max_val}"):
            value = min(max_val, value)
            value = max(min_val, value)

def predict_disease(temperature, humidity, moisture, chemical):
    # Hardcoded ranges for temperature, humidity, moisture, and chemical levels
    if 50 <= temperature <= 70 and 60 <= humidity <= 80 and 60 <= moisture <= 80 and 20 <= chemical <= 30:
        st.write("The plant is predicted to be healthy.")
    else:
        st.write("The plant is predicted to be diseased. Here are some remedial actions to consider:")
        st.write("- **Increase Humidity to 60%**:")
        st.write("   - Use overhead sprinklers or misting systems to increase humidity levels around the potato plants.")
        st.write("   - Install humidity sensors or meters to monitor humidity levels accurately.")

        st.write("- **Maintain Soil Moisture at 50%**:")
        st.write("   - Implement drip irrigation systems to provide consistent moisture to the potato plants while avoiding waterlogging.")
        st.write("   - Use mulch or organic matter to retain soil moisture and prevent rapid drying.")

        st.write("- **Apply Fungicides as Recommended**:")
        st.write("   - Consult with agricultural experts to select appropriate fungicides for controlling the specific disease affecting the potato plants.")
        st.write("   - Follow the recommended application rates and timing for fungicide treatments to effectively manage the disease.")

        st.write("The ideal percentage of nitrogen (N), phosphorus (P), and potassium (K) in fertilizer formulations for potatoes typically ranges around 5-10% nitrogen, 10-20% phosphorus pentoxide (P2O5), and 10-20% potassium oxide (K2O).")
        st.write(" Nitrogen is crucial for foliage growth and overall plant vigor, phosphorus supports root development and flowering, while potassium enhances disease resistance and tuber quality")
if __name__ == "__main__":
    main()
