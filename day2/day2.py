with open('input.txt','r') as file:
    lines = file.readlines()

def increasing_or_decreasing(list):
    if len(list) < 2:
        return True 

    increasing = False
    decreasing = False
    for i in range(2):
        if list[i] < list[i+1]:
            increasing = True
        elif list[i] > list[i+1]:
            decreasing = True
    if increasing:
        for i in range(len(list)-1):
            if list[i] >= list[i+1] or abs(list[i]-list[i+1]) > 3:
                return False
        return True 
    elif decreasing:
        for i in range(len(list)-1):
            if list[i] <= list[i+1] or abs(list[i]-list[i+1]) > 3:
                return False
        return True
    return False

count = 0
for line in lines:
    list = [int(x) for x in line.split()]
    if increasing_or_decreasing(list):
        count += 1
        print(list, increasing_or_decreasing(list))
print("part1:", count)
