from typing import Union
import requests
from fastapi import HTTPException, status
from models.data_user import LoginModel
from settings import Settings
from utils.hashing_util import hash_attribute


settings = Settings()


def validate_user_data_client(data: LoginModel) ->  Union[bool, any]:

    request_url = f"{settings.CRUD_API_URL}/user/email/{data.email}"
    response = requests.get(url=request_url)

    data.password = hash_attribute(hash_attribute(data.password, 'sha512'), 'sha512')

    if response.status_code == status.HTTP_200_OK:
        data_obj = response.json()
        if data_obj['password'] == data.password:
            return True, response
        else:
            return False, response

    elif response.status_code == status.HTTP_404_NOT_FOUND:
        return False, response

    else:
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={
                "client": "get_by_email_client",
                "detail": f"The API can't get a record at DB for user with email {email}",
            }
        )

def create_object_client(json_object):
    request_url = f"{settings.CRUD_API_URL}/user/"
    email = json_object["email"]
    response = requests.post(
        url=request_url,
        json=json_object
    )

    if (
        response.status_code == status.HTTP_201_CREATED
        or response.status_code == status.HTTP_406_NOT_ACCEPTABLE
    ):
        return response
    else:
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={
                "client": "create_object_client",
                "detail": f"The API can't create a record at DB for user with email {email}",
            },
        )


def update_password_client(json_object, user_id: str, login_token: str):
    request_url = f"{settings.CRUD_API_URL}/user/update/password/user/id/{user_id}"
    email = json_object["email"]
    response = requests.patch(
        url=request_url, json=json_object, headers={"login-token": f"{login_token}"}
    )

    if (
        response.status_code == status.HTTP_202_ACCEPTED
        or response.status_code == status.HTTP_404_NOT_FOUND
    ):
        return response
    else:
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail={
                "client": "update_object_client",
                "detail": f"The API can't update a record at DB for user with email {email}",
            },
        )
