num = int(input())

count = []
for i in range(1, num + 1):
    line = input()
    check = ""
    for j in "anton":
        if j in line:
            check += j
            line = line.replace(j, "", 1)
    if check == "anton":
        count.append(i)
print(*count)
