from typing import ByteString
from . import hashing_util


def to_hash(string: str) -> bytes:
    string = hashing_util(string, 'sha512')
    return bytes(string)
