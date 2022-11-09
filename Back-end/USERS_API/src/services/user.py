from fastapi import status
from fastapi.encoders import jsonable_encoder

from clients.user import (
    create_object_client,
    validate_user_data_client,
    update_password_client,
)
from models.data_user import LoginModel, UserModel, ChangePasswordModel
from settings import Settings
from utils.token import validate_token, write_token

settings = Settings()


def login_service(data: LoginModel):

    valid, response = validate_user_data_client(data)

    if valid:
        user_info = response.json()
        user_info['email'] = data.email
        json_token = create_token_service(user_info)
        return json_token
    else:
        return "User or password invalid"


def register_service(data: UserModel):
    # esta validacion no es necesaria ya que el API CRUD
    # hace la verificacion al momento de hacer la creacion

    request_data = jsonable_encoder(data)
    response = create_object_client(request_data)
    return response


def update_password_service(data: ChangePasswordModel):
    valid, response_data = validate_user_data_client(data)
    if valid:
        user_info = response_data.json()
        user_info['email'] = data.email
        json_token = create_token_service(user_info)
        request_data = jsonable_encoder(data)
        token = json_token['token']
        update_password_client(request_data, user_info['id'], token)
        return json_token
    else:
        return "User not found"


def create_token_service(user_info: dict):
    data_encode = {'user_id': user_info['id'], 'email': user_info['email'], 'name': user_info['name']}
    token = write_token(data_encode)
    token_dict = {'token': token}
    json_data = {**data_encode, **token_dict}
    return json_data


def validate_token_service(token: str):
    json_data = validate_token(token, output=True)
    return json_data

