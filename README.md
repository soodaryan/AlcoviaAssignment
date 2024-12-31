# 🚀 Course and Mentor Recommendation System

Hi there! 👋 Welcome to my **Course and Mentor Recommendation System** project. This implementation uses data from user profiles and mentor/course information to suggest personalized courses and mentors. 🎓💡 I’ve built this with Python and deployed it as a Streamlit app for an interactive experience! 😊

---

## ✨ What I Did

### 🧠 Course Recommendation Model
I created a recommendation system to suggest the most suitable courses for users based on their profile and historical interaction data. Here’s how it works:

- **Data Collection**: The system gathers data from user profiles and course interactions.
- **Modeling**: I implemented a recommendation algorithm that processes this data and suggests courses relevant to the user’s preferences.

### 🌟 Mentor Recommendation Model
I also developed a mentor recommendation engine that matches users with mentors who are best suited to help them based on the user's profile and needs.

- **Matching Algorithm**: The model uses the user’s preferences to match them with mentors with the right expertise and availability.

### 🎉 Streamlit App
The interactive interface is built using **Streamlit**. Users can interact with the recommendation system and receive course and mentor suggestions through an easy-to-use web app.

---

## 📂 Project Structure

```bash
soodaryan-AlcoviaAssignment/
├── SyntheticData/                          # Synthetic data files used for training and testing
│   ├── cleanedMentorData.json              # Cleaned mentor data
│   ├── userProfiles.json                   # Raw user profile data
│   ├── cleanedUserProfiles.json            # Cleaned user profile data
│   ├── .DS_Store                           # System files
│   ├── dataCleaning/                       # Scripts for cleaning the data
│   │   ├── strengths_removal.py            # Remove unnecessary strength data
│   │   ├── domain_addition.py              # Add domain-related data
│   │   ├── data_cleaning.py                # General data cleaning script
│   │   └── preferred_choices_cleaning.py   # Clean user preferences data
│   ├── courseData.json                     # Raw course data
│   ├── cleanedCourseData.json              # Cleaned course data
│   └── userCourseInteration.json           # User-course interaction data
├── recommendationModels.py                 # Core recommendation models
├── mentorRecommendation.py                 # Mentor recommendation logic
├── home.py                                 # Streamlit app to interact with recommendations
├── requirements.txt                        # Dependencies
├── README.md                               # Project documentation
└── utils.py                                # Utility functions for the project
```

---

## 🚀 How to Run the System

### 🛠️ Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/soodaryan-AlcoviaAssignment.git
   ```

2. Navigate to the project directory:

   ```bash
   cd soodaryan-AlcoviaAssignment
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### 🚀 Run the Streamlit App

To run the app and interact with the course and mentor recommendation models, use:

```bash
streamlit run home.py
```

The app will open in your browser, where you can explore personalized course and mentor recommendations. 😄

---

## 📂 Key Files

- **SyntheticData**: Contains the data files used to build and test the recommendation models.
  - `cleanedMentorData.json`: Cleaned mentor data for matching mentors to users.
  - `cleanedUserProfiles.json`: Raw data of user profiles.
  - `cleanedCourseData.json`: Course data that will be used to generate recommendations.

- **recommendationModels.py**: Implements the course and mentor recommendation algorithms.

- **mentorRecommendation.py**: Contains the mentor recommendation logic.

- **home.py**: Streamlit app that allows users to interact with the recommendation system.

---

## 📝 How It Works

1. **Data Cleaning**: The data is cleaned using the scripts inside the `dataCleaning/` folder. This includes tasks such as removing unnecessary data, adding domain information, and cleaning user preferences.

2. **Recommendation Models**: The cleaned data is fed into the recommendation models in `recommendationModels.py` to generate personalized suggestions for courses and mentors.

3. **Streamlit Interface**: The final user interface is built with **Streamlit**, which allows users to interact with the models and receive course and mentor recommendations.

---

## 🔧 Dependencies

The project requires the following Python libraries:

- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Other dependencies listed in `requirements.txt`

---

## 📌 Future Enhancements

- Integrate additional data sources (e.g., feedback from users) to improve the accuracy of the recommendations.
- Add a rating system for mentors and courses to enhance the recommendation engine.
- Implement a more advanced recommendation algorithm (e.g., collaborative filtering, deep learning-based models).

---

## 🎉 Contributing

Feel free to fork the repository and create pull requests! If you have suggestions or find issues, don’t hesitate to open an issue and discuss. Let’s improve this project together! 🤝

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.

---

Let’s make learning smarter with personalized recommendations! 🌟
