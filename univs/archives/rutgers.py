# -- coding: utf-8 --
#-------------------------------------------------------------------------------
# Name:        parser
# Purpose:
#
# Author:      Ramakrishna
#
# Created:     08/09/2015
# Copyright:   (c) Ramakrishna 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import requests, time, os, random
from lxml import html
import socks, socket

url = 'https://www.acs.rutgers.edu/pls/pdb_p/Pdb_Display.search_results?p_name_first=&p_name_last='

def boss():
    
    terms = set(open('search_terms').readlines())
    if os.path.isfile('rutgers_terms'):
        finished_terms = set(open('rutgers_terms').readlines())
        terms -= finished_terms
        
    socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
    socket.socket = socks.socksocket
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    s = requests.session()
    
    for term in terms:
        try:
            term = term.replace("\n","")
            r = s.get(url + term, headers=headers)
            
            tree = html.fromstring(r.content)
            table = tree.xpath("//table[@class='data']")
            anchors = []
            for tr in table[0].xpath("//tr"):
                d = tr.xpath("./td[2]/text()")
                if len(d) > 0:
                    if 'Student' in d[0].strip():
                        anchors.append(tr.xpath("td[1]/a/@href"))
                        
            records = []
            
            for rec in anchors:
                r2 = s.get(rec[0], verify=False, headers=headers)
                tree2 = html.fromstring(r2.content)
                div = tree2.xpath("//div[@class='dataset clear']/div")[0]
                
                name = details = ''
                
                name = div.xpath("//h3[@class='c']/text()[normalize-space()]")[0]
                
                for dt in div.xpath("//dl"):
                    recs = dt.xpath("./*//text()[normalize-space()]")
                    recs = map(str.strip, recs)
                    details += '$$$'.join(recs)
                details += ";;;"
                    
                if name != '':
                    records.append(name + '$$$' + details)
            
            with open('rutgers_data','a') as f:
                f.write('\n'.join(records)) if len(records) > 0 else None
                
        except IndexError:
            pass
        except Exception as e:
            print(e.__doc__)
            print(e.args)
        finally:
            with open('rutgers_terms','a') as f:
                f.write(term + "\n")
        
if __name__ == '__main__':
    boss()
