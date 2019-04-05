'''Entrypoint for the entire application.'''
from flask import Flask, abort, request, jsonify, Response, send_from_directory
from flask_jwt import JWT, jwt_required, current_identity

from authentication import Authentication
from create_quiz import CreateQuiz
from manage_classes import ManageClasses

auth = Authentication()
manage_classes = ManageClasses()

# FOR DEV PURPOSES
#auth._persist._shelf.clear()
#auth.add_user("jackharrhy", "foobar123", "student")
#auth.add_user("barab", "finite", "professor")
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
    username = payload['identity']
    print('User logging in with username: {}'.format(username))
    return auth.get_user(username)


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_AUTH_URL_RULE'] = '/api/login'

jwt = JWT(app, _authenticate, _identity)

@app.after_request
def apply_caching(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,HEAD,OPTIONS,POST,PUT')
    return response

@app.route('/')
@app.route('/home')
@app.route('/login')
@app.route('/account')
def send_static_homepage():
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/static/<path:path>')
def send_static_static(path):
    return send_from_directory('static/static', path)

@app.route('/static/js/<path:path>')
def send_static_static_js(path):
    return send_from_directory('static/static/js', path)

def user_as_json_without_password(username):
    return jsonify(auth.return_flat_user(username))

@app.route('/api/whoami')
@jwt_required()
def whoami():
    return user_as_json_without_password(current_identity.username)

@app.route('/api/user', methods=['POST'])
@jwt_required()
def _new_user():
    if not current_identity.is_role('professor'):
        return Response(status=403)

    data = request.get_json()
    auth_result = auth.add_user(
        data['username'],
        data['password'],
        data['role']
    )

    if auth_result['success']:
        return Response(status=204)
    else:
        return Response(auth_result['message'], status=400)

@app.route('/api/user/<username>', methods=['GET', 'POST'])
@jwt_required()
def _user(username):
    if not current_identity.is_role('professor'):
        return Response(status=403)

    if request.method == 'GET':
        user = auth.get_user(username)

        if user:
            return user_as_json_without_password(username)
        else:
            return Response(status=404)

    elif request.method == 'POST':
        user = auth.get_user(username)
        data = request.get_json()

        if data['new_class']:
            class_creation_result = manage_classes.assign_class_to_user(username, data['new_class'])

            if class_creation_result['success']:
                return Response(status=204)
            else:
                return Response(class_creation_result['message'], status=400)

        return Response(status=400)

@app.route('/api/class/', methods=['POST'])
@jwt_required()
def _create_class():
    if not current_identity.is_role('professor'):
        return Response(status=403)

    data = request.get_json()

    class_creation_result = manage_classes.add_class(
        data['classname'],
        current_identity.id,
    )

    if class_creation_result['success']:
        return Response(class_creation_result['class_id'], status=200)
    else:
        return Response(class_creation_result['message'], status=400)

@app.route('/api/changepassword', methods=['POST'])
@jwt_required()
def _change_password():
    data = request.get_json()
    auth_result = auth.change_password(
        current_identity.username,
        data['oldpassword'],
        data['newpassword'],
    )

    if auth_result['success']:
        return Response(status=204)
    else:
        return Response(auth_result['message'], status=400)

@app.route('/new/quiz', methods=["POST"])
@jwt_required()
def _create_quiz():
    if not current_identity.is_role("professor"):
        abort(403)
    data = request.get_json()
    thequiz = CreateQuiz(
        data["quizname"],
        data["numattempts"]
    )
    thequiz.add_start_time(
        data["syear"],
        data["smonth"],
        data["sday"],
        data["shour"],
        data["smin"]
    )
    thequiz.add_end_time(
        data["eyear"],
        data["emonth"],
        data["eday"],
        data["ehour"],
        data["emin"]
    )
    thequiz.add_time_limit(data["timelimit"])
    questions = data["questions"]  # this is a list
    for question in questions:
        thequiz.add_question(
            question["questiontext"],
            question["points"],
            question["answerdict"],
            question["choicesdict"]
        )
    thequiz.add_all_questions_to_bank()
    thequiz.pass_to_storage()
    return thequiz.get_id()
