#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self._session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database.


        Args:
            email (str): The user's email.
            hashed_password (str): The user's hashed password.


        Returns:
            User: The newly created user object.
        """
        # Create a new user instance
        new_user = User(email=email, hashed_password=hashed_password)

        # Add the user to the sessioni and commit to save it in the database
        self._session.add(new_user)
        self._session.commit()

        # Return the new user instance
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by arbitrary keyword arguments.

        Args:
            **kwargs: Arbitrary keword argumentts to filter the User table.

        Returns:
            User: The first user row matching the filter criteria.

        Raises:
            NoResultFound: If no user matches the criteria.
            InvalidRequestError: If the query contains invalid field namems.
        """
        if not kwargs:
            raise InvalidRequestError("No query argumentts provided.")

        try:
            # Query the first result matching the filter criteria
            user = self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("No user found with the provided criteria.")
        except Exception as e:
            raise InvalidRequestError(f"Invalid query argument: {e}")

        return user
