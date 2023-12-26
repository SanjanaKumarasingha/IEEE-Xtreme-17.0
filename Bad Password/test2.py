# Read input
n = int(input())
sequences = []
for _ in range(n):
    _, *sequence = input().split()
    sequences.append(set(sequence))

p = int(input())
password_changes = [input().split() for _ in range(p)]
print(password_changes)
# Function to check if two strings can be expressed as per the given rules
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
        ps1 = s1[len(prefix):]
        ps2 = s2[len(prefix):]
    else:    
        ps1 = s1[len(prefix):-len(suffix)] 
        ps2 = s2[len(prefix):-len(suffix)]    

    for seq in sequences:
        if ps1 in seq and ps2 in seq:
            return True
        # if len(prefix) == 0:
        #     for str in seq:
        #         if ps1 in str and ps2 in str:
        #             return True
    return False

# Check password changes and output the result
for old_password, new_password in password_changes:
    for seq in sequences:
        if old_password in seq and new_password in seq:
            print("REJECT")
            break
    else:
        if old_password == new_password:
            print("REJECT")
        if can_express(old_password, new_password):
            print("REJECT")
        else:
            print("OK")

    print(old_password,new_password)
    print()
