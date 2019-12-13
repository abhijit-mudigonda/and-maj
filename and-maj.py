#!/usr/bin/env/python

from itertools import combinations
from typing import Any, Dict, List, Tuple
import pulp
import argparse
import math


def subsetGenerator(a: List[Any], r: int) -> List[Any]:
    yield from combinations(a, r)

def getCoordinates(n):
    yield from range(-n, 0)
    yield from range(1, n+1)

def andmaj(a: Tuple[int,int]) -> int:
    assert(a[0] != 0)
    assert(a[1] != 0)
    if a[0] > 0 and a[1] > 0:
        return 1
    return -1


def isFeasible(points: List[Tuple[int, int]], d: int) -> Tuple[bool, List[Any]]:
    """
        points: a set of possible support points
        d: the degree of PTF we're testing against

        returns True iff there exists a distribution over the given points with respect
        to which the correlation of AND-MAJ with every monomial is 0
    """

    problem =  pulp.LpProblem("iwonderwhatthisdoes", pulp.LpMinimize)
    w = pulp.LpVariable.dicts("w", [i for i in range(len(points))])

    #Objective
    problem += 1
    #Sum of w_i is 1
    problem += pulp.lpSum([w[i]  for i in range(len(points))]) == 1
    #All w_i are positive
    for i in range(len(points)):
        problem += w[i] >= 0
    #Correlation of ANDMAJ with each monomial
    for a in range(d+1):
        for b in range(d-a+1):
            problem += pulp.lpSum([w[i]*(andmaj(points[i]))*(points[i][0]**a)*(points[i][1]**b) for i in range(len(points))]) == 0
    #print(problem.constraints)
    problem.solve()
    if pulp.LpStatus[problem.status] == "Infeasible":
        return (False, [])
    else:
        distr = []
        for i in range(len(points)):
            if w[i].varValue != 0:
                distr.append((points[i], w[i].varValue))
        return (True, distr)

def bruteForceSearch(n: int, d: int) -> List[List[Tuple[int,int]]]: 
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
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", default = 23, type = int, action = "store", help = "The largest allowable support point coordinate")
    parser.add_argument("--d", default = 2, type = int, action = "store", help = "The PTF degree")
    parser.add_argument("--n_low", default = 1, type = int, action = "store", help = "The value of n we start searching at")
    parser.add_argument("--h", default = 600, type = int, action = "store", help = "The value of n we start searching at")
    args = parser.parse_args()
    n = args.n
    d = args.d
    n_low = args.n_low

    for i in range(n_low,n+1):
        print("Trying n = ", i)
        #points = [(j,k) for j in getCoordinates(i) for k in getCoordinates(i)]
        for h in range(2,args.h):
            points = [(((-1)**a)*(h**j),((-1)**b)*(h**k)) for j in range(d+1) for k in range(d+1) for a in [0,1] for b in [0,1]]
            feasible, distr = isFeasible(points,d)
            if feasible is True:
                print("Found a feasible support set for n =", i, "d = ", d)
                print(distr)
                #print(bruteForceSearch(i,d))
