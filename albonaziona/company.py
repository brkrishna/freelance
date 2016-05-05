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

import requests, json, time, sqlite3, random

MIN_WAIT = 2
MAX_WAIT = 3

URL = 'http://www.albonazionalegestoriambientali.it/Services/GetRicerche.asmx/GetImpresaDettaglioConsorzio'

def main():
    conn = None
    try:
        conn = sqlite3.connect("comp.db3")
        cur = conn.cursor()

        results = cur.execute("select impresa from impresas where done = 0 order by impresa")
        impresa_list = results.fetchall()

        for impresa_id in impresa_list:
            try:
                headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type':'application/json'}
                data = "{'lang':'it', 'idImpresa':" + str(impresa_id[0]) + "}"
                r = requests.post(URL, headers=headers, data=data)
                time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
                if r.status_code == 200:
                    record = json.loads(r.content)
                    impresa = p_iscrizione = n_iscrizione = denominazione = codicefiscale = via = cap = comune = sigla_provincia = sezione = ''
                    try:
                        impresa = record['d']['IdImpresa']
                        if impresa == 0:
                            continue
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass
                    try:
                        p_iscrizione = record['d']['ProvinciaIscrizione']
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass
                    try:
                        n_iscrizione = record['d']['NumeroIscrizione']
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass
                    try:
                        denominazione = record['d']['Denominazione']
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass
                    try:
                        codicefiscale = record['d']['CodiceFiscale']
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass
                    try:
                        sezione = record['d']['Sezione']
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass
                    try:
                        via = record['d']['Via']
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass
                    try:
                        cap = record['d']['Cap']
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass
                    try:
                        comune = record['d']['Comune']
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass
                    try:
                        sigla_provincia = record['d']['SiglaProvincia']
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass
                    try:
                        sql = "insert or ignore into companies(impresa, p_iscrizione, n_iscrizione, denominazione, codicefiscale, via, cap, comune, sigla_provincia, sezione) values"
                        sql += "(?,?,?,?,?,?,?,?,?,?)"
                        cur.execute(sql, (impresa, p_iscrizione, n_iscrizione, denominazione, codicefiscale, via, cap, comune, sigla_provincia, sezione,))
                        print("companies impresa - " + str(impresa))
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass

                    cur.execute("update impresas set done = 1 where impresa = ? and done  = 0", (impresa_id[0],))
                    conn.commit()

            except Exception as e:
                print(e.__doc__)
                print(e.args)

    except Exception as e:
        print(e.__doc__)
        print(e.args)

    finally:
        if conn != None:
            conn.commit()
            conn = None

if __name__ == '__main__':
	main()