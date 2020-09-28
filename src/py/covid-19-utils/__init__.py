from requests import get
import json
from os import getcwd
#NOT PROFICIENT FOR ASYNC! May be subject to blocking.

class getCdcWorldMap:
    def __init__(self):
        fname = "cdc_world_map.png"
        url = "https://www.cdc.gov/coronavirus/2019-ncov/images/outbreak-coronavirus-world.png"
        with open(fname, 'wb') as handle:
            response = get(
                url, stream=True
                )
            if not response.ok:
                    raise "cdcWorldMap::Error::Failed to download image"
                    fname = None
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
        if fname is not None:
            fst = f"{getcwd()}/{fname}"
        else: fst = None
        self.WorldMapLocalFile = fst
        self.WorldMapLink = url
        self.WorldMapHtml = f"""<img src="{self.WorldMapLink}">"""
        

class getCountryFlag:
    # Gets BEST choice country, based on input and returns flag links.
    def __init__(self, countryName, download=False):
           
        alpha_2 = get(f"https://restcountries.eu/rest/v2/name/{countryName}").json()[0]['alpha2Code']
        self.flagHtml = f"""<img src="https://www.countryflags.io/{alpha_2}/shiny/64.png">"""
        self.flagLink = f"https://www.countryflags.io/{alpha_2}/shiny/64.png"
        
        if download:
            fname = f"{alpha_2}.png"
            with open(fname, 'wb') as handle:
                response = get(
                    self.flagLink, stream=True
                    )
                if not response.ok:
                        raise "getCountryFlag::Error::Failed to download image"
                        fname = None
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
            if fname is not None:
                self.flagLocalFile = f"{getcwd()}/{fname}"
            else: self.flagLocalFile = None             


class covidUpdate:
    def __init__(self, BOOL_country_data=False):
        # API Updated to endpoint: 'V2'
        url = "https://corona.lmao.ninja/v2/"
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

