import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("mental_tiredness_pipeline.pkl")

st.title("🧠 Mental Tiredness Score Prediction")

# Inputs
mood = st.selectbox("Mood", ["Happy", "Low", "Neutral"])

work_type = st.selectbox(
    "Work Type",
    ["Manual", "Office", "Remote", "Student"]
)

work_environment = st.selectbox(
    "Work Environment",
    ["Moderate Noise", "Noisy", "Quiet"]
)

number_of_decisions_made = st.number_input("Number of Decisions Made", 0)
context_switch_count = st.number_input("Context Switch Count", 0)
screen_time_min = st.number_input("Screen Time (Min)", 0)
deep_work_min = st.number_input("Deep Work (Min)", 0)

task_complexity_avg = st.slider(
    "Task Complexity",
    1.0, 10.0, 5.0
)

break_frequency = st.number_input("Break Frequency", 0)

sleep_hours = st.slider(
    "Sleep Hours",
    0.0, 12.0, 7.0
)

deep_sleep_pct = st.slider(
    "Deep Sleep %",
    0.0, 100.0, 50.0
)

hydration_l = st.slider(
    "Hydration (L)",
    0.0, 10.0, 2.0
)

noise_level_db = st.number_input(
    "Noise Level (dB)",
    0.0
)

temperature_c = st.number_input(
    "Temperature (°C)",
    0.0
)

workload_score = st.slider(
    "Workload Score",
    1.0, 10.0, 5.0
)

if st.button("Predict"):

    data = {
        'encoder__mood_Happy': 1 if mood == "Happy" else 0,
        'encoder__mood_Low': 1 if mood == "Low" else 0,
        'encoder__mood_Neutral': 1 if mood == "Neutral" else 0,

        'encoder__work_type_Manual': 1 if work_type == "Manual" else 0,
        'encoder__work_type_Office': 1 if work_type == "Office" else 0,
        'encoder__work_type_Remote': 1 if work_type == "Remote" else 0,
        'encoder__work_type_Student': 1 if work_type == "Student" else 0,

        'encoder__work_environment_Moderate Noise':
            1 if work_environment == "Moderate Noise" else 0,

        'encoder__work_environment_Noisy':
            1 if work_environment == "Noisy" else 0,

        'encoder__work_environment_Quiet':
            1 if work_environment == "Quiet" else 0,

        'remainder__number_of_decisions_made':
            number_of_decisions_made,

        'remainder__context_switch_count':
            context_switch_count,

        'remainder__screen_time_min':
            screen_time_min,

        'remainder__deep_work_min':
            deep_work_min,

        'remainder__task_complexity_avg':
            task_complexity_avg,

        'remainder__break_frequency':
            break_frequency,

        'remainder__sleep_hours':
            sleep_hours,

        'remainder__deep_sleep_pct':
            deep_sleep_pct,

        'remainder__hydration_l':
            hydration_l,

        'remainder__noise_level_db':
            noise_level_db,

        'remainder__temperature_c':
            temperature_c,

        'remainder__workload_score':
            workload_score
    }

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)

    st.success(
        f"Predicted Mental Tiredness Score: {prediction[0]:.2f}"
    )