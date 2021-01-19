


num = input("Enter number")
num = int(num)


sum = 0

while(num > 0):
    remainder = num % 10
    sum = sum + remainder
    num = num // 10

print(sum)


