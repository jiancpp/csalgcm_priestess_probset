import math
import bisect

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
    """ Mathematical Approach to Achieve O(n log k + n log n) """
    if n == 0:
        return []

    answers = []

    # Step 1: prefix sums for and total damage in one cycle
    damage_r = [0] * k
    damage_r[0] = d_i[0]
    
    for i in range(1, k):
        damage_r[i] = damage_r[i - 1] + d_i[i]

    cycle_damage = damage_r[-1]

    # Step 2: compute death round for each pillar
    death_rounds = []
    for strength in s_i:
        cycles_survived = (strength - 1) // cycle_damage # integer div
        remaining_strength = strength - cycles_survived * cycle_damage

        j = bisect.bisect_left(damage_r, remaining_strength) # index of round
        death_round = cycles_survived * k + (j + 1) # +1 because displayed round counts from 1
        death_rounds.append(death_round)

    # Step 3: sort death rounds
    death_rounds.sort()

    # Step 4: compute answers
    standing = n
    idx = 0
    total_rounds = max(death_rounds)

    for r in range(1, total_rounds + 1):
        # remove all towers that die this round
        while idx < n and death_rounds[idx] == r:
            standing -= 1
            idx += 1
        answers.append(str(standing))

    return answers

n,k = list(map(int,input().strip().split(" ")))
d_i = [int(input()) for i in range(k)]
s_i = [int(input()) for i in range(n)]

print("\n".join(solve(n,k,d_i,s_i)) + "\n")


