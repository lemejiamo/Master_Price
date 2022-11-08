import logging
from typing import Optional, Union
from . import state
from repositories.firebase_repository import create_object_firebase_repository, get_object_by_email_firebase_repository
from repositories.mongodb_repository import create_object_mongo_repository, get_object_by_email_mongo_repository

class Repo_Interface():

    def create_object_repository(object: any, id: str, class_name: Optional = None) -> Union[bool, any]:

        if state == 2:
            response, object_data = create_object_firebase_repository(object, id, class_name)
            logging.debug('Petition to state 2')
            return response, object_data

        elif state == 3:
            response, object_data = create_object_mongo_repository(object, id, class_name)
            logging.debug('Petition to state 3')
            return response, object_data

        elif state == 5:
            create_object_mongo_repository(object, id, class_name)
            response, object_data = create_object_firebase_repository(object, id, class_name)
            logging.debug('Petition to state 5')
            return response, object_data

        return False, None

    def get_object_by_email_repository(email: str, class_name: str, category: str = None):
        """
        CRUD method for get a user by id
        """
        if state == 2:
            response, object_data,  = get_object_by_email_firebase_repository(email, class_name, category)
            logging.debug('Petition to state 2')
            return object_data, response

        elif state == 3:
            response, object_data  = get_object_by_email_mongo_repository(email, class_name, category)
            logging.debug('Petition to state 3')
            return object_data, response

        elif state == 5:
            get_object_by_email_mongo_repository(email, class_name, category)
            response, object_data = get_object_by_email_firebase_repository(email, class_name, category)
            logging.debug('Petition to state 5')
            return object_data, response

        return False, None

    # def get_all_objects_repository(class_name: str, **filter_by):
    #     """
    #     CRUD method to retrive all objects of a certain collection
    #     Args:
    #         object: a class to retrieve the data
    #     Returns:
    #
    #     """
    #     pass
    #
    #
    # def get_object_repository(id: str, class_name: str):

    #     """
    #     Args:
    #         id: unique id from the given user
    #         class_name: class of the object
    #     Returns:
    #         retrieve data from the given id
    #     """
    #
    #
    # def delete_object_repository(id: str, class_name: str) -> bool:
    #     pass
    #
    #

    #
    # def update_object_repository(object: any,id: str,class_name: str):
    #     pass
    #
    # def update_password_repository(object: any, id: str,class_name: str):
    #     pass
    #
    # def get_objects_by_name(class_name: str, product_name: str):
    #     pass
    #
    # def Get_Category_From_Collection_Repository(class_name: str):
    #     pass
    #
    # if state == 0:
    #     # todo levantar la excepcion respectiva
    #     print("error bases de datos no inicializadas")
    #
    # elif state == 2:
    #     print("elevando peticion a firebase")
    #     pass
    #
    # elif state == 3:
    #     print('elevando peticion a MONGO')
    #     pass
    #
    # elif state == 5:
    #     print('elevando peticion tipo 2')
    #     pass
    #
