# -- coding: utf-8 --
import requests, os, time, random, json
from lxml import html
import sqlite3
import socks, socket

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
		results = cur.execute("select impresa from impresas where done = 0 and impresa not in (select impresa from companies) order by impresa")
		impresa_list = results.fetchall()
		terms = list(i[0] for i in impresa_list)

		terms_count = len(terms)
		for i in range(0, terms_count):
			result = worker(terms[i])
			if result != None:
				sql = "insert into companies(impresa,p_iscrizione,n_iscrizione,denominazione,codicefiscale,via,cap,comune,sigla_provincia) values (?,?,?,?,?,?,?,?,?)"
				cur.execute(sql, result)
				conn.commit()

	except Exception as e:
		print(e.__doc__)
		print(e.args)

	finally:
		if conn != None:
			conn.commit()
			conn = None

def worker(term):
	global conn
	try:
		print(term)
		headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type':'application/json'}
		data = "{'lang':'it', 'idImpresa':" + str(term) + "}"
		r = requests.post(URL, headers=headers, data=data)
		time.sleep(random.randint(MIN, MAX))
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
				if p_iscrizione:
					return (impresa,p_iscrizione,n_iscrizione,denominazione,codicefiscale,via,cap,comune,sigla_provincia,)
				else:
					return None
			except Exception as e:
				print(e.__doc__)
				print(e.args)
				pass

	except Exception as e:
		print(e.__doc__)
		print(e.args)

if __name__ == '__main__':
	main()