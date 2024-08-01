#!/usr/bin/env python3
"""11. More involved type annotations"""


from typing import Mapping, Any, Union, TypeVar


X = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                    default = Union[X, None]) -> Union[Any, X]:
    """Given the parameters and the return values,
    add type annotations to the function"""
    if key in dct:
        return dct[key]
    else:
        return default
