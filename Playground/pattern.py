charcater = input("Enter character")
count = int(input("Enter the number of times the character needs to repeat"))

for i in range(count):
    print(" " * (count - i), end= '')
    if i == 0 or i == (count-1):
        if  i == 0:
            print("*")
        elif i == (count-1):
            print("* " * (i+1))
    else:    
        print("*", end = '')
        print(" " * ((i*2)-1), end = '')
        print("*")
        