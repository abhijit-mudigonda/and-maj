#!/usr/bin/env/python
from feasibleSupportChecker import feasibleSupportChecker as fsc
import argparse
from typing import Any, Dict, List, Tuple


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--d_max", default = 6, type = int, action = "store", help = "Largest degree we check")
    parser.add_argument("--s", default = 2, type = int, action = "store", help = "Fan-in of the AND gate in AND-MAJ")
    args = parser.parse_args()
    s = args.s

    d = 1
    h = 2
    while(d <= args.d_max):
        points = [tuple(((-1)**int(signs[a]))*(h**int(exps[a])) for a in range(s)) for signs in fsc.genDigitStrings(s,2) for exps in fsc.genDigitStrings(s,d+1)]
        feasible, distr = fsc.isFeasible(points,d)
        if feasible is True:
            print("Found a feasible support set for d = ", d, " with n = ", h**d) 
            print(distr)
            d += 1
        else: 
            h += 1


