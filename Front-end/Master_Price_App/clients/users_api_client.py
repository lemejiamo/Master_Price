from flask import request, Response
import requests

# client for login UIR
def login(data):
    pass

# client for register URI
def register_client(data) -> object:
    # todo pasar por settings
    register_uri = "http://127.0.0.1:8800/login/register/"
    try:
        response = requests.post(register_uri, json=data)
        # todo no debe retornar el passwd
        return response
    except Exception as ex:
        # todo manejar correctamente las excepciones
        print(ex)
        print("cannot process entitty")


def login_client(data) -> Response:
    login_uri = "http://127.0.0.1:8800/login/"
    try:
        response = requests.post(login_uri, json=data)
        # todo no debe retornar el passwd
        return response
    except Exception as ex:
        # todo manejar correctamente las excepciones
        print(ex)
        print("cannot process entitty")

