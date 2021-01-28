password = input("Enter a string for password:")
validPassword = True

#A password must have at least eight characters.
if len(password) < 8:
    validPassword = False

#A password consists of only letters and digits
if not password.isalnum():
    validPassword = False

#A password must contain at least two digits
#A password must contain at least one uppercase character
digitCounter = 0
upperCaseCounter = 0
for index in range(len(password)):
    if(password[index].isnumeric()):
        digitCounter += 1
    if(password[index].isupper()):
        upperCaseCounter += 1

if digitCounter < 2:
    validPassword = False
if upperCaseCounter < 1:
    validPassword = False


if validPassword:
    print("valid password")
else:
    print("invalid password")