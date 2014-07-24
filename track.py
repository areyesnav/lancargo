#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
soup = ''

class Aduana():
	def con_exp(self, manifiesto):

		self = manifiesto

		url = 'www.aduanet.gob.pe/servlet/CRManManif?CMc1_Anno=2014&CMc1_Numero=%s&CG_cadu=235&viat=4&CMc1_Terminal=0000&TipM=mc' % manifiesto
		r = requests.get("http://" + url)
		todo = r.text
		soup = BeautifulSoup(todo)

		f = open('aduana.txt','w')
		f.write(soup.get_text().encode('utf-8'))
		f.close()
