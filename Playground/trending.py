fileName = "twitter_data.txt"

listOfHashTags = []

def getHashTags(text):

    for word in text.split():
        if(word[0] == "#"):
            listOfHashTags.append(word[1:].lower())



with open(fileName, 'r', encoding ='utf8') as f:
    lines = f.read()


getHashTags(lines)


hashTagCounter = {}
for key in listOfHashTags:
    if key in hashTagCounter: 
        hashTagCounter[key] += 1
    else:
        hashTagCounter[key] = 1

#convert the dictonairy into tuple so that we can use the sorted function to sort it
hashTagCounter = {k: v for k, v in sorted(hashTagCounter.items(), key=lambda item: item[1],reverse=True)}


print("The top 5 trending hashtags are:")
counter = 0

for key in hashTagCounter:
    print('     #' + key, " : ", hashTagCounter[key])
    counter += 1
    if(counter == 5):
        break
