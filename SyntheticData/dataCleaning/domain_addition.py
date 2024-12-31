import json
with open("SyntheticData/courseData.json", "r") as f : 
    data = json.load(f)
    

# List of original domains
original_domains = [
    "Artificial Intelligence and Machine Learning",
    "Personal Development",
    "Creative Arts",
    "Robotics and Machine Learning",
    "Cybersecurity",
    "Technology",
    "Sports",
    "Business",
    "Data Science",
    "Marketing",
    "Programming",
    "Design",
    "Finance",
    "Psychology",
    "Project Management",
    "Philosophy",
    "Art",
    "Music",
    "Health",
    "Physics",
    "Communication",
    "Mathematics",
    "Engineering",
    "Leadership",
    "Data Analysis",
    "Science",
    "Economics",
    "Anthropology"
]

# List of modified domains
modified_domains = [
    "Artificial Intelligence and Machine Learning",
    "Personal Development",
    "Arts and Creativity",
    "Robotics and Machine Learning",
    "Cybersecurity",
    "Technology Innovations",
    "Sports Science",
    "Business and Management",
    "Data Science",
    "Digital Marketing",
    "Programming",
    "Design Principles",
    "Finance and Investment",
    "Psychology",
    "Project Management",
    "Philosophy",
    "Fine Arts",
    "Music and Audio",
    "Health and Wellness",
    "Physics",
    "Public Speaking",
    "Mathematics",
    "Engineering",
    "Leadership Skills",
    "Data Analytics",
    "Environmental Science",
    "Economics",
    "Cultural Studies"
]

# Create a mapping between original domain and modified domain
domain_mapping = dict(zip(original_domains, modified_domains))

# Iterate through the JSON and add modified_domain field
for course in data["courses"]:
    original_domain = course["domain"]
    if original_domain in domain_mapping:
        course["modified_domain"] = domain_mapping[original_domain]
    else :
        print(original_domain)

with open("SyntheticData/cleanedCourseData.json", "w") as g : 
    g.write(json.dumps(data, indent=4))