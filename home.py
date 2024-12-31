import streamlit as st
from utils import input_dict 
import uuid
import json
from recommendationModels import recommendCourse
from mentorRecommendation import get_recommendations_for_new_user
 
# Inject custom CSS to style all input fields with cyan boundaries
def add_custom_css():
    st.markdown(
        """
        <style>
        /* Style for text input (e.g., name) */
        input[type="text"] {
            border: 2px solid cyan !important;
            border-radius: 5px;
            padding: 5px;
        }

        /* Style for dropdown/multiselect boxes */
        div[data-baseweb="select"] {
            border: 2px solid cyan !important;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def home_page():
    st.title("Personalized Learning Path Dashboard")
    
    st.markdown("""
    ### Welcome to the Personalized Learning Path Dashboard
    Fill in the details below to get started!
    """)

    # Input form
    with st.form("user_form"):
        # Input for Name with cyan border
        name = st.text_input("Enter your name", placeholder="Your Name")

        # Multiselect for Strengths
        strengths = st.multiselect(
            "Select your strengths:",
            options=input_dict["strengths"]
        )

        # Multiselect for Weaknesses
        weaknesses = st.multiselect(
            "Select your weaknesses:",
            options=input_dict["weaknesses"]
        )

        # Multiselect for Interests
        interests = st.multiselect(
            "Select your interests:",
            options=input_dict["weaknesses"]
        )

        # Radio button for Learning Style
        learning_style = st.radio(
            "Choose your learning style:",
            options=input_dict["learning_style"]
        )

        # Multiselect for Preferred Topics
        preferred_topics = st.multiselect(
            "Select your preferred topics:",
            options=input_dict["preferred_topics"]
        )

        # Submit button
        submit = st.form_submit_button("Submit")
    
    # On form submission
    if submit:
        # Store the data in the session state
        st.session_state["user_data"] = {
            "name": name,
            "strengths": strengths,
            "weaknesses": weaknesses,
            "interests": interests,
            "preferences": {
                "learning_style": learning_style,
                "preferred_topics": preferred_topics
            }
        }
        # Navigate to the dashboard by setting the page state
        st.session_state["page"] = "dashboard"

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
def insights_page():
    st.title("📊 Insights Dashboard")
    st.markdown("### Personalized Analysis Based on Your Input!")

    # Retrieve data from session state
    user_data = st.session_state.get("user_data", {})
    if not user_data:
        st.warning("No data available. Please go back to the home page to input your details.")
        return

    name = user_data.get("name", "User")
    strengths = user_data.get("strengths", [])
    weaknesses = user_data.get("weaknesses", [])
    interests = user_data.get("interests", [])
    learning_style = user_data.get("learning_style", "Unknown")

    # Section 1: Greeting
    st.markdown(f"""
        <div style="border: 2px solid #FFD700; border-radius: 10px; padding: 10px; margin-bottom: 20px;">
            <h3>👋 Welcome, {name}!</h3>
            <p><strong>Learning Style:</strong> {learning_style}</p>
            <p>Below is an analysis of your strengths, weaknesses, and interests to guide your learning journey.</p>
        </div>
    """, unsafe_allow_html=True)

    # Section 2: Strengths and Weaknesses with Ratings
    st.markdown("### 💪 Self-Rated Strengths and Weaknesses")
    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### Strengths")
            if strengths:
                strengths_data = {strength: st.slider(f"Rate your {strength} (1-10)", 1, 10, 5) for strength in strengths}
                strengths_df = pd.DataFrame(list(strengths_data.items()), columns=["Strength", "Rating"])
                strengths_chart = px.bar(
                    strengths_df,
                    x="Strength",
                    y="Rating",
                    title="Strength Ratings",
                    height=350,
                    width=400,
                    color="Rating",
                    color_continuous_scale="Blues",
                )
                st.plotly_chart(strengths_chart, use_container_width=True)
            else:
                st.info("No strengths selected. Please go back and update your profile.")

        with col2:
            st.markdown("#### Weaknesses")
            if weaknesses:
                weaknesses_data = {weakness: st.slider(f"Rate your {weakness} (1-10)", 1, 10, 5) for weakness in weaknesses}
                weaknesses_df = pd.DataFrame(list(weaknesses_data.items()), columns=["Weakness", "Rating"])
                weaknesses_chart = px.bar(
                    weaknesses_df,
                    x="Weakness",
                    y="Rating",
                    title="Weakness Ratings",
                    height=350,
                    width=400,
                    color="Rating",
                    color_continuous_scale="Reds",
                )
                st.plotly_chart(weaknesses_chart, use_container_width=True)
            else:
                st.info("No weaknesses selected. Please go back and update your profile.")

    # Section 3: Improved Interests Visualization
    st.markdown("### 🎯 Interests Overview")
    with st.container():
        if interests:
            # Create a visual grid for interests instead of using WordCloud or plain text
            st.markdown("#### Your Interests:")
            cols = st.columns(3)  # Dynamically create 3 columns for a grid layout
            for idx, interest in enumerate(interests):
                with cols[idx % 3]:  # Distribute interests evenly in the columns
                    st.markdown(
                        f"""
                        <div style="border: 2px solid #0d444d; border-radius: 10px; padding: 10px; margin: 5px; text-align: center; background-color: #325d63;">
                            <strong>🌟 {interest}</strong>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
        else:
            st.info("No interests selected. Please go back and update your profile.")

        # Section 4: Course Recommendations
        st.markdown("### 📚 Recommended Courses")
        with st.container():
            courses = recommendCourse(st.session_state["user_data"]["preferences"])
            for idx, course in enumerate(courses):  # Use enumerate to create a unique index for each button
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.markdown(
                        f"""
                        <div style="border: 2px solid cyan; border-radius: 10px; padding: 10px; margin-bottom: 10px;">
                            <strong>{course['title']}</strong><br>
                            <em>Platform:</em> {course['platform']}<br>
                            <a href="{course['url']}" target="_blank">Go to Course</a>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                with col2:
                    # Provide a unique key by appending the index (idx) to the button key
                    if st.button(f"📥 Enroll", key=f"enroll_button_{idx}"):
                        st.success(f"You have enrolled in {course['title']}!")
                        st.snow()


    # Section 5: Mentor Recommendations
    st.markdown("### 🧑‍🏫 Recommended Mentors")
    
    with open("SyntheticData/cleanedUserProfiles.json", "r") as f : 
            users = json.load(f)

    new_user_data = {
        "user_id": len(users), 
        "preferred_topics_defined": st.session_state["user_data"]["preferences"]["preferred_topics"],
        "learning_style": st.session_state["user_data"]["preferences"]["learning_style"], 
        "interests":  st.session_state["user_data"]["interests"]
    }
    mentors_data = get_recommendations_for_new_user(new_user_data)
    
    
   
    with st.container():
        mentors = mentors_data
        

        # Streamlit UI
        st.markdown(
            """
            <style>
            .mentor-card {
                border: 2px solid cyan;
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
                position: relative;
                transition: transform 0.2s ease;
            }
            .mentor-card:hover {
                transform: scale(1.05);
            }
            .mentor-description {
                visibility: hidden;
                background-color: #f9f9f9;
                color: #000;
                text-align: left;
                border-radius: 5px;
                padding: 10px;
                position: absolute;
                top: 120%;
                left: 0;
                width: 100%;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
                z-index: 10;
                border: 1px solid #ccc;
            }
            .mentor-card:hover .mentor-description {
                visibility: visible;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Streamlit UI
        for mentor in mentors:
            print(mentor)
            col1, col2 = st.columns([4, 1])
            with col1:
                # Custom HTML for mentor card with hover effect
                st.markdown(
                    f"""
                    <div class="mentor-card">
                        <strong>{mentor['name']}</strong><br>
                        <em>Specialization:</em> {mentor['specialization']}<br>
                        Contact: <a href="mailto:{mentor['email']}">{mentor['email']}</a>
                        <div class="mentor-description">
                            {mentor['description']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with col2:
                if st.button(f"🤝 Connect: {mentor['name']}"):
                    st.success(f"You have selected {mentor['name']} as your mentor!")
                    st.snow()

    # Section 6: Feedback
    st.markdown("### 📝 Feedback on Insights")
    with st.container():
        feedback = st.text_area("What do you think about these insights? We'd love to hear your thoughts!")
        if st.button("Submit Feedback"):
            st.success("Thank you for your feedback!")

def main():
    # Apply custom CSS
    add_custom_css()

    # Set the default page if not already set
    if "page" not in st.session_state:
        st.session_state["page"] = "home"

    # Display the appropriate page
    if st.session_state["page"] == "dashboard":
        insights_page()
    else:
        home_page()

if __name__ == "__main__":
    main()
