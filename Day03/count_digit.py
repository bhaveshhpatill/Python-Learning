count = 0
num = int(input("Enter a number: "))

while num != 0:
    count += 1
    num = num // 10

print(count)