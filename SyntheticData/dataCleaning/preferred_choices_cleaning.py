import json


with open("SyntheticData/userProfiles.json", "r") as f : 
    users_data = json.load(f)

# Mapping of old domains to new domains
domain_mapping = {
    "AI": "Artificial Intelligence and Machine Learning",
    "Art": "Arts and Creativity",
    "Art Therapy": "Psychology",
    "Artificial Intelligence": "Artificial Intelligence and Machine Learning",
    "Behavioral Science": "Psychology",
    "Blockchain": "Technology Innovations",
    "Business": "Business and Management",
    "Business Strategies": "Business and Management",
    "Creative Writing": "Arts and Creativity",
    "Cybersecurity": "Cybersecurity",
    "Data Analysis": "Data Analytics",
    "Design": "Design Principles",
    "Economics": "Economics",
    "Entrepreneurship": "Business and Management",
    "Financial Analysis": "Finance and Investment",
    "Financial Markets": "Finance and Investment",
    "Game Design": "Arts and Creativity",
    "Game Development": "Robotics and Machine Learning",
    "HR Management": "Business and Management",
    "Investment Strategies": "Finance and Investment",
    "Journalism": "Cultural Studies",
    "Leadership": "Leadership Skills",
    "Market Analysis": "Data Science",
    "Mathematics": "Mathematics",
    "Mechanical Engineering": "Engineering",
    "Media Studies": "Cultural Studies",
    "Music Theory": "Music and Audio",
    "Nutrition": "Health and Wellness",
    "Performing Arts": "Arts and Creativity",
    "Physics": "Physics",
    "Political Science": "Cultural Studies",
    "Product Development": "Technology Innovations",
    "Programming": "Programming",
    "Psychology": "Psychology",
    "Public Speaking": "Public Speaking",
    "Research Methods": "Data Analytics",
    "Robotics": "Robotics and Machine Learning",
    "Sociology": "Cultural Studies",
    "Software Engineering": "Programming",
    "Sports Science": "Sports Science",
    "Statistics": "Data Science",
    "Storytelling": "Arts and Creativity",
    "Wellness": "Health and Wellness"
}

# Function to update preferred_topics based on mapping
def update_preferred_topics(user_data, mapping):
    for id in range(50):
        ls1 = [mapping.get(topic, topic) for topic in user_data["users"][id]["preferred_topics"]]
        
        user_data["users"][id]["preferred_topics_defined"] = list(set(ls1))
    return user_data

# Update the preferred topics for all users
updated_users_data = update_preferred_topics(users_data, domain_mapping)

with open("SyntheticData/cleanedUserProfiles.json", "w") as g : 
    g.write(json.dumps(updated_users_data, indent=4))
