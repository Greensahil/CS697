def helloWorld():
    print("hello world")



# print memory address
print(helloWorld)
x = helloWorld
print(x)


def greeting(func):
    print('Inside greeting')

    func()

    print('Inside greeting')

# passing function to a function because they are basically objects
greeting(helloWorld)

# We can also return a function from a function

def greet_anyone(*names):
    def hello():
        for name in names:
            print(f'Hello, {name}')

    return hello

hello_all = greet_anyone('Dave', 'Sal', 'Mat')

hello_all() 

# or greet_anyone('Dave', 'Sal', 'Mat')()




