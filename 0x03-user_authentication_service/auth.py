#!/usr/bin/env python3
from db import DB
from user import User
from bcrypt import hashpw, gensalt
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid
from typing import Optional


class Auth:
    def __init__(self):
        self._db = DB()

    def valid_login(self, email: str, password: str) -> bool:
        """
        Check if a user can log in with the provided email and password.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            bool: True if login is valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            # bcrypt.checkpw expects bytes, so encode the password
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
        except NoResultFound:
            return False
        return False

    def create_session(self, email: str) -> Optional[str]:
        """
        Create a session ID for the user with the given email.

        Args:
            email (str): The email of the user to create a session for.

        Returns:
            Optional[str]: The session ID if the user exists,
             or None if the user does not exist.
        """
        try:
            # Find the user by email
            user = self._db.find_user_by(email=email)
            if not user:
                return None

            # Generate a new session ID
            session_id = _generate_uuid()

            # Update the user's session_id in the database
            self._db.update_user(user.id, session_id=session_id)

            return session_id

        except Exception as e:
            return None

    def get_user_from_session_id(self, session_id: str):
        """
        Retrieve a user by their session ID.

        Args:
            session_id (str): The session ID.

        Returns:
            User or None: The user corresponding to the session ID, or None
        """
        if session_id is None:
            return None

        try:
            # Query the database for a user with the given session_id
            user = self._db.find_user_by(session_id=session_id)
        except Exception:
            # If no user is found, return None
            return None

        return user


# Private utility function for generating UUIDs
def _generate_uuid() -> str:
    """
    Generate a new UUID and return its string representation.

    Returns:
        str: A string representation of a new UUID.
    """
    import uuid
    return str(uuid.uuid4())


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt and returns theh salted hash as bytes.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted hashh of the password.
    """
    # Generate a salt
    salt = bcrypt.gensalt()
    # Generate the hashed password using bcrypt.hashpw
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def register_user(self, email: str, password: str) -> User:
    """
    Registers a new user with thhe given email and password.

    Args:
        email (str): User's email.
        password (str): User's password.

    Returns:
        User: The created user object.

    Raises:
        ValueError: If a user with the given email already exists.
    """
    # Check if a user with the provided email already exists
    try:
        self._db.find_user_by(email=email)
        # If no exception is raised, the user exists
        raise ValueError(f"User {email} already exists")
    except NoResultFound:
        # User does not exist; proceed with creation
        hashed_password = self._hash_password(password)
        new_user = self._db.add_user(email, hashed_password.decode('utf-8'))
        return new_user


def _generate_uuid() -> str:
    """
    Generate a new UUID and return its string representation.

    Returns:
        str: A string representation of a new UUID.
    """
    return str(uuid.uuid4())
