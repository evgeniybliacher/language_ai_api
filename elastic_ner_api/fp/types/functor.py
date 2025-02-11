from abc import abstractmethod

from typing import Self, TypeVar, Protocol, Callable, runtime_checkable

from elastic_ner_api.fp.types.lambda_types import typed_lambda


TSource = TypeVar('TSource', covariant=True)
TResult = TypeVar('TResult')

@runtime_checkable
class Functor(Protocol[TSource]):
    """The Functor class is used for types that can be mapped over.

    Instances of Functor should satisfy the following laws:

    Haskell:
    fmap id  ==  id
    fmap (f . g)  ==  fmap f . fmap g

    Python:
    x.map(id) == id(x)
    x.map(compose(f, g)) == x.map(g).map(f)

    The instances of Functor for lists, Maybe and IO satisfy these laws.
    """

    @abstractmethod
    def map(self, fn: typed_lambda[TSource,TResult]) -> Self:
        """Map a function over wrapped values.

        Map knows how to apply functions to values that are wrapped in
        a context.
        """
        ...
        
    # def __rmod__(self, fn):
    #     """Infix version of map.

    #     Haskell: <$>

    #     Example:
    #     >>> (lambda x: x+2) % Just(40)
    #     42

    #     Returns a new Functor.
    #     """
    #     return self.map(fn)