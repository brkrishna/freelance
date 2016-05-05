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
MAX_WAIT = 5

URL = 'http://www.albonazionalegestoriambientali.it/Services/GetRicerche.asmx/GetImpresaDettaglioConsorzio'

def main():
    conn = None
    try:
        conn = sqlite3.connect("comp.db3")
        cur = conn.cursor()

        results = cur.execute("select impresa from impresas where cat = 0 order by impresa")
        impresa_list = results.fetchall()

        for impresa_id in impresa_list:
            try:
                headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type':'application/json'}
                data = "{'lang':'it', 'idImpresa':" + str(impresa_id[0]) + "}"
                r = requests.post(URL, headers=headers, data=data)
                time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
                if r.status_code == 200:
                    records = json.loads(r.content)
                    rows = []
                    record_count = len(records['d']['CategorieLista'])
                    for  i in range(0, record_count):
                        impresa = categoria = tipo_iscrizione = classe = stato = causale_sospensione = sospesa_dal = sospesa_fino_al = inizio = data_scadenza = sotto_categoria = ''
                        try:
                            impresa = str(impresa_id[0])
                            if impresa == 0:
                                continue
                        except Exception as e:
                            pass
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
                        print("categories impresa - " + str(impresa_id[0]))
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass

                    cur.execute("update impresas set cat = 1 where impresa = ? and cat = 0", (impresa_id[0],))
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

