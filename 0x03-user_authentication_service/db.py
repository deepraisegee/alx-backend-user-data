#!/usr/bin/env python3
"""DB module
"""

# import bcrypt

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """create user and save to database"""
        user = User(email=email, hashed_password=hashed_password)
        # user.email = email
        # password = hashed_password.encode("utf-8")
        # salt = bcrypt.gensalt()
        # user.hashed_password = bcrypt.hashpw(password, salt)
        # user.hashed_password = hashed_password
        # save ro db
        self._session.add(user)
        self._session.commit()

        return user
