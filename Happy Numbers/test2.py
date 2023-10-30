def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

def count_happy_numbers(a, b):
    count = 0
    for num in range(a, b + 1):
        if is_happy(num):
            count += 1
    return count

# Read input
a, b = map(int, input().split())

# Calculate and print the result
result = count_happy_numbers(a, b)
print(result)
