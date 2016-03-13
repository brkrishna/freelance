edupersonaffiliation=student&objectclass=person&tnleftutdate=false&	=netid+aa*



import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/home/ramakrishna/projects/freelance'])

Python 3.5.1 |Anaconda 2.4.1 (64-bit)| (default, Dec  7 2015, 11:16:01) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
In[2]: import requests
In[3]: url = 'https://directory.utk.edu/search'
In[4]: headers = {'User-Agent': 'Mozilla/5.0'}
In[5]: data = {'edupersonaffiliation':'student', 'objectclass':'person', 'tnleftutdate':'false', 'query':'netid+aa*'}
In[6]: s = requests.session()
In[7]: r = s.post(url, headers=headers, data=data)
In[8]: r.status_code
Out[8]: 200
In[9]: from bs4 import BeautifulSoup, SoupStrainer
In[10]: tree = BeautifulSoup(r.content, "html.parser", parse_only=SoupStrainer('dl', {'id':'queryresults'}))
In[11]: tree.findAll('dt')
Out[11]: []