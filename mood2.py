import streamlit as st
import pyjokes

def mood_finder(answers):
    # Calculate mood based on answers
    score = sum(answers.values())
    
    if score < 30:
        mood = "Sad"
    elif score < 60:
        mood = "Neutral"
    else:
        mood = "Happy"
    
    return mood

def generate_joke():
    return pyjokes.get_joke()

def main():
    st.title("Mood Magic Finder App")
    st.write("DISCLAIMER: These questions have been sourced from the materials available on verywellmind.com, and they will be utilized to assess your mood.")
   
    st.write("(Rate your mood from 1 - Not at all, 5 - Very much)")
    # Dictionary to store user answers
    answers = {}

    # Ask 10 questions
    question = "How do you feel?"
    answer = st.slider(question, 1, 10)
    answers["Q1"] = answer

    question = "How calm do you feel at the moment?"
    answer = st.slider(question, 1, 10)
    answers["Q2"] = answer

    question = "How energized do you feel right now?"
    answer = st.slider(question, 1, 10)
    answers["Q3"] = answer

    question = "Rate your level of motivation currently."
    answer = st.slider(question, 1, 10)
    answers["Q4"] = answer

    question = "How would you describe your level of relaxation?"
    answer = st.slider(question, 1, 10)
    answers["Q5"] = answer

    question = "How satisfied are you with your current situation?"
    answer = st.slider(question, 1, 10)
    answers["Q6"] = answer

    question = "How optimistic are you about the future?"
    answer = st.slider(question, 1, 10)
    answers["Q7"] = answer

    question = "How would you rate your level of focus right now?"
    answer = st.slider(question, 1, 10)
    answers["Q8"] = answer

    question = "How social do you feel today?"
    answer = st.slider(question, 1, 10)
    answers["Q9"] = answer

    question = "How would you rate your overall mood?"
    answer = st.slider(question, 1, 10)
    answers["Q10"] = answer

    # ... (repeat for the other questions)

    # Button to calculate mood
    if st.button("Find My Mood"):
        mood = mood_finder(answers)

        # Customize display based on mood
        if mood == "Happy":
            st.success(f"Your mood seems to be {mood}!")
            st.balloons()  # Optional: Add balloons for extra celebration
            st.markdown(
                """<style>div.stButton > button:first-child {background-color: #4CAF50;}</style>""",
                unsafe_allow_html=True,
            )
        elif mood == "Sad":
            st.error(f"Your mood seems to be {mood}!")
            st.markdown(
                """<style>div.stButton > button:first-child {background-color: #FF5733;}</style>""",
                unsafe_allow_html=True,
            )

            # Generate and display a random joke to cheer up the user
            joke = generate_joke()
            st.write("Cheer up with a joke:")
            st.write(joke)
        else:
            st.info(f"Your mood seems to be {mood}.")

if __name__ == "__main__":
    main()
