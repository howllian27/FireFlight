from generate import users
from model import MatchmakingModel, createData
from bio_comparison import BioComparison
import numpy as np
import matplotlib.pyplot as plt
import random
import networkx as nx
import torch
import os

class Matchmaker:
    # Initialise Matchmaker class
    def __init__(self, users, model_path):
        self.users = users
        self.graph = nx.Graph()
        self.model_path = model_path
        self.model = None
        self.bio_comparison = BioComparison()
        try:
            if not os.path.exists(model_path):
                self.model = MatchmakingModel(31, 64, 8)
                self.model.train_model()
            self.load_model()
            self.build_graph() 
        except Exception as e:
            print(f"Error loading model: {e}")
            raise
    
    # Load MatchmakingModel
    def load_model(self):
        try:
            self.model = MatchmakingModel(31, 64, 8)
            self.model.load_state_dict(torch.load(self.model_path))
            self.model.eval()
        except Exception as e:
            print(f"Error loading model: {e}")
            raise

    # Add users to graph
    def add_user_to_graph(self, user):
        try:
            self.graph.add_node(user)
        except Exception as e:
            print(f"Error adding user to graph: {e}")
            raise

    # Add edges between users using filtering criteria
    def add_edge_to_graph(self, user1, user2):
        try:
            shared_interests = set(self.users[user1]["interests"]).intersection(self.users[user2]["interests"])
            if shared_interests:
                print("Filtering: ", user1, user2)
                self.graph.add_edge(user1, user2, weight=len(shared_interests))
        except Exception as e:
            print(f"Error adding edge to graph: {e}")
            raise

    # Format age string
    def age_format(self, age_group_preference):
        if age_group_preference == "56+":
            age_group_preference = "56-100"
        return age_group_preference

    # Filtering criteria
    def basic_filtering(self, user, other_user):
        try:
            if (user["genderPreference"] != other_user["gender"]) or (user["gender"] != other_user["genderPreference"]):
                return False

            user_age = user["age"]
            other_user_age = other_user["age"]
            user_age_group = self.age_format(user["ageGroupPreference"])
            other_user_age_group = self.age_format(other_user["ageGroupPreference"])

            user_min_age, user_max_age = map(int, user_age_group.split("-"))
            other_user_min_age, other_user_max_age = map(int, other_user_age_group.split("-"))

            if (user_age < other_user_min_age or user_age > other_user_max_age) or (other_user_age < user_min_age or other_user_age > user_max_age):
                return False
            
            return True
        except Exception as e:
            print(f"Error in basic filtering: {e}")
            raise

    # Create graph for user network
    def build_graph(self):
        try:
            for user in self.users:
                self.add_user_to_graph(user)

            for i in range(len(self.users)):
                for j in range(i + 1, len(self.users)):
                    user1 = list(self.users.keys())[i]
                    user2 = list(self.users.keys())[j]

                    if self.basic_filtering(self.users[user1], self.users[user2]):
                        self.add_edge_to_graph(user1, user2)
        except Exception as e:
            print(f"Error building graph: {e}")
            raise

    # Return compatibility score for weights of graph edges
    def predict_compatibility(self, user, user_preferences, other_user_preferences, user_interests, other_user_interests, bio1, bio2):
        try:
            # Dataset categories
            gender_categories = ["male", "female"]
            age_group_categories = ["18-25", "26-35", "36-45", "46-55", "56+"]
            interest_categories = ["History", "Adventure", "Nature", "Nightlife", "Food", "Beach", "Shopping", "Cultural"]

            # One-hot encode the categorical variables
            user_preferences_encoded = [1 if gender == user_preferences[0] else 0 for gender in gender_categories] + [1 if age == user_preferences[1] else 0 for age in age_group_categories]
            other_user_preferences_encoded = [1 if gender == other_user_preferences[0] else 0 for gender in gender_categories] + [1 if age == other_user_preferences[1] else 0 for age in age_group_categories]
            user_interests_encoded = [int(interest in user_interests) for interest in interest_categories]
            other_user_interests_encoded = [int(interest in other_user_interests) for interest in interest_categories]
            potential_connections = int(len(set(user_interests) & set(other_user_interests)) > 0)

            # Create the input data tensor
            input_data = user_preferences_encoded + other_user_preferences_encoded + user_interests_encoded + other_user_interests_encoded + [potential_connections]
            input_tensor = torch.tensor([input_data], dtype=torch.float32)

            print("Tensor is ", self.model(input_tensor), self.model(input_tensor).mean().item())
            # get bio_comparison
            bio_similarity = self.bio_comparison.compare_sentences(bio1, bio2)

            # Make a prediction using the model and take the mean of the tensor to get a scalar compatibility score
            compatibility_score = self.model(input_tensor).mean().item() + bio_similarity

            print(compatibility_score)

            return compatibility_score
        except Exception as e:
            print(f"Error predicting compatibility: {e}")
            raise

    # Create Graph based on Matches Made & Rank Matched Users Based on Compatibility Score
    def graph_matchmaking(self, user):
        matches = []
        print(user)
        user_preferences = [self.users[user]["genderPreference"], self.users[user]["ageGroupPreference"]]
        user_interests = self.users[user]["interests"]
        user_bio = self.users[user]["bio"]

        for other_user in self.users:
            if other_user != user:
                other_user_preferences = [self.users[other_user]["gender"], self.users[other_user]["ageGroupPreference"]]
                other_user_interests = self.users[other_user]["interests"]
                other_user_bio = self.users[other_user]["bio"]

                if self.graph.has_edge(user, other_user):
                    print("Checking for edge between ", user, other_user)
                    compatibility_score = self.predict_compatibility(
                    user, user_preferences, other_user_preferences, user_interests, other_user_interests, user_bio, other_user_bio
                    )
                    matches.append((other_user, compatibility_score))
                    print(matches)

        sorted_scores = sorted(matches, key=lambda x: x[1], reverse=True)
        top_matches = sorted_scores[:5]

        matched_users = []
        for match in top_matches:
            matched_user = self.users[match[0]]
            matched_users.append((match[0], matched_user))

        print(matched_users)
        return matched_users
    
    # Add User and Update Existing Graph
    def add_user_and_update_graph(self, user):
        self.add_user_to_graph(user)
        for other_user in self.users:
            if other_user != user:
                if self.basic_filtering(self.users[user], self.users[other_user]):
                    print(user, other_user)
                    self.add_edge_to_graph(user, other_user)

    # Storing User Feedback
    def collect_feedback(self, user, matched_user, feedback_score):
        # Store the feedback score in the graph
        if self.graph.has_edge(user, matched_user):
            self.graph[user][matched_user]["feedback_score"] = feedback_score

    # adjust weights of graph based on feedback score        
    def adjust_weights(self):
        for user, matched_user, data in self.graph.edges(data=True):
            if "feedback_score" in data:
                data["weight"] *= data["feedback_score"]

    # Print Matched User 
    def print_matched_users(self, user, matched_users):
        print(f"Printing matches for {user}:")
        for matched_user in matched_users:
            print("Matched User:")
            print(f"User ID: {matched_user[0]}")
            print(f"Gender: {matched_user[1]['gender']}")
            print(f"Age Group: {matched_user[1]['ageGroupPreference']}")
            print(f"Interests: {', '.join(matched_user[1]['interests'])}")
            print(f"Vacation Type: {matched_user[1]['vacationType']}")
            print(f"Hotel: {matched_user[1]['hotel']}")
            print("--------------------")

if __name__ == "__main__":
    matchmaker = Matchmaker(users, "matchmaking_model.pth")
    matchmaker.build_graph()
    user = "user55"  # Select a random user
    matched_users = matchmaker.graph_matchmaking(user)
    for matched_user in matched_users:
        feedback_score = input(f"How would you rate your match with {matched_user[0]}? (0-1): ")
        matchmaker.collect_feedback(user, matched_user[0], float(feedback_score))
    # Adjust the weights based on the feedback
    matchmaker.adjust_weights()
    matchmaker.print_matched_users(user, matched_users)