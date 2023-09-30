from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# You would need to replace with actual Metaphor API integration.

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return jsonify({'username': user.username}), 201

if __name__ == '__main__':
    app.run(debug=True)
