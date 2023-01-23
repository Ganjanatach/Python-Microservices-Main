from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
#import jwt
import data_user as us

app = Flask(__name__)

@app.route('/delete', methods=['DELETE'])
def delete():
    try:
        # Get the user's login information from the request
        username = request.form.get('username')


        _user = us.find_username(username)
        
        data = [x for x in _user if x["user"]==username]
        
        if (data):
            us.delete_user(username)
            return jsonify({'message': 'Account deleted successfully.'}), 200
        else:
            return jsonify({'message': 'Cannot delete account. Invalid login information.'}), 401
    except :
         return jsonify({'message': 'User not found.'}), 401
         
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

  
