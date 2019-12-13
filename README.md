This code is for proving lower bounds on the degree of a polynomial threshold function for the Boolean function (s,t)-AND-MAJ, the conjunction of s majority gates each with fan-in t. The case of s=2 was mostly resolved in a paper of [OS10][https://www.cs.cmu.edu/~odonnell/papers/ptf-degree.pdf], which showed a lower bound of O(log t/log log t), almost matching the s=2 upper bound of O(log t) achieved by [BRS91][http://www.cs.columbia.edu/~rocco/Teaching/S12/Readings/BRS.pdf]. The best known upper bounds for the case of general s are O(slog s log t) and O(\sqrt(t)log s) by BRS and [ACW16][https://arxiv.org/pdf/1608.04355.pdf]. This code generalizes the linear programming approach of OS10 to higher s. 



