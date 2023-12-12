from typing import TypedDict
from enum import Enum


class Role(str, Enum):
    ASSISTANT = 'assistant'
    USER = 'user'
    SYSTEM = 'system'


class Message(TypedDict):
    role: Role
    content: str
