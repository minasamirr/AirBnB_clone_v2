#!/usr/bin/python3
"""
This module defines the DBStorage class
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """
    This class manages the database storage
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Creates the engine, the session, and calls the reload() method
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                       .format(getenv('HBNB_MYSQL_USER'),
                                               getenv('HBNB_MYSQL_PWD'),
                                               getenv('HBNB_MYSQL_HOST'),
                                               getenv('HBNB_MYSQL_DB')),
                                       pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of all objects
        """
        objs = {}
        classes = [User, State, City, Amenity, Place, Review]
        if cls:
            classes = [cls]
        for c in classes:
            for obj in self.__session.query(c).all():
                objs[obj.__class__.__name__ + '.' + obj.id] = obj
        return objs

    def new(self, obj):
        """
        Adds the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes obj from the current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database and creates the current database
        session
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """
        Calls remove() on the private session attribute or close() on the
        class Session
        """
        self.__session.remove()
