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
PAUSE = 3

URL = 'http://www.albonazionalegestoriambientali.it/Services/GetRicerche.asmx/GetCerDettaglio'

def main():
    conn = None
    try:
        conn = sqlite3.connect("comp.db3")
        cur = conn.cursor()

        results = cur.execute("select impresa from impresas where cer = 0 order by impresa")
        impresa_list = results.fetchall()

        counter = 0
        for impresa_id in impresa_list:
            try:
                if counter == 5:
                    time.sleep(counter)
                    counter = 0
                else:
                    counter += 1

                headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type':'application/json'}
                data = "{'lang':'it', 'idImpresa':" + str(impresa_id[0]) + "}"
                r = requests.post(URL, headers=headers, data=data)
                time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
                if r.status_code == 200:
                    records = json.loads(r.content)
                    rows = []
                    record_count = len(records['d'])
                    for  i in range(0, record_count):
                        impresa = codice = descrizione = ''
                        try:
                            impresa = str(impresa_id[0])
                            if impresa == 0:
                                continue
                        except Exception as e:
                            pass
                        try:
                            codice = records['d'][i]['Codice']
                        except Exception as e:
                            pass
                        try:
                            descrizione = records['d'][i]['Descrizione']
                        except Exception as e:
                            pass
                        rows.append((impresa, codice, descrizione,))
                    try:
                        sql = "insert into cer_own_account(impresa, codice, descrizione) values (?,?,?)"
                        cur.executemany(sql, rows)
                        print("cer_own_account impresa - " + str(impresa))
                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass

                    cur.execute("update impresas set cer = 1 where impresa = ? and cer = 0", (impresa_id[0],))
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