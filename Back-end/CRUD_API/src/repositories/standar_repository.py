import logging
from datetime import datetime
from typing import Optional

import firebase_admin.exceptions
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from . import db, db_app

def create_object_repository(object: any, id: str, class_name: Optional = None) -> bool:
    """
    CRUD method to create a API USER
    """
    if class_name is None:
        collection = object.__class__.__name__
    else:
        collection = class_name
    try:
        ref = db.reference(f"{collection}/{id}/", db_app)  # todo corregir referencia
        object['date_load'] = datetime.now()
        object['date_update'] = object['date_load']
        object_data = jsonable_encoder(object)
        ref.set(object_data)
        final_json = {str(id): object_data}
        return True, final_json
    except Exception as ex:
        logging.error(f"cant created user error: {ex}")
        return False


def get_all_objects_repository(class_name: str, **filter_by):
    """
    CRUD method to retrive all objects of a certain collection
    Args:
        object: a class to retrieve the data
    Returns:

    """
    try:
        ref = db.reference(f"/{class_name}/", db_app)
        if filter_by == {}:
            results = ref.get()
        else:
            results = (
                ref.order_by_child(filter_by["field"])
                .equal_to(filter_by["value"])
                .get()
            )
        return results
    except Exception as ex:
        logging.error(f"the error is: {ex}")
        return None


def get_object_repository(id: str, class_name: str):
    """
    Args:
        id: unique id from the given user
        class_name: class of the object
    Returns:
        retrieve data from the given id
    """
    try:
        ref = db.reference(f"/{class_name}/{id}", db_app)
        data = ref.get()
        return data
    except Exception as ex:
        logging.error(f"the error is: {ex}")
        return None


def delete_object_repository(id: str, class_name: str) -> bool:
    try:
        ref = db.reference(f"/{class_name}/{id}", db_app)
        data = ref.get()
        if data is None:
            return False
        ref.delete()
        data = ref.get()
        if data is None:
            return True
        return False
    except Exception as ex:
        logging.error(f"the error is: {ex}")
        return False


def get_object_by_email_repository(email: str, class_name: str):
    """
    CRUD method for get a user by id
    """
    try:
        ref = db.reference(f"{class_name}", db_app)
        all_results = dict(ref.order_by_child("email").equal_to(email).get())
        if all_results is None or all_results == {}:
            return None, True
        json_user = {
            list(all_results.keys())[0]: all_results[list(all_results.keys())[0]]
        }
        return json_user, True
    except HTTPException as ex:
        logging.error(f"At get_user_by_id_repository: {ex}")
        return None, False
    except firebase_admin.exceptions.InvalidArgumentError as arg_error:
        logging.error(f"Error en el argumento de busqueda email {email}")
        return None, True

def update_object_repository(
    object: any,
    id: str,
    class_name: str,
):

    check_exits = get_object_repository(
        id,
        class_name,
    )
    try:
        if check_exits is not None:
            ref = db.reference(f"/{class_name}/{id}", db_app)
            object.date_update = datetime.now()
            jsonified_object = jsonable_encoder(object)
            data = {k: v for k, v in jsonified_object.items() if v is not None}
            ref.update(data)
            return True, data
        else:
            return False, None

    except HTTPException as ex:
        logging.error(f"At update_object_repository: {ex}")
        return JSONResponse(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            content={
                "error": f"failed to update object  with id {id} class: {class_name}",
                "message": f"{ex.detail}",
            },
        )


def update_password_repository(
    object: any,
    id: str,
    class_name: str,
):

    check_exits = get_object_repository(
        id,
        class_name,
    )
    try:
        if check_exits is not None:
            ref = db.reference(f"/{class_name}/{id}", db_app)
            object.date_update = datetime.now()
            object.password = object.new_password
            delattr(object, "new_password")
            jsonified_object = jsonable_encoder(object)
            data = {k: v for k, v in jsonified_object.items() if v is not None}
            ref.update(data)
            return True, data
        else:
            return False, None

    except HTTPException as ex:
        logging.error(f"At update_object_repository: {ex}")
        return JSONResponse(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            content={
                "error": f"failed to update object  with id {id} class: {class_name}",
                "message": f"{ex.detail}",
            },
        )


def get_objects_by_name(class_name: str, product_name: str):
    ref = db.reference(f"/{class_name}/", db_app)
    results_by_name = ref.order_by_child("name").equal_to(product_name).get()
    if results_by_name is None or results_by_name == {}:
        return None, False
    return results_by_name, True


def Get_Category_From_Collection_Repository(class_name: str):
    ref = db.reference(f"/{class_name}/", db_app)
    result = ref.get()
    category_list = []
    for key, value in result.items():
        if value["category"] not in category_list:
            category_list.append(value["category"])
    if category_list is []:
        return None, False
    return category_list, True
