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
        store.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
        store.add(num)
        return is_happy(num)
    
p = is_happy(144)
print(p)
print(Happpy_num)
print(Un_Happpy_num)