fp = 'input.txt'
levels, safe = [],  []
with open(fp, 'r') as f:
    for line in f:
        level = [int(x) for x in line.replace('\n', '').split(" ")]
        levels.append(level)

def incOrdecList(list):
    return all(list[i] <= list[i + 1] for i in range(len(list) - 1)) or all(list[i] >= list[i + 1] for i in range(len(list) - 1))

def differSafe(list):
    return all(3 >= abs(list[i] - list[i + 1]) > 0 for i in range(len(list) - 1))

def dampener(list):
    for i in range(len(list)):
        inaccuracy = list[:i] + list[i + 1:]
        if inaccuracy == sorted(inaccuracy) or inaccuracy == sorted(inaccuracy, reverse=True):
            diffs = [abs(b - a) for a, b in zip(inaccuracy, inaccuracy[1:])]
            if all(1 <= diff <= 3 for diff in diffs):
                return True
                break

for level in levels:
    if incOrdecList(level) and differSafe(level):
        safe.append(level)
print("Part1:", len(safe))

safe.clear()
for level in levels:
    if dampener(level):
        safe.append(level)

print("Part2:", len(safe))