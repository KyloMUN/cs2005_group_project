"""Entrypoint for the entire application."""
from flask import Flask, abort, request, jsonify, Response
from flask_jwt import JWT, jwt_required, current_identity

from authentication import Authentication

auth = Authentication()

# FOR DEV PURPOSES
auth._persist._shelf.clear()
auth.add_user("jackharrhy", "foobar123", "student")
auth.add_user("barab", "finite", "professor")
print(auth._persist._shelf["User"])
# FOR DEV PURPOSES


def _authenticate(username, password):
    print("auth", username, password)
    auth_result = auth.login(username, password)

    if auth_result["success"]:
        print('success', auth_result)
        return auth_result["user"]
    else:
        print('fail', auth_result)


def _identity(payload):
    print("identity", payload)
    username = payload['identity']
    return auth.get_user(username)


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_AUTH_URL_RULE'] = '/login'

jwt = JWT(app, _authenticate, _identity)


@app.route('/new/user', methods=["POST"])
@jwt_required()
def _new_user():
    if not current_identity.is_role("professor"):
        abort(403)

    data = request.get_json()
    auth_result = auth.add_user(
        data["username"],
        data["password"],
        data["role"]
    )

    print(auth._persist._shelf["User"])

    if auth_result["success"]:
        return Response(status=204)
    else:
        abort(Response(auth_result["message"], 400))
