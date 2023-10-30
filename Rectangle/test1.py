group_sizes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 41

# Initialize a list to store the maximum number of tuples for each target value
max_tuples = [0] * (target + 1)

# Iterate through each group size
for size in group_sizes:
    # Calculate the possible target values starting from size
    for value in range(size, target + 1):
        # Update max_tuples[value] using the current group size
        max_tuples[value] = max(max_tuples[value], max_tuples[value - size] + 1)

# The maximum number of tuples for the target value 41
max_num_tuples = max_tuples[target]

print("Maximum number of tuples for target", target, "is:", max_num_tuples)
