Python 3.5.0 |Anaconda 2.4.0 (64-bit)| (default, Oct 20 2015, 07:26:33) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver
>>> start_url = 'http://shop.mywebgrocer.com'
>>> d = webdriver.Firefox()
>>> d.get(start_url)
>>> from bs4 import BeautifulSoup, SoupStrainer
>>> start_url = 'http://shop.mywebgrocer.com/shop.aspx?strid=5F3D126398'
>>> d.get(start_url)
>>> d.find_element_by_css_selector('#ShoppingMenuBorder')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    d.find_element_by_css_selector('#ShoppingMenuBorder')
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 402, in find_element_by_css_selector
    return self.find_element(by=By.CSS_SELECTOR, value=css_selector)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"css selector","selector":"#ShoppingMenuBorder"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10659)
    at FirefoxDriver.prototype.findElement (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10668)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> d.switch_to.frame('MenuFrame')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    d.switch_to.frame('MenuFrame')
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\switch_to.py", line 67, in frame
    self._driver.execute(Command.SWITCH_TO_FRAME, {'id': frame_reference})
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchFrameException: Message: Unable to locate frame: MenuFrame
Stacktrace:
    at FirefoxDriver.prototype.switchToFrame (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10729)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> d.switch_to.frame(d.find_element_by_name('MenuFrame'))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    d.switch_to.frame(d.find_element_by_name('MenuFrame'))
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 330, in find_element_by_name
    return self.find_element(by=By.NAME, value=name)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"name","selector":"MenuFrame"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10659)
    at FirefoxDriver.prototype.findElement (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10668)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> d.find_element_by_name('MenuFrame')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d.find_element_by_name('MenuFrame')
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 330, in find_element_by_name
    return self.find_element(by=By.NAME, value=name)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"name","selector":"MenuFrame"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10659)
    at FirefoxDriver.prototype.findElement (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10668)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> d.find_elements_by_name('MenuFrame')
[]
>>> d.find_elements_by_name('TopFrame')
[<selenium.webdriver.remote.webelement.WebElement (session="0dbbcb3d-5fae-4ab8-88d4-163aca01301d", element="{a4fed2ea-5d34-49e0-a5a6-348d7f8fd2b3}")>]
>>> topframe = d.find_elements_by_name('TopFrame')
>>> d.switch_to.frame(topframe)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d.switch_to.frame(topframe)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\switch_to.py", line 67, in frame
    self._driver.execute(Command.SWITCH_TO_FRAME, {'id': frame_reference})
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchFrameException: Message: Unable to locate frame: [object Object]
Stacktrace:
    at FirefoxDriver.prototype.switchToFrame (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10729)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> d.switch_to.frame(d.find_element_by_name('TopFrame'))
>>> d.switch_to.frame(d.find_element_by_name('MidFrame'))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d.switch_to.frame(d.find_element_by_name('MidFrame'))
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 330, in find_element_by_name
    return self.find_element(by=By.NAME, value=name)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"name","selector":"MidFrame"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10659)
    at FirefoxDriver.prototype.findElement (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10668)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> d2 = d.switch_to.frame(d.find_element_by_name('TopFrame'))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d2 = d.switch_to.frame(d.find_element_by_name('TopFrame'))
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 330, in find_element_by_name
    return self.find_element(by=By.NAME, value=name)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"name","selector":"TopFrame"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10659)
    at FirefoxDriver.prototype.findElement (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10668)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> d.get(start_url)
>>> d2 = d.switch_to.frame(d.find_element_by_name('TopFrame'))
>>> d3 = d2.switch_to.frame(d.find_element_by_name('MidFrame'))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d3 = d2.switch_to.frame(d.find_element_by_name('MidFrame'))
AttributeError: 'NoneType' object has no attribute 'switch_to'
>>> d2
>>> d.switch_to.frame(d.find_element_by_name('TopFrame'))
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    d.switch_to.frame(d.find_element_by_name('TopFrame'))
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 330, in find_element_by_name
    return self.find_element(by=By.NAME, value=name)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"name","selector":"TopFrame"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10659)
    at FirefoxDriver.prototype.findElement (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10668)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> d.switch_to.frame(d.find_element_by_name('MidFrame'))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    d.switch_to.frame(d.find_element_by_name('MidFrame'))
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 330, in find_element_by_name
    return self.find_element(by=By.NAME, value=name)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"name","selector":"MidFrame"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10659)
    at FirefoxDriver.prototype.findElement (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10668)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> d.switch_to.window
<bound method SwitchTo.window of <selenium.webdriver.remote.switch_to.SwitchTo object at 0x0000000004010160>>
>>> d.switch_to.frame(d.find_element_by_name('TopFrame'))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d.switch_to.frame(d.find_element_by_name('TopFrame'))
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 330, in find_element_by_name
    return self.find_element(by=By.NAME, value=name)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"name","selector":"TopFrame"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10659)
    at FirefoxDriver.prototype.findElement (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10668)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> d.switch_to.parent_frame
<bound method SwitchTo.parent_frame of <selenium.webdriver.remote.switch_to.SwitchTo object at 0x0000000004010160>>
>>> d.switch_to.frame(d.find_element_by_name('TopFrame'))
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    d.switch_to.frame(d.find_element_by_name('TopFrame'))
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 330, in find_element_by_name
    return self.find_element(by=By.NAME, value=name)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"name","selector":"TopFrame"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10659)
    at FirefoxDriver.prototype.findElement (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10668)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> d.title
'Market District Green Village'
>>> d.switch_to.frame(d.find_element_by_name('TopFrame'))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    d.switch_to.frame(d.find_element_by_name('TopFrame'))
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 330, in find_element_by_name
    return self.find_element(by=By.NAME, value=name)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"name","selector":"TopFrame"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10659)
    at FirefoxDriver.prototype.findElement (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10668)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> d.current_window_handle
'{6b90813c-287b-4c8c-afc8-e0d4397d0093}'
>>> d.current_window_handle.title
<built-in method title of str object at 0x000000000416BD98>
>>> d.current_window_handle.title()
'{6B90813C-287B-4C8C-Afc8-E0D4397D0093}'
>>> d.switch_to_default_content()
>>> d.switch_to.frame(d.find_element_by_name('TopFrame'))
>>> d.switch_to.frame(d.find_element_by_name('MidFrame'))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    d.switch_to.frame(d.find_element_by_name('MidFrame'))
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 330, in find_element_by_name
    return self.find_element(by=By.NAME, value=name)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"name","selector":"MidFrame"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10659)
    at FirefoxDriver.prototype.findElement (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10668)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> d.switch_to_default_content()
>>> d.switch_to.frame(d.find_element_by_name('MasterFrame'))
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    d.switch_to.frame(d.find_element_by_name('MasterFrame'))
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\switch_to.py", line 67, in frame
    self._driver.execute(Command.SWITCH_TO_FRAME, {'id': frame_reference})
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchFrameException: Message: Element is not a frame element: FRAMESET
Stacktrace:
    at FirefoxDriver.prototype.switchToFrame (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10719)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> url = 'http://shop.mywebgrocer.com/ShoppingMenu.aspx?&strid=5F3D126398'
>>> import requests
>>> r = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0'})
>>> r.status_code
200
>>> d.switch_to_default_content()
>>> d.switch_to.frame(d.find_element_by_css_selector('html > frameset:nth-child(2) > frame:nth-child(1)'))
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    d.switch_to.frame(d.find_element_by_css_selector('html > frameset:nth-child(2) > frame:nth-child(1)'))
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 402, in find_element_by_css_selector
    return self.find_element(by=By.CSS_SELECTOR, value=css_selector)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"css selector","selector":"html > frameset:nth-child(2) > frame:nth-child(1)"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10659)
    at FirefoxDriver.prototype.findElement (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10668)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> d.find_element_by_css_selector('html > frameset:nth-child(2) > frame:nth-child(1)')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    d.find_element_by_css_selector('html > frameset:nth-child(2) > frame:nth-child(1)')
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 402, in find_element_by_css_selector
    return self.find_element(by=By.CSS_SELECTOR, value=css_selector)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"css selector","selector":"html > frameset:nth-child(2) > frame:nth-child(1)"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10659)
    at FirefoxDriver.prototype.findElement (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10668)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> d.switch_to_default_content()
>>> d.title
'Market District Green Village'
>>> d.switch_to.frame(d.find_element_by_name('MenuFrame'))
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    d.switch_to.frame(d.find_element_by_name('MenuFrame'))
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 330, in find_element_by_name
    return self.find_element(by=By.NAME, value=name)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"name","selector":"MenuFrame"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10659)
    at FirefoxDriver.prototype.findElement (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10668)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> d.switch_to.frame(d.find_element_by_name('TopFrame'))
>>> d.title
'Market District Green Village'
>>> d.switch_to.frame(d.find_element_by_name('MidFrame'))
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    d.switch_to.frame(d.find_element_by_name('MidFrame'))
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 330, in find_element_by_name
    return self.find_element(by=By.NAME, value=name)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 712, in find_element
    {'using': by, 'value': value})['value']
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "C:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"name","selector":"MidFrame"}
Stacktrace:
    at FirefoxDriver.prototype.findElementInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10659)
    at FirefoxDriver.prototype.findElement (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/driver-component.js:10668)
    at DelayedCommand.prototype.executeInternal_/h (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12534)
    at DelayedCommand.prototype.executeInternal_ (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12539)
    at DelayedCommand.prototype.execute/< (file:///C:/Users/sbit25/AppData/Local/Temp/tmprbra3x8e/extensions/fxdriver@googlecode.com/components/command-processor.js:12481)
>>> d.switch_to_default_content()
>>> d.switch_to.frame(d.find_element_by_name('MidFrame'))
>>> d.switch_to.frame(d.find_element_by_name('MenuFrame'))
>>> soup= BeautifulSoup(d.page_source, parse_only=SoupStrainer('div',{'id':'ShoppingMenuBorder'}))

Warning (from warnings module):
  File "C:\Anaconda3\lib\site-packages\bs4\__init__.py", line 166
    markup_type=markup_type))
UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

To get rid of this warning, change this:

 BeautifulSoup([your markup])

to this:

 BeautifulSoup([your markup], "lxml")

>>> soup= BeautifulSoup(d.page_source, "html.parser", parse_only=SoupStrainer('div',{'id':'ShoppingMenuBorder'}))
>>> d.find_element_by_partial_link_text('Grocery')
<selenium.webdriver.remote.webelement.WebElement (session="0dbbcb3d-5fae-4ab8-88d4-163aca01301d", element="{dd5e3b5a-472e-4989-a826-86f9fcee2c9c}")>
>>> d.find_element_by_partial_link_text('Grocery').click()
>>> ul = d.find_element_by_id('ShoppingMenuClient00_ShoppingMenu')
>>> lis = ul.findAll('li')
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    lis = ul.findAll('li')
AttributeError: 'WebElement' object has no attribute 'findAll'
>>> lis = ul.find_element_by_tag_name('li')
>>> len(lis)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    len(lis)
TypeError: object of type 'WebElement' has no len()
>>> lis
<selenium.webdriver.remote.webelement.WebElement (session="0dbbcb3d-5fae-4ab8-88d4-163aca01301d", element="{17c36b96-9b60-43dd-b3aa-9d9ee60092c9}")>
>>> for li in lis:
	print(li.text)

	
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    for li in lis:
TypeError: 'WebElement' object is not iterable
>>> lis = ul.find_elements_by_tag_name('li')
>>> len(lis)
1014
>>> lis[0]
<selenium.webdriver.remote.webelement.WebElement (session="0dbbcb3d-5fae-4ab8-88d4-163aca01301d", element="{17c36b96-9b60-43dd-b3aa-9d9ee60092c9}")>
>>> lis[0].text
'Grocery\nBaby Store\nBakery\nBeverages\nBreakfast\nBulk Foods\nCanned & Packaged\nCleaning Products\nCondiment & Sauces\nDairy\nDeli\nFrozen\nIngredients\nInternational\nLiquor Store\nMeat & Seafood\nPaper & Plastics\nPasta, Sauces, Grain\nPet Shop\nProduce\nSnacks\nTobacco'
>>> for li in lis:
	print(li.text)

	
Grocery
Baby Store
Bakery
Beverages
Breakfast
Bulk Foods
Canned & Packaged
Cleaning Products
Condiment & Sauces
Dairy
Deli
Frozen
Ingredients
International
Liquor Store
Meat & Seafood
Paper & Plastics
Pasta, Sauces, Grain
Pet Shop
Produce
Snacks
Tobacco
Baby Store

















Bakery

















































Beverages






























































































Breakfast






















Bulk Foods







Canned & Packaged





































































Cleaning Products
















Condiment & Sauces













































Dairy





































Deli

































Frozen









































































Ingredients





















































International


















Liquor Store


































Meat & Seafood








































Paper & Plastics









Pasta, Sauces, Grain






























Pet Shop













Produce




































Snacks

































Tobacco


Health & Beauty



































































































































































General






















































Fresh Bakery












Organic















Specials













>>> 
