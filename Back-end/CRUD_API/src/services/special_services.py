import datetime
from utils.hashing_util import hash_attribute
from utils.hash_passwd import hashing_util
from interfaces.repository_interface import Repo_Interface
from models.user import Users

def create_user_object_service(user_model: Users):
    """
    Especial service to create users in DB
    Args:
        object_model: User model to save in DB
        class_name: class of the model

    Returns:
        response: confirmation of transaction
        data: retrieve the data of th e saved object
    """
    from .standar_services import get_object_by_email_service
    # Define the model of the object
    class_name = user_model.__class__.__name__
    object_model = dict(user_model)

    # adds creation timestamp to the object
    date = datetime.datetime.now()
    object_model['date_create'] = date.strftime("%m/%d/%Y, %H:%M:%S:%f")
    object_model['updated'] = object_model['date_create']

    # todo cambiar esta forma  de crear el hash
    # prepare the string to hash
    str_to_hash = object_model['name']+object_model['date_create']

    # check by email if the user already exists
    object, check_exist = get_object_by_email_service(object_model['email'], class_name, object_model['category'])

    if object is None:
        # todo pasar "md5" por codigo, no quemar
        id = hash_attribute(str_to_hash, "md5")
        object_model['id'] = id
        object_model['password'] =  hash_attribute(hash_attribute(object_model['password'], "sha512"), "sha512")
        response, object_model = Repo_Interface.create_object_repository(object_model, id, class_name)

        for key in object_model.values():
            key.pop('password')

        if response:
            return response, object_model
        return response, None

    else:
        return {"user": "already exists"}, None