#!/usr/bin/env python3
"""
encrypt_password.py
"""

import bcrypt

def hash_password(password):
    """expects one string argument name password
    and returns a salted, hashed password, which is a byte string."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed
