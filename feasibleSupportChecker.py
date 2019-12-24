from typing import Any, Dict, List, Tuple
import pulp
from itertools import product

class feasibleSupportChecker:
    
    @staticmethod 
    def andmaj(a: Tuple[int,...], s = 2) -> int:
        for i in range(s):
            assert(a[i] != 0)
        for i in range(s):
            assert(a[i] != 0)
            if a[i] < 0:
                return -1
        return 1

    @staticmethod
    def isFeasible(points: List[Tuple[int, ...]], d: int, s: int) -> Tuple[bool, List[Any]]:
        """
            points: a set of possible support points
            d: the degree of PTF we're testing against
            s: the fan-in of the AND gate

            returns True iff there exists a distribution over the given points with respect
            to which the correlation of AND-MAJ with every monomial is 0
        """

        N = len(points) 
        problem =  pulp.LpProblem("iwonderwhatthisdoes", pulp.LpMinimize)
        w = pulp.LpVariable.dicts("w", [i for i in range(N)])

        #Objective
        problem += 1
        #Sum of w_i is 1
        problem += pulp.lpSum([w[i]  for i in range(N)]) == 1
        #All w_i are positive
        for i in range(N):
            problem += w[i] >= 0
        #Correlation of ANDMAJ with each monomial
        for monomial in product(range(d+1), repeat = s):
            sum = 0
            for i in range(s):
                sum += monomial[i]
            if sum > d:
                continue
            prods = [1]*N
            for i in range(N):
                for j in range(s):
                    prods[i] *= points[i][j]**monomial[j]
            problem += pulp.lpSum([w[i]*feasibleSupportChecker.andmaj(points[i])*prods[i] for i in range(N)]) == 0

        problem.solve()
        if pulp.LpStatus[problem.status] == "Infeasible":
            return (False, [])
        else:
            distr = []
            for i in range(N):
                if w[i].varValue != 0:
                    distr.append((points[i], w[i].varValue))
            return (True, distr)
