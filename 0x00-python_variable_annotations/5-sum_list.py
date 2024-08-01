#!/usr/bin/env python3
"""5. Complex types - list of floats"""

import List from typing


def sum_list(input_list: List[float]) -> float:
    """function sum_list which takes a list input_list of
    floats as argument and returns their sum as a float."""
    return float(sum(input_list))
