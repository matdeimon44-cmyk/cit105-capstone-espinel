import streamlit as st
from datetime import date
from database import initialize_database, load_sessions, save_sessions

st.set_page_config(
    page_title="Baseball Training Tracker",
    page_icon="⚾",
    layout="wide"
)

initialize_database()
sessions = load_sessions()

st.title("⚾ Baseball Training Tracker")
st.write("Created by Matthew Espinel")
st.success("Welcome to your baseball training dashboard!")

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a page",
    ["Add Training", "Training History", "Summary"]
)

if page == "Add Training":
    st.header("Add a New Training Session")

    with st.form("training_form"):
        training_date = st.date_input(
            "Training Date", date.today()
        )

        training_type = st.selectbox(
            "Training Type",
            ["Hitting", "Fielding", "Throwing", "Conditioning"]
        )

        duration = st.number_input(
            "Duration (minutes)",
            min_value=1,
            value=60
        )

        notes = st.text_area("Performance Notes")

        submitted = st.form_submit_button("Save Training")

        if submitted:
            new_session = {
                "date": str(training_date),
                "type": training_type,
                "duration": int(duration),
                "notes": notes
            }

            sessions.append(new_session)
            save_sessions(sessions)
            st.success("Training session saved successfully!")

elif page == "Training History":
    st.header("Training History")

    if sessions:
        selected_type = st.selectbox(
            "Filter by Training Type",
            [
                "All", "Hitting", "Fielding",
                "Throwing", "Conditioning"
            ]
        )

        filtered_sessions = sessions

        if selected_type != "All":
            filtered_sessions = [
                session for session in sessions
                if session["type"] == selected_type
            ]

        if filtered_sessions:
            st.dataframe(
                filtered_sessions,
                use_container_width=True
            )
        else:
            st.info("No sessions found for this training type.")
    else:
        st.info("No training sessions recorded yet.")

elif page == "Summary":
    st.header("Training Summary")

    total_sessions = len(sessions)
    total_minutes = sum(
        session["duration"] for session in sessions
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Training Sessions",
            total_sessions
        )

    with col2:
        st.metric(
            "Total Training Minutes",
            total_minutes
        )

    if sessions:
        st.subheader("Training by Type")

        training_counts = {}

        for session in sessions:
            training_type = session["type"]
            training_counts[training_type] = (
                training_counts.get(training_type, 0) + 1
            )

        st.bar_chart(training_counts)