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


l1 = Location('Saginaw Valley State University')
print(l1)
