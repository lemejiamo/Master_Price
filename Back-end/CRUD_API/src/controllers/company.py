import os
from json import load
from typing import Union, Optional
from fastapi import APIRouter, Header, status
from fastapi.responses import JSONResponse
from clients.login import validate_token_client
from models.company import Company
from services.standar_services import (
    create_object_service,
    delete_object_service,
    get_all_objects_service,
    get_object_service,
    update_object_service,
)

class_name = "Company"

router = APIRouter(
    prefix="/company",
    tags=["Company"],
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary=f"get all {class_name} records from database",
)
def get_all_controller(
        logintoken: Optional[str] = Header(...),
        key: Union[str, None] = None,
        value: Optional[str] = None):
    """
    get all store records from database
    Args:
        logintoken: Required verify that the user is valid
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

#
# @router.get(
#     "/id/{company_id}",
#     status_code=status.HTTP_200_OK,
#     summary="get a single user record from database",
# )
# def get_one_controller(
#     id: str,
#     logintoken: str = Header(default=None)
# ):
#     """
#     get a single user record from database
#     Args:
#         user_id (str): user's user id
#     Returns:
#         JSON Response
#     """
#     validate_token_client(logintoken)
#     data = get_object_service(id, class_name)
#     if data is not None:
#         return JSONResponse(status_code=status.HTTP_200_OK, content=data)
#     return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=data)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary=f"create a single {class_name} record in database",
)
def create_controller(
    data: Company,
    logintoken: str = Header(default=None)
):
    """
    create a single company record in database
    Args:
        data: data from the company
    Returns:
        JSON Response
    """
    validate_token_client(logintoken)
    response, object_data = create_object_service(data)

    if response:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,  # TODO cambiar por el estatus correspondiente
            content=data,
        )
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,  # TODO cambiar por el estatus correspondiente
        content=None,
    )


@router.patch(
    "/update/id/{user_id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary=f"update a single {class_name} record in database",
)
def update_controller(
    id: str,
    data: Company,
    logintoken: str = Header(default=None)
):
    """
    update a single user record in database
    Args:
        id (str): company's id
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
    "/delete/id/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary=f"delete a single {class_name} record in database",
)
def delete_controller(id: str, logintoken: str = Header(default=None)):
    """
    delete a single user record in database
    Args:
        user_id (str): user's user id
    Returns:
        JSON Response
    """
    validate_token_client(logintoken)
    response = delete_object_service(id, class_name)
    if response:
        return JSONResponse(
            status_code=status.HTTP_202_ACCEPTED, content={"Success": "ok"}
        )
    else:
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE, content=None)


@router.get(
    "/carga_masiva",
    status_code=status.HTTP_202_ACCEPTED,
    summary=f"upload a json file with the records to the  database",
)
def create_from_file():
    JSON_FILES = '/home/ricky/Documentos/ipython/json/'
    files = os.listdir(JSON_FILES)
    print(files)
    for file in files:
        with open(JSON_FILES+file, "r") as db:
            result = load(db)
        for object, value in result.items():
            if file == 'companys.json':
                class_name = 'Company'
            elif file == 'usuarios.json':
                class_name = 'Users'
            elif file == 'stores.json':
                class_name = 'Store'
            elif file == 'products.json':
                class_name = 'Products'
            response1, response2 = create_object_service(value, class_name)
            print(response1)
            print(response2)

    return JSONResponse(status_code=200, content=None)
