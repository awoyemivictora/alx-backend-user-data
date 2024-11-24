#!/usr/bin/env python3
import bcrypt


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
