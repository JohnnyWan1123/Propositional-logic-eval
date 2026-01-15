from abc import ABC, abstractmethod
from typing import Optional
from .character_stream import CharacterStream
from .token import Token, TokenType


class TokenMatcher(ABC):
    @abstractmethod
    def matches(self, stream: CharacterStream) -> bool:
        pass

    @abstractmethod
    def create_token(self, stream: CharacterStream) -> Token:
        pass


class SingleCharTokenMatcher(TokenMatcher):
    def __init__(self, char: str, token_type: TokenType):
        self._char = char
        self._token_type = token_type

    def matches(self, stream: CharacterStream) -> bool:
        return stream.current_char == self._char

    def create_token(self, stream: CharacterStream) -> Token:
        position = stream.position
        stream.advance()
        return Token(self._token_type, self._char, position)


class AtomTokenMatcher(TokenMatcher):
    def __init__(self, allowed_chars: str = "'"):
        self._allowed_chars = allowed_chars

    def matches(self, stream: CharacterStream) -> bool:
        char = stream.current_char
        return char is not None and (char.isalnum() or char in self._allowed_chars)

    def create_token(self, stream: CharacterStream) -> Token:
        position = stream.position
        atom_name = ""
        
        while stream.current_char is not None:
            char = stream.current_char
            if char.isalnum() or char in self._allowed_chars:
                atom_name += char
                stream.advance()
            else:
                break
        
        if not atom_name:
            raise ValueError(f"Empty atom at position {position}")
        
        return Token(TokenType.ATOM, atom_name, position)


class EOFTokenMatcher(TokenMatcher):
    def matches(self, stream: CharacterStream) -> bool:
        return stream.is_eof()

    def create_token(self, stream: CharacterStream) -> Token:
        return Token(TokenType.EOF, "", stream.position)
