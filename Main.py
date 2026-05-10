import streamlit as st
import google.generativeai as genai

# Configure Gemini-Pro API (replace 'YOUR_API_KEY' with your actual key)
genai.configure(api_key="YOUR_API_KEY")

def get_diet_plan(weight, goal, preference):
    guidelines = """
    1. The diet should be structured into 3 main meals and 2 snacks.
    2. It should include a calorie breakdown and macronutrient distribution.
    3. Provide portion sizes and alternative food choices.
    4. Use simple, easy-to-follow meal ideas.
    """
    
    keywords = {
        "Weight Loss": "Caloric deficit, high-protein, fiber-rich, low-carb options, healthy fats",
        "Muscle Gain": "High-protein, calorie surplus, strength training support, complex carbs",
        "General Fitness": "Balanced diet, nutrient-dense, hydration, sustainable eating"
    }

    prompt = f"""
    Generate a personalized diet plan for a person weighing {weight} kg whose goal is {goal}.
    The diet should follow a {preference} preference. Use these guidelines: 
    {guidelines}
    
    Focus on these keywords for {goal}: {keywords[goal]}.
    """
    
    model = genai.GenerativeModel("gemini-2.0-pro-exp-02-05")  # Update model name if needed
    response = model.generate_content(prompt)
    
    return response.text if hasattr(response, "text") else response.candidates[0].content



# Streamlit UI
st.title("AI Diet Planning Chatbot")
st.header("Get a personalized diet plan!")

# User Inputs
weight = st.number_input("Enter your weight (kg)", min_value=30, max_value=200, step=1)
goal = st.selectbox("Select your goal", ["Weight Loss", "Muscle Gain", "General Fitness"])
preference = st.selectbox("Dietary Preference", ["Vegetarian", "Vegan", "Non-Vegetarian", "Keto", "Balanced"])

if st.button("Generate Diet Plan"):
    with st.spinner("Generating your diet plan..."):
        diet_plan = get_diet_plan(weight, goal, preference)
        st.subheader("Your Personalized Diet Plan:")
        st.write(diet_plan)
