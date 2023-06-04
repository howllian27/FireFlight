from generate import users
from model import MatchmakingModel, createData
import numpy as np
import matplotlib.pyplot as plt
import random
import networkx as nx
import torch

# Create a graph to represent user connections
graph = nx.Graph()

def add_user_to_graph(user):
    graph.add_node(user)

def add_edge_to_graph(user1, user2):
    shared_interests = set(users[user1]["interests"]).intersection(users[user2]["interests"])
    if shared_interests:
        graph.add_edge(user1, user2, weight=len(shared_interests))

def ageFormat(ageGroupPreference):
    if ageGroupPreference == "55 and above":
        ageGroupPreference = "55-100"
    return ageGroupPreference

# Apply basic filtering to determine if two users can be connected
def basic_filtering(user, other_user):
    if (user["genderPreference"] != other_user["gender"]) or (user["gender"] != other_user["genderPreference"]):
        return False
    
    user_age = user["age"]
    other_user_age = other_user["age"]
    user_age_group = ageFormat(user["ageGroupPreference"])
    other_user_age_group = ageFormat(other_user["ageGroupPreference"])

    user_min_age, user_max_age = map(int, user_age_group.split("-"))
    other_user_min_age, other_user_max_age = map(int, other_user_age_group.split("-"))

    if (user_age < other_user_min_age or user_age > other_user_max_age) or (other_user_age < user_min_age or other_user_age > user_max_age):
        return False

    return True

# Add users to the graph and create connections based on filtering
for user in users:
    add_user_to_graph(user)

for i in range(len(users)):
    for j in range(i + 1, len(users)):
        user1 = list(users.keys())[i]
        user2 = list(users.keys())[j]


        if basic_filtering(users[user1], users[user2]):
            add_edge_to_graph(user1, user2)

# Deep learning compatibility prediction function
def predict_compatibility(user_preferences, other_user_preferences, user_interests, other_user_interests):
    # Define the input size, hidden size, and output size based on your trained model
    input_size = 31
    hidden_size = 64  
    output_size = 8 

    # Load the trained deep learning model (if not already loaded)
    if "model" not in predict_compatibility.__dict__:
        predict_compatibility.model = MatchmakingModel(input_size, hidden_size, output_size)
        model_state_dict = torch.load("matchmaking_model.pth")

    # Dataset categories
    gender_categories = ["male", "female"]
    age_group_categories = ["18-25", "26-35", "36-45", "46-54", "55 and above"]
    interest_categories = ["History", "Adventure", "Nature", "Nightlife", "Food", "Beach", "Shopping", "Cultural"]

    # One-hot encode the categorical variables
    user_preferences_encoded = [1 if gender == user_preferences[0] else 0 for gender in gender_categories] + [1 if age == user_preferences[1] else 0 for age in age_group_categories]
    other_user_preferences_encoded = [1 if gender == other_user_preferences[0] else 0 for gender in gender_categories] + [1 if age == other_user_preferences[1] else 0 for age in age_group_categories]
    user_interests_encoded = [int(interest in user_interests) for interest in interest_categories]
    other_user_interests_encoded = [int(interest in other_user_interests) for interest in interest_categories]
    potential_connections = int(len(set(user_interests) & set(other_user_interests)) > 0)

    # Create the input data tensor
    input_data = user_preferences_encoded + other_user_preferences_encoded + user_interests_encoded + other_user_interests_encoded + [potential_connections]
    print(input_data)
    input_tensor = torch.tensor([input_data], dtype=torch.float32)

    # Make a prediction using the model
    compatibility_score = predict_compatibility.model(input_tensor)

    return compatibility_score

# Matchmaking function
def graph_matchmaking(user):
    matches = []

    user_preferences = [users[user]["genderPreference"], users[user]["ageGroupPreference"]]
    user_interests = users[user]["interests"]

    for other_user in users:
        if other_user != user:
            other_user_preferences = [users[other_user]["gender"], users[other_user]["ageGroupPreference"]]
            other_user_interests = users[other_user]["interests"]

            if graph.has_edge(user, other_user):
                compatibility_score = predict_compatibility(
                    user_preferences, other_user_preferences, user_interests, other_user_interests
                )
                # compatibility_score = random.randint(0, 100)/10
                matches.append((other_user, compatibility_score))

    print(matches)

    sorted_scores = sorted(matches, key=lambda x: x[1], reverse=True)
    top_matches = sorted_scores[:5]

    matched_users = []
    for match in top_matches:
        matched_user = users[match[0]]
        matched_users.append((match[0], matched_user))

    return matched_users

# Draw the graph using matplotlib
pos = nx.spring_layout(graph)  # Compute node positions
nx.draw_networkx_nodes(graph, pos)
nx.draw_networkx_edges(graph, pos)
nx.draw_networkx_labels(graph, pos)
# plt.show()

# Main code
if __name__ == "__main__":
    user = "user8"  # Select a random user

    matched_users = graph_matchmaking(user)

    print(matched_users)

    # Print the matched users
    for matched_user in matched_users:
        print("Matched User:")
        print(f"User ID: {matched_user[0]}")
        print(f"Gender: {matched_user[1]['gender']}")
        print(f"Age Group: {matched_user[1]['ageGroupPreference']}")
        print(f"Interests: {', '.join(matched_user[1]['interests'])}")
        print(f"Vacation Type: {matched_user[1]['vacationType']}")
        print(f"Hotel: {matched_user[1]['hotel']}")
        print("--------------------")
