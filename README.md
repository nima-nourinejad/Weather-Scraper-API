# Weather Scraper API


## Introduction
This project utilizes FastAPI, requests, and BeautifulSoup to create an API that fetches real-time weather data from weather.com. It provides a simple and efficient way to retrieve weather information based on location.

## Features
- FastAPI: Utilizes FastAPI for building the web API, providing high performance and easy-to-use endpoints.
- Web Scraping: Implements web scraping with BeautifulSoup to extract weather data from weather.com.
- Real-Time Data: Fetches real-time weather data, including temperature, location, and unit of measurement.
- Dynamic Location Detection: Automatically detects the location based on the user's IP address.

## Usage
1. Send a GET request to the root endpoint ("/") to retrieve real-time weather data.
2. The API will scrape weather data from weather.com and return it in the response.
3. The response includes the location, temperature, and unit of measurement.

