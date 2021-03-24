#import math
import matplotlib.pyplot as plt
#Read files
governmentJobsFile = "gov.csv"
privateJobsFile = "private.csv"
presidentsFile = "presidents.txt"
outputFile = "output.txt"


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


    
# print("Private employment average per month (thousands)")
# for key in dictPrivateEmploymentAverage:
#     print(lookupAdjective[key], ":{:>15}".format(str(dictPrivateEmploymentAverage[key])) )

# print("")



# print("Government employment average per month (thousands)")
# for key in dictGovernmentEmploymentAverage:
#     print(lookupAdjective[key], ":{:>15}".format(str(dictGovernmentEmploymentAverage[key])) )




# print(dictPresidents)
# print(dictPrivateJobs)


def getTheAverageEmploymentByPresident(dictPresidents, dictJobs):
    dictEmploymentAverageByPresident = {}
    for key in dictPresidents:
        lastYearOfPresidency = 0
        currentYear = key
        currentPresident = dictPresidents[currentYear][0]
        #TODO: This is probably not the most effcient way to do this because I have to keep updating the dictonary. I need to run another process that gives me the first and last year for each president and have this not be a loop
        if currentPresident in dictEmploymentAverageByPresident:
            dictEmploymentAverageByPresident[currentPresident]['lastMonthEmploymentNumber'] = dictJobs[currentYear][11]
        else:
            dictEmploymentAverageByPresident[currentPresident] = {'firstMonthEmploymentNumber':dictJobs[currentYear][0], 'lastMonthEmploymentNumber':0}

    #Add some more properties to this object
    for key in dictEmploymentAverageByPresident:
        dictEmploymentAverageByPresident[key]['Difference'] = dictEmploymentAverageByPresident[key]['lastMonthEmploymentNumber'] - dictEmploymentAverageByPresident[key]['firstMonthEmploymentNumber']
        dictEmploymentAverageByPresident[key]['Percentage'] = round((dictEmploymentAverageByPresident[key]['Difference']/dictEmploymentAverageByPresident[key]['firstMonthEmploymentNumber']) * 100,1)

    return dictEmploymentAverageByPresident
    

dictPrivateEmploymentAverageByPresident = getTheAverageEmploymentByPresident(dictPresidents, dictPrivateJobs)
dictGovernmentEmploymentAverageByPresident = getTheAverageEmploymentByPresident(dictPresidents, dictGovermentJobs)




def printEmployementAveragePerPresident(dictAverage,out_file):
    out_file.write("\n")
    out_file.write("{:<20} {:<20} {:<20}{:<20}{:<20}".format('President','First Month','Last Month', 'Difference', 'Pecentage'))
    out_file.write("\n")
    for key in dictAverage:
        currentLine = dictAverage[key]
        out_file.write("{:<20} {:<20} {:<20}{:<20}{:<20}"
        .format(key.split(" ")[2], 
        currentLine['firstMonthEmploymentNumber'],currentLine['lastMonthEmploymentNumber'],
        currentLine['Difference'],str(currentLine['Percentage']) + "%"
        ))
        out_file.write("\n")

# print("")
# print("Private employment average by president (thousands)")
# printEmployementAveragePerPresident(dictPrivateEmploymentAverageByPresident)

# print("Government employment average by president (thousands)")
# printEmployementAveragePerPresident(dictGovernmentEmploymentAverageByPresident)

with open(outputFile, 'w') as out_file:
    out_file.write("Private employment average per month (thousands)\n")
    for key in dictPrivateEmploymentAverage:
        lineOutput = lookupAdjective[key] + ":{:>15}".format(str(dictPrivateEmploymentAverage[key]) + "\n") 
        out_file.write(lineOutput)
    out_file.write("\n")

    out_file.write("Government employment average per month (thousands)\n")
    for key in dictGovernmentEmploymentAverage:
        lineOutput = lookupAdjective[key] + ":{:>15}".format(str(dictGovernmentEmploymentAverage[key]) + "\n") 
        out_file.write(lineOutput)
    out_file.write("\n")
    
    out_file.write("Private employment average by president (thousands)")
    printEmployementAveragePerPresident(dictPrivateEmploymentAverageByPresident,out_file)
    out_file.write("\n")

    out_file.write("Government employment average by president (thousands)")
    printEmployementAveragePerPresident(dictGovernmentEmploymentAverageByPresident,out_file)
    out_file.write("\n")






def Average(lst): 
    return sum(lst) / len(lst) 

#Average number of private jobs  each year and government jobs each year
x = [key for key in dictPrivateJobs]
y = [Average(dictPrivateJobs[key]) for key in dictPrivateJobs ]

plt.plot(x,y)


x = [key for key in dictGovermentJobs]
y = [Average(dictGovermentJobs[key]) for key in dictGovermentJobs ]

plt.plot(x,y)

plt.xlabel('Year')
plt.ylabel('Average Number of Jobs')
plt.legend(['Average Number Of Private Jobs', 'Average Number of Governemnt Jobs'])
plt.title('Average Number of governemnt and private jobs trend')

plt.show()




dicNumberOfYearsForEachPresident= {}

for key in dictPresidents:
    if dictPresidents[key][1] in dicNumberOfYearsForEachPresident:
         dicNumberOfYearsForEachPresident[dictPresidents[key][1]] += 1
    else:
        dicNumberOfYearsForEachPresident[dictPresidents[key][1]] = 1

plt.title('Percentage of Democratic vs Republican presidents in the last 44 years')
labels = ['Democratic President', 'Republican President']

plt.pie([dicNumberOfYearsForEachPresident[key] for key in dicNumberOfYearsForEachPresident], labels=labels,shadow=True,autopct='%1.1f%%')

plt.show()