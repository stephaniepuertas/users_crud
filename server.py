from flask_app import app, Flask, render_template, session, request, redirect
from flask_app.controllers import users_controller


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)