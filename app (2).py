import streamlit as st
import pandas as pd
import joblib

# Load the trained model
# Assuming the model is saved as 'student_grade_model.joblib' in the current directory
model = joblib.load('student_grade_model.joblib')

st.header("Student Grade Prediction App")

student_id = st.text_input(
    "Student ID",
    placeholder="Enter student ID"
)

weekly_self_study_hours = st.number_input(
    "Weekly Self-Study Hours",
    min_value=0.0,
    max_value=168.0,
    value=10.0,
    step=0.5
)

attendance_percentage = st.number_input(
    "Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=80.0,
    step=1.0
)

class_participation = st.number_input(
    "Class Participation",
    min_value=0.0,
    max_value=100.0,
    value=70.0,
    step=1.0
)

total_score = st.number_input(
    "Total Assessment Score",
    min_value=0.0,
    max_value=100.0,
    value=70.0,
    step=1.0
)

# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("Predict Student Grade", type="primary"):

    # Create input dataframe
    input_data = pd.DataFrame({
        "weekly_self_study_hours": [weekly_self_study_hours],
        "attendance_percentage": [attendance_percentage],
        "class_participation": [class_participation],
        "total_score": [total_score]
    })

    # Generate prediction
    prediction = model.predict(input_data)[0]

    # Display prediction
    st.subheader("Prediction Result")

    st.metric(
        label="Predicted Grade",
        value=f"{prediction:.2f}"
    )

    # --------------------------------------------------
    # Optional interpretation
    # --------------------------------------------------

    if prediction >= 80:
        st.success("Excellent predicted academic performance.")
    elif prediction >= 70:
        st.success("Good predicted academic performance.")
    elif prediction >= 60:
        st.info("Moderate predicted academic performance.")
    elif prediction >= 50:
        st.warning("The student may require additional academic support.")
    else:
        st.error("The student may be at high risk of poor academic performance.")

    # Display input information
    st.subheader("Student Information")

    result = input_data.copy()
    result["predicted_grade"] = prediction

    st.dataframe(result, use_container_width=True)
