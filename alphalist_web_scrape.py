from bs4 import BeautifulSoup
import urllib.request
import time
import requests

url='https://www.alphalists.com/list/alphabetical-list-fruit'
name='FruitList.txt'

def get_alphalist_site(url, parser='html.parser'):
	response = requests.get(url)
	print("site collected")
	soup = BeautifulSoup(response.text, parser)
	t_list = soup.find_all('div', class_='field field-name-field-list field-type-text-long field-label-hidden')
	if not t_list:
		print("list was empty")
		return False
	else:
		print("getting first in list")
		target_list = t_list[0].get_text()
	title = soup.title.get_text().split('|')[0]
	title = title.replace(title.split(' ')[0],'').strip()
	title = title.replace(' ','_').lower()
	write_to_file(title, target_list)

def get_alphalist(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	target_text = soup.find_all('div', class_='field field-name-field-list field-type-text-long field-label-hidden')[0].get_text()
	# target_text = soup.find_all('p')[0].get_text()
	print(target_text)
	return target_text

def get_list_name(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	title = soup.title.get_text().split('|')[0]
	title = title.replace(title.split(' ')[0],'').strip()
	title = title.replace(' ','_').lower()
	return title

def write_to_file(filename, text, append=False):
	newfile = open(filename, 'a+') if append else open(filename, 'w+')
	newfile.write(text)
	newfile.close()
	print("File written")

# print(get_alphalist('http://www.alphalists.com/list/alphabetical-list-vegetables'))
# time.sleep(5)
# get_alphalist_site('http://www.alphalists.com/list/alphabetical-list-vegetables')

# target = get_alphalist(url)
# write_to_file(name, get_alphalist(url))
# time.sleep(5)

# get_alphalist('http://www.alphalists.com/list/alphabetical-list-fruit')
url_file = open('alphalist_urls.txt', 'r')
# url_list = url_file.readlines()


# print(url_list)
# for u in url_list:
# 	print(u)

for u in url_file:
	if(u.endswith("\n")):
		newU = u.rsplit('\n', 1)[0]
		get_alphalist_site(newU)
	else:
		get_alphalist_site(u)
	time.sleep(3)

url_file.close()