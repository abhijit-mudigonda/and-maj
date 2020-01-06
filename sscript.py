from typing import Any, Dict, List, Tuple
from any_supports import anySupport
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s_max", default = 10, type = int, action = "store", help = "The fan-in of the AND gate")
    parser.add_argument("-s_min", default = 2, type = int, action = "store", help = "The fan-in of the AND gate")
    parser.add_argument("-d", default = 2, type = int, action = "store", help = "The PTF degree")
    parser.add_argument("-n_max", default = 23, type = int, action = "store", help = "The largest allowable support point coordinate")
    parser.add_argument("-solver",  default = "pulp", type = str, action = "store", help = "Which LP optimizer/solver to use")
    args = parser.parse_args()
    d = args.d
    n_max = args.n_max
    s_min = args.s_min
    s_max = args.s_max
    solver = args.solver

    f = open("out.txt", "a")
    n = 23
    for s in range(s_min, s_max):
        if anySupport(n,2,s,solver) is True:
            print("s = {0}, n = {1}".format(s,n))
            f.write("s = {0}, n = {1}\n".format(s,n))
            s += 1
            n -= 1
        else:
            print("s = {0}, n = {1}".format(s,n+1))
            f.write("s = {0}, n = {1}\n".format(s,n+1))
            s += 1
    f.close()
