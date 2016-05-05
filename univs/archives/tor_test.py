from selenium import webdriver

if __name__ == "__main__":
    profile=webdriver.FirefoxProfile()
    profile.set_preference('network.proxy.type', 1)
    profile.set_preference('network.proxy.socks', '127.0.0.1')
    profile.set_preference('network.proxy.socks_port', 9150)
    browser=webdriver.Firefox(profile)
    browser.get("http://www.albonazionalegestoriambientali.it/ElenchiIscritti.aspx#tipoRicerca=9&idImpresa=23980")
    #browser.close()
