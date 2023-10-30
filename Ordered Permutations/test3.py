from itertools import permutations

def check_condition(numbers, condition):
    con = ''
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            con += '>'
        else:
            con += '<'
    if con == condition:        
        return True

# Read input
N = int(input())
condition = input().strip()

numbers = tuple(range(1, N + 1))
del N
permutations_list = list(permutations(numbers))

count = 0
for set in permutations_list:
    if check_condition(set, condition):
        #print(set)
        count += 1
print(count)