import requests
import haversine


class RequestForm:
    def __init__(self, stpoint, edpoint='МКАД'):
        # setup the parameters to make a request
        self.api_key = '9051fbbb-da35-4559-8a75-0cdf78717b74'
        self.url_bse = 'https://geocode-maps.yandex.ru/1.x/?'
        # start point
        self.stpoint = stpoint
        # endpoint -> default = 'МКАД' (Moscow Ring Road)
        self.edpoint = edpoint

    def get_response(self, point):
        # Make a request and convert to json
        return requests.get(
            self.url_bse,
            params={
                'apikey': self.api_key,
                'geocode': point,
                'format': 'json'
            }
        ).json()

    def get_coord(self, response):
        try:
            distance = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(
                ' ')
        except:
            distance = [0, 0]

        return (float(distance[0]), float(distance[1]))

    def get_distance(self, coordA, coordB):
        return haversine.haversine((coordA), (coordB))

    def call_func(self):
        coordA = self.get_coord(self.get_response(self.stpoint))
        coordB = self.get_coord(self.get_response(self.edpoint))

        return self.get_distance(coordA, coordB)
