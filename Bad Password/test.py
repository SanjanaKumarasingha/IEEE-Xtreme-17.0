import difflib

n = int(input())
sequences = []
for _ in range(n):
    sequences.append(input().split(" ")[1:])

p = int(input())
for _ in range(p):
    old_pass, new_pass = map(str, input().split(" "))
    differ = difflib.Differ()
    diff = list(differ.compare(old_pass, new_pass))
    # additions = [line[2:] for line in diff if line.startswith('+ ')]
    # # add_string =  ''.join(additions)
    # subtractions = [line[2:] for line in diff if line.startswith('- ')]
    # # sub_string = ''.join(subtractions)
    additions = []
    substract = []
    if diff[0].startswith("+ "):
        if diff[1].startswith(" "):
            print("REJECT")
            continue
        additions.append(diff[0][2:])
    elif diff[0].startswith("- "):
        if diff[1].startswith(" "):
            print("REJECT")
            continue
        substract.append(diff[0][2:])
    for a in range(1 , len(diff)):
        if (diff[a].startswith("+ ") and diff[a-1].startswith("+ ")) :
            additions[-1] += diff[a][2:]
        elif (diff[a].startswith("- ") and diff[a-1].startswith("- ")):
            substract[-1] += diff[a][2:]
        elif diff[a].startswith("+ "):
            additions.append(diff[a][2:])
        elif diff[a].startswith("- "):
            substract.append(diff[a][2:])
    
    for k in range (len(additions)):
        for sequence in sequences:
            if additions[k] in sequence and substract[k] in sequence:
                print("REJECT")
                break
        else:
            print("OK")
            break
            