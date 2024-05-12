from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def ft_get():
	url = "https://weather.com/"
	response = requests.get(url)
	html_content = response.content
	soup = BeautifulSoup(html_content, "html.parser")
	
	elements_temp = soup.find("span", {"class": "TodayDetailsCard--feelsLikeTempValue--2icPt", "data-testid": "TemperatureValue"})
	temp = elements_temp.text
	new_temp = ""
	index = 0
	while (index < len(temp) - 1):
		new_temp += temp[index]
		index += 1
	elements_location = soup.find("h1", {"class": "CurrentConditions--location--1YWj_"})
	location = elements_location.text
	index = 0
	new_location = ""
	while (index < len(location) and location[index] != ","):
		new_location += location[index]
		index += 1
	elements_unit = soup.find("span", {"class": "LanguageSelector--unitDisplay--mr3Rx"})
	result = "Temperature in " + new_location + " feels like " + new_temp + " " + elements_unit.text
	return result
