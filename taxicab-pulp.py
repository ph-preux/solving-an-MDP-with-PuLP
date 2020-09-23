#
# Resolution of Howard's taxicab MDP by linear programming.
#
# Demo code to illustrate how to solve an MDP with LP in Python.
#
# philippe.preux@univ-lille.fr
# Sep 2020
#
'''
 This code has been developed and is provided to the community only to
 serve as a demonstrator. It might not work on your computer, it mght not
 meet your expectations. In any case, this code has not been made in order
 to cause any harm neither to anyone, nor to any computer, nor to anything.
 That being said, you use this code under your own responsability, and risks.

 This code is freely available under MIT licence.
'''

import numpy as np
import pulp

# definition of the MDP
N = 3 # nb of states
A = 3 # nb of actions
# the transition tensor: P [current state, action, next state] = probability of transiting to next state when emitting action in current state
P = np.array ([[[1/2, 1/4, 1/4],
                [1/16, 3/4, 3/16],
                [1/4, 1/8, 5/8]], 
               [[1/2, 0, 1/2],
                [0,0,0],
                [1/16, 7/8, 1/16]],
               [[1/4, 1/4, 1/2], 
                [1/8, 3/4, 1/8], 
                [3/4, 1/16, 3/16]]])
# the return function: expected return when transiting to next state when emitting action in current state
R = np.array ([10, 4, 8, 8, 2, 4, 4, 6, 4, 14, 0, 18, 0, 0, 0, 8, 16, 8, 10, 2, 8, 6, 4, 2, 4, 0, 8])
R = R.reshape ([N, A, N])
gamma = .9

# define the LP
v = pulp.LpVariable.dicts ("s", (range (N))) # the variables
prob = pulp.LpProblem ("taxicab", pulp.LpMinimize) # minimize the objective function
prob += sum ([v [i] for i in range (N)]) # defines the objective function
# now, we define the constrain: there is one for each (state, action) pair.
for i in range (N):
    for a in range (0, 3):
        prob += v [i] - gamma * sum (P [i, a, j] * v [j] for j in range(N)) >= sum (P [i, a, j] * R [i, a, j] for j in range(N))

# Solve the LP
prob.solve ()
# after resolution, the status of the solution is available and can be printed:
# print("Status:", pulp.LpStatus[prob.status])
# in this case, it should print "Optimal"

# extract the value function
V = np.zeros (N) # value function
for i in range (N):
    V [i] = v [i]. varValue

# extract the optimal policy
pi_star = np.zeros ((N), dtype=np.int64)
vduales = np.zeros ((N, 3))
s = 0
a = 0
for name, c in list(prob.constraints.items()):
    vduales [s, a] = c.pi
    if a < A - 1:
        a = a + 1
    else:
        a = 0
        if s < N - 1:
            s = s + 1
        else:
            s = 0
for s in range(N):
    pi_star [s] = np.argmax (vduales [s, :])
