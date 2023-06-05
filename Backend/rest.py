from flask import Flask, request, jsonify
from matchmaker import Matchmaker
from generate import users

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

if __name__ == '__main__':
    matchmaker.build_graph()
    app.run(debug=True)
