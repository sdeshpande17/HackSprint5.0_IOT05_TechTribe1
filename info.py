import streamlit as st

# Hardcoded data for plant threats and information
plant_threats = {
    "Potato": {
        "Winter": {
            "Threats": ["Aphids", "Whiteflies"],
            "Information": "For optimal potato growth, aim for a relative humidity level of approximately 70-80%. Soil moisture content should ideally be maintained at 60-70% of field capacity throughout the growing season. Regarding NPK values, typical recommendations include around 100-150 kg/ha of nitrogen, 50-100 kg/ha of phosphorus, and 100-200 kg/ha of potassium, adjusted based on soil test results and specific crop requirements."
        },
        "Spring": {
            "Threats": ["Aphids", "Fruitworms"],
            "Information": "Potatoes are susceptible to aphids and fruitworms during the spring season. Proper pest management is essential to protect the plants."
        },
        # Add information for other seasons
    },
    "Tomato": {
        "Spring": {
            "Threats": ["Aphids", "Whiteflies"],
            "Information": "Tomatoes are vulnerable to aphids and whiteflies during the spring season. Implementing integrated pest management strategies can help mitigate these threats and ensure healthy plant growth."
        },
        "Summer": {
            "Threats": ["Whiteflies", "Blight"],
            "Information": "During the summer, tomatoes may face challenges from whiteflies and blight. Timely watering, proper air circulation, and disease-resistant varieties can aid in managing these issues."
        },
        # Add information for other seasons
    },
    # Add more plant entries as needed
}

# Function to provide threats and information for a given plant and season
def get_plant_info(plant_name, season):
    plant_name = plant_name.capitalize()
    season = season.capitalize()
    threats = plant_threats.get(plant_name, {}).get(season)
    if threats:
        st.write(f"Potential threats for {plant_name} in {season}: {', '.join(threats['Threats'])}")
        st.write(f"Information: {threats['Information']}")
    else:
        st.write("No information available for the provided plant and season.")

def main():
    st.title("Farmers' Handbook")

    # Take user input for plant name and season
    plant_name = st.text_input("Enter the name of the plant:", "Tomato")
    season = st.selectbox("Select the season:", ["Spring", "Summer", "Fall", "Winter"])

    # Get plant threats and display them
    if st.button("Predict Threats"):
        get_plant_info(plant_name, season)

if __name__ == "__main__":
    main()
