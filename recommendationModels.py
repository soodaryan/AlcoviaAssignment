import warnings

warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", message=".*urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'.*")

import json
import numpy as np
import pandas as pd

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class CourseRecommender:
    def __init__(self):
        
        with open("SyntheticData/userCourseInteration.json", "r") as f : 
            self.user_course_interactions = json.load(f)

        with open("SyntheticData/cleanedUserProfiles.json", "r") as f : 
            self.users = json.load(f)
            
        with open("SyntheticData/cleanedCourseData.json", "r") as f : 
            self.course_details = json.load(f)

        self.df_interactions = pd.DataFrame(self.user_course_interactions["user_course_interactions"])
        self.df_users = pd.DataFrame(self.users["users"])
        self.df_courses = pd.DataFrame(self.course_details["courses"])
        
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        self._prepare_data()
        self._generate_embeddings()
        self._compute_content_scores()
        self._compute_collaborative_scores()
    
    def _prepare_data(self):
        self.df_users["preferred_topics_defined_text"] = self.df_users["preferred_topics_defined"].apply(lambda x: x[0])

    def _generate_embeddings(self):
        self.user_embeddings = self.embedding_model.encode(self.df_users["preferred_topics_defined_text"].tolist())
        self.course_embeddings = self.embedding_model.encode(self.df_courses["modified_domain"].tolist())

    def _compute_content_scores(self):
        self.content_scores = []
        for user_emb in self.user_embeddings:
            scores = cosine_similarity([user_emb], self.course_embeddings)[0]
            self.content_scores.append(scores)
        self.df_users["content_scores"] = self.content_scores

    def _compute_collaborative_scores(self):
        interaction_matrix = self.df_interactions.pivot_table(
            index="user_id",
            columns="course_id",
            values="interaction",
            fill_value=0
        )
        collab_similarity = cosine_similarity(interaction_matrix)
        self.collab_scores = np.dot(collab_similarity, interaction_matrix)

    def _prepare_meta_features(self, user_id):
        user_idx = user_id - 1
        collaborative_scores = np.zeros(len(self.content_scores[0]))
        
        if user_idx < len(self.collab_scores):
            collab_user_scores = self.collab_scores[user_idx]
            course_ids = self.df_interactions.columns
            for i, course_id in enumerate(course_ids):
                if i < len(collab_user_scores):
                    collaborative_scores[i] = collab_user_scores[i]
        
        return np.column_stack((self.content_scores[user_idx], collaborative_scores))

    def _get_course_details(self, course_ids, courses_json):
        course_dict = {course['course_id']: course for course in courses_json['courses']}
        return [course_dict[course_id] for course_id, _ in course_ids if course_id in course_dict]

    def recommend_courses(self, user_id, top_n=5):
        meta_features = self._prepare_meta_features(user_id)
        final_scores = meta_features[:, 0] * 0.8 + meta_features[:, 1] * 0.2
        course_ids = self.df_courses["course_id"].tolist()
        course_scores = list(zip(course_ids, final_scores))

        sorted_courses = sorted(course_scores, key=lambda x: x[1], reverse=True)

        interacted_courses = self.df_interactions[self.df_interactions["user_id"] == user_id]["course_id"].tolist()
        recommended_courses = [course for course in sorted_courses if course[0] not in interacted_courses]
        top_n_recommended_courses = recommended_courses[:top_n]
        
        return self._get_course_details(top_n_recommended_courses, self.course_details)

    def add_new_user(self, user_id, preferred_topics, interactions=None):
        """Adds a new user to the system and updates embeddings."""
        # Add to users DataFrame
        new_user_row = {
            "user_id": user_id,
            "preferred_topics_defined": [preferred_topics],
            "preferred_topics_defined_text": preferred_topics
        }
        self.df_users.loc[len(self.df_users)] = new_user_row

        # Update user embeddings
        new_user_embedding = self.embedding_model.encode([preferred_topics])[0]
        self.user_embeddings = np.vstack([self.user_embeddings, new_user_embedding])

        # Add interactions if provided
        if interactions:
            for course_id, interaction in interactions:
                new_interaction_row = {
                    "user_id": user_id,
                    "course_id": course_id,
                    "interaction": interaction
                }
                self.df_interactions = self.df_interactions.append(new_interaction_row, ignore_index=True)
def recommendCourse (preferred_topics) : 
    recommender = CourseRecommender()

    with open("SyntheticData/cleanedUserProfiles.json", "r") as f : 
            users = json.load(f)
    # Add a new user
    new_user_id = len(users)

    recommender.add_new_user(new_user_id, preferred_topics)

    # Get recommendations for the new user
    recommended_courses = recommender.recommend_courses(user_id=new_user_id, top_n=5)
    
    return recommended_courses
    
if __name__ == "__main__" : 
    preferred_topics = ["Programming", "Cybersecurity"]
    print(recommendCourse(preferred_topics))

