#import math

#Read files
governmentJobsFile = "gov.csv"
privateJobsFile = "private.csv"
presidentsFile = "presidents.txt"


lookupAdjective = {
    "Democrat": "Democratic",
    "Republican" : "Republican"
}

dictPresidents = {}
with open(presidentsFile,'r') as reader:
    lines = reader.read().splitlines()
    for line in lines:
        tempArray = line.split(",")
        presidentTenure = tempArray[1]
        presidentTenure = presidentTenure.split("-")

        for i in range(int(presidentTenure[0]),int(presidentTenure[1])):
            dictPresidents[i] = [tempArray[0].strip(), tempArray[2].strip()]

#Return Dictonairy of lists
def returnJobDictonaryFromFile(fileName):
    tempDict = {}
    with open(fileName,'r') as reader:
        next(reader) #Skip first line which is the header : YEAR JAN FEB MAR ....
        lines = reader.read().splitlines()
        for line in lines:
            tempArray= line.split(",")
            tempYear = tempArray[0]
            tempDict[int(tempYear)] = [int(tempArray[i]) for i in range(1,len(tempArray))]
    return tempDict

dictGovermentJobs = returnJobDictonaryFromFile(governmentJobsFile)
dictPrivateJobs = returnJobDictonaryFromFile(privateJobsFile)


#First lets just calculate the total number of jobs under each party affiliation
#Because totalNumberOfJobs/(12 * TotalNumberOfYearsForEachSAffilication) should give the average per month
def returnTotalNumberOfJobsBasedOnDict(dictPresidents, dictJobs):
    dictPartyAffiliationCounter = {}
    dictAverage = {}
    for key in dictJobs:
        if int(key) in dictPresidents:    
            partyAffiliation = dictPresidents[int(key)][1]
            if(partyAffiliation in dictAverage):
                dictAverage[partyAffiliation] = dictAverage[partyAffiliation] +  sum(dictJobs[key])
                dictPartyAffiliationCounter[partyAffiliation] += 1
            else:
                dictAverage[partyAffiliation] = sum(dictJobs[key])
                dictPartyAffiliationCounter[partyAffiliation] = 1

    for key in dictAverage:
        dictAverage[key] = round(dictAverage[key]/(12 * dictPartyAffiliationCounter[key]))

    return dictAverage



dictPrivateEmploymentAverage = returnTotalNumberOfJobsBasedOnDict(dictPresidents, dictPrivateJobs)
dictGovernmentEmploymentAverage = returnTotalNumberOfJobsBasedOnDict(dictPresidents, dictGovermentJobs)


    
print("Private employment average per month (thousands)")
for key in dictPrivateEmploymentAverage:
    print(lookupAdjective[key], ":{:>15}".format(str(dictPrivateEmploymentAverage[key])) )

print("Government employment average per month (thousands)")
for key in dictGovernmentEmploymentAverage:
    print(lookupAdjective[key], ":{:>15}".format(str(dictGovernmentEmploymentAverage[key])) )


print("Private employment average by president (thousands)")