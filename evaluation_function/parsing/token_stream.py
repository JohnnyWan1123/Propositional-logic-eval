from typing import List, Optional
from .token import Token, TokenType


class TokenStream:
    def __init__(self, tokens: List[Token]):
        self._tokens = tokens
        self._position = 0

    @property
    def current_token(self) -> Optional[Token]:
        if self._position >= len(self._tokens):
            return None
        return self._tokens[self._position]

    @property
    def position(self) -> int:
        return self._position

    def advance(self):
        if self._position < len(self._tokens):
            self._position += 1

    def peek(self, offset: int = 1) -> Optional[Token]:
        peek_pos = self._position + offset
        if peek_pos >= len(self._tokens):
            return None
        return self._tokens[peek_pos]

    def is_eof(self) -> bool:
        return self._position >= len(self._tokens) or (
            self.current_token is not None and self.current_token.type == TokenType.EOF
        )
