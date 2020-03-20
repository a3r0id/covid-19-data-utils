# Covid 19 Tools

## THE API CREDIT GOES TO [corona.lmao.ninja](https://github.com/NovelCOVID/API), big thanks!

## Javascript Example
Just a basic (but totally working) concept for a live Covid-19 update webpage, by country.

## Python API Wrapper
Interacts with the API.
Hopefully this saves some people a few steps :)
Enjoy!

-------

### Without using "countries" endpoint:

```py

from covid-19-utils import *

#define the object
x = covidUpdate(BOOL_country_data=False)

print(x.totalCases)
print(x.totalDeaths)
print(x.totalRecovered)
print(x.timeUpdatedUnix)
```
-------

### Using both endpoints:
```py

from covid-19-utils import *

#define the object
x = covidUpdate(BOOL_country_data=True)

print(x.totalCases)
print(x.totalDeaths)
print(x.totalRecovered)
print(x.timeUpdatedUnix)

#Possible Usage: cases, todayCases, deaths, todayDeaths, recovered, active, critical, casesPerOneMillion
print(x.countryData['China']['cases'])
print(x.countryData['China']['todayCases'])

```

### Enjoy and be safe!
