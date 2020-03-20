from requests import get
import json

class covidUpdate:
    def __init__(self, BOOL_country_data=False):
        #
        url = "https://corona.lmao.ninja/"
        serializedCountryData = None
        #
        try:
            a = get(f"{url}all", allow_redirects=True)
        except Exception as b:
            raise b
        aj = a.json()
        #
        if BOOL_country_data:
            serializedCountryData = {}
            try:
                c = get(f"{url}countries", allow_redirects=True)
            except Exception as d:
                raise d
            #
            unserializedCountryData = json.loads(c.text)
            #
            for x in range(0, len(unserializedCountryData)):
                serializedCountryData[unserializedCountryData[x]['country']] = unserializedCountryData[x]
        #
        self.totalCases = aj['cases']
        self.totalDeaths = aj['deaths']
        self.totalRecovered = aj['recovered']
        self.timeUpdatedUnix = aj['updated']
        #
        self.countryData = serializedCountryData
        # cases, todayCases, deaths, todayDeaths, recovered, active, critical, casesPerOneMillion
