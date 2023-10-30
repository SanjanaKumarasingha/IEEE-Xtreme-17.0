import math

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the angle in degrees
    a = float(input())

    # Initialize variables to store the minimum cosine value and corresponding n
    min_cos_value = math.cos(math.radians(a * 1))  # Initialize with cos(a)
    min_n = 1

    # Iterate over positive integers n and find the minimum cosine value
    for n in range(2, 1000000):  # You can adjust the range based on the problem constraints
        cos_value = math.cos(math.radians(a * n))
        if abs(cos_value) < abs(min_cos_value):
            min_cos_value = cos_value
            min_n = n

    # Output the result for this test case
    print(min_n)
