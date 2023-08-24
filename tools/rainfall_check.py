from langchain.agents import Tool
import requests
import urllib
import urllib.parse

def rainfall_check(input):
    res = requests.get("https://data.weather.gov.hk/weatherAPI/opendata/hourlyRainfall.php?lang=en")
    for element in res.json()['hourlyRainfall']:
        if element['automaticWeatherStation'] == input:
            return [f"{element['automaticWeatherStation']} is {element['value']} {element['unit']}"]

rainfall_checking = Tool(
    name="rainfall",
    func=rainfall_check,
    description="Use this tool when user want to ask for the rainfall.",
    return_direct=True
)