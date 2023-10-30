'''3
2 22 10 3 7 23
2 21 1 8 2 127
2 07 1 1 1 5 '''

'''n t h_0 a b q'''
# Read the number of test cases
c = int(input())

# Process each test case
for _ in range(c):
    # Read input values for each test case
    n, t, h_0, a, b, q = map(int, input().split())

    h_set = set()
    h_set.add(h_0)

    def func(a, b, q, h_i):
        return (a * h_i + b) % q
        
    while True:
        Val = func(a, b, q, h_0)

        if Val in h_set:
            break
        else:
            h_0 = Val
            if len(str(Val)) > n:
                Val = Val % (10 ** n)
            h_set.add(Val)

    print(h_set)