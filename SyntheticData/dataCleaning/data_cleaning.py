import json 
with open("SyntheticData/userCourseInteration.json", "r") as f : 
    data = json.load(f)
userID = []
courseID = []
interaction = []
for idx, row in enumerate(data["user_course_interactions"]): 
    userID.append(row["user_id"])
    courseID.append(row["course_id"])
    interaction.append(row["interaction"])
    
final = {
    "user_course_interactions" : {
        "user_id" : userID,
        "course_id" : courseID,
        "interaction" : interaction
    }
}
with open("SyntheticData/cleanedUserProfiles.json", "w") as g : 
    g.write(json.dumps(final, indent=4))