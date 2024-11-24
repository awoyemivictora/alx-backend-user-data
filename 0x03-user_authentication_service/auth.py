#!/usr/bin/env python3
from db import DB
from user import User
from bcrypt import hashpw, gensalt


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
