#!/usr/bin/env/python

from itertools import product
from typing import Any, Dict, List, Tuple
import argparse
from feasibleSupportChecker import feasibleSupportChecker as fsc
import time


def getCoordinates(n: int):
    """
        Yields {-n, -n+1, ..., -1, 1, 2, ..., n}
    """
    yield from range(-n, 0)
    yield from range(1, n+1)


def anySupport(n, d, s, solver):
    """
        checks over the s-dimensional hypercube with corners (+/- n, +/- n, ...) \ coordinateaxes to 
        see if there's a distribution that works
    """
    points = [point for point in product([x for x in getCoordinates(n)], repeat = s)]   
    if solver == "gurobi":
        feasible, distr = fsc.isFeasible_gurobi(points, d, s)
    elif solver == "pulp":
        feasible, distr = fsc.isFeasible_pulp(points, d, s)
    else:
        raise ValueError("Not a valid solver")

    if feasible is True:
        print("Found a feasible support set for d = ", d, "n =", n)
        print(distr)
        return True
    else: 
        print("Failed to find a feasible support set")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("d", default = 2, type = int, action = "store", help = "The PTF degree")
    parser.add_argument("n_max", type = int, action = "store", help = "The largest allowable support point coordinate")
    parser.add_argument("-n_min", default = 1000, type = int, action = "store", help = "The value of n we start searching at")
    parser.add_argument("-s", default = 2, type = int, action = "store", help = "The fan-in of AND gate")
    parser.add_argument("-solver",  default = "pulp", type = str, action = "store", help = "Which LP optimizer/solver to use")

    args = parser.parse_args()
    d = args.d
    n_max = args.n_max
    n_min = args.n_min
    solver = args.solver

    if n_min == 1000:
        n_min = n_max
    s = args.s

    for n in range(n_min, n_max+1):
        print("Trying n = ", n)
        t0 = time.time()
        anySupport(n, d, s, solver)
        t1 = time.time()
        print("Took time ", t1-t0)
        
