from typing import List
from models.message import Role, Message


class MessageLog:
    """Represents the log of messages exchanged between a user and assistant."""

    def __init__(self) -> None:
        self.messages: List[Message] = []

    def get_message_log(self) -> List[Message]:
        """Returns all the messages in the log."""
        return self.messages

    def add_user_message(self, text: str) -> None:
        message: Message = {'role': Role.USER, 'content': text}
        self._add_message(message)

    def add_assistant_message(self, text: str) -> None:
        message: Message = {'role': Role.ASSISTANT, 'content': text}
        self._add_message(message)

    def _add_message(self, message: Message) -> None:
        self.messages.append(message)
