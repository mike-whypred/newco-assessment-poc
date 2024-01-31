import streamlit as st
import pandas as pd

def run_questionnaire():
    st.title("✅Dental Lifestyle Assessment🦷")
    st.caption("A questionnaire on your oral health")

    # Load the data with the correct encoding
    data = pd.read_csv('data.csv', encoding='ISO-8859-1')  # Replace with the correct path

    # Initialize total score and recommendations string
    total_score = 0
    recommendations = ""

    # Create a form for the questionnaire
    with st.form(key='questionnaire_form'):
        # Iterate through each question
        for index, row in data.iterrows():
            question = row['question']
            yes_score = row['yes_score']
            no_score = row['no_score']
            comment = row['comments']
            qn = row['q_no']

            # Display the question with a unique key for each radio button
            answer = st.radio(f'Q{qn}. {question}', ('Yes', 'No'), key=f'question_{index}')

            # Store the score and recommendation for processing after submission
            if answer == 'Yes':
                if yes_score == 0:
                    recommendations += f"Your answer to question {index + 1} was 'Yes'. To improve your oral health, it is recommended {comment}\n\n"
            else:
                if no_score == 0:
                    recommendations += f"Your answer to question {index + 1} was 'No'. To improve your oral health, it is recommended {comment}\n\n"

        # Submit button at the end of the questionnaire
        submitted = st.form_submit_button("Submit")

    # Process and display the results after submission
    if submitted:
        # Calculate the total score
        for index, row in data.iterrows():
            answer = st.session_state[f'question_{index}']
            total_score += row['yes_score'] if answer == 'Yes' else row['no_score']

        # Display the total score and recommendations
        st.write("Your total score is:", total_score)
        with st.expander("Recommendations"):
            st.write(recommendations)

if __name__ == "__main__":
    run_questionnaire()
