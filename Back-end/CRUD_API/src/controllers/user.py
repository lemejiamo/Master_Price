from typing import Optional, Union
from fastapi import APIRouter, Header, status
from fastapi.responses import JSONResponse
from clients.login import validate_token_client
from models.user import UpdatePassword, Users
from services.standar_services import *


class_name = "Users"

router = APIRouter(
    prefix="/user",
    tags=["Users"],
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="get all users records from database",
)
def get_all_controller(logintoken: Optional[str] = Header(...),key: Union[str, None] = None,value: Optional[str] = None):
    """
    get all store records from database
    Args:
        login-token: Required to verify that the user is valid
        key: optional filter field
        value: required if key, filter by value
    Returns:
        JSON Response
    """

    validate_token_client(logintoken)

    if key is not None and value is not None:
        filter_by = {"field": key}
        filter_by.update({"value": value})
        data = get_all_objects_service(class_name, **filter_by)
    else:
        data = get_all_objects_service(class_name)

    len_data = len(data)

    if len_data > 0:
        if len_data > 1:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=data,
            )
        elif len_data == 1:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=data[0],
            )
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=data,
        )


@router.get(
    "/email/{email}",
    status_code=status.HTTP_200_OK,
    summary="get a single user record from database",
)
def get_by_email_controller(email: str):
    """
    get a single user record from database
    Args:
        user_id (str): user's user id
    Returns:
        JSON Response
    """
    category = 'user'
    object_data, result = get_object_by_email_service(email, class_name, category)

    if result is False:
        return JSONResponse(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            content={"error": f"failed to get a user with id {email}"},
        )
    elif object_data is not None:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=object_data
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"error": "User with email {email} not found"},
        )


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="create a single user record in database",
)
def create_controller(data: Users):
    """
    create a single user record in database
    Args:
        user_id (str): user's user id
    Returns:
        JSON Response
    """
    response, object_data = create_object_service(data)

    if response and object_data:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            # todo cambiar el timpo de contenido no veo la necesidad de retornar el usuario
            content=object_data,
        )
    elif response and object_data is None:
        return JSONResponse(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            content={"user": "Already exists a user with this email"},
        )


@router.patch(
    "/update/password/user/id/{user_id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="update a single user record in database",
)
def update_password_controller(user_id: str, data: UpdatePassword, logintoken: str = Header(...)):
    """
    update a single user record in database
    Args:
        id (str): user's user id
    Returns:
        JSON Response
    """
    validate_token_client(logintoken)
    result, response = update_password_service(data, class_name, user_id)
    if result:
        return JSONResponse(
            status_code=status.HTTP_202_ACCEPTED,
            content=response
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=response
        )


@router.patch(
    "/update/id/{user_id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="update a single user record in database",
)
def update_controller(id: str, data: class_name, logintoken: str = Header(...)):
    """
    update a single user record in database
    Args:
        id (str): user's user id
    Returns:
        JSON Response
    """
    validate_token_client(logintoken)
    result, response = update_object_service(data, class_name, id)
    if result:
        return JSONResponse(
            status_code=status.HTTP_202_ACCEPTED,
            content=response
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=response
        )


@router.delete(
    "/delete/id/{user_id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="delete a single user record in database",
)
def delete_controller(user_id: str, logintoken: str = Header(...)):
    """
    delete a single user record in database
    Args:
        user_id (str): user's user id
    Returns:
        JSON Response
    """
    validate_token_client(logintoken)
    response = delete_object_service(user_id, class_name)
    if response:
        return JSONResponse(
            status_code=status.HTTP_202_ACCEPTED,
            content={"Success": "ok"}
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            content=None
        )
