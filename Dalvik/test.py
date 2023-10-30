def simulate_smali(A, B, C):
    v0 = A
    v1 = B
    v2 = C
    
    # Calculate the number of iterations required
    iterations = (v2 // v0) * 2
    
    # Calculate the remaining values after iterations
    remaining_v1 = v2 % v0
    remaining_v0 = (v1 - remaining_v1) // 2
    
    # Calculate the final result
    result = (iterations * v0) + (remaining_v0 * 2) + remaining_v1
    return result

# Read input
T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    result = simulate_smali(A, B, C)
    print(result)
