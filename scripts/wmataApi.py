######################################
# Request data from the WMATA API
######################################

import requests

class WMATA_API_ERROR(Exception):
    def __init__(self, requestObj):
        self.requestObj = requestObj
    def __str__(self):
        return 'Url=%s, status_code=%i'%(self.requestObj.url, self.requestObj.status_code)

class WMATA_API(object):
    
    def __init__(self, key):
        self.API_KEY = key
        self.URL_BASE = 'http://api.wmata.com'
        if not self.API_KEY:
            raise RuntimeError('WMATA_API received invalid API key')

    # Check if a request is okay. If it isn't raise WMATA_API_ERROR
    def checkRequest(self, req):    
        if req.status_code != requests.codes.ok:
            raise WMATA_API_ERROR(req)

    def request(self, url, params):
        payload = { 'api_key' : self.API_KEY }
        if params is not None:
            payload.update(params)
        r = requests.get(url, params=payload)
        self.checkRequest(r)
        return r

    # Request the static webpage with elevator/escalator status
    def getEscalatorWebpageStatus(self):
        url = 'http://www.wmata.com/rider_tools/metro_service_status/elevator_escalator.cfm'
        r = requests.get(url)
        return r

    def getStations(self, params = None):
        base = '%s/Rail.svc/json'%self.URL_BASE
        url = '{base}/JStations'.format(base=base)
        return self.request(url, params)

    def getLines(self, params = None):
        base = '%s/Rail.svc/json'%self.URL_BASE
        url = '{base}/JLines'.format(base=base)
        return self.request(url, params)

    def getStationInfo(self, params = None):
        base = '%s/Rail.svc/json'%self.URL_BASE
        url = '{base}/JStationInfo'.format(base=base)
        return self.request(url, params)

    def getIncidents(self, params = None):
        base = '%s/Incidents.svc/json'%(self.URL_BASE)
        url = '{base}/Incidents'.format(url)
        return self.request(url, params)

    def getEscalator(self, params = None):
        base = '%s/Incidents.svc/json'%(self.URL_BASE)
        url = '{base}/ElevatorIncidents'.format(base=base)
        return self.request(url, params)
