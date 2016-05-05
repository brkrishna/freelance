# _*_ coding:utf-8 _*_
#-------------------------------------------------------------------------------
# Name:         albonazionalegestoriambientali_it
# Purpose:      Parse linked in given a list of companies and write users to a csv file
#
# Author:       Ramakrishna
#
# Created:      21/Feb/2016
# Copyright:    (c) Ramakrishna 2016
# Licence:      <your licence>
#-------------------------------------------------------------------------------

import requests, os, time, random, json
from selenium import webdriver
from lxml import html
import sqlite3
import socks, socket
from threading import Thread
from queue import Queue

MIN = 1
MAX = 3

URL = 'http://www.albonazionalegestoriambientali.it/Services/GetRicerche.asmx/GetImpresaDettaglioConsorzio'

conn = sqlite3.connect("comp.db3")

socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9150)
socket.socket = socks.socksocket

def main():
	global conn
	try:
		cur = conn.cursor()

		results = cur.execute("select impresa from impresas where impresa not in (select impresa from categories) order by impresa")
		impresa_list = results.fetchall()
		terms = list(i[0] for i in impresa_list)

		queue = Queue()

		for x in range(2):
			worker = Worker(queue)
			worker.daemon = True
			worker.start()

		terms_count = len(terms)
		for i in range(0, terms_count):
			queue.put(terms[i])

		queue.join()

	except Exception as e:
		print(e.__doc__)
		print(e.args)
	finally:
		if conn:
			conn.commit()
			conn = None

def process(term):
	conn = sqlite3.connect("comp.db3")
	#global conn
	try:
		headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type':'application/json'}
		data = "{'lang':'it', 'idImpresa':" + str(term) + "}"
		time.sleep(random.randint(MIN, MAX))
		r = requests.post(URL, headers=headers, data=data)
		cur = conn.cursor()

		if r.status_code == 200:
			records = r.json()

			rows = []
			record_count = len(records['d']['CategorieLista'])
			impresa = ''
			try:
				impresa = str(term)
				if impresa == 0:
					return
			except Exception as e:
				pass

			for  i in range(0, record_count):
				categoria = tipo_iscrizione = classe = stato = causale_sospensione = sospesa_dal = sospesa_fino_al = inizio = data_scadenza = sotto_categoria = ''
				try:
					categoria = records['d']['CategorieLista'][i]['SiglaCategoria']
				except Exception as e:
					pass
				try:
					tipo_iscrizione = records['d']['CategorieLista'][i]['TipoIscrizione']
				except Exception as e:
					pass
				try:
					classe = records['d']['CategorieLista'][i]['Classe']
				except Exception as e:
					pass
				try:
					stato = records['d']['CategorieLista'][i]['Stato']
				except Exception as e:
					pass
				try:
					causale_sospensione = records['d']['CategorieLista'][i]['SospensioneCausale']
				except Exception as e:
					pass
				try:
					sospesa_dal = records['d']['CategorieLista'][i]['SospensioneDal']
				except Exception as e:
					pass
				try:
					sospesa_fino_al = records['d']['CategorieLista'][i]['SospensioneAl']
				except Exception as e:
					pass
				try:
					inizio = records['d']['CategorieLista'][i]['DataIscrizione']
				except Exception as e:
					pass
				try:
					data_scadenza = records['d']['CategorieLista'][i]['DataScadenza']
				except Exception as e:
					pass
				try:
					sotto_categoria = records['d']['CategorieLista'][i]['SottoCategoria']
				except Exception as e:
					pass
				rows.append((impresa,categoria,tipo_iscrizione,classe,stato,causale_sospensione,sospesa_dal,sospesa_fino_al,inizio,data_scadenza,sotto_categoria,))
			try:
				if len(rows) > 0:
					sql = "insert into categories(impresa,categoria,tipo_iscrizione,classe,stato,causale_sospensione,sospesa_dal,sospesa_fino_al,inizio,data_scadenza,sotto_categoria) values (?,?,?,?,?,?,?,?,?,?,?)"
					cur.executemany(sql, rows)
				else:
					sql = "insert into categories(impresa) values (?)"
					cur.execute(sql, (impresa,))
			except Exception as e:
				print(e.__doc__)
				print(e.args)
				pass

			conn.commit()

	except Exception as e:
		print(e.__doc__)
		print(e.args)

class Worker(Thread):
	def __init__(self, queue):
		Thread.__init__(self)
		self.queue = queue

	def run(self):
		while True:
			term = self.queue.get()
			process(term)
			self.queue.task_done()

if __name__ == '__main__':
	main()

