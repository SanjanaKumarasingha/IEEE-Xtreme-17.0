def generate_primes(N):
    primes = [True] * (N + 1)
    primes[0] = primes[1] = False
    
    for num in range(2, int(N**0.5) + 1):
        if primes[num]:
            for multiple in range(num * num, N + 1, num):
                primes[multiple] = False
    
    return [num for num in range(2, N + 1) if primes[num]]

# Read input as two integers separated by a space
# M, N = map(int, input().split())

# Generate and print prime numbers up to N
prime_numbers = generate_primes(12)
prime_numbers.append(1)
print(prime_numbers)
