import streamlit as st

# Set the title of the dashboard
st.title("CareWise Dashboard")

# Create sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "Symptom Checker", "Contact Us"])

# Home page
if page == "Home":
    st.header("Welcome to CareWise")
    st.write("CareWise is an innovative application designed to provide users with immediate, accurate medical advice based on their symptoms.")
    st.write("Leveraging advanced AI technology, CareWise offers tailored recommendations for over-the-counter medications, potential side effects, allergy cautions, and home remedies.")

# Symptom Checker page
elif page == "Symptom Checker":
    st.header("Symptom Checker")
    st.write("Enter your symptoms below to get medical advice.")
    symptoms = st.text_area("Enter your symptoms:")
    if st.button("Check Symptoms"):
        if symptoms:
            st.write("Processing your symptoms...")  # Placeholder for symptom checking logic
        else:
            st.error("Please enter your symptoms.")

# Contact Us page
elif page == "Contact Us":
    st.header("Contact Us")
    st.write("If you have any questions or feedback, please feel free to reach out to us.")
    user_message = st.text_area("Your Message:")
    if st.button("Submit"):
        if user_message:
            st.write("Thank you for your message!")  # Placeholder for message submission logic
        else:
            st.error("Please enter a message.")
