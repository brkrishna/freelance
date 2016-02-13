# -- coding: utf-8 --
import requests, os, time, random
from lxml import html

url = 'http://www.oddsshark.com/nfl/offensive-stats'

def main():

    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, headers=headers)
        time.sleep(random.randint(0,2))
        tree = html.fromstring(r.content)
        records = []
        trs = tree.xpath("//table[@class='base-table base-table-sortable']//tr")
        print(len(trs))
        for tr in trs:
            line = '$$$'.join(tr.xpath("*//text()[normalize-space()]"))
            records.append(line.replace("\n", ""))
                
        with open('oddshark','a') as f:
            f.write("\n".join(records))
                
    except Exception as e:
        print(e.__doc__)
        print(e.args)

if __name__ == '__main__':
    main()