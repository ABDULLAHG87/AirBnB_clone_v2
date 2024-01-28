#!/usr/bin/python3
"""Database stroage engins using SQLAlchemy with a mysql database connetion"""

import os
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

name_to_class = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}

class DBStorage:
    """Datebase storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of instance variables"""
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__egnine = create_engine('mysql+mysqldb://{}:{}@{}'
                                       .format(user, passwd, host, database))
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns all objects presents in the dictionary"""
        if not self.__session:
            self.reload()
        objects = {}
        if type(cls) == str:
            cls = name_to_class.get(cls, None)
        if cls:
            for obj in self.__session.query(cls):
                objects[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for cls in name_to_class.values():
                for obj in self.__session.query(cls):
                    objects[obj.__class__.__name__ + '.' + obj.id] = obj
        return objects

    def reload(self):
        """method that reloads objects from the database"""
        session_factory = sesionmaker(bind=self.__egnine,
                                      expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(session_factory)

    def new(self, obj):
        """create a new object"""
        self.__session.add(obj)

    def save(self, obj):
        """Save  a new object to as session"""
        self.__session.commit(obj)

    def delete(self, obj):
        """Delete a  object"""
        if not self.__session:
            self.reload()
        if obj:
            self.__session.delete(obj)

    def close(self, obj):
        """create a new object"""
        self.__session.remove(obj)

    def count(self, cls=None):
        """methods that counts the number of objects"""
        total = 0
        if type(cls) == str and cls in name_to_class:
            cls = name_to_class[cls]
            total = self.__sessin.query(cls).count()
        elif cls is None:
            for cls in name_to_class.values():
                total = self.__session.query(cls).count()
        return total

    def get(self, cls, id):
        """Retrieve object based on it id"""
        if cls is not None  and type(cls) is str:
            if id is not None and type(id) is str:
                if cls in name_to_class:
                    cls = name_to_class[cls]
                    result = self.__session.query(cls).filter(cls.id == id)\
                                                      .first()
                    return result
                else:
                    return None
