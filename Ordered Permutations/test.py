MOD = 10**9 + 7


def count_permutations(N, restrictions):
    dp = [0] * (N)
    dp[0] = 1
    
    for i in range(1, N):
        if restrictions[i - 1] == '<':
            dp[i] = (dp[i - 1] * i) % MOD
        else:
            dp[i] = (dp[i - 1] * (N - i + 1)) % MOD
    
    return dp

# Read input
N = int(input())
restrictions = input().strip()

# Calculate and output the result
result = count_permutations(N, restrictions)
print(result)
