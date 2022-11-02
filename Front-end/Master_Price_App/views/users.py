from datetime import datetime

import flask

from views import views
from flask import request,  jsonify, render_template, flash, url_for, Response
from flask.helpers import make_response
from clients.users_api_client import register_client, login_client
from views import views


@views.route('/registration/', methods=['POST', 'GET'])
def registration() -> Response:
    if request.method == 'POST':
        data = dict(request.form)
        data['date_load'] = datetime.strftime (datetime.now(), "%m/%d/%Y, %H:%M:%S")
        data['date_update'] = data['date_load']

        if data['password'] != data['repeat_password']:
            # todo cambiar esta asignacion no quemar el resultado
            status_register_response = 401
            flash('Error password dosen\'t match', category="error")
        else:
            status_register_response = register_client(data).status_code

        if status_register_response == 406:
            flash('user already exists', category="error")

        elif status_register_response == 201:
            flash('User created successful please login to enjoy the services', category='success')

        else:
            flash('It\'s no possible to create the user', category="error")

    else:
        return  make_response(render_template('registration.html'))

    return make_response(render_template('registration.html', status=status_register_response),
                         status_register_response)


@views.route('/login/', methods=['POST', 'GET'])
def login() -> Response:
    if request.method == 'POST':
        data = dict(request.form)
        login_response: Response = login_client(data)

        if login_response.status_code == 401:
            flash('User or Password invalid', category="error")

        else:
            flask.redirect('home.html',code=200,)

    return make_response(render_template('login.html'))
