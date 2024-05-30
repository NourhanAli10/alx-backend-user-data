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
