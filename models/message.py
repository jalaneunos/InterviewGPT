from typing import TypedDict
from enum import Enum


class Role(str, Enum):
    ASSISTANT = 'assistant'
    USER = 'user'


class Message(TypedDict):
    role: Role
    content: str
