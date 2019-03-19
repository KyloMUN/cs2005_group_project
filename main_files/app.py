from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity

from authentication import Authentication

auth = Authentication()

# FOR DEV PURPOSES
auth._persist._shelf.clear()
auth.add_user("jackharrhy", "foobar123", "student")
print(auth._persist._shelf["User"])
# FOR DEV PURPOSES

def authenticate(username, password):
    print("auth", username, password)
    auth_result = auth.login(username, password)

    if auth_result["success"]:
        print('success', auth_result)
        return auth_result["user"]
    else:
        print('fail', auth_result)

def identity(payload):
    print("identity", payload)
    username = payload['identity']
    return auth.get_user(username)

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_AUTH_URL_RULE'] = '/login'

jwt = JWT(app, authenticate, identity)

@app.route('/new/user', methods=["POST"])
@jwt_required()
def new_user():
    print(current_identity)
    return
