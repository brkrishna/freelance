# -- coding: utf-8 --
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

		results = cur.execute("select impresa from impresas where impresa not in (select impresa from companies) order by impresa")
		impresa_list = results.fetchall()
		terms = list(i[0] for i in impresa_list)

		queue = Queue()

		for x in range(1):
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
		print(term)
		headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type':'application/json'}
		data = "{'lang':'it', 'idImpresa':" + str(term) + "}"
		r = requests.post(URL, headers=headers, data=data)
		time.sleep(random.randint(MIN, MAX))
		cur = conn.cursor()

		if r.status_code == 200:
			records = r.json()
			impresa = p_iscrizione = n_iscrizione = denominazione = codicefiscale = via = cap = comune = sigla_provincia = ''
			try:
				impresa = str(term)
				if impresa == 0:
					return
			except Exception as e:
				pass
			try:
				p_iscrizione = records['d']['ProvinciaIscrizione']
			except Exception as e:
				pass
			try:
				n_iscrizione = records['d']['NumeroIscrizione']
			except Exception as e:
				pass
			try:
				denominazione = records['d']['Denominazione']
			except Exception as e:
				pass
			try:
				codicefiscale = records['d']['CodiceFiscale']
			except Exception as e:
				pass
			try:
				via = records['d']['Via']
			except Exception as e:
				pass
			try:
				cap = records['d']['Cap']
			except Exception as e:
				pass
			try:
				comune = records['d']['Comune']
			except Exception as e:
				pass
			try:
				sigla_provincia = records['d']['SiglaProvincia']
			except Exception as e:
				pass
			try:
				if p_iscrizione != '':
					sql = "insert or ignore into companies(impresa,p_iscrizione,n_iscrizione,denominazione,codicefiscale,via,cap,comune,sigla_provincia) values (?,?,?,?,?,?,?,?,?)"
					cur.execute(sql, (impresa,p_iscrizione,n_iscrizione,denominazione,codicefiscale,via,cap,comune,sigla_provincia,))
			except Exception as e:
				print(e.__doc__)
				print(e.args)
				pass

			rows = []
			record_count = len(records['d']['CategorieLista'])
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

