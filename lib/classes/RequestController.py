import json
import requests
#'https://opensky-network.org/api/states/all?lamin=45.8389&lomin=5.9962&lamax=47.8229&lomax=10.5226'
#https://opensky-network.org/api/states/all
class RequestController:
    def __init__(self, api):
        self.api = api

    def request(self):
        r = requests.get(self.api)
        packages_json = r.json()
        packages_str = json.dumps(packages_json, indent = 2)
        packages_dict = json.loads(packages_str)
        res = list()
        for el in packages_dict['states']:
            temp = self.to_dict(el)
            res.append(temp)
        return res

    def to_dict(self, A):
        d = dict()
        d['id'] = A[0]
        d['callsight'] = A[1]
        d['country'] = A[2]
        d['time_position'] = A[3]
        d['last_contact'] = A[4]
        d['longitude'] = A[5]
        d['latitude'] = A[6]
        d['baro_altitude'] = A[7]
        d['on_ground'] = A[8]
        d['velocity'] = A[9]
        d['true_track'] = A[10]
        d['vertical_rate'] = A[11]
        d['sensors'] = A[12]
        d['geo_altitude'] = A[13]
        d['squawk'] = A[14]
        d['spi'] = A[15]
        d['position_source'] = A[16]
        return d

test = RequestController('https://opensky-network.org/api/states/all')
print(test.request())




