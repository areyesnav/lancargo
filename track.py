#!/usr/var/python
#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import string
import random
soup = ''
class Aduana():
		
	def str_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))

	def mimp(self, manifiesto):
		url = 'www.aduanet.gob.pe/servlet/CRManManif?CMc1_Anno=2014&CMc1_Numero=%s&CG_cadu=235&viat=4&CMc1_Terminal=0000&TipM=mc' % manifiesto
		r = requests.get("http://" + url)
		todo = r.text
		soup = BeautifulSoup(todo)

		f = open('aduana.xls','w')
		f.write(soup.get_text().encode('utf-8'))
		f.close()

	def mexp(self, *manifiesto):
		session = self.str_generator()
		self = manifiesto
		#www.aduanet.gob.pe/servlet/CRManManif;jsessionid=JLWsBc40J!18593?CMc1_Anno=2014&CMc1_Numero=1011&CG_cadu=235&viat=4&CMc1_Terminal=0000&TipM=mx'
		for man in manifiesto:
			url = 'www.aduanet.gob.pe/servlet/CRManManif;jsessionid=%s?CMc1_Anno=2014&CMc1_Numero=%s&CG_cadu=235&viat=4&CMc1_Terminal=0000&TipM=mx' % (session, manifiesto)
			r = requests.get("http://" + url)
			soup = BeautifulSoup(r.text)
			calato = soup.get_text().encode('utf-8')	
			
			# magia = [s.strip() for s in calato.splitlines()]

			f = open('aduana.txt','a')
			f.write(str(calato))
			f.close(
