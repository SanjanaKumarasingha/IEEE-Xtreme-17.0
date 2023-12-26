# number of iterated sequences
# n = int(input())
# sequences = []
# for _ in range(n):
#     _, *sequence = input().split()
#     sequences.append(set(sequence))
# print(sequences)

n = 6
sequences = [
    {"5", "4", "2", "0", "9", "8", "7", "3", "6", "1"},
    {
        "February",
        "April",
        "August",
        "July",
        "January",
        "October",
        "March",
        "May",
        "June",
        "September",
        "November",
        "December",
    },
    {"Tuesday", "Saturday", "Monday", "Friday", "Thursday", "Sunday", "Wednesday"},
    {"qwerty", "zxcv", "asdf"},
    {"bob", "ana"},
    {".", "?", "!"},
]

# number of password changes
# p = int(input())
# password_changes = [input().split() for _ in range(p)]
# print(password_changes)

p = 20
password_changes = [
    ["password1", "password2"],
    ["Pass123", "pass124"],
    ["ShhMonday", "ShhMarch"],
    ["January23", "March23"],
    ["ABCJanuary", "MarchABC"],
    ["January23", "february23"],
    ["Tuesday", "Sunday"],
    ["xyz123", "124xyz"],
    ["zxcvz", "qwertyz"],
    ["asdfasdf", "asdfzxcv"],
    ["asdfasdf", "zxvcasdf"],
    ["bobobob", "anaobob"],
    ["bobobob", "boboana"],
    ["banana", "bbobna"],
    ["banana", "banbob"],
    ["banana", "baboba"],
    ["password!!!", "!password!!"],
    ["password!!!", "password???"],
    ["password?!!", "password?!?"],
    ["password!!!", "password!?!"],
]


def can_express(s1, s2):
    prefix, suffix = "", ""
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            prefix += s1[i]
        else:
            break

    for i in range(1, min(len(s1), len(s2)) + 1):
        if s1[-i] == s2[-i]:
            suffix = s1[-i] + suffix
        else:
            break

    if len(suffix) == 0:
        ps1 = s1[len(prefix) :]
        ps2 = s2[len(prefix) :]
    else:
        ps1 = s1[len(prefix) : -len(suffix)]
        ps2 = s2[len(prefix) : -len(suffix)]
    return ps1, ps2


for old_password, new_password in password_changes:
    if old_password == new_password:
        print(old_password, new_password, "-->", "REJECT")
        continue
    ps1, ps2 = can_express(old_password, new_password)
    if ps1 == old_password:
        print(old_password, new_password, "-->", "OK")
        continue

    for seq in sequences:
        count = 0
        # if ps1 in seq and ps2 in seq:
        #     print(old_password, new_password, "-->", "REJECT")
        #     break

        for str in seq:
            if ps1 in str and str in old_password:
                # old_password = old_password.replace(str, "")
                count += 1
            if ps2 in str and str in new_password:
                # new_password = new_password.replace(str, "")
                count += 1

        if count == 2:
            print(old_password, new_password, "-->", "REJECT")
            break

    else:
        print(old_password, new_password, "-->", "OK")