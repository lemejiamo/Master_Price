from typing import Optional, Union

from fastapi import APIRouter, Header, status
from fastapi.responses import JSONResponse

from clients.login import validate_token_client
from models.product import Products
from services.standar_services import (
    Get_Category_From_Collection_Service,
    Get_Product_By_Name_Service,
    create_object_service,
    delete_object_service,
    get_all_objects_service,
    get_object_service,
    update_object_service,
    get_all_emails_service
)

class_name = "Products"

router = APIRouter(
    prefix="/product",
    tags=["Products"],
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="get all " + class_name + " records from database",
)
def get_all_controller(
        logintoken: Optional[str] = Header(...),
        key: Optional[Union[str, None]] = None,
        value: Optional[Union[str, None]] = None):
    """
    get all product records from database
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


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary=f"create a {class_name} record in database",
)
def create_controller(
    data: Products,
    logintoken: str = Header(default=None)
):
    """
    create a single product record in database
    Args:
        data:
    Returns:
        JSON Response
    """
    validate_token_client(logintoken)
    response, data = create_object_service(data)

    if response and data is not None:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,  # TODO cambiar por el estatus correspondiente
            content=data,
        )
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,  # TODO cambiar por el estatus correspondiente
        content=None,
    )


@router.patch(
    "/update/id/{product_id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="update a single product record in database",
)
def update_controller(
    id: str,
    data: Products,
    logintoken: str = Header(default=None)
):
    """
    update a single product record in database
    Args:
        id (str): user's user id
    Returns:
        JSON Response
    """
    validate_token_client(logintoken)
    result, response = update_object_service(data, class_name, id)
    if result:
        return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=response)
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=response)


@router.delete(
    "/delete/id/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    summary="delete a single product record in database",
)
def delete_controller(
    id: str,
    logintoken: str = Header(default=None)
):
    """
    delete a single product record in database
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
    "/categories",
    status_code=status.HTTP_202_ACCEPTED,
    summary="get all category products from database",
)
def get_categories_controller(
    logintoken: str = Header(default=None)
):
    """
    get all category products from database
    Returns:
        JSON Response
    """
    validate_token_client(logintoken)
    category_list = Get_Category_From_Collection_Service(class_name)
    if category_list != []:
        return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content=category_list)
    else:
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE, content=None)
