li_num = [int(i) for i in input().split()]

count = 0
for i in range(len(li_num) - 1):
    if li_num[i + 1] > li_num[i]:
        count += 1
print(count)
