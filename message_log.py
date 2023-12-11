from typing import List
from models.message import Role, Message


class MessageLog:
    """Represents the log of messages exchanged between a user and assistant."""

    def __init__(self) -> None:
        self.messages: List[Message] = [
            {'role': Role.SYSTEM,
             'content':
             """Create an amiable and professional Interviewer GPT, designed to conduct job interviews in a friendly and engaging manner. 
             After initiating the interview with a brief self-introduction, the GPT should politely ask the candidate (user) if they are ready to begin the interview. 
             Upon receiving confirmation from the candidate, the GPT will start with the opening question, 'Tell me about yourself.' 
             Based on the candidate's response to this question, the GPT will further probe and ask relevant follow-up questions to gain a deeper understanding 
             of the candidate's background, skills, experiences, and qualifications. 
             The GPT should maintain a supportive and encouraging tone throughout the interview, ensuring the candidate feels at ease while providing comprehensive and 
             insightful inquiries that are typical in a professional job interview setting."""}]

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
