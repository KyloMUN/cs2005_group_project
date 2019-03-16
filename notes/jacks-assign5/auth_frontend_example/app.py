from flask import Flask, request

from authentication import Authentication

app = Flask(__name__)

auth = Authentication(None)

@app.route('/')
def display_example_page():
    return """
<form method="post" action="/login">
<h1>Login</h1>
<input type="text" name="username" placeholder="Username"/>
<input type="password" name="password" placeholder="Password"/>
<input type="submit" value="Submit">
</form>
<p>Forgot your password? <a>Click Here!</a></p>
    """

@app.route('/login', methods=['POST'])
def authenticate_user():
    username = request.form['username']
    password = request.form['password']
    auth_status = auth.login(username, password)
    if auth_status["success"]:
        return "{0}, you are logged in!".format(username)
    return "Log in failed!"
