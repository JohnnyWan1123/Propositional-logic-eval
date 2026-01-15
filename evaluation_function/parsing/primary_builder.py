from ..domain.formula import Formula, Atom, Truth, Falsity, Negation
from .token_stream import TokenStream
from .token import TokenType
from .expression_builder import ExpressionBuilder


class PrimaryBuilder(ExpressionBuilder):
    def __init__(self, expression_builder: ExpressionBuilder):
        self._expression_builder = expression_builder

    def build(self, stream: TokenStream) -> Formula:
        token = stream.current_token
        if token is None:
            raise ValueError("Unexpected end of input")

        if token.type == TokenType.TRUTH:
            stream.advance()
            return Truth()

        if token.type == TokenType.FALSITY:
            stream.advance()
            return Falsity()

        if token.type == TokenType.NEGATION:
            stream.advance()
            operand = self.build(stream)
            return Negation(operand)

        if token.type == TokenType.LEFT_PAREN:
            stream.advance()
            formula = self._expression_builder.build(stream)
            if stream.current_token is None or stream.current_token.type != TokenType.RIGHT_PAREN:
                raise ValueError(f"Expected ')' at position {stream.position}")
            stream.advance()
            return formula

        if token.type == TokenType.ATOM:
            atom_name = token.value
            stream.advance()
            return Atom(atom_name)

        raise ValueError(f"Unexpected token {token.type.name} at position {token.position}")
