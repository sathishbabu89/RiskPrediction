import streamlit as st

# Page Title
st.title("Project Risk Prediction Dashboard")

# Sidebar for navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Select a Page", ["Generate Excel", "Risk Prediction"])

if page == "Generate Excel":
    # Redirect to the Generate Excel page
    st.write("### Generate Excel File for Project Metrics")
    st.write("This page allows you to generate a sample Excel file with project metrics for risk prediction.")

    # Import the Excel file generator script
    from generate_excel import generate_excel_file

    # Generate Excel file when button is clicked
    if st.button("Generate Excel File"):
        generate_excel_file()

elif page == "Risk Prediction":
    # Redirect to the Risk Prediction page
    st.write("### Upload Excel File for Risk Prediction")
    st.write("This page allows you to upload the generated Excel file and analyze risk prediction.")

    # Import the Risk Prediction script
    from predict_risk import risk_prediction

    # File uploader for Excel file
    uploaded_file = st.file_uploader("Upload Project Metrics Excel", type="xlsx")

    # When the user uploads a file, process it
    if uploaded_file is not None:
        # Predict risk for the uploaded file
        risk_prediction(uploaded_file)
