def doStuff():
    print(5)

def main():
    doStuff()

main()


def division(num1, num2):
    q= num1//num2
    r= num1%num2
    return q,r

a,b = division(7,5)

print(a,b)


def sum(num1, *args):
    total = num1
    for x in args:
        total += x
    return total

print(sum(5,6,7))

#in build method

print(max(6,7,5,7,8))
print(min(6,7,4,5))

#kwargs is dictonairy
def printInfo(**kwargs):
    for key,value in kwargs.items():
        print(key, " : ", value)

printInfo(name="sahil",age=23)
printInfo(name="jack",age=23, gpa=3.5)