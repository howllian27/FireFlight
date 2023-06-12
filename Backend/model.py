import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from generate import users

# Define the deep learning model architecture
class MatchmakingModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(MatchmakingModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return torch.sigmoid(x)
    
    def train_model(self):
        # Define hyperparameters
        input_size = len(X_train[0])
        hidden_size = 64
        output_size = len(y_train[0])
        learning_rate = 0.001
        num_epochs = 50

        # Create an instance of the matchmaking model
        model = MatchmakingModel(input_size, hidden_size, output_size)

        # Define the loss function and optimizer
        criterion = nn.BCELoss()
        optimizer = optim.Adam(model.parameters(), lr=learning_rate)

        # Convert your data to PyTorch tensors
        X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
        y_train_tensor = torch.tensor(y_train, dtype=torch.float32)

        # Training loop
        for epoch in range(num_epochs):
            # Forward pass
            outputs = model(X_train_tensor)
            loss = criterion(outputs, y_train_tensor)

            # Backward pass and optimization
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # Print the loss for this epoch
            print(f"Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}")

        # Save the trained model
        torch.save(model.state_dict(), "matchmaking_model.pth")
    

# Prepare your dataset (features and labels)
X_train = []
y_train = []

gender_categories = ["male", "female"]
age_group_categories = ["18-25", "26-35", "36-45", "46-54", "55 and above"]
interest_categories = ["History", "Adventure", "Nature", "Nightlife", "Food", "Beach", "Shopping", "Cultural"]


def createData(filtered_users, user_preferences, user_interests):
    for other_user in filtered_users:
        other_user_preferences = [gender_categories.index(users[other_user]["genderPreference"]),
                                  age_group_categories.index(users[other_user]["ageGroupPreference"])]
        other_user_interests = users[other_user]["interests"]
        
        # Potential Connections: Check for common interests
        common_interests = list(set(user_interests) & set(other_user_interests))
        potential_connections = int(len(common_interests) > 0)
        
        # Interest Extrapolation: Generate potential interests
        potential_interests = list(set(user_interests + other_user_interests))
        
        # One-hot encode the categorical variables
        user_preferences_encoded = np.eye(len(gender_categories))[user_preferences[0]].tolist() + np.eye(len(age_group_categories))[user_preferences[1]].tolist()
        other_user_preferences_encoded = np.eye(len(gender_categories))[other_user_preferences[0]].tolist() + np.eye(len(age_group_categories))[other_user_preferences[1]].tolist()
        user_interests_encoded = [int(interest in user_interests) for interest in interest_categories]
        other_user_interests_encoded = [int(interest in other_user_interests) for interest in interest_categories]
        potential_interests_encoded = [int(interest in potential_interests) for interest in interest_categories]
        
        X_train.append(user_preferences_encoded + other_user_preferences_encoded + user_interests_encoded + other_user_interests_encoded + [potential_connections])
        y_train.append(potential_interests_encoded)

def preprocessData():
    for user in users:
        user_preferences = [gender_categories.index(users[user]["genderPreference"]),
                            age_group_categories.index(users[user]["ageGroupPreference"])]
        user_interests = users[user]["interests"]
        
        # Filtering based on gender and age group preferences
        filtered_users = [u for u in users if u != user]
        
        createData(filtered_users, user_preferences, user_interests)    

preprocessData()    