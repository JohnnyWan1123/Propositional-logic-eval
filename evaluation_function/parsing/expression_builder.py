from abc import ABC, abstractmethod
from ..domain.formula import Formula
from .token_stream import TokenStream


class ExpressionBuilder(ABC):
    @abstractmethod
    def build(self, stream: TokenStream) -> Formula:
        pass
