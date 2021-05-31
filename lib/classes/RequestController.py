import datetime
import requests

class RequestController:
    '''
    RequestController class made for using API inside application
    example init: RequestController("https://opensky-network.org/api/flights/departure?")
    '''

    def __init__(self, api: str):
        self.__api = api

    def request(self, airport: str):
        begin_date = datetime.datetime(2020, 10, 18)
        end_date = datetime.datetime(2020, 10, 19)
        begin = int(begin_date.replace(tzinfo=datetime.timezone.utc).timestamp())
        end = int(end_date.replace(tzinfo=datetime.timezone.utc).timestamp())
        print(airport, begin, end)
        r = self.__api + f'airport={airport}&begin={begin}&end={end}'
        data_json = requests.get(r).json()

        return data_json







