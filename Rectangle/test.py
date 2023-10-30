from itertools import combinations

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_relatively_prime(dimensions):
    for i in range(len(dimensions)):
        for j in range(i + 1, len(dimensions)):
            if gcd(dimensions[i], dimensions[j]) != 1:
                return False
    return True

# Read input
M, N = map(int, input().split())

# Find all combinations of group sizes from 1 to 12 that add up to 41
group_sizes = [1, 3, 5, 7, 9, 11]
valid_combinations = []
for r in range(1, len(group_sizes) + 1):
    for combination in combinations(group_sizes, r):
        if sum(combination) == M:
            if is_relatively_prime(combination):
                valid_combinations.append(combination)

# Print the sum of valid combinations
print(sum(group_sizes))
