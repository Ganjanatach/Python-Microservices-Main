from flask import Flask, request, jsonify
import data_user as us

app = Flask(__name__)

# Find and update data in json
def _update_user(user, new_user, username):
    for x in username:
        if x["user"] == user:
            x["user"] = new_user
            return True
    return False

@app.route('/update', methods=['PUT'])
def update():
    # Get the user's login information from the request
    username = request.form.get('username')
    password = request.form.get('password')
    new_name = request.form.get('new_name')

    _user = us.find_username(username)
   

    if _user:
        us.update_user(username, password, new_name)
        if update:
            return jsonify({'message': 'Update successfully.'}), 200
        else:
            return jsonify({'message': 'User not found.'}), 404
    else:
        return jsonify({'message': 'Invalid username or password.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)