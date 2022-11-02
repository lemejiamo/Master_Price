# !/usr/bin/python3
from datetime import datetime
from views import views
from flask import request, make_response, jsonify, render_template, flash, url_for
from flask.helpers import make_response
from flask.json import jsonify
from clients.users_api_client import register_client


@views.route('/index', methods=['GET'])
def index():
    return render_template('index.html')




@views.route('/catalog-page/', methods=['POST', 'GET'])
def catalog_page():
    if request.method == 'POST':
        return {'hey': 'recibiendo el post',
                'ya': 'puedes redireccionar'}
    else:
        return  render_template('catalog-page.html')


@views.route('/features/', methods=['POST', 'GET'])
def features():
    if request.method == 'POST':
        return {'hey': 'recibiendo el post',
                'ya': 'puedes redireccionar'}
    else:
        return  render_template('features.html')


@views.route('/product-page/', methods=['POST', 'GET'])
def product_page():
    if request.method == 'POST':
        return {'hey': 'recibiendo el post',
                'ya': 'puedes redireccionar'}
    else:
        return  render_template('product-page.html')


@views.route('/about-us/', methods=['POST', 'GET'])
def about_us():
    if request.method == 'POST':
        return {'hey': 'recibiendo el post',
                'ya': 'puedes redireccionar'}
    else:
        return  render_template('about-us.html')


@views.route('/contact-us/', methods=['POST', 'GET'])
def contact_us():
    if request.method == 'POST':
        return {'hey': 'recibiendo el post',
                'ya': 'puedes redireccionar'}
    else:
        return  render_template('contact-us.html')
