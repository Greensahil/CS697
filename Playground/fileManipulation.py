reader = open('helloworld.py','r')  #r == access mode (default optional), read write and append

#try:
    # Futher file processing
#finally:
 #   reader.close()

#Alternative syntatuc sugar method
#with open('somefile.txt') as reader

with open('inputfile.txt','r') as reader:
    x = reader.read()

print(x)



with open('inputfile.txt','r') as reader:
    x = reader.readlines()          #contains \n

print(x)

with open('inputfile.txt','r') as reader:
    x = reader.readline()          #contains \n
print(x)


with open('inputfile.txt','w') as writer:
    writer.write("TEST")         #contains \n
