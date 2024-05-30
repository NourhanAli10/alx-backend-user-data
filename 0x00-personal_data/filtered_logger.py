#!/usr/bin/env python3
"""
filtered_logger.py
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns the log message obfuscated """
    pattern = f"({'|'.join(fields)})=[^;{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
