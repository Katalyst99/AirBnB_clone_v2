#!/usr/bin/python3
"""This is the DBStorage module"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """The DBStorage class handles storage in mysql database for HBNB"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of new instance"""
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        l_host = getenv('HBNB_MYSQL_HOST')
        dbase = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format
                                      (user, passwd, l_host, dbase),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method to return Dictionary"""
        cls_dict = {}
        if cls is None:
            obj_all = [User, State, City, Amenity, Place, Review]
            for cls_name in obj_all:
                objs = self.__session.query(cls_name).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    cls_dict[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = cls.__class__.__name__ + "." + obj.id
                cls_dict[key] = obj
        return cls_dict

    def new(self, obj):
        """Method to add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Method to commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Method to delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Method to reload and recreate all tables in the database"""
        Base.metadata.create_all(self.__engine)
        sesh = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sesh)
        self.__session = Session()

    def close(self):
        """Method to close the session"""
        self.__session.close()
