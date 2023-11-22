import streamlit as st
import random

class WorkoutRecommendationSystem:
    def __init__(self, user_profile):
        self.user_profile = user_profile

    def suggest_diet(self):
        if "Weight Loss" in self.user_profile["Goals"]:
            return "Focus on a balanced diet with a slight caloric deficit. Include more vegetables, lean proteins, and whole grains."
        elif "Muscle Gain" in self.user_profile["Goals"]:
            return "Consume a diet rich in protein to support muscle growth. Include sources like chicken, fish, eggs, and legumes."

def main():
    st.title("Personalized Workout Recommendation App")

    # Collect user input
    age = st.number_input("Enter your age", min_value=1, max_value=100, step=1)
    gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
    fitness_level = st.selectbox("Select your fitness level", ["Beginner", "Intermediate", "Advanced"])
    goals = st.text_input("Enter your fitness goals, separated by commas (e.g., Weight Loss, Muscle Gain)")

    # Process user input
    user_profile = {
        "Age": age,
        "Gender": gender,
        "Fitness_Level": fitness_level,
        "Goals": goals.split(","),
    }

    recommendation_system = WorkoutRecommendationSystem(user_profile)
    workout_plan = recommendation_system.generate_workout_plan()
    diet_recommendation = recommendation_system.suggest_diet()

    st.header("Diet Recommendation:")
    st.write(diet_recommendation)

if __name__ == "__main__":
    main()