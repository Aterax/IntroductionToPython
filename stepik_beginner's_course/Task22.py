# Dog age

n = int(input())

age = 0
if n <= 2:
    for i in range(n):
        age += 10.5
    print(age)
else:
    for i in range(2):
        age += 10.5
    age += (n - 2) * 4
    print(int(age))