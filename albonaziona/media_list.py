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
import socks, socket

socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9150)
socket.socket = socks.socksocket

MIN_WAIT = 1
MAX_WAIT = 2

URL = 'http://www.albonazionalegestoriambientali.it/Services/GetRicerche.asmx/GetImpresaMezzi'

def main():
    conn = None
    try:
        conn = sqlite3.connect("comp.db3")
        cur = conn.cursor()

        results = cur.execute("select impresa from impresas where impresa not in (select impresa from media_list) order by impresa")
        impresa_list = results.fetchall()

        for impresa_id in impresa_list:
            try:
                headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type':'application/json'}
                data = "{'lang':'it', 'idImpresa':" + str(impresa_id[0]) + "}"
                r = requests.post(URL, headers=headers, data=data)
                time.sleep(random.randint(MIN_WAIT, MAX_WAIT))
                if r.status_code == 200:
                    records = r.json()
                    rows = []
                    record_count = len(records['d']['itemsList'])
                    for  i in range(0, record_count):
                        impresa = targa = tipo_mezzo = catg_attive = ''
                        try:
                            impresa = str(impresa_id[0])
                            if impresa == 0:
                                continue
                        except Exception as e:
                            pass
                        try:
                            targa = records['d']['itemsList'][i]['Targa']
                        except Exception as e:
                            pass
                        try:
                            catg_attive = records['d']['itemsList'][i]['CategorieAttive']
                        except Exception as e:
                            pass
                        try:
                            tipo_mezzo = records['d']['itemsList'][i]['TipoMezzo']
                        except Exception as e:
                            pass
                        rows.append((impresa, targa, tipo_mezzo, catg_attive,))

                    try:
                        if len(rows) > 0:
                            sql = "insert into media_list(impresa, targa, tipo_mezzo, catg_attive) values (?,?,?,?)"
                            cur.executemany(sql, rows)
                        else:
                            sql = "insert into media_list(impresa) values (?)"
                            cur.execute(sql, (impresa_id[0],))

                    except Exception as e:
                        print(e.__doc__)
                        print(e.args)
                        pass

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