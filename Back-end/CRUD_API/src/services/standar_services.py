import datetime
from datetime import date
from utils.hashing_util import hash_attribute
from typing import Optional
from repositories.standar_repository import (
    Get_Category_From_Collection_Repository,
    create_object_repository,
    delete_object_repository,
    get_all_objects_repository,
    get_object_by_email_repository,
    get_object_repository,
    get_objects_by_name,
    update_object_repository,
    update_password_repository,
)

def get_all_objects_service(class_name: str, **filter_by):
    """
        get the object of the given class filter by given criteria
    Args:
        class_name: Model
        **filter_by:  criteria for filter data
    Returns:
        id_list: list of dicts with the data of the objects
    """
    result = get_all_objects_repository(class_name, **filter_by)
    id_list = []
    if result == None:
        return  id_list
    for item, value in result.items():
        value['id'] = item
        id_list.append(value)
    return id_list


def get_object_service(id: str, class_name: str):
    """
    Get a single record from database
    Args:
        id:  id of the model to retrieve data
        class_name:  class of the object
    Returns:
        data: a Dict with the data of the object
    """
    data = get_object_repository(id, class_name)
    return data


def get_object_by_email_service(email: str, class_name: str):
    """
    Get a single record from database searching by email
    Args:
        email:  email from object
        class_name:  class of the object
    Returns:
        data: a Dict with the data of the object
    """
    user, result = get_object_by_email_repository(email, class_name)
    return user, result


def create_object_service(object_model: any, class_name: Optional = None):
    """
    Get persistence of an object in db
    Args:
        object_model: model to save in DB
        class_name: class of the model

    Returns:
        response: confirmation of transaction
        data: retrieve the data of th e saved object
    """

    # Define the model of the object
    if class_name == None:
        class_name = object_model.__class__.__name__
    object_model = dict(object_model)

    # adds creation timestamp
    date = datetime.datetime.now()
    object_model['date_load'] = date.strftime("%m/%d/%Y, %H:%M:%S:%f")
    object_model['date_update'] = object_model['date_load']

    # prepare the string to hash
    str_to_hash = object_model['name']+object_model['date_load']

    # check by email if the user already exists
    if class_name != 'Products':
        object, check_exist = get_object_by_email_service(object_model['email'], class_name)
    else:
        object = None

    if object is None:
        id = hash_attribute(str_to_hash, "md5")
        object_model['id'] = id
        response, object_data = create_object_repository(object_model, id, class_name)
        if response:
            return response, object_data
        return response, None
    else:
        return {"user": "already exists"}, None


def delete_object_service(id: str, class_name: str):
    """
    Delete a single instance of the DB
    Args:
        id: id of the object to delete
        class_name:  class of the object

    Returns:
        response: State of transaction
    """
    response = delete_object_repository(id, class_name)
    return response


def update_object_service(object: any, class_name: str, id: str):
    """
    update a single instance of the object data
    Args:
        object: instance of object to update
        class_name:  class of the object
        id: id of the object
    Returns:
        result: object data updated
        response: confirmation of transaction
    """
    result, response = update_object_repository(object, id, class_name)
    return result, response


def update_password_service(object: any, class_name: str, id: str):
    """
    update a password of the single instance of the object
    Args:
        object: instance of object to update
        class_name:  class of the object
        id: id of the object
    Returns:
        result: object data updated
        response: confirmation of transaction
    """
    result, response = update_password_repository(object, id, class_name)
    return result, response


def Get_Category_From_Collection_Service(class_name: str):
    """
    Get a list with the categories of the given collection
    Args:
        class_name: class of the collection to retrieve data
    Returns:
        result: a list with the categories
    """
    result, response = Get_Category_From_Collection_Repository(class_name)
    if response:
        return result
    return None


def Get_Product_By_Name_Service(class_name: str, product_name: str):
    """
    Get a single product by name
    Args:
        class_name:  class of the object
        product_name:
    Returns:
        result: product data
    """
    products_by_name, result = get_objects_by_name(class_name, product_name)
    products_list=[]
    if result:
        products_list = [v for k, v in products_by_name.items()]
    return products_list


def get_all_emails_service(class_name: str, **filter_by):
    """
    get all email from the given class
    Args:
        class_name:  class of the object
        **filter_by:  filter criteria

    Returns:
        a dict with the emails
    """
    result = get_all_objects_repository(class_name, **filter_by)
    id_list = {}
    for item, value in result.items():
        id_list[item] = value['email']
    return id_list