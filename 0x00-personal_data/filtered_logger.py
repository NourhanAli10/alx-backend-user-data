#!/usr/bin/env python3
"""
filtered_logger.py
"""

import re
import logging
from typing import List, Tuple


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (List[str]): List of fields to obfuscate.
        redaction (str): The string to replace field values with.
        message (str): The original log message.
        separator (str): The separator used in the log message.

    Returns:
        str: The obfuscated log message.
    """
    pattern = f"({'|'.join(fields)})=[^;{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class to obfuscate sensitive
    information in log records.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initializes the formatter with the specified fields to redact.

        Args:
            fields (List[str]): List of fields to obfuscate.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the log record, redacting specified fields.

        Args:
            record (logging.LogRecord): The original log record.

        Returns:
            str: The formatted and obfuscated log record.
        """
        original_message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original_message, self.SEPARATOR)


PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """
    Creates and returns a logger object.

    The logger is named "user_data" and logs up to INFO level.
    It does not propagate messages to other loggers.
    It has a StreamHandler with RedactingFormatter as formatter.

    Returns:
        logging.Logger: Configured logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger
