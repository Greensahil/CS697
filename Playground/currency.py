

money = input("Enter the currency in knuts")
money = int(money)

sickle = money//29
knuts = money%29 


galleon = sickle//17
sickle = sickle%17


print(money , "knuts =" ,galleon," galleons",  sickle, "sickles and",  knuts, "knuts")
print("------------------------------------------------------------------------------")