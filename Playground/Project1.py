import requests
import requests


#i have my proxy enabled so the request does  not work so doing this
#FIX ME COMMENT OUT BEFORE SUBMITTING -- ALSO REMOVE FORM EACH REQUEST
proxies = {
  "http": None,
  "https": None,
}

class Location:
    def __init__(self, address):
        # self.latitude = latitude
        # self.longitude = longitude
        self.address = address
        res = requests.get(f'https://api.tomtom.com/search/2/geocode/{address}.json?key=eOLkHP2OmPP0sZMvegeShZXWUuYx3UKt', proxies=proxies)
        if res.status_code == 200:
            locationResult = res.json()
            #print(locationResult['results'][0]['position'])
            self.latitude = locationResult['results'][0]['position']['lat']
            self.longitude = locationResult['results'][0]['position']['lon']
        elif res.status_code == 404:
            print('Not Found.')

    def __str__(self):        
        return f'Lattitude is {self.latitude} and longitude is {self.longitude}'


class Trip:
    def __init__(self, *locationsToVisit):
        # self.latitude = latitude
        # self.longitude = longitude
        self.places = []
        for item in locationsToVisit:
            self.places.append(Location(item))


    def generateTrip(self):
        tempPlaces = self.places
        tempList = []
        
        for index in range(len(tempPlaces)):
            if(index != len(tempPlaces)-1):
                 longOfCurLoc = tempPlaces[index].longitude
                 latOfCurLoc = tempPlaces[index].latitude
                 longOfNextLoc = tempPlaces[index+1].longitude
                 latOfNextLoc = tempPlaces[index+1].latitude   

                 res = requests.get(f'https://api.tomtom.com/routing/1/calculateRoute/{latOfCurLoc},{longOfCurLoc}:{latOfNextLoc},{longOfNextLoc}/json?&key=eOLkHP2OmPP0sZMvegeShZXWUuYx3UKt', proxies=proxies)
                 
                 #print(f'https://api.tomtom.com/routing/1/calculateRoute/{longOfCurLoc},{latOfCurLoc}:{longOfNextLoc},{latOfNextLoc}/json?&key=eOLkHP2OmPP0sZMvegeShZXWUuYx3UKt')

                 if res.status_code == 200:
                    tripResponse = res.json()
                    tempTuple = (tripResponse['routes'][0]['summary']['lengthInMeters'],tripResponse['routes'][0]['summary']['travelTimeInSeconds'])
                    tempList.append(tempTuple)
                 elif res.status_code == 404:
                    print('Not Found.')
        return tempList

   
    def getWeather(self,locObject):
        tempPlaces = self.places
        
        for item in tempPlaces:
            res = requests.get(f'http://api.weatherstack.com/current?access_key=3a9d8c0b203696e4497003a061de3659&query={item.latitude},{item.longitude}&units=f', proxies=proxies)
            if res.status_code == 200:
                apiResponse = res.json()
                locObject['temperature'] = apiResponse['current']['temperature']
            elif res.status_code == 404:
                print('Not Found.')

    def convertSecondsToHoursMinutesAndSeconds(self, timeInSeconds):
        hours = timeInSeconds // 3600
        minutes = timeInSeconds %3600 //60
        seconds = timeInSeconds %3600 % 60

        return f'{hours} hours {minutes} minutes {seconds} seconds'

        
    def convertMetersToMiles(self, distanceInMeter):
        return round(distanceInMeter * 0.000621371192,2)

    def summary(self):
        tempPlaces = self.places
        tripInfoList = self.generateTrip()
        totalDistanceInMeters = 0
        totalTimeInSeconds = 0
        print(f'Here is a summary of your trip from {tempPlaces[0].address} to {tempPlaces[len(tempPlaces)-1].address}')   
        print('-----------------------------------------------------------------------------------------------------------------------------------------------------') 
     
        print("{:<20} {:<30} {:<30}{:<30}{:<30}".format('No','Origin','Destination', 'Distance (miles)', '  Time'))
        locationObject = {}

        for index in range(len(tempPlaces)):
            if(index != len(tempPlaces)-1):
                print("{:<20} {:<30} {:<30} {:<30} {:<30}".format(index, tempPlaces[index].address, tempPlaces[index+1].address,self.convertMetersToMiles(tripInfoList[index][0]),self.convertSecondsToHoursMinutesAndSeconds(tripInfoList[index][1])))
                totalDistanceInMeters = totalDistanceInMeters + tripInfoList[index][0]
                totalTimeInSeconds = totalTimeInSeconds + tripInfoList[index][1]
            else:
                #this is the last location of the trip so lets get the weather for this locaiton
                locationObject['longitude'] = tempPlaces[index].longitude
                locationObject['latitude'] = tempPlaces[index].latitude
                locationObject['address'] = tempPlaces[index].address
                #this method adds the current temperature to the locaiton object
                self.getWeather(locationObject)
        


        print('-----------------------------------------------------------------------------------------------------------------------------------------------------') 
        print("{:<20} {:<30} {:<30}{:<30}{:<30}".format('','','Total', self.convertMetersToMiles(totalDistanceInMeters), self.convertSecondsToHoursMinutesAndSeconds(totalTimeInSeconds)))   
        
        print(f'It is currently {locationObject["temperature"]} degrees in {locationObject["address"]}. Have a safe trip!')         
        print()

    def __add__(self,other):        
        if type(other) == str:
            tempLocationObject = Location(other) 
            self.places.append(tempLocationObject)
            return self

    def __mul__(self,numberOfTrips):
        tempPlaces = self.places[:]     
        if(numberOfTrips > 0):
            for index in range(numberOfTrips-1):
                if index % 2 == 0: 
                    for index2 in range(len(tempPlaces)-2,-1,-1):
                        self.places.append(tempPlaces[index2])
                else:
                    for index2 in range(len(tempPlaces)):
                        if(index2 !=0):
                            self.places.append(tempPlaces[index2])
            return self
        else:
            print('The multipied number must be a postive integer')


    @staticmethod   
    def getDistance(tempPlaces,tripInfoListSelf):        
        totalDistanceInMeters = 0
        for index in range(len(tempPlaces)-1):
            totalDistanceInMeters = totalDistanceInMeters + tripInfoListSelf[index][0]
        return totalDistanceInMeters

    def __gt__(self, other):
        tempPlacesSelf = self.places
        tempPlacesOther = other.places
        tripInfoListSelf = self.generateTrip()
        tripInfoListOther= other.generateTrip()

        totalDistanceInMetersSelf = self.getDistance(self.places, tripInfoListSelf)
        totalDistanceInMetersOther = self.getDistance(other.places, tripInfoListOther)

      

        if(totalDistanceInMetersSelf > totalDistanceInMetersOther):
            return True
        else:
            return False
    

    def __eq__(self,other):
        tempPlacesSelf = self.places
        tempPlacesOther = other.places
        tripInfoListSelf = self.generateTrip()
        tripInfoListOther= other.generateTrip()

        totalDistanceInMetersSelf = self.getDistance(self.places, tripInfoListSelf)
        totalDistanceInMetersOther = self.getDistance(other.places, tripInfoListOther)

        if(totalDistanceInMetersSelf == totalDistanceInMetersOther):
            return True
        else:
            return False


    def __lt__(self, other):
        return not (self.__gt__(other) or self.__eq__(other))

    def __str__(self):
        placesString = ""
        tempPlaces = self.places
        for item in range(len(tempPlaces)):
            placesString = placesString+ f'Location1 object {item} has latitude of {tempPlaces[item].latitude} and longitude of {tempPlaces[item].longitude} \n'
        
        return placesString








# l1 = Location('Saginaw Valley State University')
# print(l1)

t1 = Trip('new york , ny ','boston, ma ','washington, dc')


# t1.getWeather({})
t1.summary()


# t2 = Trip('flatiron building ny ','smithsonian dc', 'yankees stadium boston ')
# t2 = t2 + 'boston city hall'
# t2.summary()


t3 = Trip('7400 bay rd saginaw','bay city mi','midland, mi')
t3 = t3 * 4
t3.summary()

print(t3==t3)
