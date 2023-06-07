from flask import Flask, request, jsonify
from matchmaker import Matchmaker
from generate import users
import os

app = Flask(__name__)
matchmaker = Matchmaker(users, "matchmaking_model.pth")

@app.route('/match', methods=['POST'])
def match():
    user = request.json['user']
    matched_users = matchmaker.graph_matchmaking(user)
    print(matched_users)
    return jsonify(matched_users)

@app.route('/feedback', methods=['POST'])
def feedback():
    user = request.json['user']
    matched_user = request.json['matched_user']
    feedback_score = request.json['feedback_score']
    matchmaker.collect_feedback(user, matched_user, feedback_score)
    matchmaker.adjust_weights()
    return jsonify({'status': 'success'})

@app.route('/addUser', methods=['POST'])
def add_user():
    user = request.json['user']
    gender = request.json['gender']
    interests = request.json['interests']
    print("This is the user: ", str(user))
    users[user] = {'gender': 'female', 'age': 20, 'genderPreference': gender, 'interests': interests, 'vacationType': 'History', 'hotel': 'Hotel 50', 'ageGroupPreference': '26-35', 'userID': user}
    # Change the working directory to the Backend directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    outFile = open("generate.py","w")
    outFile = open("generate.py","w")
    outFile.write("users = %s" % (str(users)))
    outFile.close()
    matchmaker.add_user_and_update_graph(user)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    matchmaker.build_graph()
    app.run(debug=True)
