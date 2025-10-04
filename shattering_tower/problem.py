import math

"""
Takes in the key input values and returns a list of strings containing the 
answers.

Parameters:
n : int - number of pillars
k : int - number of attacks
d_i : array-like - list of shape (k,) containing the damage dealt by each attack
s_i : array_like - list of shape (n,) containing the strength of each pillar

Returns:

list of strings to be printed. For example, if the answer to be printed is:

5
2
0

return ["5","2","0"]
"""
def solve(n,k,d_i,s_i):     
    pass

n,k = list(map(int,input().strip().split(" ")))
d_i = [int(input()) for i in range(k)]
s_i = [int(input()) for i in range(n)]

print("\n".join(solve(n,k,d_i,s_i)) + "\n")