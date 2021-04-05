import requests

class Location:
    def __init__(self, address):
        # self.latitude = latitude
        # self.longitude = longitude
        self.address = address
        res = requests.get(f'https://api.tomtom.com/search/2/geocode/{address}.json?key=eOLkHP2OmPP0sZMvegeShZXWUuYx3UKt')
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

                 res = requests.get(f'https://api.tomtom.com/routing/1/calculateRoute/{latOfCurLoc},{longOfCurLoc}:{latOfNextLoc},{longOfNextLoc}/json?&key=eOLkHP2OmPP0sZMvegeShZXWUuYx3UKt')
                 
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
            res = requests.get(f'http://api.weatherstack.com/current?access_key=3a9d8c0b203696e4497003a061de3659&query={item.latitude},{item.longitude}&units=f')
            print(f'http://api.weatherstack.com/current?access_key=3a9d8c0b203696e4497003a061de3659&query={item.latitude},{item.longitude}&units=f')
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
        print(tempPlaces)
        print(f'Here is a summer of your trip from {tempPlaces[0].address} to {tempPlaces[len(tempPlaces)-1].address}')   
        
     
        print("{:<20} {:<20} {:<30}{:<30}{:<30}".format('No','Origin','Destination', 'Distance (miles)', '  Time'))
        for index in range(len(tempPlaces)):
           
            if(index != len(tempPlaces)-1):
                
                print("{:<20} {:<20} {:<30} {:<30} {:<30}".format(index, tempPlaces[index].address, tempPlaces[index+1].address,self.convertMetersToMiles(tripInfoList[index][0]),self.convertSecondsToHoursMinutesAndSeconds(tripInfoList[index][1])))
    



    def __str__(self):
        placesString = ""
        tempPlaces = self.places
        for item in range(len(tempPlaces)):
            placesString = placesString+ f'Location1 object {item} has latitude of {tempPlaces[item].latitude} and longitude of {tempPlaces[item].longitude} \n'
        
        return placesString








l1 = Location('Saginaw Valley State University')
print(l1)

t1 = Trip('new york , ny ','boston, ma ','washington, dc')
print(t1)

t1.getWeather({})
t1.summary()


t2 = Trip('flatiron building ny ','smithsonian dc', 'yankees stadium boston ')
t2.summary()