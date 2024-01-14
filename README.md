# Demo of a python code to solve a Markov Decision Problem with PuLP

[This code has moved to this place](https://philippe-preux.github.io/software/solving-an-MDP-with-PuLP).

I just leave the Readme here.

## Purpose of this repo

I wanted to solve MDPs with linear programming in python. [On this blog post](https://towardsdatascience.com/linear-programming-and-discrete-optimization-with-python-using-pulp-449f3c5f6e99), I read about the PuLP package that solves LPs in python. As I am not fluent in Python, it took me a couple of days to figure out how to do it. So, I report my experience here and provide some very basic examples. Hope this helps!

This repo is absolutly not dealing with what LP is, what MDPs are, how to express an MDP as an LP. This is well documented elsewhere. If you do not know what I am talking baout, this repo is not for you.

This repo only concerns small MDPs. The purpose is not to show how one can solve large MDPs with LP (anyway, I do not think this is a good idea in the first place because of we know more efficient algorithms to solve MDPs than LP); my goal is simply to show how to use PuLP to solve an MDP.


## MDP being solved

I will consider Howard's taxicab example: 3 states, 2 or 3 actions per state, discounted MDP.

The MDP is defined at the beginning of the example code:
- variable ``N'' contains the number of states = 3, named A, B, and C.
- variable ``A'' contains the number of different ations = 3. In state A and C, all 3 actions are possible. In state B, only actions 1 and 3 are possible.
- variable ``P'' contains the transition function expressed as a tensor (3D array)
- variable ``P'' contains the return function expressed as a tensor (3D array)

## Resolution

We need to define the LP. The objective is the sum of the value of each state. There is a constraing for each state, action pair.
Then, we simply call the ``solve()'' function.

## Results

The solution to the primal is the value function.
The solution to the dual is the optimal policy.

The primal is available is a python dictionary. We get the value for each state.

The dual variables are available in this ``prob.constraints.items()'' object.
Being not fluent in python, I am pretty sure one can do it better than I do, but my code works.

Finally, we build the optimal policy from the dual variables: ``pi_star [state]'' is the number of the optimal action in ``state''.
