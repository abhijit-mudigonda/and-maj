#!/usr/bin/env/python

from itertools import product
from typing import Any, Dict, List, Tuple
import argparse
from feasibleSupportChecker import feasibleSupportChecker as fsc


def getCoordinates(n: int):
    """
        Yields {-n, -n+1, ..., -1, 1, 2, ..., n}
    """
    yield from range(-n, 0)
    yield from range(1, n+1)


def anySupport(n, d, s):
    """
        checks over the s-dimensional hypercube with corners (+/- n, +/- n, ...) \ coordinateaxes to 
        see if there's a distribution that works
    """
    points = [point for point in product([x for x in getCoordinates(n)], repeat = s)]   
    feasible, distr = fsc.isFeasible(points, d, s)
    if feasible is True:
        print("Found a feasible support set for d = ", d, "n =", n)
        print(distr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("d", default = 2, type = int, action = "store", help = "The PTF degree")
    parser.add_argument("n_max", type = int, action = "store", help = "The largest allowable support point coordinate")
    parser.add_argument("-n_min", default = 1000, type = int, action = "store", help = "The value of n we start searching at")
    parser.add_argument("-s", default = 2, type = int, action = "store", help = "The fan-in of AND gate")
    args = parser.parse_args()
    d = args.d
    n_max = args.n_max
    n_min = args.n_min
    if n_min == 1000:
        n_min = n_max
    s = args.s

    for n in range(n_min, n_max+1):
        anySupport(n, d, s)
        
