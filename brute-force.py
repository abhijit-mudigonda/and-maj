#!/usr/bin/env/python

from itertools import combinations
from typing import Any, Dict, List, Tuple
import argparse
import math

def subsetGenerator(a: List[Any], r: int) -> List[Any]:
    yield from combinations(a, r)

if __name__ == "__main__":
    """
        n: the largest coordinate of any support point
        d: the degree of PTF we're testing against

        return: 

        Searches through subsets of the relevant points for a given n
        and prints all the satisfying support sets for this d.  
    """
    points = [(i,j) for i in getCoordinates(n) for j in getCoordinates(n)]
    D = math.ceil((d+1)*(d+2)/2)
    subsets = []
    for subset in subsetGenerator(points, D):
        if isFeasible(subset, d) is True:
            subsets.append(subset)
            print(subset)
    return subsets
     
