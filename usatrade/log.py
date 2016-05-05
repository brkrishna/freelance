Python 3.5.1 |Anaconda 2.4.1 (64-bit)| (default, Dec  7 2015, 11:16:01) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver
>>> 
>>> d = webdriver.Firefox()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    d = webdriver.Firefox()
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/firefox/webdriver.py", line 77, in __init__
    self.binary, timeout),
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/firefox/extension_connection.py", line 49, in __init__
    self.binary.launch_browser(self.profile)
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/firefox/firefox_binary.py", line 68, in launch_browser
    self._wait_until_connectable()
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/firefox/firefox_binary.py", line 103, in _wait_until_connectable
    raise WebDriverException("Can't load the profile. Profile "
selenium.common.exceptions.WebDriverException: Message: Can't load the profile. Profile Dir: %s If you specified a log_file in the FirefoxBinary constructor, check it for details.

>>> 
=============================== RESTART: Shell ===============================
>>> from selenium import webdriver
>>> d = webdriver.Firefox()
>>> url ='https://usatrade.census.gov/'
>>> d.get(url)
>>> d.find_element_by_partial_link_text('LOG IN').click()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    d.find_element_by_partial_link_text('LOG IN').click()
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 338, in find_element_by_partial_link_text
    return self.find_element(by=By.PARTIAL_LINK_TEXT, value=link_text)
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 744, in find_element
    {'using': by, 'value': value})['value']
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 233, in execute
    self.error_handler.check_response(response)
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"partial link text","selector":"LOG IN"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///tmp/tmpytgxaqxt/extensions/fxdriver@googlecode.com/components/driver-component.js:10770)
    at FirefoxDriver.prototype.findElement (file:///tmp/tmpytgxaqxt/extensions/fxdriver@googlecode.com/components/driver-component.js:10779)
    at DelayedCommand.prototype.executeInternal_/h (file:///tmp/tmpytgxaqxt/extensions/fxdriver@googlecode.com/components/command-processor.js:12661)
    at DelayedCommand.prototype.executeInternal_ (file:///tmp/tmpytgxaqxt/extensions/fxdriver@googlecode.com/components/command-processor.js:12666)
    at DelayedCommand.prototype.execute/< (file:///tmp/tmpytgxaqxt/extensions/fxdriver@googlecode.com/components/command-processor.js:12608)
>>> d.find_element_by_class_name('uto_button').click()
>>> from selenium.webdriver.common.keys import Keys
>>> d.find_element_by_id('struserid').send_keys('8GCG9XW')
>>> d.find_element_by_id('pwdfld').send_keys('Sanajana@1234')
>>> d.find_element_by_id('buttonid').click()
>>> d.find_element_by_id('pwdfld').clear()
>>> d.find_element_by_id('pwdfld').send_keys('Sanjana@1234')
>>> d.find_element_by_id('buttonid').click()
>>> d.find_element_by_css_selector('#Table2 > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > a:nth-child(1)').click()
>>> d.find_element_by_partial_link_text('Measures').click()
>>> boxes = d.find_elements_by_class_name('rtChk')
>>> len(boxes)
5
>>> for box in boxes:
	if box.is_selected():
		continue
	else:
		box.click()

		
>>> 
d.find_element_by_partial_link_text('Commodity').click()
>>> d.find_element_by_css_selector('#ctl00_MainContent_RadMembersTree > ul:nth-child(1) > li:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > div:nth-child(1) > label:nth-child(3) > input:nth-child(1)').click()
>>> d.find_element_by_partial_link_text('Country').click()
>>> d.find_element_by_css_selector('.rtHover > label:nth-child(3) > input:nth-child(1)').click()
>>> d.find_element_by_css_selector('#ctl00_MainContent_RadMembersTree > ul:nth-child(1) > li:nth-child(1) > div:nth-child(1) > span:nth-child(2)').click()
>>> d.find_element_by_id('Level1ClearImage').click()
>>> d.find_element_by_partial_link_text('Afghanistan').click()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    d.find_element_by_partial_link_text('Afghanistan').click()
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 338, in find_element_by_partial_link_text
    return self.find_element(by=By.PARTIAL_LINK_TEXT, value=link_text)
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 744, in find_element
    {'using': by, 'value': value})['value']
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 233, in execute
    self.error_handler.check_response(response)
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"partial link text","selector":"Afghanistan"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///tmp/tmpytgxaqxt/extensions/fxdriver@googlecode.com/components/driver-component.js:10770)
    at FirefoxDriver.prototype.findElement (file:///tmp/tmpytgxaqxt/extensions/fxdriver@googlecode.com/components/driver-component.js:10779)
    at DelayedCommand.prototype.executeInternal_/h (file:///tmp/tmpytgxaqxt/extensions/fxdriver@googlecode.com/components/command-processor.js:12661)
    at DelayedCommand.prototype.executeInternal_ (file:///tmp/tmpytgxaqxt/extensions/fxdriver@googlecode.com/components/command-processor.js:12666)
    at DelayedCommand.prototype.execute/< (file:///tmp/tmpytgxaqxt/extensions/fxdriver@googlecode.com/components/command-processor.js:12608)
>>> chks = d.find_elements_by_class('rtChk')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    chks = d.find_elements_by_class('rtChk')
AttributeError: 'WebDriver' object has no attribute 'find_elements_by_class'
>>> chks = d.find_elements_by_class_name('rtChk')
>>> len(chks)
200
>>> d.find_element_by_link_text('Afghanistan').click()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    d.find_element_by_link_text('Afghanistan').click()
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 314, in find_element_by_link_text
    return self.find_element(by=By.LINK_TEXT, value=link_text)
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 744, in find_element
    {'using': by, 'value': value})['value']
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 233, in execute
    self.error_handler.check_response(response)
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 194, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"link text","selector":"Afghanistan"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///tmp/tmpytgxaqxt/extensions/fxdriver@googlecode.com/components/driver-component.js:10770)
    at FirefoxDriver.prototype.findElement (file:///tmp/tmpytgxaqxt/extensions/fxdriver@googlecode.com/components/driver-component.js:10779)
    at DelayedCommand.prototype.executeInternal_/h (file:///tmp/tmpytgxaqxt/extensions/fxdriver@googlecode.com/components/command-processor.js:12661)
    at DelayedCommand.prototype.executeInternal_ (file:///tmp/tmpytgxaqxt/extensions/fxdriver@googlecode.com/components/command-processor.js:12666)
    at DelayedCommand.prototype.execute/< (file:///tmp/tmpytgxaqxt/extensions/fxdriver@googlecode.com/components/command-processor.js:12608)
>>> chks = d.find_elements_by_class_name('rtLI')
>>> len(chks)
216
>>> chks[0].find_element_by_class_name('rtIn').text
'Measures'
>>> chks[7].find_element_by_class_name('rtIn').text
'Afghanistan'
>>> chks[7].find_element_by_class_name('rtIn').click()
>>> chks[7].find_element_by_class_name('rtIn').parent.click()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    chks[7].find_element_by_class_name('rtIn').parent.click()
AttributeError: 'WebDriver' object has no attribute 'click'
>>> chks[7].click()
>>> chks[7].click()
>>> chks[7].click()
>>> chks[7].get_attribute('checked')
>>> chks[7].get_attribute('checked')
>>> chks[7].click()
>>> chks[6].click()
>>> chks[8].click()
>>> chks[8].find_element_by_class_name('rtIn').text
'Albania'
>>> chks[7].click()
>>> chks[7].is_selected()
False
>>> chks[7].send_keys("SPACE")
>>> chks[7].send_keys("SPACE")
>>> chks[7].text
'Afghanistan'
>>> chks[7].find_element_by_tag_name('input').click()
>>> d.find_element_by_link_text('Report').click()
>>> from bs4 import BeautifulSoup, SoupStrainer
>>> from lxml import html
>>> tree = html.fromstring(d.page_source)
>>> tree.xpath("//th[@id='C00']//text()")
['2016 through February']
>>> tree.xpath("//th[@id='C01']//text()")
['Value ($US)']
>>> tree.xpath("//th[@id='C11']//text()")
['Quantity 1']
>>> tree.xpath("//th[@id='C12']//text()")
['01 Live Animals']
>>> 
