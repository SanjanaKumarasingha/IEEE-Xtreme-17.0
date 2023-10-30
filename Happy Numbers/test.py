Happpy_num = {1, 7, 10, 13, 19, 23, 28, 31, 32, 44}
Un_Happpy_num = {2, 3, 4, 5, 6, 8, 9, 11, 12,
                 14,15,16,17,18, 20,21,22,
                  24,25,26,27,29,30,33,34,35,36, 37,
                   38,39,40, 58, 89, 145}

def is_happy(num):
    store = set()
    if num in Happpy_num:
        Happpy_num.union(store)
        return True
    elif num in Un_Happpy_num:
        Un_Happpy_num.union(store)
        return False
    else:
        num = sum(int(digit) ** 2 for digit in str(num))
        return is_happy(num)
    # seen = set()
    # while num != 1 and num not in seen:
    #     seen.add(num)
    #     num = sum(int(digit) ** 2 for digit in str(num))
    # return num == 1

def count_happy_numbers(a, b):
    count = 0
    for num in range(b, a-1, -1):
        if is_happy(num):
            count += 1
    return count

# Read input
a, b = map(int, input().split())

# Calculate and print the result
result = count_happy_numbers(a, b)
print(result)
