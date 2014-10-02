#!/usr/bin/python
#-*- coding: utf-8 -*-


from bs4 import BeautifulSoup
import requests
import string
import random
soup = ''
session	= ''
numid = ''

class Manifiesto():
	def cruzada(size=6, chars=string.ascii_uppercase + string.digits):
		session = ''.join((random(chars) for _ in range(size)))

		
	def mimp(self, *numids):
		for numid in numids:
			url = 'www.aduanet.gob.pe/servlet/CRManManif?CMc1_Anno=2014&CMc1_Numero=%s&CG_cadu=235&viat=4&CMc1_Terminal=0000&TipM=mc' % numid
			r = requests.get("http://" + url)
			todo = r.text
			soup = BeautifulSoup(todo)

			for table in soup.find_all('table'):
				mazorca = [text for text in table.stripped_strings]
				print granos
				# f = open('aduana.txt','a')
				# f.write(table.get_text().encode('utf-8'))
				# f.close()

	def mexp(self, *numids): 
		session = self.cruzada()
		for numid in numids:
			#www.aduanet.gob.pe/servlet/CRManManif;jsessionid=JLWsBc40J!18593?CMc1_Anno=2014&CMc1_Numero=1011&CG_cadu=235&viat=4&CMc1_Terminal=0000&TipM=mx
			url = 'www.aduanet.gob.pe/servlet/CRManManif;jsessionid=%s?CMc1_Anno=2014&CMc1_Numero=%s&CG_cadu=235&viat=4&CMc1_Terminal=0000&TipM=mx' % (session, numid)
			r = requests.get("http://" + url)
			todo = r.text
			soup = BeautifulSoup(todo)
			
			f = open('aduana.txt','a')
			f.write(soup.get_text().encode('utf-8'))
			f.close()
