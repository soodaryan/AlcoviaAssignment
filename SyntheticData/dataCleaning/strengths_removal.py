import json
with open("SyntheticData/mentor_data.json", "r") as f : 
    data = json.load(f)

# Remove "strengths" from each mentor
for mentor in data["mentors"]:
    mentor.pop("strengths", None)

with open("SyntheticData/cleanedMentorData.json", "w") as g : 
    g.write(json.dumps(data, indent=4))
