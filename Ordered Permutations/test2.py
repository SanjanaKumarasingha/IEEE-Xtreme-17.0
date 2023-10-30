MOD = 10**9 + 7

def calculate_permutations(N, R):
    dp = [0] * (N)
    dp[0] = 1
    total_permutations = 1

    for i in range(1, N):
        if R[i - 1] == '<':
            dp[i] = (dp[i - 1] + total_permutations) % MOD
        else:
            dp[i] = dp[i - 1]
            total_permutations = (total_permutations * i) % MOD

    return sum(dp) % MOD

if __name__ == "__main__":
    N = int(input())
    R = input().strip()
    result = calculate_permutations(N, R)
    print(result)
