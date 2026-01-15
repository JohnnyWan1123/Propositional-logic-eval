from typing import Optional


class CharacterStream:
    def __init__(self, text: str):
        self._text = text
        self._position = 0

    @property
    def current_char(self) -> Optional[str]:
        if self._position >= len(self._text):
            return None
        return self._text[self._position]

    @property
    def position(self) -> int:
        return self._position

    def advance(self):
        if self._position < len(self._text):
            self._position += 1

    def peek(self, offset: int = 1) -> Optional[str]:
        peek_pos = self._position + offset
        if peek_pos >= len(self._text):
            return None
        return self._text[peek_pos]

    def is_eof(self) -> bool:
        return self._position >= len(self._text)
