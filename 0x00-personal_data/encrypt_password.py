#!/usr/bin/env python3
"""
encrypt_password.py
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """expects one string argument name password
    and returns a salted, hashed password, which is a byte string."""
    salt: bytes = bcrypt.gensalt()
    hashed: bytes = bcrypt.hashpw(password.encode(), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password against a hashed password using bcrypt.

    Args:
    - hashed_password (bytes): The hashed password stored in bytes.
    - password (str): The password to validate.

    Returns:
    - bool: True if the password matches the hashed password, False otherwise.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
