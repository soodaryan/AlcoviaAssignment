import json

class Mentor:
    def __init__(self, mentor_id, name, topics, learning_style):
        self.mentor_id = mentor_id
        self.name = name
        self.topics = topics
        self.learning_style = learning_style

class User:
    def __init__(self, user_id, preferred_topics_defined, learning_style, interests):
        self.user_id = user_id
        self.preferred_topics_defined = preferred_topics_defined
        self.learning_style = learning_style
        self.interests = interests

class RecommendationEngine:
    def __init__(self, users, mentors_data):
        self.mentor_data = mentors_data
        self.users = [
            User(
                user["user_id"],
                user["preferred_topics_defined"],
                user["learning_style"],
                user["interests"]
            ) for user in users
        ]
        self.mentors = [
            Mentor(
                mentor["mentor_id"],
                mentor["name"],
                mentor["topics"],
                mentor["learning_style"]
            ) for mentor in self.mentor_data["mentors"]
        ]

    @staticmethod
    def calculate_score(user, mentor):
        score = 0

        topic_matches = set(user.preferred_topics_defined).intersection(set(mentor.topics))
        score += len(topic_matches) * 10

        if user.learning_style == mentor.learning_style:
            score += 5

        interest_matches = set(user.interests).intersection(set(mentor.topics))
        score += len(interest_matches) * 2

        return score

    def _match_mentors(self, score_data):
        mentors_lookup = {mentor["mentor_id"]: mentor for mentor in self.mentor_data["mentors"]}
        
        matched_mentors = []
        for key, value in score_data.items():
            mentor_id = value["mentor_id"]
            if mentor_id in mentors_lookup:
                matched_mentor = {
                    "mentor_id": mentor_id,
                    "name": mentors_lookup[mentor_id]["name"],
                    "score": value["score"],
                    "learning_style": mentors_lookup[mentor_id]["learning_style"],
                    "topics": mentors_lookup[mentor_id]["topics"],
                    "time_available": mentors_lookup[mentor_id]["time_available"],
                    "description": mentors_lookup[mentor_id]["description"],
                    "specialization" : mentors_lookup[mentor_id]["specialization"],
                    "email": mentors_lookup[mentor_id]["email"],
                }
                matched_mentors.append(matched_mentor)

        return matched_mentors
    
    def recommend_for_user(self, new_user_data):
        best_mentors = []
        new_user = User(
            new_user_data["user_id"],
            new_user_data["preferred_topics_defined"],
            new_user_data["learning_style"],
            new_user_data["interests"]
        )

        scores = {}
        for mentor in self.mentors:
            score = self.calculate_score(new_user, mentor)
            scores[mentor.mentor_id] = {
                "mentor_id": mentor.mentor_id,
                "score": score
            }

        sorted_scores = sorted(scores.items(), key=lambda x: x[1]["score"], reverse=True)
        top_5_mentors = sorted_scores[:5] 

        top_5_mentor_data = self._match_mentors({mentor[0]: mentor[1] for mentor in top_5_mentors})
        
        return top_5_mentor_data


import json

def get_recommendations_for_new_user(new_user_data):
    
    with open("SyntheticData/cleanedMentorData.json", "r") as f : 
        mentor_data = json.load(f)
        
    with open("SyntheticData/cleanedUserProfiles.json", "r") as f : 
        existing_users = json.load(f)["users"]
    existing_users.append(new_user_data)

    engine = RecommendationEngine(existing_users, mentor_data)

    recommendations = engine.recommend_for_user(new_user_data)

    return recommendations

if __name__ == "__main__":
    
    new_user_data = {
        "user_id": 123,  
        "preferred_topics_defined": ["Python", "Machine Learning"],  
        "learning_style": "Visual", 
        "interests": ["AI", "Deep Learning"]  
    }
    
    recommendations = get_recommendations_for_new_user(new_user_data)

    print(recommendations)

