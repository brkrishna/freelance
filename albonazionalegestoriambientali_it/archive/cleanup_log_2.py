Python 3.5.1 |Anaconda 2.4.1 (64-bit)| (default, Dec  7 2015, 11:16:01) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import requests
>>> from bs4 import BeautifulSoup
>>> base_url = 'https://groups.freecycle.org/group/bathfreecycle/posts/all'
>>> 
>>> headers = {'User-Agent': 'Mozilla/5.0'}
>>> 
>>> r = requests.get(base_url, headers=headers)
>>> tree = BeautifulSoup(r.content, "html.parser")
>>> table = tree,findAll('table', {'id':'group_posts_table'})
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    table = tree,findAll('table', {'id':'group_posts_table'})
NameError: name 'findAll' is not defined
>>> table = tree,find_all('table', {'id':'group_posts_table'})
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    table = tree,find_all('table', {'id':'group_posts_table'})
NameError: name 'find_all' is not defined
>>> tree.title
<title>Posts on the Bath Group | The Freecycle Network</title>
>>> table= tree.findAll('table', {'id':'group_posts_table'})
>>> anchors = table.find_all('a', href=True)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    anchors = table.find_all('a', href=True)
AttributeError: 'ResultSet' object has no attribute 'find_all'
>>> anchors = table.findAll('a', href=True)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    anchors = table.findAll('a', href=True)
AttributeError: 'ResultSet' object has no attribute 'findAll'
>>> table
[<table id="group_posts_table"> <tr class="candy2">
<td>
<a class="noDecoration" href="https://groups.freecycle.org/group/bathfreecycle/posts/53061324/4foot6%20bed%20headboard"> <span class="post_icon icon_wanted"><span>•</span> WANTED</span> </a>
<br/> Mon Mar  7 23:40:09 2016<br/>
    (#53061324)
  </td>
<td>
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53061324/4foot6%20bed%20headboard">4foot6 bed headboard</a>  (Westburry) <br/> <p class="textCenter">
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53061324/4foot6%20bed%20headboard">See details</a>
</p> </td>
</tr> <tr class="candy1">
<td>
<a class="noDecoration" href="https://groups.freecycle.org/group/bathfreecycle/posts/53059846/Upright%20piano"> <span class="post_icon icon_offer"><span>&gt;</span> OFFER</span> </a>
<br/> Mon Mar  7 21:47:48 2016<br/>
    (#53059846)
  </td>
<td>
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53059846/Upright%20piano">Upright piano</a>  (Bear Flat, Bath) <br/> <p class="textCenter">
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53059846/Upright%20piano">See details</a>
</p> </td>
</tr> <tr class="candy2">
<td>
<a class="noDecoration" href="https://groups.freecycle.org/group/bathfreecycle/posts/53057106/Bloc%20motocross%20goggles"> <span class="post_icon icon_offer"><span>&gt;</span> OFFER</span> </a>
<br/> Mon Mar  7 19:12:48 2016<br/>
    (#53057106)
  </td>
<td>
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53057106/Bloc%20motocross%20goggles">Bloc motocross goggles</a>  (Combe Down) <br/> <p class="textCenter">
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53057106/Bloc%20motocross%20goggles">See details</a>
</p> </td>
</tr> <tr class="candy1">
<td>
<a class="noDecoration" href="https://groups.freecycle.org/group/bathfreecycle/posts/53057084/Nachos%20%2F%20Crisps%20dip%20bowl"> <span class="post_icon icon_offer"><span>&gt;</span> OFFER</span> </a>
<br/> Mon Mar  7 19:10:54 2016<br/>
    (#53057084)
  </td>
<td>
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53057084/Nachos%20%2F%20Crisps%20dip%20bowl">Nachos / Crisps dip bowl</a>  (Combe Down) <br/> <p class="textCenter">
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53057084/Nachos%20%2F%20Crisps%20dip%20bowl">See details</a>
</p> </td>
</tr> <tr class="candy2">
<td>
<a class="noDecoration" href="https://groups.freecycle.org/group/bathfreecycle/posts/53055558/Monitor%20hp1702"> <span class="post_icon icon_offer"><span>&gt;</span> OFFER</span> </a>
<br/> Mon Mar  7 17:37:20 2016<br/>
    (#53055558)
  </td>
<td>
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53055558/Monitor%20hp1702">Monitor hp1702</a>  (Chilcompton) <br/> <p class="textCenter">
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53055558/Monitor%20hp1702">See details</a>
</p> </td>
</tr> <tr class="candy1">
<td>
<a class="noDecoration" href="https://groups.freecycle.org/group/bathfreecycle/posts/53055128/2%20dining%20chairs%20"> <span class="post_icon icon_offer"><span>&gt;</span> OFFER</span> </a>
<br/> Mon Mar  7 17:18:39 2016<br/>
    (#53055128)
  </td>
<td>
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53055128/2%20dining%20chairs%20">2 dining chairs </a>  (Widcombe) <br/> <p class="textCenter">
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53055128/2%20dining%20chairs%20">See details</a>
</p> </td>
</tr> <tr class="candy2">
<td>
<a class="noDecoration" href="https://groups.freecycle.org/group/bathfreecycle/posts/53054264/2%20venetian%20blinds"> <span class="post_icon icon_offer"><span>&gt;</span> OFFER</span> </a>
<br/> Mon Mar  7 16:44:23 2016<br/>
    (#53054264)
  </td>
<td>
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53054264/2%20venetian%20blinds">2 venetian blinds</a>  (Claverton Down) <br/> <p class="textCenter">
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53054264/2%20venetian%20blinds">See details</a>
</p> </td>
</tr> <tr class="candy1">
<td>
<a class="noDecoration" href="https://groups.freecycle.org/group/bathfreecycle/posts/53052630/Dreams%20Super%20King%20Size%20Memory%20Foam%20Mattress"> <span class="post_icon icon_offer"><span>&gt;</span> OFFER</span> </a>
<br/> Mon Mar  7 15:15:56 2016<br/>
    (#53052630)
  </td>
<td>
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53052630/Dreams%20Super%20King%20Size%20Memory%20Foam%20Mattress">Dreams Super King Size Memory Foam Mattress</a>  (Larkhall) <br/> <p class="textCenter">
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53052630/Dreams%20Super%20King%20Size%20Memory%20Foam%20Mattress">See details</a>
</p> </td>
</tr> <tr class="candy2">
<td>
<a class="noDecoration" href="https://groups.freecycle.org/group/bathfreecycle/posts/53049596/Leather%20sofa"> <span class="post_icon icon_offer"><span>&gt;</span> OFFER</span> </a>
<br/> Mon Mar  7 12:20:40 2016<br/>
    (#53049596)
  </td>
<td>
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53049596/Leather%20sofa">Leather sofa</a>  (Bradford on Avon) <br/> <p class="textCenter">
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53049596/Leather%20sofa">See details</a>
</p> </td>
</tr> <tr class="candy1">
<td>
<a class="noDecoration" href="https://groups.freecycle.org/group/bathfreecycle/posts/53048890/Paving%20slabs"> <span class="post_icon icon_wanted"><span>•</span> WANTED</span> </a>
<br/> Mon Mar  7 11:32:13 2016<br/>
    (#53048890)
  </td>
<td>
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53048890/Paving%20slabs">Paving slabs</a>  (Melksham ) <br/> <p class="textCenter">
<a href="https://groups.freecycle.org/group/bathfreecycle/posts/53048890/Paving%20slabs">See details</a>
</p> </td>
</tr> </table>]
>>> anchors = table[0].findAll('a', href=True)
>>> len(anchors)
30
>>> anchors[0]
<a class="noDecoration" href="https://groups.freecycle.org/group/bathfreecycle/posts/53061324/4foot6%20bed%20headboard"> <span class="post_icon icon_wanted"><span>•</span> WANTED</span> </a>
>>> anchors[0]['href']
'https://groups.freecycle.org/group/bathfreecycle/posts/53061324/4foot6%20bed%20headboard'
>>> from bs4 import BeautifulSoup, SoupStrainer
>>> tree = BeautifulSoup(r.content, "html.parser", SoupStrainer('table', {'id':'group_posts_table'}))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    tree = BeautifulSoup(r.content, "html.parser", SoupStrainer('table', {'id':'group_posts_table'}))
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/bs4/__init__.py", line 169, in __init__
    self.is_xml = builder.is_xml
AttributeError: 'SoupStrainer' object has no attribute 'is_xml'
>>> tree = BeautifulSoup(r.content, "html.parser", SoupStrainer=('table', {'id':'group_posts_table'}))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    tree = BeautifulSoup(r.content, "html.parser", SoupStrainer=('table', {'id':'group_posts_table'}))
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/bs4/__init__.py", line 143, in __init__
    "__init__() got an unexpected keyword argument '%s'" % arg)
TypeError: __init__() got an unexpected keyword argument 'SoupStrainer'
>>> tree = BeautifulSoup(r.content, "html.parser", parse_only=SoupStrainer('table', {'id':'group_posts_table'}))
>>> anchors = tree.findAll('a', href=True)
>>> anchors[0]
<a class="noDecoration" href="https://groups.freecycle.org/group/bathfreecycle/posts/53061324/4foot6%20bed%20headboard"> <span class="post_icon icon_wanted"><span>•</span> WANTED</span> </a>
>>> anchors = tree.findAll('a', href=True)['href']
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    anchors = tree.findAll('a', href=True)['href']
TypeError: list indices must be integers or slices, not str
>>> anchors = tree.findAll('a', href=True).get_attribute('href')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    anchors = tree.findAll('a', href=True).get_attribute('href')
AttributeError: 'ResultSet' object has no attribute 'get_attribute'
>>> url = 'https://groups.freecycle.org/group/bathfreecycle/posts/53048890/Paving%20slabs'
>>> r = requests.get(url, headers=headers)
>>> url = 'https://groups.freecycle.org/group/bathfreecycle/posts/53059846/Upright%20piano'
>>> r = requests.get(url, headers=headers)
>>> tree = BeautifulSoup(r.content, "html.parser", parse_only=SoupStrainer('div', {'id':'group_post'}))
>>> tree.contents
[<div id="group_post"> <nav> <a class="previousLink" href="https://groups.freecycle.org/group/bathfreecycle/posts/53057106">← Previous</a> <a class="nextLink" href="https://groups.freecycle.org/group/bathfreecycle/posts/53061324">Next →</a> <div class="clearLeft"></div>
</nav> <header>
<h2>Post ID: 53059846</h2>
<h2>OFFER: Upright piano</h2>
</header>
<div id="post_details"> <div><span>Location :</span>Bear Flat, Bath</div> <div><span>Date :</span> Mon Mar  7 21:47:48 2016</div> </div>
<div>
<h2>Description</h2> <div class="floatLeft textCenter">
<a href="https://groups.freecycle.org/group/bathfreecycle/post_image/53059846" onclick='fullsize_post_image( "https://groups.freecycle.org/group/bathfreecycle/post_image/53059846", "Upright piano"); return false'>
<img alt="Post image for Upright piano" id="post_thumbnail" src="https://groups.freecycle.org/group/bathfreecycle/post_thumb/53059846" width="128"/></a><br/> (click on the thumbnail for full size image) </div> <p>Upright piano available to collector. Last tuned 2 years ago.</p>
</div>
<div class="textCenter clearLeft">  You need to be <a class="link_login" href="http://my.freecycle.org/login?referer=https%3A%2F%2Fgroups.freecycle.org%2Fgroup%2Fbathfreecycle%2Fposts%2F53059846%2FUpright%2520piano">logged in</a> and a Member of this Group to reply to this Post  </div> <nav> <a class="previousLink" href="https://groups.freecycle.org/group/bathfreecycle/posts/53057106">← Previous</a> <a class="nextLink" href="https://groups.freecycle.org/group/bathfreecycle/posts/53061324">Next →</a> <div class="clearLeft"></div>
</nav> </div>]
>>> import re
>>> tree.find('h2', {'text':re.compile('^(Post)')})
>>> tree.find('h2')
<h2>Post ID: 53059846</h2>
>>> tree.findAll('h2')
[<h2>Post ID: 53059846</h2>, <h2>OFFER: Upright piano</h2>, <h2>Description</h2>]
>>> tree.find('h2', {'text':re.compile('Post')})
>>> tree.find('h2', {'text':re.compile('Post+')})
>>> tree.find('h2', {'text':re.compile('?(Post)+')})
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    tree.find('h2', {'text':re.compile('?(Post)+')})
  File "/home/ramakrishna/anaconda3/lib/python3.5/re.py", line 224, in compile
    return _compile(pattern, flags)
  File "/home/ramakrishna/anaconda3/lib/python3.5/re.py", line 293, in _compile
    p = sre_compile.compile(pattern, flags)
  File "/home/ramakrishna/anaconda3/lib/python3.5/sre_compile.py", line 536, in compile
    p = sre_parse.parse(p, flags)
  File "/home/ramakrishna/anaconda3/lib/python3.5/sre_parse.py", line 829, in parse
    p = _parse_sub(source, pattern, 0)
  File "/home/ramakrishna/anaconda3/lib/python3.5/sre_parse.py", line 437, in _parse_sub
    itemsappend(_parse(source, state))
  File "/home/ramakrishna/anaconda3/lib/python3.5/sre_parse.py", line 638, in _parse
    source.tell() - here + len(this))
sre_constants.error: nothing to repeat at position 0
>>> tree.find('h2', {'text':re.compile('(Post)+')})
>>> tree.find('h2', {'text':re.compile('Post')})
>>> tree.find('h2', {'text':re.compile('Post*')})
>>> p = tree.find('h2', {'text':re.compile('Post*')})
>>> p
>>> tree.find('h2', text = re.compile('Post*'))
<h2>Post ID: 53059846</h2>
>>> tree.find('h2', text = re.compile('Post*')).text
'Post ID: 53059846'
>>> tree.find('h2', text = re.compile('offer*')).text
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    tree.find('h2', text = re.compile('offer*')).text
AttributeError: 'NoneType' object has no attribute 'text'
>>> tree.find('h2', text = re.compile('offer*', re.IGNORECASE)).text
'OFFER: Upright piano'
>>> tree.find('h2', text = re.compile('ofr*', re.IGNORECASE)).text
'OFFER: Upright piano'
>>> tree.find('h2', text = re.compile('(ofr)*', re.IGNORECASE)).text
'Post ID: 53059846'
>>> tree.find('h2', text = re.compile('(offer)*', re.IGNORECASE)).text
'Post ID: 53059846'
>>> tree.find('h2', text = re.compile('offer*', re.IGNORECASE)).text
'OFFER: Upright piano'
>>> tree.find('h2', text = re.compile('oe*', re.IGNORECASE)).text
'Post ID: 53059846'
>>> tree.find('h2', text = re.compile('oe*')).text
'Post ID: 53059846'
>>> tree.find('h2', text = re.compile('e*')).text
'Post ID: 53059846'
>>> tree.find('h2', text = re.compile('post*')).text
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    tree.find('h2', text = re.compile('post*')).text
AttributeError: 'NoneType' object has no attribute 'text'
>>> tree.find('h2', text = re.compile('post*', re.IGNORECASE)).text
'Post ID: 53059846'
>>> tree.find('h2', text = re.compile('offer*', re.IGNORECASE)).text
'OFFER: Upright piano'
>>> tree.find('h2', text = re.compile('wanted*', re.IGNORECASE)).text
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    tree.find('h2', text = re.compile('wanted*', re.IGNORECASE)).text
AttributeError: 'NoneType' object has no attribute 'text'
>>> tree.find('h2', text = re.compile('wanted*', re.IGNORECASE))
>>> tree.find('h2', text = re.compile('offer*', re.IGNORECASE))
<h2>OFFER: Upright piano</h2>
>>> post_id = tree.find('h2', text = re.compile('post*', re.IGNORECASE))
>>> re.search("[0-9]*", post_id)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    re.search("[0-9]*", post_id)
  File "/home/ramakrishna/anaconda3/lib/python3.5/re.py", line 173, in search
    return _compile(pattern, flags).search(string)
TypeError: expected string or bytes-like object
>>> re.search("[0-9]*", post_id.text)
<_sre.SRE_Match object; span=(0, 0), match=''>
>>> re.search("[0-9]*", post_id.text).group()
''
>>> post_id
<h2>Post ID: 53059846</h2>
>>> res = re.match("[0-9]*", post_id.text)
>>> res
<_sre.SRE_Match object; span=(0, 0), match=''>
>>> res.groups()
()
>>> res.group()
''
>>> res = re.match("*[0-9]*", post_id.text)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    res = re.match("*[0-9]*", post_id.text)
  File "/home/ramakrishna/anaconda3/lib/python3.5/re.py", line 163, in match
    return _compile(pattern, flags).match(string)
  File "/home/ramakrishna/anaconda3/lib/python3.5/re.py", line 293, in _compile
    p = sre_compile.compile(pattern, flags)
  File "/home/ramakrishna/anaconda3/lib/python3.5/sre_compile.py", line 536, in compile
    p = sre_parse.parse(p, flags)
  File "/home/ramakrishna/anaconda3/lib/python3.5/sre_parse.py", line 829, in parse
    p = _parse_sub(source, pattern, 0)
  File "/home/ramakrishna/anaconda3/lib/python3.5/sre_parse.py", line 437, in _parse_sub
    itemsappend(_parse(source, state))
  File "/home/ramakrishna/anaconda3/lib/python3.5/sre_parse.py", line 638, in _parse
    source.tell() - here + len(this))
sre_constants.error: nothing to repeat at position 0
>>> res = re.match("+[0-9]*", post_id.text)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    res = re.match("+[0-9]*", post_id.text)
  File "/home/ramakrishna/anaconda3/lib/python3.5/re.py", line 163, in match
    return _compile(pattern, flags).match(string)
  File "/home/ramakrishna/anaconda3/lib/python3.5/re.py", line 293, in _compile
    p = sre_compile.compile(pattern, flags)
  File "/home/ramakrishna/anaconda3/lib/python3.5/sre_compile.py", line 536, in compile
    p = sre_parse.parse(p, flags)
  File "/home/ramakrishna/anaconda3/lib/python3.5/sre_parse.py", line 829, in parse
    p = _parse_sub(source, pattern, 0)
  File "/home/ramakrishna/anaconda3/lib/python3.5/sre_parse.py", line 437, in _parse_sub
    itemsappend(_parse(source, state))
  File "/home/ramakrishna/anaconda3/lib/python3.5/sre_parse.py", line 638, in _parse
    source.tell() - here + len(this))
sre_constants.error: nothing to repeat at position 0
>>> res = re.match("[0-9]", post_id.text)
>>> res
>>> post_id.text[post_id.text.find(":")+1:]
' 53059846'
>>> type_content = tree.find('h2', text = re.compile('offer*', re.IGNORECASE))
>>> type_content.text
'OFFER: Upright piano'
>>> res = re.match("[0-9]{3,8}", post_id.text)
>>> res
>>> res = re.match("[0-9]*", post_id.text)
>>> post_id.text
'Post ID: 53059846'
>>> res = re.match("[0-9]*", str(post_id.text))
>>> res
<_sre.SRE_Match object; span=(0, 0), match=''>
>>> res = re.match("[0-9]+", str(post_id.text))
>>> res
>>> res = re.match("[0-9]+", post_id.text)
>>> res
>>> re.search("[0-9]+", post_id.text)
<_sre.SRE_Match object; span=(9, 17), match='53059846'>
>>> re.search("[0-9]+", post_id.text).group()
'53059846'
>>> re.search("(Offer)+", type_content/text).group()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    re.search("(Offer)+", type_content/text).group()
NameError: name 'text' is not defined
>>> re.search("(Offer)+", type_content.text).group()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    re.search("(Offer)+", type_content.text).group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> type_content.text
'OFFER: Upright piano'
>>> re.search("(Offer)*", type_content.text).group()
''
>>> re.search("Offer*", type_content.text).group()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    re.search("Offer*", type_content.text).group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> re.search("OFFER*", type_content.text).group()
'OFFER'
>>> tree.find('h2', text = re.compile('post*', re.IGNORECASE))
<h2>Post ID: 53059846</h2>
>>> tree.find('h2', text = re.compile('offer*', re.IGNORECASE))
<h2>OFFER: Upright piano</h2>
>>> tc = tree.find('h2', text = re.compile('offer*', re.IGNORECASE))
>>> tc[tc.find(":")+1:]
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    tc[tc.find(":")+1:]
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
>>> tc = tree.find('h2', text = re.compile('offer*', re.IGNORECASE)).text
>>> tc[tc.find(":")+1:]
' Upright piano'
>>> tree.find('div',{'id':'post_details'})
<div id="post_details"> <div><span>Location :</span>Bear Flat, Bath</div> <div><span>Date :</span> Mon Mar  7 21:47:48 2016</div> </div>
>>> tree.find('div',{'id':'post_details'}).text
' Location :Bear Flat, Bath Date : Mon Mar  7 21:47:48 2016 '
>>> details = tree.find('div',{'id':'post_details'}).text
>>> details[details.find("Location:")+9:]
'n :Bear Flat, Bath Date : Mon Mar  7 21:47:48 2016 '
>>> details[details.find("Location:")+10:]
' :Bear Flat, Bath Date : Mon Mar  7 21:47:48 2016 '
>>> details[details.find("Location:")+11:]
':Bear Flat, Bath Date : Mon Mar  7 21:47:48 2016 '
>>> details[details.find("Location:")+12:]
'Bear Flat, Bath Date : Mon Mar  7 21:47:48 2016 '
>>> details[details.find("Location :")+10:]
'Bear Flat, Bath Date : Mon Mar  7 21:47:48 2016 '
>>> details[details.find("Location :")+10:details.find("Date")]
'Bear Flat, Bath '
>>> re.search("[0-9]{4}", details)
<_sre.SRE_Match object; span=(54, 58), match='2016'>
>>> re.match("[0-9]{4}", details)
>>> re.search("[0-9]{4}", details)
<_sre.SRE_Match object; span=(54, 58), match='2016'>
>>> re.search("([0-9]{2}):([0-9]{2}):([0-9]{2})", details)
<_sre.SRE_Match object; span=(45, 53), match='21:47:48'>
>>> re.search("([0-9]{2}):([0-9]{2}):([0-9]{2})", details).group()
'21:47:48'
>>> loc = details[details.find("Location :")+10:details.find("Date")]
>>> time = re.search("([0-9]{2}):([0-9]{2}):([0-9]{2})", details).group()
>>> date = details.replace(loc, "").replace(time, "")
>>> date
' Location :Date : Mon Mar  7  2016 '
>>> 
>>> date = details.replace(loc, "").replace(time, "").replace(":").replace("Location").replace("Date")
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    date = details.replace(loc, "").replace(time, "").replace(":").replace("Location").replace("Date")
TypeError: replace() takes at least 2 arguments (1 given)
>>> date = details.replace(loc, "").replace(time, "").replace(":").replace("Location").replace("Date")tree.find('h2', text = re.compile('Post*'))
SyntaxError: invalid syntax
>>> tree.find('h2', text = re.compile('Description*'))
<h2>Description</h2>
>>> tree.find("div", {"id":"post_details"}).find("p")
>>> tree.find("div", {"id":"group_post"}).find("p")
<p>Upright piano available to collector. Last tuned 2 years ago.</p>
>>> tree.find("div", {"id":"post_details"}).find("a", href=True)
>>> tree.find("div", {"id":"group_post"}).find("a")
<a class="previousLink" href="https://groups.freecycle.org/group/bathfreecycle/posts/53057106">← Previous</a>
>>> tree.find("div", {"id":"post_details"}).find("a", href=True)tree.find("div", {"id":"group_post"}).find("a")
SyntaxError: invalid syntax
>>> 
>>> tree.find("div", {"id":"group_post"}).findAll("a", href=True)
[<a class="previousLink" href="https://groups.freecycle.org/group/bathfreecycle/posts/53057106">← Previous</a>, <a class="nextLink" href="https://groups.freecycle.org/group/bathfreecycle/posts/53061324">Next →</a>, <a href="https://groups.freecycle.org/group/bathfreecycle/post_image/53059846" onclick='fullsize_post_image( "https://groups.freecycle.org/group/bathfreecycle/post_image/53059846", "Upright piano"); return false'>
<img alt="Post image for Upright piano" id="post_thumbnail" src="https://groups.freecycle.org/group/bathfreecycle/post_thumb/53059846" width="128"/></a>, <a class="link_login" href="http://my.freecycle.org/login?referer=https%3A%2F%2Fgroups.freecycle.org%2Fgroup%2Fbathfreecycle%2Fposts%2F53059846%2FUpright%2520piano">logged in</a>, <a class="previousLink" href="https://groups.freecycle.org/group/bathfreecycle/posts/53057106">← Previous</a>, <a class="nextLink" href="https://groups.freecycle.org/group/bathfreecycle/posts/53061324">Next →</a>]
>>> tree.find("div", {"id":"group_post"}).findAll("a", onclick=True)
[<a href="https://groups.freecycle.org/group/bathfreecycle/post_image/53059846" onclick='fullsize_post_image( "https://groups.freecycle.org/group/bathfreecycle/post_image/53059846", "Upright piano"); return false'>
<img alt="Post image for Upright piano" id="post_thumbnail" src="https://groups.freecycle.org/group/bathfreecycle/post_thumb/53059846" width="128"/></a>]
>>> tree.find("div", {"id":"group_post"}).findAll("a", onclick=True)['href']
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    tree.find("div", {"id":"group_post"}).findAll("a", onclick=True)['href']
TypeError: list indices must be integers or slices, not str
>>> tree.find("div", {"id":"group_post"}).findAll("a", onclick=True)[0]['href']
'https://groups.freecycle.org/group/bathfreecycle/post_image/53059846'
>>> url = ''https://groups.freecycle.org/group/bathfreecycle/posts/53048890/Paving%20slabs'
SyntaxError: invalid syntax
>>> url = 'https://groups.freecycle.org/group/bathfreecycle/posts/53048890/Paving%20slabs'
>>> r = requests.get(url, headers=headers)
>>> tree = BeautifulSoup(r.content, "html.parser", parse_only=SoupStrainer('div', {'id':'group_post'}))
>>> image_url = tree.find("div", {"id":"group_post"}).findAll("a", onclick=True)
>>> image_url
[]
>>> f = open('/home/ramakrishna/projects/freelance/albonazionalegestoriambientali_it/cittametropolitana', 'r')
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    f = open('/home/ramakrishna/projects/freelance/albonazionalegestoriambientali_it/cittametropolitana', 'r')
FileNotFoundError: [Errno 2] No such file or directory: '/home/ramakrishna/projects/freelance/albonazionalegestoriambientali_it/cittametropolitana'
>>> f = open('/home/ramakrishna/projects/freelance/albonazionalegestoriambientali_it/archives/cittametropolitana', 'r')
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    f = open('/home/ramakrishna/projects/freelance/albonazionalegestoriambientali_it/archives/cittametropolitana', 'r')
FileNotFoundError: [Errno 2] No such file or directory: '/home/ramakrishna/projects/freelance/albonazionalegestoriambientali_it/archives/cittametropolitana'
>>> f = open('/home/ramakrishna/projects/freelance/albonazionalegestoriambientali_it/archive/cittametropolitana', 'r')
>>> lines = f.readlines()
>>> for line in lines:
	row = line.split("$$$")
	emails = []
	for r in row:
		if 'e-mail' in r:
			emails.append(row[row.index("e-mail")+1].replace("###", "").replace("%%%", "").strip())
			
	try:
		print(emails[0])
	except:
		print("$$$")

consultastranieri@comune.abbiategrasso.mi.it
sportello.stranieri@comune.abbiategrasso.mi.it
lucianasala@aliceposta.it
faduma7@msn.com
$$$
$$$
$$$
sportello.stranieri@virgilio.it
$$$
ctparcore@virgilio.it
sportello.migranti@comune.rho.mi.it
$$$
orientamondo@comune.corsico.mi.it
Traceback (most recent call last):
  File "<pyshell#144>", line 6, in <module>
    emails.append(row[row.index("e-mail")+1].replace("###", "").replace("%%%", "").strip())
ValueError: 'e-mail' is not in list
>>>  for line in lines:
	row = line.split("$$$")
	emails = []
	if 'e-mail' in row or 'Email' in row or 'email' in row:
		emails.append(row[row.index("e-mail")+1].replace("###", "").replace("%%%", "").strip())
	try:
		print(emails[0])
	except:
		print("$$$")
		
SyntaxError: unexpected indent
>>> for line in lines:
	row = line.split("$$$")
	emails = []
	if 'e-mail' in row or 'Email' in row or 'email' in row:
		emails.append(row[row.index("e-mail")+1].replace("###", "").replace("%%%", "").strip())
	try:
		print(emails[0])
	except:
		print("$$$")

		
consultastranieri@comune.abbiategrasso.mi.it
sportello.stranieri@comune.abbiategrasso.mi.it
lucianasala@aliceposta.it
faduma7@msn.com
$$$
$$$
$$$
sportello.stranieri@virgilio.it
$$$
ctparcore@virgilio.it
sportello.migranti@comune.rho.mi.it
$$$
orientamondo@comune.corsico.mi.it
$$$
$$$
$$$
$$$
$$$
$$$
$$$
stars@comune.bernareggio.mi.it
servizisociali@comune.bernateticino.mi.it
$$$
$$$
$$$
servizisociali@comunebinasco.it
$$$
servizi.sociali@comune.bollate.mi.it
$$$
$$$
$$$
m.casiraghi@comune.brugherio.mi.it
$$$
orientamondo@comune.corsico.mi.it
$$$
sportello.stranieri@virgilio.it
$$$
$$$
ass.sociale@comune.bustogarolfo.mi.it
$$$
$$$
$$$
sociali@comune.canegrate.mi.it
$$$
carateservizisociali@tiscali.it
stars@comune.carnate.mi.it
$$$
$$$
$$$
$$$
$$$
$$$
amjadiqbal@libero.it
$$$
$$$
sportello.stranieri@virgilio.it
stars@comune.cavenagobrianza.mi.it
dagjoka@tiscali.it
$$$
$$$
orientamondo@comune.corsico.mi.it
$$$
floriana.pulcini@comune.cesano-maderno.mi.it
spazioimmigrazione@comuni-insieme.mi.it
africplus@yahoo.it
$$$
mappa_mondo_cinisellob@yahoo.it
$$$
$$$
$$$
Traceback (most recent call last):
  File "<pyshell#147>", line 5, in <module>
    emails.append(row[row.index("e-mail")+1].replace("###", "").replace("%%%", "").strip())
ValueError: 'e-mail' is not in list
>>> for line in lines:
	row = line.split("$$$")
	emails = []
	for r in row:
		if 'e-mail' in row or 'Email' in row or 'email' in row:
			emails.append(row[row.index("e-mail")+1].replace("###", "").replace("%%%", "").strip())
	try:
		print(emails)
	except:
		print("$$$")

		
['consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it']
['sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it']
['lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it']
['faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com']
[]
[]
[]
['sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it']
[]
['ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it']
['sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it']
[]
['orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it']
[]
[]
[]
[]
[]
[]
[]
['stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it']
['servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it']
[]
[]
[]
['servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it']
[]
['servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it']
[]
[]
[]
['m.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it']
[]
['orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it']
[]
['sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it']
[]
[]
['ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it']
[]
[]
[]
['sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it']
[]
['carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it']
['stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it']
[]
[]
[]
[]
[]
[]
['amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it']
[]
[]
['sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it']
['stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it']
['dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it']
[]
[]
['orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it']
[]
['floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it']
['spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it']
['africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it']
[]
['mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it']
[]
[]
[]
Traceback (most recent call last):
  File "<pyshell#149>", line 6, in <module>
    emails.append(row[row.index("e-mail")+1].replace("###", "").replace("%%%", "").strip())
ValueError: 'e-mail' is not in list
>>> for line in lines:
	row = line.split("$$$")
	emails = []
	for r in row:
		if 'e-mail' in row or 'Email' in row or 'email' in row:
			emails.append(row[row.index("e-mail")+1].replace("###", "").replace("%%%", "").strip())
	try:
		print(emails)
	except:
		print("$$$")
	email = []

	
['consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it', 'consultastranieri@comune.abbiategrasso.mi.it']
['sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it', 'sportello.stranieri@comune.abbiategrasso.mi.it']
['lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it', 'lucianasala@aliceposta.it']
['faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com', 'faduma7@msn.com']
[]
[]
[]
['sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it']
[]
['ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it', 'ctparcore@virgilio.it']
['sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it', 'sportello.migranti@comune.rho.mi.it']
[]
['orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it']
[]
[]
[]
[]
[]
[]
[]
['stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it', 'stars@comune.bernareggio.mi.it']
['servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it', 'servizisociali@comune.bernateticino.mi.it']
[]
[]
[]
['servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it', 'servizisociali@comunebinasco.it']
[]
['servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it', 'servizi.sociali@comune.bollate.mi.it']
[]
[]
[]
['m.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it', 'm.casiraghi@comune.brugherio.mi.it']
[]
['orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it']
[]
['sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it']
[]
[]
['ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it', 'ass.sociale@comune.bustogarolfo.mi.it']
[]
[]
[]
['sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it', 'sociali@comune.canegrate.mi.it']
[]
['carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it', 'carateservizisociali@tiscali.it']
['stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it', 'stars@comune.carnate.mi.it']
[]
[]
[]
[]
[]
[]
['amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it', 'amjadiqbal@libero.it']
[]
[]
['sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it', 'sportello.stranieri@virgilio.it']
['stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it', 'stars@comune.cavenagobrianza.mi.it']
['dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it', 'dagjoka@tiscali.it']
[]
[]
['orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it', 'orientamondo@comune.corsico.mi.it']
[]
['floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it', 'floriana.pulcini@comune.cesano-maderno.mi.it']
['spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it', 'spazioimmigrazione@comuni-insieme.mi.it']
['africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it', 'africplus@yahoo.it']
[]
['mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it', 'mappa_mondo_cinisellob@yahoo.it']
[]
[]
[]
Traceback (most recent call last):
  File "<pyshell#152>", line 6, in <module>
    emails.append(row[row.index("e-mail")+1].replace("###", "").replace("%%%", "").strip())
ValueError: 'e-mail' is not in list
>>> for line in lines:
	row = line.split("$$$")
	emails = []
	for r in row:
		if 'e-mail' in r or 'Email' in r or 'email' in r:
			emails.append(row[row.index("e-mail")+1].replace("###", "").replace("%%%", "").strip())
	try:
		print(emails)
	except:
		print("$$$")
	email = []

	
['consultastranieri@comune.abbiategrasso.mi.it']
['sportello.stranieri@comune.abbiategrasso.mi.it']
['lucianasala@aliceposta.it']
['faduma7@msn.com']
[]
[]
[]
['sportello.stranieri@virgilio.it']
[]
['ctparcore@virgilio.it']
['sportello.migranti@comune.rho.mi.it']
[]
['orientamondo@comune.corsico.mi.it']
Traceback (most recent call last):
  File "<pyshell#154>", line 6, in <module>
    emails.append(row[row.index("e-mail")+1].replace("###", "").replace("%%%", "").strip())
ValueError: 'e-mail' is not in list
>>> lines[0]
'Consulta Stranieri - Abbiategrasso $$$Consulta Stranieri di  Abbiategrasso$$$###%%%    area di intervento$$$###%%%    cultura, mediazione$$$###%%%profilo$$$###%%%la Consulta Stranieri vuole essere un osservatorio delle problematiche che  implicano un mutamento sociale, ed essere di supporto sia alle istituzioni  italiane sia alle comunitÃ\xa0 straniere per migliorare la conoscenza e il rispetto  reciproco. La consulta Ã¨ una figura â\x80\x9cponteâ\x80\x9d, che mette in contatto tutte le  realtÃ\xa0 civili con le diverse comunitÃ\xa0 straniere. $$$###%%%AttivitÃ\xa0 principali:###%%%$$$OrganizzaÂ\xa0 incontri di mediazione culturale nelle scuole  e corsi di aggiornamento;$$$Partecipa  come espositore in diverse fiere del volontariato;$$$Partecipa  ed organizza incontri pubblici relativi allâ\x80\x99immigrazione;$$$Ha tradotto  diversi materiali cartacei di enti scolastici o di altre istituzioni pubbliche;$$$Partecipa a  tutte le Feste e celebrazioni pubblicheÂ\xa0  ( festa della liberazione, festa della Repubblica ecc);$$$Partecipa  alle commissioni comunali.$$$###%%%    sede$$$Abbiategrasso$$$via Pavia, 44Â\xa0$$$ tel. $$$347 6094985$$$e-mail$$$consultastranieri@comune.abbiategrasso.mi.it$$$###%%%    referenti$$$       presidente$$$       Francisca AbregÃ¹ LÃ²pez (PerÃ¹)$$$vice-presidente$$$Hamid Mously (Marocco)\n'
>>> rows = line.split("$$$")
>>> for r in row:
	print(r)

	
Baranzate
Comune Baranzate
###%%%        tipologia di intervento
###%%%consulenza, formazione, informazione,  mediazione
###%%%  profilo
      ###%%%  Ã¨ attivo il progetto 
Spazio Immigrazione
, sportello di informazione, consulenza ed orientamento sulle normative ed i servizi riguardanti persone straniere; Ã¨ aperto ai cittadini stranieri, italiani, agli operatori dei servizi del territorio ed ai volontari.###%%%Offre servizi di mediazione linguistico culturale, servizi di consulenza legale e formazione e orientamento agli operatori dei servizi al territorio.
###%%%    sede
Â 
Â 
Spazio Immigrazione
Baranzate
Via Trieste     - c/o Biblioteca
tel.
02 39306776
e-mail 
spazioimmigrazione@comune.baranzate.mi.it
orario
martedÃ¬: 9.30 - 12.30 
###%%%      referente
Azienda âComuni Insiemeâ per ###%%%âSpazio Immigrazioneâ:
Lucia  Catenacci
tel.
02 38348408
e-mail 
spazioimmigrazione@comuni-insieme.mi.it
Â 
Â 
responsabile comunale 
Sabrina Agosteo, servizi sociali 
tel.
02 92851979
e-mail 
sabrina.agosteo@comune.baranzate.mi.it
###%%%      note
###%%%     Spazio Immigrazione Ã¨ un'attivitÃ  prevista dal piano Sociale di Zona, e viene gestita dall'Azienda Speciale Consortile "Comuni Insieme per lo Sviluppo Sociale" in collaborazione con le Cooperative Progetto Integrazione e Farsi prossimo.###%%%Aderiscono i Comuni di Baranzate, Bollate, Cesate, Garbagnate Milanese, Limbiate, Novate Milanese, Paderno Dugnano, Senago e Solaro.###%%%

>>> for r in rows:
	print(r)

	
Baranzate
Comune Baranzate
###%%%        tipologia di intervento
###%%%consulenza, formazione, informazione,  mediazione
###%%%  profilo
      ###%%%  Ã¨ attivo il progetto 
Spazio Immigrazione
, sportello di informazione, consulenza ed orientamento sulle normative ed i servizi riguardanti persone straniere; Ã¨ aperto ai cittadini stranieri, italiani, agli operatori dei servizi del territorio ed ai volontari.###%%%Offre servizi di mediazione linguistico culturale, servizi di consulenza legale e formazione e orientamento agli operatori dei servizi al territorio.
###%%%    sede
Â 
Â 
Spazio Immigrazione
Baranzate
Via Trieste     - c/o Biblioteca
tel.
02 39306776
e-mail 
spazioimmigrazione@comune.baranzate.mi.it
orario
martedÃ¬: 9.30 - 12.30 
###%%%      referente
Azienda âComuni Insiemeâ per ###%%%âSpazio Immigrazioneâ:
Lucia  Catenacci
tel.
02 38348408
e-mail 
spazioimmigrazione@comuni-insieme.mi.it
Â 
Â 
responsabile comunale 
Sabrina Agosteo, servizi sociali 
tel.
02 92851979
e-mail 
sabrina.agosteo@comune.baranzate.mi.it
###%%%      note
###%%%     Spazio Immigrazione Ã¨ un'attivitÃ  prevista dal piano Sociale di Zona, e viene gestita dall'Azienda Speciale Consortile "Comuni Insieme per lo Sviluppo Sociale" in collaborazione con le Cooperative Progetto Integrazione e Farsi prossimo.###%%%Aderiscono i Comuni di Baranzate, Bollate, Cesate, Garbagnate Milanese, Limbiate, Novate Milanese, Paderno Dugnano, Senago e Solaro.###%%%

>>> for r in rows:
	if '@' in r:
		print(r)

		
spazioimmigrazione@comune.baranzate.mi.it
spazioimmigrazione@comuni-insieme.mi.it
sabrina.agosteo@comune.baranzate.mi.it
>>> for line in lines:
	rows = line.split("$$$")
	emails = '$$$'
	for r in rows:
		if '@' in r:
			emails += "###" + r
	print(emails)

	
$$$###consultastranieri@comune.abbiategrasso.mi.it
$$$###sportello.stranieri@comune.abbiategrasso.mi.it
$$$###lucianasala@aliceposta.it
$$$###faduma7@msn.com
$$$
$$$
$$$
$$$###sportello.stranieri@virgilio.it
$$$
$$$###ctparcore@virgilio.it
$$$###sportello.migranti@comune.rho.mi.it
$$$
$$$###orientamondo@comune.corsico.mi.it###intrecci@farsiprossimo.it
$$$###spazioimmigrazione@comune.baranzate.mi.it###spazioimmigrazione@comuni-insieme.mi.it###sabrina.agosteo@comune.baranzate.mi.it
$$$
$$$
$$$
$$$
$$$
$$$
$$$###stars@comune.bernareggio.mi.it
$$$###servizisociali@comune.bernateticino.mi.it
$$$###sportello.immigrati@tiscalinet.it

$$$
$$$
$$$###servizisociali@comunebinasco.it###progettocon-tatto@libero.it
$$$
$$$###spazioimmigrazione@comune.bollate.mi.it###servizi.sociali@comune.bollate.mi.it###spazioimmigrazione@comuni-insieme.mi.it
$$$
$$$
$$$
$$$###m.casiraghi@comune.brugherio.mi.it

$$$
$$$###orientamondo@comune.corsico.mi.it###intrecci@farsiprossimo.it###ilsogno@aclimilano.com
$$$
$$$###sportello.stranieri@virgilio.it
$$$
$$$
$$$###sportello.stranieri@comune.bustogarolfo.mi.it###ass.sociale@comune.bustogarolfo.mi.it###ombretta@comune.bustogarolfo.mi.it###sportellostranieri@comune.bustogarolfo.mi.it

$$$
$$$
$$$
$$$###sociali@comune.canegrate.mi.it
$$$
$$$###carateservizisociali@tiscali.it###sportello.immigrati@tiscalinet.it

$$$###stars@comune.carnate.mi.it
$$$
$$$
$$$
$$$
$$$
$$$
$$$###amjadiqbal@libero.it

$$$
$$$
$$$###sportello.stranieri@virgilio.it
$$$###stars@comune.cavenagobrianza.mi.it
$$$###dagjoka@tiscali.it
$$$
$$$
$$$###orientamondo@comune.corsico.mi.it###intrecci@farsiprossimo.it###ilsogno@aclimilano.com
$$$###wilhid@hotmail.com
$$$###floriana.pulcini@comune.cesano-maderno.mi.it###ornella.oltolini@comune.cesano-maderno.mi.it
$$$###spazioimmigrazione@comuni-insieme.mi.it
$$$###africplus@yahoo.it
$$$###el.taha24@libero.it
$$$###mappa_mondo_cinisellob@yahoo.it###teresa.torres@comune.cinisello-balsamo.mi.it###mariagrazia.landoni@comune.cinisello-balsamo.mi.it
$$$###assoleluna@gmail.com

$$$
$$$
$$$###info@tibetculturehouseitaly.org
$$$
$$$
$$$
$$$
$$$###sportello.migranti@comune.rho.mi.it
$$$
$$$
$$$###itacacorsico@yahoo.it
$$$###orientamondo@comune.corsico.mi.it###intrecci@farsiprossimo.it###ilsogno@aclimilano.com
$$$
$$$###orientamondo@comune.corsico.mi.it###intrecci@farsiprossimo.it###ilsogno@aclimilano.com
$$$###o.riva@comune.cusano-milanino.mi.it

$$$
$$$###servizisociali@comune.desio.mi.it
$$$
$$$###sportellostranieri@comune.gaggiano.mi.it
$$$###aknasr@hotmail.it
$$$###educazione@comune.garbagnate-milanese.mi.it###sociali@comune.garbagnate-milanese.mi.it###spazioimmigrazione@comune.garbagnate-milanese.mi.it###spazioimmigrazione@comuni-insieme.mi.it
$$$
$$$
$$$
$$$
$$$
$$$###sportello.stranieri@virgilio.it
$$$
$$$###posta@comune.lacchiarella.mi.it
$$$###sportello.migranti@comune.rho.mi.it
$$$
$$$
$$$
$$$
$$$###spazioimmigrazione@comune.limbiate.mi.it###spazioimmigrazione@comuni-insieme.mi.it
$$$
$$$###Elio.Bassani@comune.lissone.mi.it###sportello.immigrati@tiscalinet.it

$$$
$$$
$$$
$$$
$$$###assistenti.sociali@comune.bareggio.mi.it
$$$
$$$
$$$###sportello.immigra@katamail.com
$$$###zkps.milano@tiscali.it
$$$
$$$
$$$
$$$
$$$###info@afriaca.it
$$$
$$$###vicman@apomilano.it
$$$###alkeosbox-1@yhaoo.it###alkeos_onlus@yahoo.it
$$$###rzpzleo@hotmail.com
$$$###info@arabafenicenet.it
$$$###aslat@libero.it
$$$###info@asmp.it
$$$###info@aspeonlus.org
$$$###moodafrica@yahoo.com
$$$
$$$###brigg_brijuega@yahoo.com
$$$###loyola_nonoy@hotmail.com
$$$###eresinternational@eres.it######%%%    eres@eres.it
$$$###correo@casahispanoamericana.com
$$$
$$$
$$$###paololimonta@fastwebnet.it
$$$###cile.lombardia@libero.it
$$$
$$$###v.silva@fastwebnet.it
$$$###tomascartagena@yahoo.it
$$$
$$$
$$$
$$$###a.mbaraga@aliceposta.it
$$$###crecer_it@yahoo.it
$$$###toribiorodolfo@hotmail.com
$$$
$$$###josesanti@libero.it
$$$
$$$
$$$###v.silva@fastwebnet.it
$$$###cia29@libero.it
$$$###infoaml@virgilio.it
$$$
$$$###milon@bamli.it
$$$
$$$###info@ibrit.it###biblioteca@ibrit.it###corsi@ibrit.it###eventi@ibrit.it
$$$###assoeritrea@libero.it
$$$###eresinternational@eres.it######%%%    eres@eres.it
$$$###italiacina@tiscali.it
$$$###italiapertutti@yahoo.it
$$$###info.associazione@italiarussia.it
$$$###info@associazione-italoegiziana.it
$$$###armapace@alice.it
$$$
$$$###khouiderahmed@yahoo.fr
$$$###infoaml@virgilio.it
$$$###info@mitadelmundo.com###galvez_jose@hotmail.com###miryambo_9@libero.com###mariana.garcia@tiscali.it
$$$###newcomfoundation@tiscali.it
$$$###aslat@libero.it
$$$###bogdan@nuovamultietnica.org
$$$
$$$
$$$###aspel@email.it
$$$###jacobomonte@hotmail.it
$$$
$$$
$$$
$$$###allodi_o@hotmail.com
$$$###olga_noriega@hotmail.com###asso.republicadelecuador@hotmail.it
$$$###giorgio.casadio@associazionesodalis.it
$$$
$$$
$$$###modougueye@libero.it
$$$###web@todaslassangres.net
$$$###todo.cambia@libero.it###info@todocambia.org
$$$
$$$
$$$###pilar.herrera@unidosporcolombia.org
$$$###adulti.stranieri2@comune.milano.it###adulti.stranieri@comune.milano.it
$$$###amelinc_2004@yahoo.it###luiszan@tin.it
$$$###info@coopcrinali.it
$$$###info@donneincammino.org

$$$###kantara@tiscalinet.it
$$$###info@proficua.com
$$$
$$$###info@studio3r.net
$$$
$$$
$$$
$$$###ass.sociale@comune.mottavisconti.mi.it
$$$###servizi.persone@muggio.org

$$$###spaziocomune@comune.nerviano.mi.it
$$$
$$$
$$$###atilombardia@libero.it
$$$###spazioimmigrazione@comune.novate-milanese.it###spazioimmigrazione@comuni-insieme.mi.it
$$$
$$$###ecuadorsolidario@gmail.com
$$$
$$$
$$$
$$$
$$$
$$$
$$$###sportello.immigra@katamail.com
$$$
$$$###sportello.immigra@katamail.com
$$$###sportello.migranti@comune.rho.mi.it
$$$###sportello.immigra@katamail.com
$$$
$$$
$$$
$$$
$$$
$$$###perladelpacifico2@hotmail.com
$$$###stranieri@comune.pioltello.mi.it###consultaintercultura@tiscali.it
$$$###sportello.migranti@comune.rho.mi.it
$$$
$$$
$$$###sportello.migranti@comune.rho.mi.it
$$$
$$$
$$$###griotkoffimiche@libero.it###compafricana@iol.it
$$$###sportello.migranti@comune.rho.mi.it
$$$###sportello.stranieri@virgilio.it
$$$
$$$
$$$
$$$
$$$
$$$###assoased@yahoo.fr
$$$###shoqata.shqiponja@tiscali.it
$$$
$$$###punto.immigrazione@comune.rozzano.mi.it
$$$
$$$###isagani_casunuran@fastwebnet.it

$$$
$$$###ufficio.stranieri@comune.sandonatomilanese.mi.it
$$$
$$$
$$$###vatraromaneasca2004@yahoo.it
$$$###ufficio.stranieri@sangiulianonline.it
$$$
$$$
$$$
$$$
$$$###omnibus@comune.segrate.mi.it
$$$###spazioimmigrazione@comune.senago.mi.it###spazioimmigrazione@comuni-insieme.mi.it
$$$
$$$###cosafrica@hotmail.com
$$$###areamigranti@cooplotta.org
$$$
$$$###sportello.migranti@comune.rho.mi.it
$$$
$$$###spazioimmigrazione@comune.solaro.mi.it###spazioimmigrazione@comuni-insieme.mi.it###servizisociali@comune.solaro.mi.it
$$$
$$$
$$$
$$$###orientamondo@comune.corsico.mi.it###intrecci@farsiprossimo.it###ilsogno@aclimilano.com
$$$
$$$###sportello.immigra@katamail.com
$$$
$$$
$$$###sportello.stranieri@virgilio.it
$$$
$$$###sportello.stranieri@virgilio.it
$$$###sportello.migranti@comune.rho.mi.it
$$$
$$$###m.libera@comune.varedo.mi.it###servizisociali@comune.varedo.mi.it

$$$
$$$###olfabach@tiscali.it###linoretajak@tiscali.it
$$$
$$$###intercultura@scuoleverano.it
$$$
$$$
$$$
$$$
$$$###sportello.immigrati@tiscalinet.it

$$$
$$$###sportellolegale@kayros.it
$$$
$$$
$$$
$$$
$$$
$$$###gabriella.maggi@comune.zibidosangiacomo.mi.it

$$$###scopro@provincia.milano.it
>>> 
