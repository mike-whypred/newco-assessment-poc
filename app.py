import streamlit as st

def main():
    # Questions list
    st.title("✅Dental Health Check Tool🦷")
    st.caption("A quick questionnaire to check your oral health")

    questions = [
        "Have you experienced tooth sensitivity to hot, cold, or sweet foods and drinks recently?",
        "Do your gums bleed when you brush or floss your teeth?",
        "Do you often suffer from a dry mouth, even if you are well-hydrated?",
        "Have you had any toothaches or persistent tooth pain in the past six months?",
        "Are your gums swollen, red, or tender?",
        "Do you frequently suffer from bad breath, regardless of oral hygiene practices?",
        "Have any of your teeth become loose without any apparent injury?",
        "Do you experience difficulty or discomfort when chewing food?",
        "Have you had a new cavity or required a dental filling in the last two years?",
        "Do you use tobacco products, including smoking or chewing tobacco?"
    ]

    # Initialize a dictionary to store responses
    responses = {q: False for q in questions}

    # Display all questions
    for question in questions:
        responses[question] = st.radio(question, ("Yes", "No"), key=question)

    # Submit button
    if st.button('Submit'):
        # Count 'Yes' responses
        counter = sum(1 for response in responses.values() if response == "Yes")
        # Determine risk category
        if counter > 7:
            st.error("You are in the High Risk category.")
        elif counter > 2:
            st.warning("You are in the Medium Risk category.")
        else:
            st.success("You are in the Low Risk category.")

        dentist_url = "https://portal.ada.org.au/Portal/Shared_Content/Smart-Suite/Smart-Maps/Public/Find-a-Dentist.aspx"
        if st.button("Talk to a Dentist!"):
            st.write('You are being directed to the Find A Dentist Portal!👩')
            js = f"window.open('{dentist_url}')"  # JavaScript to open a new window/tab
            st.components.v1.html(f"<script>{js}</script>", height=0)

# Run the app
if __name__ == "__main__":
    main()



# Button to talk to a dentist
    

