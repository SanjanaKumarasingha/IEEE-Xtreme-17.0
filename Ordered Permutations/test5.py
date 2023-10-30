def count_permutations_with_condition(N, condition):
    if N == 1:
        return 1
    
    # Initialize count to 1 for the single permutation (N,)
    count = 1
    
    # Iterate through numbers from N-1 to 1
    for num in range(N - 1, 0, -1):
        # Count the number of permutations that satisfy the condition for each number
        if condition == '>' and num > N:
            count += 1
        elif condition == '<' and num < N:
            count += 1
        N -= 1
    
    return count

# Read input
N = int(input())
condition = input().strip()

# Calculate and print the result
result = count_permutations_with_condition(N, condition)
print(result)
