import csv
import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import urllib.parse
import config

request = urllib.request.Request(config.LINK_TO_SCRAPE)
response = urllib.request.urlopen(request)
soup = BeautifulSoup(response, "html.parser")
downloads_dir = os.path.dirname(os.path.abspath(__file__)) + '\downloads'
table = soup.find('table', attrs={'id':'calendar'})

for a in table.findAll('a'):
	filename = a['href'] 
	dir = filename.replace("/", "\\")
	file_path = os.path.join(downloads_dir, dir)
'''
	if not os.path.isfile(file_path):
		url = config.FILE_BASE + filename
		path = urllib.parse.urlparse(url).path
		ext = os.path.splitext(path)[1]
		if ext in config.FILE_TYPES:
			file = urllib.request.urlopen(url)
			print (file_path)
			output = open(os.path.join(file_path),'wb')
			output.write(file.read())
			output.close()
			print('Downloaded: ' + filename)
	else:
		print (dir + " was already downloaded.")
'''