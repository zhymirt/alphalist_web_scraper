from bs4 import BeautifulSoup
import requests
import urllib.request
import time

url = ''

def get_website ( url ):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')