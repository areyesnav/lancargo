#!/usr/bin/python
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import string
import random
soup = ''
pais = ''
paises = ()

for pais in paises:
	#http://www.flightstats.com/go/Airline/airlinesOfTheWorld.do?query=A
	url = 'www.flightstats.com/go/Airport/airportsOfTheWorld.do?countryCode=%s' % pais

	r = requests.get("http://" + url)
	todo = r.text
	soup = BeautifulSoup(todo)
	
	for table in soup.find_all("table", "tableListingTable"):
		f = open('airports.html','a')
		f.write('<tr>' + pais + '</tr>')
		f.write(table.prettify())
		f.close()
