from typing import Any, Dict, List, Tuple
import pulp

class feasibleSupportChecker:
    @staticmethod
    def genDigitStrings(l: int, m: int):
        """
            iterates through the strings in [0,m-1]^l
        """
        out = [0]*l
        for step in range(m**l):
            yield ''.join(map(str,out))
            for i in reversed(range(l)):
                if out[i] != m-1:
                    out[i] += 1
                    break
                else:
                    out[i] = 0
     
    @staticmethod 
    def andmaj(a: Tuple[int,int], s = 2) -> int:
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
        for monomial in itertools.product(range(d+1), repeat = s):
            prod = 1
            for j in range(s):
                prod *= points[i][j]**monomial[j]
            problem += pulp.lpSum([w[i]*prod for i in range(len(points))]) == 0

        problem.solve()
        if pulp.LpStatus[problem.status] == "Infeasible":
            return (False, [])
        else:
            distr = []
            for i in range(len(points)):
                if w[i].varValue != 0:
                    distr.append((points[i], w[i].varValue))
            return (True, distr)


