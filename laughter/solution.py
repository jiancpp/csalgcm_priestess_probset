def solve(n,k):
  # solve problem here. Return correct answer
    # Precompute lengths with cap = k+1 so comparisons stay correct,
    # but numbers don't explode.
    cap = k + 1
    if n == 0: return "H"
    if n == 1: return "A"
    lengths = [1, 1]  # len(S0), len(S1)
    for i in range(2, n+1):
        s = lengths[i-1] + lengths[i-2]
        if s > cap:
            s = cap
        lengths.append(s)

    # S_n = S_{n-2} + S_{n-1}
    # Walk down until base case
    while n > 1:
        if k < lengths[n-2]:        # k-th index is in the first part S_{n-2}
            n = n - 2               # jump to S_{n-2}
        else:                       # k-th index is in the first part S_{n-2}
            k -= lengths[n-2]       # subtract length as first part is skipped
            n = n - 1               # jump to S_{n-1}

    return "H" if n == 0 else "A"


n, k = list(map(int,input().rstrip().split(" ")))
print(solve(n,k))


"""
Suppose we want n = 4, k = 3 (0-based index).

S = "HAAHA". The letters are: H(0) A(1) A(2) H(3) A(4).

Answer should be "H".

Now let's see how code finds it without building "HAAHA":

lengths = [1,1,2,3,5]

At n=4: length(S₂)=2. Since k=3 ≥ 2 → go to S₃ with k=1.

At n=3: length(S₁)=1. Since k=1 ≥ 1 → go to S₂ with k=0.

At n=2: length(S₀)=1. Since k=0 < 1 → go to S₀.

At n=0 → return "H". ✅
"""