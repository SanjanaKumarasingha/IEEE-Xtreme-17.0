
MOD = 998244353

def calculate_power(s, n):
    power = 1
    for char in s:
        power = (power * pow(2, n.count(char), MOD)) % MOD
    return power

def main():
    N, M = map(int, input().split())
    strings = [input().strip() for _ in range(M)]

    total_power = 0
    for i in range(1 << M):
        current_string = ''.join(strings[j] for j in range(M) if (i >> j) & 1)
        total_power = (total_power + calculate_power(current_string, current_string)) % MOD  # Pass current_string instead of N

    print(total_power)

if __name__ == "__main__":
    main()
