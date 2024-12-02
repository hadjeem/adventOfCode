with open('input.txt', 'r') as file:
    lines = file.readlines()

list1, list2 = [], []

for line in lines:
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))

list1.sort()
list2.sort()

somme = sum(abs(val1-val2) for val1, val2 in zip(list1, list2))
print("Partie 1 : ", somme)

distance = sum(list1[i] * list2.count(list1[i]) for i in range(len(list1)))
print("Part2 : ", distance)
