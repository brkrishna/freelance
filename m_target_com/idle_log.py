Python 3.5.1 |Anaconda 2.4.1 (64-bit)| (default, Dec  7 2015, 11:16:01) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver
>>> from selenium.webdriver.common.keys import Keys
>>> from bs4 import BeautifulSoup, SoupStrainer
>>> BASE_URL = 'http://m.target.com/c/grocery-essentials/-/N-5xt1a'
>>> import requests
>>> headers = {'User-Agent': 'Mozilla/5.0'}
>>> s = requests.session()
>>> r = s.get(BASE_URL, headers=headers)
>>> r.status_code
200
>>> tree = html.fromstring(r.content)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    tree = html.fromstring(r.content)
NameError: name 'html' is not defined
>>> from lxml import html
>>> tree = html.fromstring(r.content)
>>> tree.xpath("//li[@class='product']")
[]
>>> r.content
b'<!DOCTYPE html>\n<html lang="en" class="no-js">\n  <head>\n\t\t<meta charset="utf-8" />\n<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n<meta name="viewport" content="width=device-width, maximum-scale=1, minimum-scale=1, user-scalable=no" />\n<link id="favicon" rel="shortcut icon" type="image/png" href="//static.targetimg1.com/mobile-config/favicon.ico" />\n<link rel="apple-touch-icon-precomposed" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/apple-touch-icon-precomposed.png" />\n<link rel="icon" type="image/png" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/apple-touch-icon-precomposed.png" sizes="192x192">\n<link rel="icon" type="image/png" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/favicon-96x96.png" sizes="96x96">\t\n<link rel="icon" type="image/png" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/favicon-32x32.png" sizes="32x32">\n<link rel="icon" type="image/png" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/favicon-16x16.png" sizes="16x16">\n<meta name="msapplication-TileColor" content="#cc0000">\n<meta name="msapplication-TileImage" content="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/android-chrome-192x192.png">\n<meta name="format-detection" content="telephone=no" />\n<script>document.createElement("picture");</script>\n<script>\n\t(function(){if(window.BOOMR&&window.BOOMR.version){return}var dom,doc,where,iframe=document.createElement(\'iframe\');iframe.src="javascript:false";iframe.title="";iframe.role="presentation";(iframe.frameElement||iframe).style.cssText="width:0;height:0;border:0;display:none;";where=document.getElementsByTagName(\'script\')[0];where.parentNode.insertBefore(iframe,where);try{doc=iframe.contentWindow.document}catch(e){dom=document.domain;iframe.src="javascript:var d=document.open();d.domain=\'"+dom+"\';void(0);";doc=iframe.contentWindow.document}doc.open()._l=function(){var js=this.createElement("script");if(dom)this.domain=dom;js.id="boomr-if-as";js.src=\'//c.go-mpulse.net/boomerang/KQTS5-4NBTD-EYGLE-64UYR-S5892\';BOOMR_lstart=new Date().getTime();this.body.appendChild(js)};doc.write(\'<body onload="document._l();">\');doc.close()})();\n\t!function(a){if(a.XMLHttpRequest&&(new XMLHttpRequest).addEventListener){var b,c=document.createElement("A"),d=XMLHttpRequest,e=[],f=["uninitialized","open","responseStart","domInteractive","responseEnd"];a.BOOMR=a.BOOMR||{},BOOMR.xhr={stop:function(c){return b=c,a.XMLHttpRequest=d,delete BOOMR.xhr,setTimeout(function(){e=[]}),e}};var g=function(){try{if("performance"in a)return function(){return Math.round(performance.now()+performance.timing.navigationStart)}}catch(b){}return Date.now||function(){return(new Date).getTime()}}();a.XMLHttpRequest=function(){var h=new d,i=h.open;return h.open=function(d,j,k){function l(){if(!n.timing.loadEventEnd){if(n.timing.loadEventEnd=g(),"performance"in a&&a.performance&&"function"==typeof a.performance.getEntriesByName){var c=a.performance.getEntriesByName(n.url),d=c&&c.length&&c[c.length-1];if(d){var f=a.performance.timing.navigationStart;0!==d.responseEnd&&(n.timing.responseEnd=Math.round(f+d.responseEnd)),0!==d.responseStart&&(n.timing.responseStart=Math.round(f+d.responseStart)),0!==d.startTime&&(n.timing.requestStart=Math.round(f+d.startTime))}}b?b(n):e.push(n)}}function m(a,b){h.addEventListener(a,function(){"readystatechange"===a?(n.timing[f[h.readyState]]=g(),4===h.readyState&&l()):(n.status=void 0===b?h.status:b,l())},!1)}c.href=j;var n={timing:{},url:c.href,method:d};k===!0?m("readystatechange"):n.synchronous=!0,m("load"),m("timeout",-1001),m("error",-998),m("abort",-999);try{i.apply(h,arguments);var o=h.send;h.send=function(){n.timing.requestStart=g(),o.apply(h,arguments)}}catch(p){n.status=-997,l()}},h}}}(window);\n</script>\n<script type="text/javascript">\n\n  var configJSON = {\n\tpreUrlMobileConstructor\t\t: "http://m.target.com/",\n\tsecurePreUrlMobileConstructor\t: "https://m-secure.target.com/",\n\tpreUrlTabletConstructor\t\t: "http://www.target.com/",\n\tsecurePreUrlTabletConstructor\t: "https://www-secure.target.com/",\n\tapiServer\t\t\t\t: {\n\t\tdomain : "http://api.target.com",\n\t\tsecuredomain : "https://secure-api.target.com",\n\t\taccesskey :"eb2551e4accc14f38cc42d32fbc2b2ea",\n\t\tsecureaccesskey : "SxR9X7XoWw2fW1PBWfXswf3q5NeIuGAu"\n\t},\n\tsearchURL\t\t\t\t: "http://tws.target.com/searchservice/item/search_results/v2/by_keyword?",\n    searchURLV2             : "http://tws.target.com/searchservice/item/search_results/v2/by_keyword?",\n    brandURL                : "http://tws.target.com/searchservice/item/brand_results/v2/by_brand?",\n    itemPriceURL            : "http://dcd-prc.target.com/item/price/v1/{tcins}?key=8cb043b2dace9afc0680e6bae5cd316f",\n\tbrowseURL\t\t\t\t: "http://tws.target.com/productservice/services/item_service/v1/by_itemid?",\n\tbrowseSecureURL\t\t\t: "https://tws-secure.target.com/productservice/services/item_service/v1/by_itemid?",\n\tbazaarVoiceURL\t\t\t: "display.ugc.bazaarvoice.com/static/targetcom/uimod/en_US/bvapi.js",\n\tdvmChannelId\t\t\t: "mtarget",\n\tpersonalizationEngineURL: "https://prz-secure.target.com/recommendations/v1",\n\tthreatMerticsURL\t\t: "https://img9.target.com",\n    redcardPromoEnabled\t\t: true,\n    useServiceController\t: false,\n\twcsTimeoutIntervel\t\t: 600,\n\tcartTimeoutIntervel\t\t: 600000,\n\tsearchTimeoutIntervel\t: 10000,\n\tbrowseTimeoutIntervel\t: 10000,\n\tglobalAjaxTimeout       : 30000,\n\tglobalATPServiceTimeout : 5000,\n\tenvMpulse\t\t\t\t: "prod",\n\tmpulseUrl\t\t\t\t: "//c.go-mpulse.net/boomerang/KQTS5-4NBTD-EYGLE-64UYR-S5892",\n\tslingshotPreviewURL\t\t: "https://content-preview-secure.target.com/content-preview",\n\tslingshotURL\t\t\t: "https://content-delivery-secure.target.com/content-publish",\n\tslingshotURL_http       : "http://content-delivery.target.com/content-publish",\n\tslingshotCategoryId\t\t: "/slingshot/category/2222222",\n\tmobileDomain\t\t\t: "http://m.target.com",\n\tmobileSecureDomain\t\t: "https://m-secure.target.com",\n\ttabletDVMChannelId\t\t: "target",\n\tsubscriptionModURL\t\t: "https://subscriptions-secure.target.com",\n\tseoApiURL\t\t\t\t: "https://content-delivery-secure.target.com/content-publish/taxonomy/v1/seo?",\n\tseoApiURL_http\t\t\t: "http://content-delivery.target.com/content-publish/taxonomy/v1/seo?",\n\thlURL\t\t\t\t\t: "http://www.hlserve.com/delivery/api",\n\thlKey\t\t\t\t\t: "764937a9-7afb-4cf1-8631-d8a5edca8f36",\n\thlId\t\t\t\t\t: "[CS]v1|2AC0BE5905079201-6000010B000429CD[CE]",\n\tsfCert\t\t\t\t\t: "",\n\tsfCID\t\t\t\t\t: "",\n\tsfURL\t\t\t\t\t: "",\n\tchkURL\t\t\t\t\t: "https://checkout-api-secure.target.com",\n\tchkWalletAPIURL\t\t\t: "https://checkout-api-secure.target.com",\n\tgamURL\t\t\t\t\t: "https://gam-api-secure.target.com",\n\tgamKey\t\t\t\t\t: "OGFiNjJhOWMtMWI4Ni00ZDJhLTlkNGItMTUwODJiYzNmMDA0OjNpSnRQamVNdkk=",\n\tmodAjaxTimeout\t\t\t: "20000",\n\ttwsDomain\t\t\t\t: "http://tws.target.com",\n\ttwsSecureDomain\t\t\t: "https://tws-secure.target.com",\n\ttreeCategoryUrl\t\t\t: "http://m.target.com/TreeCategory",\n\tsecureTreeCategoryUrl\t: "https://m-secure.target.com/TreeCategory",\n\tcategoriesXml           : "http://img1.targetimg1.com/wcsstore/marketing/com/mobile/en/xml/products/categories.xml",\n\timageIncludes\t\t\t: "/wcsstore/marketing/com/mobile/includes",\n\tbreadCrumbUrl           : "http://tws.target.com/searchservice/catalog/bread_crumb/v2/by_category_id?",\n\tfireflySchemaId         : "1184",\n\tfireflyTopic            : "firefly_estore_eventstream",\n\tfireflyHost             : "firefly.target.com",\n\tsecEnabled\t\t\t\t: "true",\n\tapiNonPCIDomain\t\t\t: "https://api.target.com",\n\tsubscriptionUrl         : "/wcsstore/marketing/com/mobile/en/html/spot/target-subscriptions_1.html",\n\tsapphireUrl: "http://sapphire.edge-csp1-e1-npe.target.com/sapphire/runtime/api/v1/qualified-experiments?",\n  typeaheadUrl: "http://typeahead.target.com/",\n  typeaheadSecureUrl: "https://typeahead-secure.target.com/",\n\tshapeJs: "//static.targetimg1.com/ssx/ssx.mod.js"\n  };\n\n\n var mobileDomain = "http://m.target.com";\n var mobileSecureDomain = "https://m-secure.target.com";\n var tabletDomain = "http://www.target.com";\n var tabletSecureDomain = "https://www-secure.target.com";\n\n  if(tabletDomain.indexOf(window.location.hostname.replace(/origin.{3}-/,"")) != -1 || tabletSecureDomain.indexOf(window.location.hostname.replace(/origin.{3}-/,"")) != -1 ){\n\t  configJSON["preUrlConstructor"] = configJSON["preUrlTabletConstructor"];\n\t  configJSON["securePreUrlConstructor"] = configJSON["securePreUrlTabletConstructor"];\n  }else{\n\t  configJSON["preUrlConstructor"] = configJSON["preUrlMobileConstructor"];\n\t  configJSON["securePreUrlConstructor"] = configJSON["securePreUrlMobileConstructor"];\n  }\n\n  // setting secure/nonsecure image server path\n  if (window.location.protocol =="https:") {\n    configJSON["imageServerDomain"] = "https://img3-secure.targetimg3.com";\n  } else {\n    configJSON["imageServerDomain"] = "http://img3.targetimg3.com";\n  }\n\n</script>\n<script type="text/javascript">\n  \n  var isSecure = (window.location.protocol !== "http:");\n  var noSeoCall = (window.location.pathname.indexOf(\'target-crush\') !== -1 || window.location.pathname.indexOf(\'mcategories\') !== -1);\n  var seoHttpRequestPromise = null;\n  var seoHttpRequest = null;\n  var seoReadyStateHandler = null;\n  var dateSearchParam = \'\';\n  var isSapphireEnabled = false;\n  // global function to getVisitorId\n  var getVisitorIdCookie = function getVisitorIdCookie() {\n    var name = "visitorId=";\n    var ca = document.cookie.split(\';\');\n    for(var i=0; i<ca.length; i++) {\n        var c = ca[i];\n        while (c.charAt(0)===\' \') c = c.substring(1);\n        if (c.indexOf(name) === 0) return c.substring(name.length,c.length);\n    }\n    return "";\n  };\n\n  // firefly vistorId changes starts here\n  (function(){\n\tfunction getByteArrayFromInteger(integer, desiredBytes) {\n        var byteValue, byteArray, index;\n\n        byteArray = [];\n\n        for (index = 0; index < desiredBytes; index++) {\n            byteValue = integer & 0xff;\n            byteArray.push(byteValue);\n            integer = (integer - byteValue) / 256;\n        }\n\n        return byteArray.reverse();\n    }\n\n\tfunction getRandomNumber(min, max) {\n        return Math.floor(Math.random() * (max - min)) + min;\n    }\n\n\tfunction getHexStringFromByte (byte) {\n        var hexCharArray, hexString;\n\n        hexCharArray = [\'0\', \'1\', \'2\', \'3\', \'4\', \'5\', \'6\', \'7\', \'8\', \'9\', \'A\', \'B\', \'C\', \'D\', \'E\', \'F\'];\n        hexString = hexCharArray[(byte >> 4) & 0x0f] + hexCharArray[byte & 0x0f];\n\n        return hexString;\n    }\n\n\tfunction getHexStringFromByteArray(byteArray) {\n        return byteArray.map(getHexStringFromByte, this).join("");\n    }\n\n    function create48BitTimeByteArray() {\n        return getByteArrayFromInteger(new Date(), 6);\n    }\n\n    function create64BitRandomByteArray() {\n        var randomValue, sixteenBitRandomValue, fortyEightBitRandomValue;\n\n        randomValue = getRandomNumber(0, 9000000000000000);\n        sixteenBitRandomValue = getByteArrayFromInteger(randomValue, 2);\n\n        randomValue = getRandomNumber(0, 9000000000000000);\n        fortyEightBitRandomValue = getByteArrayFromInteger(randomValue, 6);\n\n        return sixteenBitRandomValue.concat(fortyEightBitRandomValue);\n    }\n\n\tfunction createVisitorId(source) {\n        var byteArray, decorator, randomByteArray, source, timeByteArray;\n\n        timeByteArray = create48BitTimeByteArray();\n        randomByteArray = create64BitRandomByteArray();\n\n        byteArray = timeByteArray.concat([1, source]).concat(randomByteArray);\n\n        return getHexStringFromByteArray(byteArray);\n\t}\n\n\tfunction isMobile() {\n\t    mobile = ["Android", "webOS", "iPhone", "iPod", "BlackBerry", "Windows Phone", "Opera Mini", "IEMobile"];\n\t    for (var i = 0; i <= mobile.length - 1; i++) {\n\t        var mobilex = navigator.userAgent.indexOf(mobile[i]);\n\t        if (mobilex != -1) {\n\t            return true;\n\t            break;\n\t        }\n\t    }\n\t    return false;\n\t }\n\n\t function isPad() {\n\t     pad = ["iPad"];\n\t     for (var i = 0; i <= pad.length - 1; i++) {\n\t         var mobilex = navigator.userAgent.indexOf(pad[i]);\n\t         if (mobilex != -1) {\n\t             return true;\n\t             break;\n\t         }\n\t     }\n\t     return false;\n\t  }\n\n\t  function isDesktop() {\n\t      return !navigator.userAgent.match(/Android|BlackBerry|iPhone|iPad|iPod|Opera Mini|IEMobile|NokiaBrowser|Silk|mobile|tablet/i);\n\t  }\n\n\t  function getVisitorId() {\n          var source;\n\n          if (isDesktop()) {\n              source = 1;\n          } else if (isMobile()) {\n              source = 2;\n          } else if (isPad()) {\n              source = 3;\n          } else {\n              source = 0;\n          }\n\n          return createVisitorId(source);\n\t  }\n\n\t  function createVisitorIdCookie(visitorId) {\n\t\t  var d = new Date();\n\t\t  d.setTime(d.getTime() + 31536000000);\n\t\t  var expires = "expires="+d.toUTCString();\n\t\t  return "visitorId=" + visitorId + ";" + expires + ";domain=.target.com;path=/";\n\t  }\n\n\t  if (getVisitorIdCookie() === "") {\n\t\t  var session, sessionId, visitorId;\n\t\t  visitorId = getVisitorId();\n\t\t  document.cookie = createVisitorIdCookie(visitorId);\n\t\t  \n\t\t  // init firefly session\n\t\t  sessionId = (Math.floor(Math.random() * (9007199254740960 - 11184840)) + 11184840).toString(16);\n\t\t  session = {\n\t\t  \t\'newGuest\': \'true\',\n\t\t  \t\'sessionHash\': sessionId\n\t\t  };\n\t\t  document.cookie = "ffsession=" + JSON.stringify(session) + ";domain=.target.com;path=/";\n\t  }\n  })();\n\n  if (!isSecure && !noSeoCall) {\n    (function(){\n    var seoApi = (true && window.location.protocol == "http:") ? "http://content-delivery.target.com/content-publish/taxonomy/v1/seo?" : "https://content-delivery-secure.target.com/content-publish/taxonomy/v1/seo?";\n    var appPath = window.location.pathname.replace(\'home\',\'\') + ((false)?"": window.location.search)\n        seoApi = seoApi + \'url=\' + encodeURIComponent(appPath) + \'&children=true&breadcrumbs=true\';\n\n        if (false) {\n          // below changes are to give preference to effective date url parameter\n          var regex = new RegExp("[\\\\?&]" + \'effective_date\' + "=([^&#]*)");\n          var results = regex.exec(location.search);\n          var effectiveDate = results == null ? "" : decodeURIComponent(results[1].replace(/\\+/g, " "));\n          if(effectiveDate){\n            dateSearchParam = \'&effective_date=\' + effectiveDate;\n            document.getElementById(\'previewDate\').value = effectiveDate.replace(\'Z\',\'\');\n          }else{\n            dateSearchParam = \'&effective_date=\' + document.getElementById(\'previewDate\').value + \'Z\';\n          }\n          if(dateSearchParam){\n              seoApi = seoApi + dateSearchParam;\n          }\n\n        }\n        seoHttpRequest = new XMLHttpRequest();\n        seoHttpRequest.onreadystatechange = function(){\n          if(seoHttpRequest.readyState == 4 && seoReadyStateHandler){\n            seoReadyStateHandler();\n          }\n        };\n        seoHttpRequest.open("GET", seoApi, true);\n        seoHttpRequest.send();\n      })();\n    }\n</script>\n<meta name="google-site-verification" content="1rmXsZRZGP3uOmdg4qvP1A0zVaAKoxvrWtBavkX0LCE" />\n    <link  href="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/css/patlab/global.css" media="all" rel="stylesheet" type="text/css" />\n\n\t<script id="domains" type="text/javascript">\n\n\t\tif(tabletDomain.indexOf(window.location.hostname.replace(/origin.{3}-/,"")) != -1 || tabletSecureDomain.indexOf(window.location.hostname.replace(/origin.{3}-/,"")) != -1 ){\n\t\tdomain = tabletDomain;\n\t\tsecure_domain = tabletSecureDomain;\n\t\t}else{\n\t\tdomain = mobileDomain;\n\t\tsecure_domain = mobileSecureDomain;\n\t\t}\n\n\t\timg_domain = "http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01";\n\t\timageSerURL="http://img3.targetimg3.com/wcsstore/marketing";\n\t\twcs_server="http://www-int.att.target.com/wcs/resources";\n\t\twcs_secure_server="https://www-int.att.target.com/wcs/resources";\n\t\t\n\t\t\t\tisSecure = false;\n\t\t\t</script>\n\n\n\n    <script>\n\t\tvar FF_GEO_FEATURE = \'ON\';\n\t\tvar FF_PRG_2  = \'true\';\n\t\tvar defualtPickupWindow = \'false\';\n\t\tvar sfsenable = (\'true\'===\'true\');\n\t\tvar rushDelByAddress = \'on\';\n\t\tvar IS_REPROMISE_ENABLE =  \'true\';\n\t\tvar USE_ORDER_ITEM_ID =  \'true\';\n\t\tvar formFactor=\'tablet\'||"phone";\n\t\tvar useV1OrderDetails=\'false\';\n\t\tvar showCreateACcount=\'true\';\n\t\tvar STORE_RESULT_LIMIT=\'20\';\n\t\tvar prodAvailCount = \'10\';\n\t\tvar redCard_new = \'true\';\n\t\tvar plugins_mod = \'http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/plugins.mod.js\';\n\t\tvar mod_0 = \'http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/plp.mod.js\';\n\t\tvar mod_1 = \'http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/non-plp.mod.js\';\n\t</script>\n\t\n    <script type="text/javascript" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/plugins.mod.js" ></script>\n\t\t\t<script type="text/javascript" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/plp.mod.js" ></script>\n\t\t<script type="text/javascript" src="//nexus.ensighten.com/target/tcom-ui-prod/Bootstrap.js"></script>\n\t\t<script>\n\t  var scr = document.createElement("script");\n\t  scr.src = configJSON.imageServerDomain + configJSON.imageIncludes + \'/foresee2/foresee-trigger.js\';\n    scr.async = true;\n\t  document.getElementsByTagName("head")[0].appendChild(scr);\n\t</script>\n<script id="dvm" type="text/javascript">\n\tvar gptadslots=[];\n\tvar googletag = googletag || {};\n\tgoogletag.cmd = googletag.cmd || [];\n\t(function(){ var gads = document.createElement(\'script\');\n\t\tgads.async = true; gads.type = \'text/javascript\';\n\t\tvar useSSL = \'https:\' == document.location.protocol;\n\t\tgads.src = (useSSL ? \'https:\' : \'http:\') + \'//www.googletagservices.com/tag/js/gpt.js\';\n\t\tvar node = document.getElementsByTagName(\'script\')[0];\n\t\tnode.parentNode.insertBefore(gads, node);\n\t})();\n</script>\n<script type="text/javascript">\n      if ((/iphone|ipod|ipad.*os /gi).test(navigator.appVersion)) {\n        window.onpageshow = function(evt) {\n          // If persisted then it is in the page cache, force a reload of the page.\n          if (evt.persisted) {\n    \t    window.location.reload();\n          }\n        };\n      }\n</script>\n</head>\n  <body id="home" ontouchstart="">\n  <div tabindex="-1" class="TGTloading" style="display: none">\n    <div class="loading-container">\n      <div class="loading-spinner"></div>\n      <div class="loading-message"></div>\n    </div>\n  </div>\n\t<div id="viewport">\n\t\t\t\t<div id="pageStart"></div>\n\t\t\t</div>\n\t\t<script id="page-meta" type="application/json">\n\t\t{\n  "img_domain" : "http://img3.targetimg3.com",\n  "img_secure_domain" : "https://img3-secure.targetimg3.com",\n  "generated_time" : "Wed Mar 23 14:34:11 EDT 2016",\n  "build_number" : "716-03162016-01",\n  "page_name" : "mProductList",\n  "view_def" : {\n    "header" : [ {\n      "path" : "http://img3.targetimg3.com/wcsstore/marketing/com/mobile/includes/template/header_v2.html",\n      "position" : 1\n    } ],\n    "nav" : [ {\n      "path" : "http://img3.targetimg3.com/wcsstore/marketing/com/mobile/includes/template/header_v2.html",\n      "position" : 1\n    } ],\n    "main_body" : [ {\n      "path" : "mCategoryResult",\n      "position" : 2,\n      "attribute" : [ {\n        "name" : "googleAdsHeader",\n        "value" : "Sponsored Links"\n      }, {\n        "name" : "pubId",\n        "value" : "mobile-targetcorp-browse"\n      }, {\n        "name" : "googleAdtest",\n        "value" : "off"\n      } ]\n    } ],\n    "footer" : [ {\n      "path" : "http://img3.targetimg3.com/wcsstore/marketing/com/mobile/includes/template/header_v2.html",\n      "position" : 1\n    } ]\n  },\n  "page_grid" : "<div id=\\"header\\" class=\\"l-sticky\\" data-name=\\"views/tablet/common/header.view\\"></div><div id=\\"nav\\" data-name=\\"views/tablet/common/nav.view\\"></div><div id=\\"plp-facet-wrap\\" class=\\"l-container-fixed\\" data-page=\\"category\\" data-name=\\"views/tablet/category/wrapper.shell.view\\"></div><div id=\\"categoryList\\" data-child=\\"true\\" class=\\"l-col-xs-12 h-standardSpacingBottom\\" data-name=\\"views/tablet/category/category-list.view\\" data-parent=\\"views/tablet/category/wrapper.shell.view\\"></div><div id=\\"facet\\" class=\\"l-col-xs-12 l-col-lg-3\\" data-child=\\"true\\" data-name=\\"views/tablet/category/facet.view\\" data-parent=\\"views/tablet/category/wrapper.shell.view\\"></div><div id=\\"plp\\" class=\\"l-col-xs-flex\\" data-child=\\"true\\" data-page=\\"product listing page\\" data-name=\\"views/tablet/category/plp.view\\" data-parent=\\"views/tablet/category/wrapper.shell.view\\"></div><div id=\\"fiats\\" data-name=\\"views/tablet/common/fiats.view\\"></div><div id=\\"adcontainer\\" data-name=\\"views/tablet/category/adsense.view\\"></div><div id=\\"footer\\" class=\\"footer\\" data-name=\\"views/tablet/common/footer.view\\"></div>",\n  "tracking" : {\n    "attribute" : [ {\n      "name" : "s.prop4",\n      "value" : "mobile"\n    } ]\n  },\n  "device_info" : {\n    "attribute" : [ {\n      "name" : "deviceType"\n    }, {\n      "name" : "formFactor",\n      "value" : "tablet"\n    } ]\n  },\n  "banners" : [ {\n    "id" : "54x94",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/20140904-clinicMobile.html"\n  }, {\n    "id" : "54vl9",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/20141022-storeredirection.html"\n  }, {\n    "id" : "4ybij",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/05212015-eddie-borgo-redirect.html"\n  }, {\n    "id" : "4yinn",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/06302015-online-check-In-Redirect.html"\n  }, {\n    "id" : "55md5",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/06302015-beauty-redirect-needed.html"\n  }, {\n    "id" : "4y7cg",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/08282015_willo.html"\n  }, {\n    "id" : "4y57c",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/08212015-plaid-redirect.html"\n  }, {\n    "id" : "4yn3w",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/08242015-faq-ways-to-shop.html"\n  }, {\n    "id" : "4y8o9",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/06302015-optical-redirect.html"\n  }, {\n    "id" : "5xtyp",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/09042015_backtoschool_redirect.html"\n  }, {\n    "id" : "55emz",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/09102015_apple6s_redirect.html"\n  }, {\n    "id" : "4y22r",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/09152015_beautyevents.html"\n  }, {\n    "id" : "54uci",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/21102015_faribault_redirect.html"\n  }, {\n    "id" : "4xw73",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/10122015_apple_watch-redirect.html"\n  }, {\n    "id" : "55d5o",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/25102015_topgifts_toys_redirect.html"\n  }, {\n    "id" : "54und",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/10132015_apple6_redirect.html"\n  }, {\n    "id" : "4xupo",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/10292015_gifting_experts-redirect.html"\n  }, {\n    "id" : "4y4de",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/01112015_wonderlist_redirect.html"\n  }, {\n    "id" : "55epy",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/11012015_apple-tv-redirect.html"\n  }, {\n    "id" : "551st",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/11122015-freeshipping-redirect.html"\n  }, {\n    "id" : "4xpm4",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/11182015-adele-redirect.html"\n  }, {\n    "id" : "55yvt",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/11252015-blackfridaymap-redirects.html"\n  }, {\n    "id" : "55o14",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/redirect-hasbro-01042016.html"\n  }, {\n    "id" : "5xtig",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/01102015-girls-clothing-redirect.html"\n  }, {\n    "id" : "5xtjb",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/01192015-boys-clothing-redirect.html"\n  }, {\n    "id" : "4yn9m",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/01192015-pharmacy-redirect.html"\n  }, {\n    "id" : "4vq64",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/marimekko-redirect.html"\n  } ],\n  "title" : "",\n  "processing_time" : 322,\n  "jsfiles" : [ ],\n  "cssfiles" : [ ],\n  "spot_categories" : {\n    "4yn3w" : "/redcard/faq-ways-to-shop",\n    "4ybij" : "/spot/eddie-borgo",\n    "4xpm4" : "/spot/adele25",\n    "4y22r" : "/spot/beautyevents",\n    "55epy" : "/spot/brand/2015/apple-tv",\n    "54uci" : "/spot/faribault",\n    "55d5o" : "/spot/Top-gifts",\n    "4y8o9" : "/spot/optical",\n    "54vl9" : "/store-locator/find-stores",\n    "551st" : "/spot/shipping-returns",\n    "5xtjb" : "/c/boys-clothing/-/N-5xty4",\n    "4vq64" : "/spot/marimekko",\n    "55o14" : "/spot/dvm/hasbro",\n    "55md5" : "/spot/beauty/concierge",\n    "5xtyp" : "/spot/back-to-school",\n    "4yinn" : "/spot/clinic/onlinecheckin",\n    "4y4de" : "/spot/Wonderlist",\n    "4y7cg" : "/spot/willo",\n    "4y57c" : "/spot/plaid",\n    "54und" : "/spot/brand/2015/apple6",\n    "4yn9m" : "/c/pharmacy-faqs/-/N-4umyp",\n    "4xw73" : "/spot/brand/2015/apple-watch",\n    "5xtig" : "/c/girls-clothing/-/N-5xtwa",\n    "4xupo" : "/spot/Gifting-Experts",\n    "54x94" : "/spot/clinic",\n    "55emz" : "/spot/brand/2015/apple6s",\n    "55yvt" : "/spot/black-friday-maps"\n  },\n  "feature" : {\n    "FORESEE" : "false",\n    "TEA_LEAF" : "false",\n    "SECURE_TEA_LEAF" : "false",\n    "FF_ENABLE" : "true",\n    "BV_ENABLED" : "true",\n    "TRACKER" : "false",\n    "SFS_ENABLE" : "true",\n    "FF_PRG_2" : "true",\n    "REGISTRY_RESET_FLAG" : "false",\n    "TNL_COOKIE" : "false",\n    "IS_REPROMISE_ENABLE" : "true",\n    "SHOW_MODAL_BOX" : "true",\n    "ONE_PAGE_CHECKOUT_ENABLE" : "true",\n    "ONE_PAGE_CHECKOUT_ENABLE_FOR_IPAD" : "true",\n    "REVIEW_PAGE_ENABLE_CRTE_ACCT" : "false",\n    "IS_DUMMY_THANK_YOU" : "true",\n    "SEARCH_OPT_FLAG" : "false",\n    "USE_ORDER_ITEM_ID" : "true",\n    "DVM" : "true",\n    "SHIPPING_LIMITED_OFFER" : "false",\n    "PREVIEW_ENABLE" : "false",\n    "ORDER_DETAIL_V1" : "false",\n    "SHOW_CREATE_ACCOUNT" : "true",\n    "SUBSCRIPTION_ENABLED" : "true",\n    "STS_ENABLE" : "true",\n    "SUBS_SHIP_PROMO_MODALMSG" : "true",\n    "PRZ_ENABLE" : "true",\n    "CHKOUT_EXP_ELIGBLE" : "true",\n    "PEAK_HOURS_FLAG" : "false",\n    "THREAT_METRICS_ENABLE" : "true",\n    "ORD_PRZ_ENABLE" : "true",\n    "REDCARD_NEW" : "true",\n    "SLINGSHOT_ENABLED" : "true",\n    "EXPERIAN_EMAIL_SERVICE" : "true",\n    "CART_GET_DEALS" : "false",\n    "APPLE_GIFTCARD_MERCH_CLASS" : "true",\n    "SLING_SHOT_PREVIEW_ENABLE" : "false",\n    "SLINGSHOT_SERVER_CONTROLE" : "false",\n    "IS_CARDINAL" : "false",\n    "ADVANCE_ORDER_CROSSOVER" : "false",\n    "ADVANCE_ORDER_ENABLE" : "true",\n    "MOBILE_ONLY_CHANNEL" : "true",\n    "DELIVERY_DISPLAY_PRICE_ENABLE" : "false",\n    "SITESKIN_ENABLED" : "false",\n    "SUBSCRIPTION_MOD_ENDPOINT" : "true",\n    "SUBSCRIPTION_UI_DISABLED" : "false",\n    "NONSECURE_SIGNIN_OVERLAY_ENABLED" : "true",\n    "ADAPIVE_GC" : "true",\n    "FULL_ADAPTIVE" : "true",\n    "PLP_TO_PDP_PARTIAL_LOAD" : "false",\n    "LIMITED_QTY_ENABLED" : "false",\n    "OBGB_ENABLED" : "true",\n    "ENABLE_TRACKJS" : "false",\n    "REORDER_TWO_TAP_OVERLAY" : "true",\n    "DELIVERY_EMAIL_VALIDATION" : "false",\n    "PAGE_SCRIPT_ENABLE" : "false",\n    "STORE_LIMITED_QTY_ENABLED" : "true",\n    "REPROMISE_OPTIMIZATION_ENABLE" : "true",\n    "WXS_LIMITED_QTY_ENABLED" : "true",\n    "AISLEINFOSERVICE_ENABLE" : "true",\n    "TAG_PAGE_ENABLED" : "true",\n    "CATEGORY_SLINGSHOT_ENABLED" : "true",\n    "SLINGSHOT_HTTP_ENABLED" : "true",\n    "STORE_LOCATOR_SEO_URL" : "true",\n    "CART_PROMO_CODE_ENTRY" : "true",\n    "FF_V3_TO_ATP_ENABLE" : "true",\n    "CRUSH_ACTIVE" : "true",\n    "REFRESH_JOB" : "false",\n    "BROWSE_BY_CATEGORIES_SLINGSHOT" : "true",\n    "FIREFLY_ENABLED" : "true",\n    "REPOPULATE_GEO_COOKIE" : "true",\n    "DEFAULT_TABLET_VIEW" : "true",\n    "PDP_DYNAMIC_PRICING" : "true",\n    "GET_THIS_PHONE" : "true",\n    "GIFT_REGISTRY_RENAME" : "true",\n    "CRUSH_FEED_CURATION" : "true",\n    "EMPTY_CART_DVM_FLAG" : "true",\n    "ENABLE_FORESEE" : "true",\n    "IS_VIEWCART_OPTIMIZED" : "true",\n    "PAYMENT_SERVICES_ENABLED" : "true",\n    "GIFTCARD_ACTIVATION_MSG_ENABLE" : "false",\n    "SUB_RECO" : "false",\n    "PROMO_INJECTION_ENABLED" : "false",\n    "SECURITY_FIX_ENABLED" : "true",\n    "EXPRESS_CHECKOUT" : "true",\n    "OBGB_MSG_ON_LISTING_PAGES" : "true",\n    "FGC_FIX_ENABLE" : "false",\n    "SFS_BACKORDER" : "false",\n    "SHOW_ORDER_OVERLAY" : "true",\n    "USE_MOD_ORDERS" : "false",\n    "PHARMACY_INTERSTITIAL" : "true",\n    "ENABLE_WRITE_REVIEW" : "true",\n    "ENABLE_CRITICAL_REVIEW" : "true",\n    "DISABLE_MOBILE_GC" : "true",\n    "SUBSCRIPTION_FLYOUT" : "true",\n    "SEARCH_INSTEAD_FOR" : "false",\n    "DID_YOU_MEAN" : "false",\n    "ATC_RECOMMANDATIONS" : "false",\n    "SAPPHIRE" : "false",\n    "STORE_LOCATOR_ACCORDION_FIX" : "true",\n    "GAM_REPROMISE_FLYOUT" : "true",\n    "SSX_ENABLED" : "false",\n    "EnableSFL" : "true",\n    "FF_GEO_FEATURE" : "ON",\n    "DEFAULT_PICKUP_WINDOW" : "4",\n    "RELATED_CATEGORY" : "Y",\n    "CATEGORY_FEATURE_BRAND" : "Y",\n    "CATEGORY_GOOGLE_ADS" : "Y",\n    "CATEGORY_DVM_ADS" : "Y",\n    "DVM_CHANNLE_ID" : "mtarget",\n    "TABLET_DVM_CHANNLE_ID" : "target",\n    "SEARCH_OPT_RESP_GROUP" : "VariationSummary,Items",\n    "RUSH_DELIVERY_RADIUS" : "10",\n    "STORE_FINDER" : "100",\n    "RUSH_DEL_BY_ADDR" : "on",\n    "AVAILABILITY_SERVICE_PROD_COUNT" : "10",\n    "STORE_RESULT_LIMIT" : "20",\n    "THREAT_METRICS_ORG_ID" : "9p00aymw",\n    "SLINGSHOT_CATG_ID" : "/slingshot/category/2222222",\n    "FREE_SHIPPING_THRESHHOLD_VALUE" : "25",\n    "AO_MAX_STORES" : "5",\n    "ORD_HISTORY_DAY_LIMIT" : "1",\n    "ORD_HISTORY_COUNT_LIMIT" : "100",\n    "AO_STORES_RADIUS" : "25",\n    "GAM_DASH_ORDERS_LIMIT_COUNT" : "3",\n    "HOOK_LOGIC_KEY" : "764937a9-7afb-4cf1-8631-d8a5edca8f36",\n    "HOOK_LOGIC_ID" : "[CS]v1|2AC0BE5905079201-6000010B000429CD[CE]",\n    "TRACKJS_APPID" : "mobileweb",\n    "TRACKJS_TOKEN" : "913e59b71ca34b21aa95bc55121a0871",\n    "STORE_LIMITED_QTY" : "5",\n    "EVENT_TYPE" : "star",\n    "EVENT_STORES" : "4,61,64,90,93,199,215,221,230,246,301,320,346,348,351,359,361,617,627,636,676,686,687,755,766,769,794,810,818,822,824,827,830,844,861,870,885,911,935,937,938,942,969,992,995,1010,1018,1021,1025,1029,1034,1043,1056,1058,1092,1102,1107,1139,1140,1150,1153,1163,1166,1182,1191,1207,1224,1238,1244,1249,1252,1254,1257,1261,1266,1268,1275,1285,1306,1338,1339,1347,1350,1351,1354,1355,1357,1363,1364,1367,1368,1370,1376,1377,1384,1391,1397,1408,1409,1427,1431,1439,1443,1445,1449,1453,1455,1473,1476,1478,1481,1483,1501,1502,1505,1506,1510,1518,1541,1751,1755,1756,1767,1768,1774,1783,1787,1795,1797,1799,1806,1820,1821,1822,1856,1858,1869,1874,1883,1895,1903,1912,1916,1921,1930,1932,1934,1944,1954,1961,1965,1981,2014,2019,2022,2031,2034,2035,2036,2051,2093,2101,2105,2106,2108,2124,2129,2138,2170,2176,2189,2190,2205,2208,2210,2227,2244,2266,2271,2303,2313,2322,2338,2339,2348,2350,2356,2360,2371,2372,2373,2403,2410,2429,2473,2532,2542,2572,2682,2737,2757,2760,2764,2767,2771,2824,2843",\n    "CRUSH_URL_PROD" : "https://gnc-secure.target.com/guestpreference",\n    "FEED_URL_PROD" : "https://prz-secure.target.com/recommendations/v1?",\n    "MOD_INTEG_BUILD_NUMBER" : "12345",\n    "CRUSH_FEED_MAX" : "96",\n    "ITUNES_MERCH_CLASS" : "PREPAID CARDS, ENTERTAINMENT CARDS, ITUNES, DIGITAL CONTENT, VERIZON CONTRACT, BATTERIES",\n    "INVALID_CALLOUTS" : "testCallOut",\n    "GET_THIS_PHONEURL" : "https://mobile.target.com/web/controller/landing.php?",\n    "DLP_PARAMS" : "[\\"AFID\\",\\"CPNG\\",\\"KID\\",\\"LID\\",\\"LNM\\",\\"MT\\",\\"N\\",\\"gclid\\",\\"ref\\",\\"adgroup\\",\\"network\\",\\"device\\",\\"querystring\\",\\"location\\",\\"gclsrc\\",\\"emseq\\",\\"link\\",\\"tp\\"]",\n    "DYNAMIC_PROMO_VAL" : "TGTA39R9",\n    "PRIVACY_UPDATED_DATE" : "2015-10-26",\n    "ATP_SERVICE_PAYLOAD_MAX_PRODUCTS" : "20",\n    "GIFTCARD_PURCHASED_TODAY_ACTIVATION_24HOURS" : "If you purchased a Target GiftCard on December 20, your gift card will be activated on December 21.",\n    "MERCH_SUBCLASS_ARRAY" : "[{\\"DPCI\\":\\"255-02\\",\\"content\\":\\"atnt\\",\\"corpId\\":\\"596\\"},{\\"DPCI\\":\\"255-04\\",\\"content\\":\\"verizon\\",\\"corpId\\":\\"660\\"},{\\"DPCI\\":\\"255-08\\",\\"content\\":\\"sprint\\",\\"corpId\\":\\"545\\"},{\\"DPCI\\":\\"255-14\\",\\"content\\":\\"iphones\\",\\"corpId\\":\\"731\\"}]",\n    "ORD_HISTORY_RECENT_LIMIT" : "30",\n    "ORD_HISTORY_ALL_LIMIT" : "365",\n    "SERVICE_CALL_DATA_TYPE" : "jsonp",\n    "WHITE_LIST_MERCH_CONTENT" : "merchandizingSlot1"\n  },\n  "datacenter" : "SCS"\n}</script>\n  </body>\n</html>\n\n'
>>> d = webdriver.Firefox()
>>> d.get(BASE_URL)
>>> 
>>> prod_links = d.find_element_by_tag_name("li")
>>> len(prod_links)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    len(prod_links)
TypeError: object of type 'WebElement' has no len()
>>> prod_links
<selenium.webdriver.remote.webelement.WebElement (session="c5f2a437-b396-424d-91f1-a8d474e3a84b", element="{a58a6493-b03b-4401-994f-c338895cce72}")>
>>> prod_links = d.find_elements_by_tag_name("li")
>>> len(prod_links)
873
>>> prod_links[0]
<selenium.webdriver.remote.webelement.WebElement (session="c5f2a437-b396-424d-91f1-a8d474e3a84b", element="{a58a6493-b03b-4401-994f-c338895cce72}")>
>>> prod_links[0].get_attribute('href')
>>> links = BeautifulSoup(d.page_source, "html.parser", parse_only=SoupStrainer('li', {'class':'product '}))
>>> links
<li class="product " data-id="201952074" data-row="0-1">
<a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-original-blend-medium-roast-whole-bean-coffee-12-oz/-/A-13400831">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin' Donuts Original Blend Medium Roast Whole Bean Coffee 12oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13400831?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin' Donuts Original Blend Medium Roast...
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13400831"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin' Donuts Original Blend Medium Roast Whole Bean Coffee 12oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="201937086" data-row="1-1">
<a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-medium-roast-original-blend-ground-coffee-12-oz/-/A-13399846">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin' Donuts Medium Roast Original Blend Ground Coffee 12oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13399846?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin' Donuts Medium Roast Original Blend...
      </p><!-- /.details--title -->
<div class="details--ratingSwatch">
<div class="ratings-block ">
<div class="ratings ratings-xs h-float-left">
<img aria-hidden="true" class="ratings-img" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-off.svg"/>
<div class="ratings-score" style="width:100%;">
<img alt="5 out of 5 stars" class="ratings-img" role="link" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-on.svg"/>
</div>
</div>
<span class="h-sr-only">5 reviews </span>
<span aria-hidden="true" class="ratings--count"> 5 </span>
<!-- /.ratings -->
</div>
<!-- /.ratings-block -->
</div>
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13399846"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin' Donuts Medium Roast Original Blend Ground Coffee 12oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="201938529" data-row="2-1">
<a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-french-vanilla-flavored-ground-coffee-12-oz/-/A-13399847">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin' Donuts French Vanilla Flavored Ground Coffee 12oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13399847?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin' Donuts French Vanilla Flavored Gro...
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13399847"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin' Donuts French Vanilla Flavored Ground Coffee 12oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="201972808" data-row="3-2">
<a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-hazelnut-ground-coffee-12-oz/-/A-13400186">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin' Donuts Hazelnut Ground Coffee 12oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13400186?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin' Donuts Hazelnut Ground Coffee 12oz
      </p><!-- /.details--title -->
<div class="details--ratingSwatch">
<div class="ratings-block ">
<div class="ratings ratings-xs h-float-left">
<img aria-hidden="true" class="ratings-img" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-off.svg"/>
<div class="ratings-score" style="width:100%;">
<img alt="5 out of 5 stars" class="ratings-img" role="link" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-on.svg"/>
</div>
</div>
<span class="h-sr-only">1 reviews </span>
<span aria-hidden="true" class="ratings--count"> 1 </span>
<!-- /.ratings -->
</div>
<!-- /.ratings-block -->
</div>
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13400186"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin' Donuts Hazelnut Ground Coffee 12oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="300808259" data-row="4-2">
<a class="product--link js-redirect-to-pdp" href="/p/tic-tac-bunny-burst-1oz/-/A-50355453">
<!-- call outs-->
<!--call outs-->
<img alt="Tic Tac Bunny Burst 1oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/50355453?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $1.00
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $1.09
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Tic Tac Bunny Burst 1oz
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_50355453"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Tic Tac Bunny Burst 1oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="300698967" data-row="5-2">
<a class="product--link js-redirect-to-pdp" href="/p/8-oz-candy-treasures-chocolates/-/A-50247436">
<!-- call outs-->
<!--call outs-->
<img alt="Minions Treasure Egg .8oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/50247436?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          $1.00
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Minions Treasure Egg .8oz
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_50247436"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Minions Treasure Egg .8oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="206481687" data-row="6-3">
<a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-colombian-11oz/-/A-15351375">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin Donuts Colombian 11oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/15351375?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin Donuts Colombian 11oz
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_15351375"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin Donuts Colombian 11oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="200365548" data-row="7-3">
<a class="product--link js-redirect-to-pdp" href="/p/del-monte-french-style-fresh-cut-green-beans-14-5-oz/-/A-13204304">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Del Monte French Style Fresh Cut Green Beans 14.5 oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13204304?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $0.89
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $1.02
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Del Monte French Style Fresh Cut Green Bea...
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $10 gift card with $50 purchase
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13204304"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Del Monte French Style Fresh Cut Green Beans 14.5 oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="201976776" data-row="8-3">
<a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-dunkin-dark-ground-coffee-11-oz/-/A-13396911">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin' Donuts Dunkin' Dark Ground Coffee 11-oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13396911?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin' Donuts Dunkin' Dark Ground Coffee ...
      </p><!-- /.details--title -->
<div class="details--ratingSwatch">
<div class="ratings-block ">
<div class="ratings ratings-xs h-float-left">
<img aria-hidden="true" class="ratings-img" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-off.svg"/>
<div class="ratings-score" style="width:100%;">
<img alt="5 out of 5 stars" class="ratings-img" role="link" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-on.svg"/>
</div>
</div>
<span class="h-sr-only">1 reviews </span>
<span aria-hidden="true" class="ratings--count"> 1 </span>
<!-- /.ratings -->
</div>
<!-- /.ratings-block -->
</div>
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13396911"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin' Donuts Dunkin' Dark Ground Coffee 11-oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="300603337" data-row="9-4">
<a class="product--link js-redirect-to-pdp" href="/p/4-oz-haribo-fruit-chewy-candy/-/A-50245780">
<!-- call outs-->
<!--call outs-->
<img alt="Haribo Happy Hoppers Gummi Candy 4oz Bag" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/50245780?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          $1.00
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Haribo Happy Hoppers Gummi Candy 4oz Bag
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_50245780"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Haribo Happy Hoppers Gummi Candy 4oz Bag view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="300429849" data-row="10-4">
<a class="product--link js-redirect-to-pdp" href="/p/1-5-oz-russell-stover-milk-chocolate-cross/-/A-49144133">
<!-- call outs-->
<!--call outs-->
<img alt="1.5 oz Russell Stover Milk  Chocolate Cross" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/49144133?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          $1.00
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        1.5 oz Russell Stover Milk  Chocolate Cross
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_49144133"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="1.5 oz Russell Stover Milk  Chocolate Cross view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="201937980" data-row="11-4">
<a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-medium-roast-dunkin-decaf-ground-coffee-12-oz/-/A-13400772">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin' Donuts Medium Roast Dunkin' Decaf Ground Coffee 12oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13400772?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin' Donuts Medium Roast Dunkin' Decaf ...
      </p><!-- /.details--title -->
<div class="details--ratingSwatch">
<div class="ratings-block ">
<div class="ratings ratings-xs h-float-left">
<img aria-hidden="true" class="ratings-img" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-off.svg"/>
<div class="ratings-score" style="width:100%;">
<img alt="5 out of 5 stars" class="ratings-img" role="link" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-on.svg"/>
</div>
</div>
<span class="h-sr-only">1 reviews </span>
<span aria-hidden="true" class="ratings--count"> 1 </span>
<!-- /.ratings -->
</div>
<!-- /.ratings-block -->
</div>
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13400772"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin' Donuts Medium Roast Dunkin' Decaf Ground Coffee 12oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="206027755" data-row="12-5">
<a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-caramel-coffee-cake-ground-coffee-11-oz/-/A-14775093">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin' Donuts Caramel Coffee Cake Ground Coffee 11oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/14775093?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin' Donuts Caramel Coffee Cake Ground ...
      </p><!-- /.details--title -->
<div class="details--ratingSwatch">
<div class="ratings-block ">
<div class="ratings ratings-xs h-float-left">
<img aria-hidden="true" class="ratings-img" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-off.svg"/>
<div class="ratings-score" style="width:100%;">
<img alt="5 out of 5 stars" class="ratings-img" role="link" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-on.svg"/>
</div>
</div>
<span class="h-sr-only">2 reviews </span>
<span aria-hidden="true" class="ratings--count"> 2 </span>
<!-- /.ratings -->
</div>
<!-- /.ratings-block -->
</div>
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_14775093"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin' Donuts Caramel Coffee Cake Ground Coffee 11oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="300409851" data-row="13-5">
<a class="product--link js-redirect-to-pdp" href="/p/kisses-easter-milk-chocolate-filled-plastic-chick-64-oz/-/A-50053676">
<!-- call outs-->
<!--call outs-->
<img alt="Kisses Easter Milk Chocolate Filled Plastic Chick,  .64 oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/50053676?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $1.00
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $1.09
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Kisses Easter Milk Chocolate Filled Plasti...
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_50053676"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Kisses Easter Milk Chocolate Filled Plastic Chick,  .64 oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="300312680" data-row="14-5">
<a class="product--link js-redirect-to-pdp" href="/p/1-125-oz-peeps-marshmallow-marshmallows/-/A-49148855">
<!-- call outs-->
<!--call outs-->
<img alt="Peeps Yellow Marshmallow Bunnies 4 ct 1.125 oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/49148855?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          $1.00
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Peeps Yellow Marshmallow Bunnies 4 ct 1.12...
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_49148855"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Peeps Yellow Marshmallow Bunnies 4 ct 1.125 oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="205749947" data-row="15-6">
<a class="product--link js-redirect-to-pdp" href="/p/maruchan-ramen-chicken-noodle-soup-mix-2-25-oz/-/A-14568314">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Maruchan Ramen Chicken Noodle Soup Mix 2.25 oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/14568314?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          $0.29
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Maruchan Ramen Chicken Noodle Soup Mix 2.2...
      </p><!-- /.details--title -->
<div class="details--ratingSwatch">
<div class="ratings-block ">
<div class="ratings ratings-xs h-float-left">
<img aria-hidden="true" class="ratings-img" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-off.svg"/>
<div class="ratings-score" style="width:80%;">
<img alt="4 out of 5 stars" class="ratings-img" role="link" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-on.svg"/>
</div>
</div>
<span class="h-sr-only">1 reviews </span>
<span aria-hidden="true" class="ratings--count"> 1 </span>
<!-- /.ratings -->
</div>
<!-- /.ratings-block -->
</div>
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $10 gift card with $50 purchase
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_14568314"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Maruchan Ramen Chicken Noodle Soup Mix 2.25 oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="300496873" data-row="16-6">
<a class="product--link js-redirect-to-pdp" href="/p/1-2-oz-jelly-belly-apple-jelly-beans/-/A-49147898">
<!-- call outs-->
<!--call outs-->
<img alt="Jelly Belly Flip Top Box Kids Mix/Spring Mix 1.2oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/49147898?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          $1.00
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Jelly Belly Flip Top Box Kids Mix/Spring M...
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_49147898"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Jelly Belly Flip Top Box Kids Mix/Spring Mix 1.2oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="300441898" data-row="17-6">
<a class="product--link js-redirect-to-pdp" href="/p/party-favor-confetti-eggs/-/A-50219309">
<!-- call outs-->
<!--call outs-->
<img alt="Party Favor Confetti Eggs" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/50219309?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $2.09
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $2.49
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Party Favor Confetti Eggs
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_50219309"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Party Favor Confetti Eggs view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="206481712" data-row="18-7">
<a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-cinnamon-bun-11-oz/-/A-15351374">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin Donuts Cinnamon Bun 11oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/15351374?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin Donuts Cinnamon Bun 11oz
      </p><!-- /.details--title -->
<div class="details--ratingSwatch">
<div class="ratings-block ">
<div class="ratings ratings-xs h-float-left">
<img aria-hidden="true" class="ratings-img" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-off.svg"/>
<div class="ratings-score" style="width:100%;">
<img alt="5 out of 5 stars" class="ratings-img" role="link" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-on.svg"/>
</div>
</div>
<span class="h-sr-only">1 reviews </span>
<span aria-hidden="true" class="ratings--count"> 1 </span>
<!-- /.ratings -->
</div>
<!-- /.ratings-block -->
</div>
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_15351374"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin Donuts Cinnamon Bun 11oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="200349734" data-row="19-7">
<a class="product--link js-redirect-to-pdp" href="/p/starbucks-espresso-roast-whole-bean-12-oz/-/A-13302672">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Starbucks Espresso Roast Whole Bean 12oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13302672?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          $7.99
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Starbucks Espresso Roast Whole Bean 12oz
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $10 gift card with $50 purchase
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13302672"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Starbucks Espresso Roast Whole Bean 12oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="208966221" data-row="20-7">
<a class="product--link js-redirect-to-pdp" href="/p/m-m-s-milk-chocolate-gift-box-3-4-oz/-/A-18759966">
<!-- call outs-->
<!--call outs-->
<img alt="M&amp;M's Milk Chocolate Gift Box 3.4 oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/18759966?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          see store for price
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        M&amp;M's Milk Chocolate Gift Box 3.4 oz
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_18759966"></div>
<!--  OBGB message end -->
<div class="details--button">
<button class="btn is-disabled btn-sm">
               only in stores
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="206420618" data-row="21-8">
<a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-french-roast-11-oz/-/A-15251110">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin Donuts French Roast 11oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/15251110?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin Donuts French Roast 11oz
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_15251110"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin Donuts French Roast 11oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="300598823" data-row="22-8">
<a class="product--link js-redirect-to-pdp" href="/p/1-74-oz-pez-fruit-hard-candy/-/A-50246521">
<!-- call outs-->
<!--call outs-->
<img alt="PEZ Easter Blister Dispenser 1.74oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/50246521?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $1.66
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $1.99
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        PEZ Easter Blister Dispenser 1.74oz
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_50246521"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="PEZ Easter Blister Dispenser 1.74oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li><li class="product " data-id="206351943" data-row="23-8">
<a class="product--link js-redirect-to-pdp" href="/p/arm-hammer-baking-soda-1-lb/-/A-15133726">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Arm &amp; Hammer Baking Soda 1 LB" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/15133726?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          $0.79
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Arm &amp; Hammer Baking Soda 1 LB
      </p><!-- /.details--title -->
<div class="details--ratingSwatch">
<div class="ratings-block ">
<div class="ratings ratings-xs h-float-left">
<img aria-hidden="true" class="ratings-img" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-off.svg"/>
<div class="ratings-score" style="width:90%;">
<img alt="4.5 out of 5 stars" class="ratings-img" role="link" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-on.svg"/>
</div>
</div>
<span class="h-sr-only">19 reviews </span>
<span aria-hidden="true" class="ratings--count"> 19 </span>
<!-- /.ratings -->
</div>
<!-- /.ratings-block -->
</div>
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $10 gift card with $50 purchase
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_15133726"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Arm &amp; Hammer Baking Soda 1 LB view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
</li>
>>> for link in links:
	print(link.find('a').get_attribute('href'))

	
Traceback (most recent call last):
  File "<pyshell#29>", line 2, in <module>
    print(link.find('a').get_attribute('href'))
TypeError: 'NoneType' object is not callable
>>> links.find('a')
<a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-original-blend-medium-roast-whole-bean-coffee-12-oz/-/A-13400831">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin' Donuts Original Blend Medium Roast Whole Bean Coffee 12oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13400831?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin' Donuts Original Blend Medium Roast...
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13400831"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin' Donuts Original Blend Medium Roast Whole Bean Coffee 12oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
>>> links.findAll('a')
[<a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-original-blend-medium-roast-whole-bean-coffee-12-oz/-/A-13400831">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin' Donuts Original Blend Medium Roast Whole Bean Coffee 12oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13400831?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin' Donuts Original Blend Medium Roast...
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13400831"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin' Donuts Original Blend Medium Roast Whole Bean Coffee 12oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-medium-roast-original-blend-ground-coffee-12-oz/-/A-13399846">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin' Donuts Medium Roast Original Blend Ground Coffee 12oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13399846?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin' Donuts Medium Roast Original Blend...
      </p><!-- /.details--title -->
<div class="details--ratingSwatch">
<div class="ratings-block ">
<div class="ratings ratings-xs h-float-left">
<img aria-hidden="true" class="ratings-img" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-off.svg"/>
<div class="ratings-score" style="width:100%;">
<img alt="5 out of 5 stars" class="ratings-img" role="link" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-on.svg"/>
</div>
</div>
<span class="h-sr-only">5 reviews </span>
<span aria-hidden="true" class="ratings--count"> 5 </span>
<!-- /.ratings -->
</div>
<!-- /.ratings-block -->
</div>
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13399846"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin' Donuts Medium Roast Original Blend Ground Coffee 12oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-french-vanilla-flavored-ground-coffee-12-oz/-/A-13399847">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin' Donuts French Vanilla Flavored Ground Coffee 12oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13399847?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin' Donuts French Vanilla Flavored Gro...
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13399847"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin' Donuts French Vanilla Flavored Ground Coffee 12oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-hazelnut-ground-coffee-12-oz/-/A-13400186">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin' Donuts Hazelnut Ground Coffee 12oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13400186?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin' Donuts Hazelnut Ground Coffee 12oz
      </p><!-- /.details--title -->
<div class="details--ratingSwatch">
<div class="ratings-block ">
<div class="ratings ratings-xs h-float-left">
<img aria-hidden="true" class="ratings-img" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-off.svg"/>
<div class="ratings-score" style="width:100%;">
<img alt="5 out of 5 stars" class="ratings-img" role="link" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-on.svg"/>
</div>
</div>
<span class="h-sr-only">1 reviews </span>
<span aria-hidden="true" class="ratings--count"> 1 </span>
<!-- /.ratings -->
</div>
<!-- /.ratings-block -->
</div>
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13400186"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin' Donuts Hazelnut Ground Coffee 12oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/tic-tac-bunny-burst-1oz/-/A-50355453">
<!-- call outs-->
<!--call outs-->
<img alt="Tic Tac Bunny Burst 1oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/50355453?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $1.00
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $1.09
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Tic Tac Bunny Burst 1oz
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_50355453"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Tic Tac Bunny Burst 1oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/8-oz-candy-treasures-chocolates/-/A-50247436">
<!-- call outs-->
<!--call outs-->
<img alt="Minions Treasure Egg .8oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/50247436?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          $1.00
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Minions Treasure Egg .8oz
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_50247436"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Minions Treasure Egg .8oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-colombian-11oz/-/A-15351375">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin Donuts Colombian 11oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/15351375?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin Donuts Colombian 11oz
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_15351375"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin Donuts Colombian 11oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/del-monte-french-style-fresh-cut-green-beans-14-5-oz/-/A-13204304">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Del Monte French Style Fresh Cut Green Beans 14.5 oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13204304?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $0.89
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $1.02
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Del Monte French Style Fresh Cut Green Bea...
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $10 gift card with $50 purchase
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13204304"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Del Monte French Style Fresh Cut Green Beans 14.5 oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-dunkin-dark-ground-coffee-11-oz/-/A-13396911">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin' Donuts Dunkin' Dark Ground Coffee 11-oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13396911?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin' Donuts Dunkin' Dark Ground Coffee ...
      </p><!-- /.details--title -->
<div class="details--ratingSwatch">
<div class="ratings-block ">
<div class="ratings ratings-xs h-float-left">
<img aria-hidden="true" class="ratings-img" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-off.svg"/>
<div class="ratings-score" style="width:100%;">
<img alt="5 out of 5 stars" class="ratings-img" role="link" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-on.svg"/>
</div>
</div>
<span class="h-sr-only">1 reviews </span>
<span aria-hidden="true" class="ratings--count"> 1 </span>
<!-- /.ratings -->
</div>
<!-- /.ratings-block -->
</div>
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13396911"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin' Donuts Dunkin' Dark Ground Coffee 11-oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/4-oz-haribo-fruit-chewy-candy/-/A-50245780">
<!-- call outs-->
<!--call outs-->
<img alt="Haribo Happy Hoppers Gummi Candy 4oz Bag" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/50245780?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          $1.00
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Haribo Happy Hoppers Gummi Candy 4oz Bag
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_50245780"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Haribo Happy Hoppers Gummi Candy 4oz Bag view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/1-5-oz-russell-stover-milk-chocolate-cross/-/A-49144133">
<!-- call outs-->
<!--call outs-->
<img alt="1.5 oz Russell Stover Milk  Chocolate Cross" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/49144133?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          $1.00
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        1.5 oz Russell Stover Milk  Chocolate Cross
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_49144133"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="1.5 oz Russell Stover Milk  Chocolate Cross view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-medium-roast-dunkin-decaf-ground-coffee-12-oz/-/A-13400772">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin' Donuts Medium Roast Dunkin' Decaf Ground Coffee 12oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13400772?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin' Donuts Medium Roast Dunkin' Decaf ...
      </p><!-- /.details--title -->
<div class="details--ratingSwatch">
<div class="ratings-block ">
<div class="ratings ratings-xs h-float-left">
<img aria-hidden="true" class="ratings-img" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-off.svg"/>
<div class="ratings-score" style="width:100%;">
<img alt="5 out of 5 stars" class="ratings-img" role="link" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-on.svg"/>
</div>
</div>
<span class="h-sr-only">1 reviews </span>
<span aria-hidden="true" class="ratings--count"> 1 </span>
<!-- /.ratings -->
</div>
<!-- /.ratings-block -->
</div>
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13400772"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin' Donuts Medium Roast Dunkin' Decaf Ground Coffee 12oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-caramel-coffee-cake-ground-coffee-11-oz/-/A-14775093">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin' Donuts Caramel Coffee Cake Ground Coffee 11oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/14775093?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin' Donuts Caramel Coffee Cake Ground ...
      </p><!-- /.details--title -->
<div class="details--ratingSwatch">
<div class="ratings-block ">
<div class="ratings ratings-xs h-float-left">
<img aria-hidden="true" class="ratings-img" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-off.svg"/>
<div class="ratings-score" style="width:100%;">
<img alt="5 out of 5 stars" class="ratings-img" role="link" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-on.svg"/>
</div>
</div>
<span class="h-sr-only">2 reviews </span>
<span aria-hidden="true" class="ratings--count"> 2 </span>
<!-- /.ratings -->
</div>
<!-- /.ratings-block -->
</div>
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_14775093"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin' Donuts Caramel Coffee Cake Ground Coffee 11oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/kisses-easter-milk-chocolate-filled-plastic-chick-64-oz/-/A-50053676">
<!-- call outs-->
<!--call outs-->
<img alt="Kisses Easter Milk Chocolate Filled Plastic Chick,  .64 oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/50053676?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $1.00
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $1.09
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Kisses Easter Milk Chocolate Filled Plasti...
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_50053676"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Kisses Easter Milk Chocolate Filled Plastic Chick,  .64 oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/1-125-oz-peeps-marshmallow-marshmallows/-/A-49148855">
<!-- call outs-->
<!--call outs-->
<img alt="Peeps Yellow Marshmallow Bunnies 4 ct 1.125 oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/49148855?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          $1.00
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Peeps Yellow Marshmallow Bunnies 4 ct 1.12...
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_49148855"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Peeps Yellow Marshmallow Bunnies 4 ct 1.125 oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/maruchan-ramen-chicken-noodle-soup-mix-2-25-oz/-/A-14568314">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Maruchan Ramen Chicken Noodle Soup Mix 2.25 oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/14568314?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          $0.29
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Maruchan Ramen Chicken Noodle Soup Mix 2.2...
      </p><!-- /.details--title -->
<div class="details--ratingSwatch">
<div class="ratings-block ">
<div class="ratings ratings-xs h-float-left">
<img aria-hidden="true" class="ratings-img" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-off.svg"/>
<div class="ratings-score" style="width:80%;">
<img alt="4 out of 5 stars" class="ratings-img" role="link" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-on.svg"/>
</div>
</div>
<span class="h-sr-only">1 reviews </span>
<span aria-hidden="true" class="ratings--count"> 1 </span>
<!-- /.ratings -->
</div>
<!-- /.ratings-block -->
</div>
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $10 gift card with $50 purchase
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_14568314"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Maruchan Ramen Chicken Noodle Soup Mix 2.25 oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/1-2-oz-jelly-belly-apple-jelly-beans/-/A-49147898">
<!-- call outs-->
<!--call outs-->
<img alt="Jelly Belly Flip Top Box Kids Mix/Spring Mix 1.2oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/49147898?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          $1.00
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Jelly Belly Flip Top Box Kids Mix/Spring M...
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_49147898"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Jelly Belly Flip Top Box Kids Mix/Spring Mix 1.2oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/party-favor-confetti-eggs/-/A-50219309">
<!-- call outs-->
<!--call outs-->
<img alt="Party Favor Confetti Eggs" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/50219309?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $2.09
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $2.49
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Party Favor Confetti Eggs
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_50219309"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Party Favor Confetti Eggs view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-cinnamon-bun-11-oz/-/A-15351374">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin Donuts Cinnamon Bun 11oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/15351374?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin Donuts Cinnamon Bun 11oz
      </p><!-- /.details--title -->
<div class="details--ratingSwatch">
<div class="ratings-block ">
<div class="ratings ratings-xs h-float-left">
<img aria-hidden="true" class="ratings-img" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-off.svg"/>
<div class="ratings-score" style="width:100%;">
<img alt="5 out of 5 stars" class="ratings-img" role="link" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-on.svg"/>
</div>
</div>
<span class="h-sr-only">1 reviews </span>
<span aria-hidden="true" class="ratings--count"> 1 </span>
<!-- /.ratings -->
</div>
<!-- /.ratings-block -->
</div>
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_15351374"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin Donuts Cinnamon Bun 11oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/starbucks-espresso-roast-whole-bean-12-oz/-/A-13302672">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Starbucks Espresso Roast Whole Bean 12oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13302672?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          $7.99
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Starbucks Espresso Roast Whole Bean 12oz
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $10 gift card with $50 purchase
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13302672"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Starbucks Espresso Roast Whole Bean 12oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/m-m-s-milk-chocolate-gift-box-3-4-oz/-/A-18759966">
<!-- call outs-->
<!--call outs-->
<img alt="M&amp;M's Milk Chocolate Gift Box 3.4 oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/18759966?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          see store for price
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        M&amp;M's Milk Chocolate Gift Box 3.4 oz
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_18759966"></div>
<!--  OBGB message end -->
<div class="details--button">
<button class="btn is-disabled btn-sm">
               only in stores
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-french-roast-11-oz/-/A-15251110">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin Donuts French Roast 11oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/15251110?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin Donuts French Roast 11oz
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_15251110"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin Donuts French Roast 11oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/1-74-oz-pez-fruit-hard-candy/-/A-50246521">
<!-- call outs-->
<!--call outs-->
<img alt="PEZ Easter Blister Dispenser 1.74oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/50246521?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $1.66
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $1.99
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        PEZ Easter Blister Dispenser 1.74oz
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_50246521"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="PEZ Easter Blister Dispenser 1.74oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>, <a class="product--link js-redirect-to-pdp" href="/p/arm-hammer-baking-soda-1-lb/-/A-15133726">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Arm &amp; Hammer Baking Soda 1 LB" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/15133726?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span>
          $0.79
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Arm &amp; Hammer Baking Soda 1 LB
      </p><!-- /.details--title -->
<div class="details--ratingSwatch">
<div class="ratings-block ">
<div class="ratings ratings-xs h-float-left">
<img aria-hidden="true" class="ratings-img" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-off.svg"/>
<div class="ratings-score" style="width:90%;">
<img alt="4.5 out of 5 stars" class="ratings-img" role="link" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/images/icons/star-rating-on.svg"/>
</div>
</div>
<span class="h-sr-only">19 reviews </span>
<span aria-hidden="true" class="ratings--count"> 19 </span>
<!-- /.ratings -->
</div>
<!-- /.ratings-block -->
</div>
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $10 gift card with $50 purchase
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_15133726"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Arm &amp; Hammer Baking Soda 1 LB view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>]
>>> hrefs = links.findAll('a')
>>> for h in hrefs:
	print(h.get_attribute('href'))

	
Traceback (most recent call last):
  File "<pyshell#35>", line 2, in <module>
    print(h.get_attribute('href'))
TypeError: 'NoneType' object is not callable
>>> len(hrefs)
24
>>> hrefs[0]
<a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-original-blend-medium-roast-whole-bean-coffee-12-oz/-/A-13400831">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin' Donuts Original Blend Medium Roast Whole Bean Coffee 12oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13400831?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin' Donuts Original Blend Medium Roast...
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13400831"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin' Donuts Original Blend Medium Roast Whole Bean Coffee 12oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
>>> 
=============================== RESTART: Shell ===============================
>>> from selenium import webdriver
>>> from selenium.webdriver.common.keys import Keys
>>> from bs4 import BeautifulSoup, SoupStrainer
>>> BASE_URL = 'http://m.target.com/c/grocery-essentials/-/N-5xt1a'
>>> d = webdriver.Firefox()
>>> d.get(BASE_URL)
>>> soup = BeautifulSoup(d.page_source, "html.parser", parse_only=SoupStrainer('div', {'id':'plp '}))
>>> anchors = soup.findAll('a', href=True)
>>> len(anchors)
0
>>> len(soup)
0
>>> soup = BeautifulSoup(d.page_source, "html.parser", parse_only=SoupStrainer('div', {'id':'plp'}))
>>> anchors = soup.findAll('a', href=True)
>>> len(anchors)
719
>>> anchors[0]
<a class="product--link js-redirect-to-pdp" href="/p/dunkin-donuts-original-blend-medium-roast-whole-bean-coffee-12-oz/-/A-13400831">
<!-- call outs-->
<div class="details--ribbon">
</div>
<!--call outs-->
<img alt="Dunkin' Donuts Original Blend Medium Roast Whole Bean Coffee 12oz" aria-level="3" class="product--image" role="heading" src="//scene7.targetimg1.com/is/image/Target/13400831?wid=290&amp;hei=290&amp;qlt=80&amp;fmt=pjpeg"/>
<div class="details details-plp">
<div class="price">
<span class="h-text-red">
          $5.99
        </span>
<span class="price--saveStory h-text-lowercase">
          Reg: $7.59
        </span>
</div><!-- /.price -->
<p class="details--title">
        
        Dunkin' Donuts Original Blend Medium Roast...
      </p><!-- /.details--title -->
<!-- /.details--ratingSwatch -->
<div class="details--messaging">
<!--promo messages-->
<ul class="h-text-red">
<li>
                      $5 gift card with purchase of 3
                    </li>
</ul>
<!--subscription messages-->
<!--subscription messages-->
</div>
<!--details messaging-->
<!--  limited qty start -->
<!--  limited qty end -->
<!--  OBGB message start -->
<div id="obgbMessage_13400831"></div>
<!--  OBGB message end -->
<div class="details--button">
<button aria-label="Dunkin' Donuts Original Blend Medium Roast Whole Bean Coffee 12oz view details" class="btn btn-primary btn-sm">
                view details
            </button>
<!-- /.btn-primary -->
<div class="h-float-right h-standardSpacingLeft" data-behavior="popover" data-html="true" data-original-title="" data-placement="top" data-template='&lt;div style="width:100%" class="popover popover-gray" role="tooltip"&gt;&lt;div class="arrow"&gt;&lt;/div&gt;&lt;h3 class="popover-title"&gt;&lt;/h3&gt;&lt;div class="popover-content"&gt;&lt;/div&gt;&lt;/div&gt;' id="popover-demo">
<button class="btn btn-sm btn-icon-only btn-round btn-favorites js-tgtcrush js-favorites"><i class=" icon icon-heart-outline">love this item</i></button>
</div>
</div><!-- /.details--button -->
</div>
<!-- /.details -->
</a>
>>> anchors[0].get('href')
'/p/dunkin-donuts-original-blend-medium-roast-whole-bean-coffee-12-oz/-/A-13400831'
>>> anchors[719].get('href')
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    anchors[719].get('href')
IndexError: list index out of range
>>> anchors[718].get('href')
'javascript:void(0)'
>>> import re
>>> anchors = soup.findAll('a', href=re.compile("\/"))
>>> len(anchors)
28
>>> domain = "http://m.target.com"
>>> d.get(domain + anchors[0])
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    d.get(domain + anchors[0])
TypeError: Can't convert 'Tag' object to str implicitly
>>> d.get(domain + anchors[0].get('href))
			      
SyntaxError: EOL while scanning string literal
>>> d.get(domain + anchors[0].get('href'))
>>> d.quit()
>>> d = webdriver.Firefox()
>>> d.get(domain + anchors[0].get('href'))
>>> d.quit()
>>> from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
>>> server_url = "http://%s:%s/wd/hub" % ('127.0.0.1', '4444')
>>> dc = DesiredCapabilities.HTMLUNIT
>>> d = webdriver.Remote(server_url, dc)
>>> d.get(domain + anchors[0].get('href'))
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    d.get(domain + anchors[0].get('href'))
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 213, in get
    self.execute(Command.GET, {'url': url})
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 201, in execute
    self.error_handler.check_response(response)
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/errorhandler.py", line 181, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: TypeError: Cannot set property "_l" of null to "function () {
    var js = this.createElement("script");
    if (dom) {
        this.domain = dom;
    }
    js.id = "boomr-if-as";
    js.src = "//c.go-mpulse.net/boomerang/" + "WEG9J-MZCPB-GYJ8Z-24VAX-JQP4W";
    BOOMR_lstart = new Date().getTime();
    this.body.appendChild(js);
}" (script in http://www.target.com/p/dunkin-donuts-original-blend-medium-roast-whole-bean-coffee-12oz/-/A-13400831?force-full-site=1&full-site-confirm from (33, 10) to (35, 11)#34)
Screenshot: available via screen
Stacktrace:
    at net.sourceforge.htmlunit.corejs.javascript.ScriptRuntime.constructError (ScriptRuntime.java:3935)
    at net.sourceforge.htmlunit.corejs.javascript.ScriptRuntime.constructError (ScriptRuntime.java:3919)
    at net.sourceforge.htmlunit.corejs.javascript.ScriptRuntime.typeError (ScriptRuntime.java:3944)
    at net.sourceforge.htmlunit.corejs.javascript.ScriptRuntime.typeError3 (ScriptRuntime.java:3966)
    at net.sourceforge.htmlunit.corejs.javascript.ScriptRuntime.undefWriteError (ScriptRuntime.java:3983)
    at net.sourceforge.htmlunit.corejs.javascript.ScriptRuntime.setObjectProp (ScriptRuntime.java:1667)
    at net.sourceforge.htmlunit.corejs.javascript.Interpreter.interpretLoop (Interpreter.java:1255)
    at net.sourceforge.htmlunit.corejs.javascript.Interpreter.interpret (Interpreter.java:798)
    at net.sourceforge.htmlunit.corejs.javascript.InterpretedFunction.call (InterpretedFunction.java:105)
    at net.sourceforge.htmlunit.corejs.javascript.ContextFactory.doTopCall (ContextFactory.java:411)
    at com.gargoylesoftware.htmlunit.javascript.HtmlUnitContextFactory.doTopCall (HtmlUnitContextFactory.java:310)
    at net.sourceforge.htmlunit.corejs.javascript.ScriptRuntime.doTopCall (ScriptRuntime.java:3286)
    at net.sourceforge.htmlunit.corejs.javascript.InterpretedFunction.exec (InterpretedFunction.java:115)
    at com.gargoylesoftware.htmlunit.javascript.JavaScriptEngine$3.doRun (JavaScriptEngine.java:738)
    at com.gargoylesoftware.htmlunit.javascript.JavaScriptEngine$HtmlUnitContextAction.run (JavaScriptEngine.java:850)
    at net.sourceforge.htmlunit.corejs.javascript.Context.call (Context.java:628)
    at net.sourceforge.htmlunit.corejs.javascript.ContextFactory.call (ContextFactory.java:513)
    at com.gargoylesoftware.htmlunit.javascript.JavaScriptEngine.execute (JavaScriptEngine.java:747)
    at com.gargoylesoftware.htmlunit.javascript.JavaScriptEngine.execute (JavaScriptEngine.java:722)
    at com.gargoylesoftware.htmlunit.html.HtmlPage.executeJavaScriptIfPossible (HtmlPage.java:945)
    at com.gargoylesoftware.htmlunit.html.HtmlScript.executeInlineScriptIfNeeded (HtmlScript.java:351)
    at com.gargoylesoftware.htmlunit.html.HtmlScript.executeScriptIfNeeded (HtmlScript.java:411)
    at com.gargoylesoftware.htmlunit.html.HtmlScript$3.execute (HtmlScript.java:270)
    at com.gargoylesoftware.htmlunit.html.HtmlScript.onAllChildrenAddedToPage (HtmlScript.java:290)
    at com.gargoylesoftware.htmlunit.html.HTMLParser$HtmlUnitDOMBuilder.endElement (HTMLParser.java:800)
    at org.apache.xerces.parsers.AbstractSAXParser.endElement (None:-1)
    at com.gargoylesoftware.htmlunit.html.HTMLParser$HtmlUnitDOMBuilder.endElement (HTMLParser.java:757)
    at org.cyberneko.html.HTMLTagBalancer.callEndElement (HTMLTagBalancer.java:1170)
    at org.cyberneko.html.HTMLTagBalancer.endElement (HTMLTagBalancer.java:1072)
    at org.cyberneko.html.filters.DefaultFilter.endElement (DefaultFilter.java:206)
    at org.cyberneko.html.filters.NamespaceBinder.endElement (NamespaceBinder.java:330)
    at org.cyberneko.html.HTMLScanner$ContentScanner.scanEndElement (HTMLScanner.java:3126)
    at org.cyberneko.html.HTMLScanner$ContentScanner.scan (HTMLScanner.java:2093)
    at org.cyberneko.html.HTMLScanner.scanDocument (HTMLScanner.java:920)
    at org.cyberneko.html.HTMLConfiguration.parse (HTMLConfiguration.java:499)
    at org.cyberneko.html.HTMLConfiguration.parse (HTMLConfiguration.java:452)
    at org.apache.xerces.parsers.XMLParser.parse (None:-1)
    at com.gargoylesoftware.htmlunit.html.HTMLParser$HtmlUnitDOMBuilder.parse (HTMLParser.java:1040)
    at com.gargoylesoftware.htmlunit.html.HTMLParser.parse (HTMLParser.java:253)
    at com.gargoylesoftware.htmlunit.html.HTMLParser.parseHtml (HTMLParser.java:199)
    at com.gargoylesoftware.htmlunit.DefaultPageCreator.createHtmlPage (DefaultPageCreator.java:272)
    at com.gargoylesoftware.htmlunit.DefaultPageCreator.createPage (DefaultPageCreator.java:160)
    at com.gargoylesoftware.htmlunit.WebClient.loadWebResponseInto (WebClient.java:476)
    at com.gargoylesoftware.htmlunit.WebClient.getPage (WebClient.java:350)
    at com.gargoylesoftware.htmlunit.WebClient.getPage (WebClient.java:415)
    at org.openqa.selenium.htmlunit.HtmlUnitDriver.get (HtmlUnitDriver.java:541)
    at org.openqa.selenium.htmlunit.HtmlUnitDriver.get (HtmlUnitDriver.java:530)
    at sun.reflect.NativeMethodAccessorImpl.invoke0 (NativeMethodAccessorImpl.java:-2)
    at sun.reflect.NativeMethodAccessorImpl.invoke (NativeMethodAccessorImpl.java:57)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke (DelegatingMethodAccessorImpl.java:43)
    at java.lang.reflect.Method.invoke (Method.java:606)
    at org.openqa.selenium.support.events.EventFiringWebDriver$2.invoke (EventFiringWebDriver.java:103)
    at com.sun.proxy.$Proxy12.get (None:-1)
    at org.openqa.selenium.support.events.EventFiringWebDriver.get (EventFiringWebDriver.java:163)
    at org.openqa.selenium.remote.server.handler.ChangeUrl.call (ChangeUrl.java:40)
    at org.openqa.selenium.remote.server.handler.ChangeUrl.call (ChangeUrl.java:1)
    at java.util.concurrent.FutureTask.run (FutureTask.java:262)
    at org.openqa.selenium.remote.server.DefaultSession$1.run (DefaultSession.java:176)
    at java.util.concurrent.ThreadPoolExecutor.runWorker (ThreadPoolExecutor.java:1145)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run (ThreadPoolExecutor.java:615)
    at java.lang.Thread.run (Thread.java:745)
>>> d.quit()
>>> d = webdriver.Firefox()
>>> d.get(domain + anchors[0].get('href'))
>>> import requests
>>> headers = {'User-Agent': 'Mozilla/5.0'}
>>> s = requests.session()s = requests.se
SyntaxError: invalid syntax
>>> s = requests.session()
>>> r = s.get(domain + anchors[0].get('href'), headers=headers)
>>> r.status_code
200
>>> r.content
b'<!DOCTYPE html>\n<html lang="en" class="no-js">\n  <head>\n\t\t<meta charset="utf-8" />\n<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n<meta name="viewport" content="width=device-width, maximum-scale=1, minimum-scale=1, user-scalable=no" />\n<link id="favicon" rel="shortcut icon" type="image/png" href="//static.targetimg1.com/mobile-config/favicon.ico" />\n<link rel="apple-touch-icon-precomposed" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/apple-touch-icon-precomposed.png" />\n<link rel="icon" type="image/png" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/apple-touch-icon-precomposed.png" sizes="192x192">\n<link rel="icon" type="image/png" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/favicon-96x96.png" sizes="96x96">\t\n<link rel="icon" type="image/png" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/favicon-32x32.png" sizes="32x32">\n<link rel="icon" type="image/png" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/favicon-16x16.png" sizes="16x16">\n<meta name="msapplication-TileColor" content="#cc0000">\n<meta name="msapplication-TileImage" content="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/android-chrome-192x192.png">\n<meta name="format-detection" content="telephone=no" />\n<script>document.createElement("picture");</script>\n<script>\n\t(function(){if(window.BOOMR&&window.BOOMR.version){return}var dom,doc,where,iframe=document.createElement(\'iframe\');iframe.src="javascript:false";iframe.title="";iframe.role="presentation";(iframe.frameElement||iframe).style.cssText="width:0;height:0;border:0;display:none;";where=document.getElementsByTagName(\'script\')[0];where.parentNode.insertBefore(iframe,where);try{doc=iframe.contentWindow.document}catch(e){dom=document.domain;iframe.src="javascript:var d=document.open();d.domain=\'"+dom+"\';void(0);";doc=iframe.contentWindow.document}doc.open()._l=function(){var js=this.createElement("script");if(dom)this.domain=dom;js.id="boomr-if-as";js.src=\'//c.go-mpulse.net/boomerang/KQTS5-4NBTD-EYGLE-64UYR-S5892\';BOOMR_lstart=new Date().getTime();this.body.appendChild(js)};doc.write(\'<body onload="document._l();">\');doc.close()})();\n\t!function(a){if(a.XMLHttpRequest&&(new XMLHttpRequest).addEventListener){var b,c=document.createElement("A"),d=XMLHttpRequest,e=[],f=["uninitialized","open","responseStart","domInteractive","responseEnd"];a.BOOMR=a.BOOMR||{},BOOMR.xhr={stop:function(c){return b=c,a.XMLHttpRequest=d,delete BOOMR.xhr,setTimeout(function(){e=[]}),e}};var g=function(){try{if("performance"in a)return function(){return Math.round(performance.now()+performance.timing.navigationStart)}}catch(b){}return Date.now||function(){return(new Date).getTime()}}();a.XMLHttpRequest=function(){var h=new d,i=h.open;return h.open=function(d,j,k){function l(){if(!n.timing.loadEventEnd){if(n.timing.loadEventEnd=g(),"performance"in a&&a.performance&&"function"==typeof a.performance.getEntriesByName){var c=a.performance.getEntriesByName(n.url),d=c&&c.length&&c[c.length-1];if(d){var f=a.performance.timing.navigationStart;0!==d.responseEnd&&(n.timing.responseEnd=Math.round(f+d.responseEnd)),0!==d.responseStart&&(n.timing.responseStart=Math.round(f+d.responseStart)),0!==d.startTime&&(n.timing.requestStart=Math.round(f+d.startTime))}}b?b(n):e.push(n)}}function m(a,b){h.addEventListener(a,function(){"readystatechange"===a?(n.timing[f[h.readyState]]=g(),4===h.readyState&&l()):(n.status=void 0===b?h.status:b,l())},!1)}c.href=j;var n={timing:{},url:c.href,method:d};k===!0?m("readystatechange"):n.synchronous=!0,m("load"),m("timeout",-1001),m("error",-998),m("abort",-999);try{i.apply(h,arguments);var o=h.send;h.send=function(){n.timing.requestStart=g(),o.apply(h,arguments)}}catch(p){n.status=-997,l()}},h}}}(window);\n</script>\n<script type="text/javascript">\n\n  var configJSON = {\n\tpreUrlMobileConstructor\t\t: "http://m.target.com/",\n\tsecurePreUrlMobileConstructor\t: "https://m-secure.target.com/",\n\tpreUrlTabletConstructor\t\t: "http://www.target.com/",\n\tsecurePreUrlTabletConstructor\t: "https://www-secure.target.com/",\n\tapiServer\t\t\t\t: {\n\t\tdomain : "http://api.target.com",\n\t\tsecuredomain : "https://secure-api.target.com",\n\t\taccesskey :"eb2551e4accc14f38cc42d32fbc2b2ea",\n\t\tsecureaccesskey : "SxR9X7XoWw2fW1PBWfXswf3q5NeIuGAu"\n\t},\n\tsearchURL\t\t\t\t: "http://tws.target.com/searchservice/item/search_results/v2/by_keyword?",\n    searchURLV2             : "http://tws.target.com/searchservice/item/search_results/v2/by_keyword?",\n    brandURL                : "http://tws.target.com/searchservice/item/brand_results/v2/by_brand?",\n    itemPriceURL            : "http://dcd-prc.target.com/item/price/v1/{tcins}?key=8cb043b2dace9afc0680e6bae5cd316f",\n\tbrowseURL\t\t\t\t: "http://tws.target.com/productservice/services/item_service/v1/by_itemid?",\n\tbrowseSecureURL\t\t\t: "https://tws-secure.target.com/productservice/services/item_service/v1/by_itemid?",\n\tbazaarVoiceURL\t\t\t: "display.ugc.bazaarvoice.com/static/targetcom/uimod/en_US/bvapi.js",\n\tdvmChannelId\t\t\t: "mtarget",\n\tpersonalizationEngineURL: "https://prz-secure.target.com/recommendations/v1",\n\tthreatMerticsURL\t\t: "https://img9.target.com",\n    redcardPromoEnabled\t\t: true,\n    useServiceController\t: false,\n\twcsTimeoutIntervel\t\t: 600,\n\tcartTimeoutIntervel\t\t: 600000,\n\tsearchTimeoutIntervel\t: 10000,\n\tbrowseTimeoutIntervel\t: 10000,\n\tglobalAjaxTimeout       : 30000,\n\tglobalATPServiceTimeout : 5000,\n\tenvMpulse\t\t\t\t: "prod",\n\tmpulseUrl\t\t\t\t: "//c.go-mpulse.net/boomerang/KQTS5-4NBTD-EYGLE-64UYR-S5892",\n\tslingshotPreviewURL\t\t: "https://content-preview-secure.target.com/content-preview",\n\tslingshotURL\t\t\t: "https://content-delivery-secure.target.com/content-publish",\n\tslingshotURL_http       : "http://content-delivery.target.com/content-publish",\n\tslingshotCategoryId\t\t: "/slingshot/category/2222222",\n\tmobileDomain\t\t\t: "http://m.target.com",\n\tmobileSecureDomain\t\t: "https://m-secure.target.com",\n\ttabletDVMChannelId\t\t: "target",\n\tsubscriptionModURL\t\t: "https://subscriptions-secure.target.com",\n\tseoApiURL\t\t\t\t: "https://content-delivery-secure.target.com/content-publish/taxonomy/v1/seo?",\n\tseoApiURL_http\t\t\t: "http://content-delivery.target.com/content-publish/taxonomy/v1/seo?",\n\thlURL\t\t\t\t\t: "http://www.hlserve.com/delivery/api",\n\thlKey\t\t\t\t\t: "764937a9-7afb-4cf1-8631-d8a5edca8f36",\n\thlId\t\t\t\t\t: "[CS]v1|2AC0BE5905079201-6000010B000429CD[CE]",\n\tsfCert\t\t\t\t\t: "",\n\tsfCID\t\t\t\t\t: "",\n\tsfURL\t\t\t\t\t: "",\n\tchkURL\t\t\t\t\t: "https://checkout-api-secure.target.com",\n\tchkWalletAPIURL\t\t\t: "https://checkout-api-secure.target.com",\n\tgamURL\t\t\t\t\t: "https://gam-api-secure.target.com",\n\tgamKey\t\t\t\t\t: "OGFiNjJhOWMtMWI4Ni00ZDJhLTlkNGItMTUwODJiYzNmMDA0OjNpSnRQamVNdkk=",\n\tmodAjaxTimeout\t\t\t: "20000",\n\ttwsDomain\t\t\t\t: "http://tws.target.com",\n\ttwsSecureDomain\t\t\t: "https://tws-secure.target.com",\n\ttreeCategoryUrl\t\t\t: "http://m.target.com/TreeCategory",\n\tsecureTreeCategoryUrl\t: "https://m-secure.target.com/TreeCategory",\n\tcategoriesXml           : "http://img1.targetimg1.com/wcsstore/marketing/com/mobile/en/xml/products/categories.xml",\n\timageIncludes\t\t\t: "/wcsstore/marketing/com/mobile/includes",\n\tbreadCrumbUrl           : "http://tws.target.com/searchservice/catalog/bread_crumb/v2/by_category_id?",\n\tfireflySchemaId         : "1184",\n\tfireflyTopic            : "firefly_estore_eventstream",\n\tfireflyHost             : "firefly.target.com",\n\tsecEnabled\t\t\t\t: "true",\n\tapiNonPCIDomain\t\t\t: "https://api.target.com",\n\tsubscriptionUrl         : "/wcsstore/marketing/com/mobile/en/html/spot/target-subscriptions_1.html",\n\tsapphireUrl: "http://sapphire.edge-csp1-e1-npe.target.com/sapphire/runtime/api/v1/qualified-experiments?",\n  typeaheadUrl: "http://typeahead.target.com/",\n  typeaheadSecureUrl: "https://typeahead-secure.target.com/",\n\tshapeJs: "//static.targetimg1.com/ssx/ssx.mod.js"\n  };\n\n\n var mobileDomain = "http://m.target.com";\n var mobileSecureDomain = "https://m-secure.target.com";\n var tabletDomain = "http://www.target.com";\n var tabletSecureDomain = "https://www-secure.target.com";\n\n  if(tabletDomain.indexOf(window.location.hostname.replace(/origin.{3}-/,"")) != -1 || tabletSecureDomain.indexOf(window.location.hostname.replace(/origin.{3}-/,"")) != -1 ){\n\t  configJSON["preUrlConstructor"] = configJSON["preUrlTabletConstructor"];\n\t  configJSON["securePreUrlConstructor"] = configJSON["securePreUrlTabletConstructor"];\n  }else{\n\t  configJSON["preUrlConstructor"] = configJSON["preUrlMobileConstructor"];\n\t  configJSON["securePreUrlConstructor"] = configJSON["securePreUrlMobileConstructor"];\n  }\n\n  // setting secure/nonsecure image server path\n  if (window.location.protocol =="https:") {\n    configJSON["imageServerDomain"] = "https://img3-secure.targetimg3.com";\n  } else {\n    configJSON["imageServerDomain"] = "http://img3.targetimg3.com";\n  }\n\n</script>\n<script type="text/javascript">\n  \n  var isSecure = (window.location.protocol !== "http:");\n  var noSeoCall = (window.location.pathname.indexOf(\'target-crush\') !== -1 || window.location.pathname.indexOf(\'mcategories\') !== -1);\n  var seoHttpRequestPromise = null;\n  var seoHttpRequest = null;\n  var seoReadyStateHandler = null;\n  var dateSearchParam = \'\';\n  var isSapphireEnabled = false;\n  // global function to getVisitorId\n  var getVisitorIdCookie = function getVisitorIdCookie() {\n    var name = "visitorId=";\n    var ca = document.cookie.split(\';\');\n    for(var i=0; i<ca.length; i++) {\n        var c = ca[i];\n        while (c.charAt(0)===\' \') c = c.substring(1);\n        if (c.indexOf(name) === 0) return c.substring(name.length,c.length);\n    }\n    return "";\n  };\n\n  // firefly vistorId changes starts here\n  (function(){\n\tfunction getByteArrayFromInteger(integer, desiredBytes) {\n        var byteValue, byteArray, index;\n\n        byteArray = [];\n\n        for (index = 0; index < desiredBytes; index++) {\n            byteValue = integer & 0xff;\n            byteArray.push(byteValue);\n            integer = (integer - byteValue) / 256;\n        }\n\n        return byteArray.reverse();\n    }\n\n\tfunction getRandomNumber(min, max) {\n        return Math.floor(Math.random() * (max - min)) + min;\n    }\n\n\tfunction getHexStringFromByte (byte) {\n        var hexCharArray, hexString;\n\n        hexCharArray = [\'0\', \'1\', \'2\', \'3\', \'4\', \'5\', \'6\', \'7\', \'8\', \'9\', \'A\', \'B\', \'C\', \'D\', \'E\', \'F\'];\n        hexString = hexCharArray[(byte >> 4) & 0x0f] + hexCharArray[byte & 0x0f];\n\n        return hexString;\n    }\n\n\tfunction getHexStringFromByteArray(byteArray) {\n        return byteArray.map(getHexStringFromByte, this).join("");\n    }\n\n    function create48BitTimeByteArray() {\n        return getByteArrayFromInteger(new Date(), 6);\n    }\n\n    function create64BitRandomByteArray() {\n        var randomValue, sixteenBitRandomValue, fortyEightBitRandomValue;\n\n        randomValue = getRandomNumber(0, 9000000000000000);\n        sixteenBitRandomValue = getByteArrayFromInteger(randomValue, 2);\n\n        randomValue = getRandomNumber(0, 9000000000000000);\n        fortyEightBitRandomValue = getByteArrayFromInteger(randomValue, 6);\n\n        return sixteenBitRandomValue.concat(fortyEightBitRandomValue);\n    }\n\n\tfunction createVisitorId(source) {\n        var byteArray, decorator, randomByteArray, source, timeByteArray;\n\n        timeByteArray = create48BitTimeByteArray();\n        randomByteArray = create64BitRandomByteArray();\n\n        byteArray = timeByteArray.concat([1, source]).concat(randomByteArray);\n\n        return getHexStringFromByteArray(byteArray);\n\t}\n\n\tfunction isMobile() {\n\t    mobile = ["Android", "webOS", "iPhone", "iPod", "BlackBerry", "Windows Phone", "Opera Mini", "IEMobile"];\n\t    for (var i = 0; i <= mobile.length - 1; i++) {\n\t        var mobilex = navigator.userAgent.indexOf(mobile[i]);\n\t        if (mobilex != -1) {\n\t            return true;\n\t            break;\n\t        }\n\t    }\n\t    return false;\n\t }\n\n\t function isPad() {\n\t     pad = ["iPad"];\n\t     for (var i = 0; i <= pad.length - 1; i++) {\n\t         var mobilex = navigator.userAgent.indexOf(pad[i]);\n\t         if (mobilex != -1) {\n\t             return true;\n\t             break;\n\t         }\n\t     }\n\t     return false;\n\t  }\n\n\t  function isDesktop() {\n\t      return !navigator.userAgent.match(/Android|BlackBerry|iPhone|iPad|iPod|Opera Mini|IEMobile|NokiaBrowser|Silk|mobile|tablet/i);\n\t  }\n\n\t  function getVisitorId() {\n          var source;\n\n          if (isDesktop()) {\n              source = 1;\n          } else if (isMobile()) {\n              source = 2;\n          } else if (isPad()) {\n              source = 3;\n          } else {\n              source = 0;\n          }\n\n          return createVisitorId(source);\n\t  }\n\n\t  function createVisitorIdCookie(visitorId) {\n\t\t  var d = new Date();\n\t\t  d.setTime(d.getTime() + 31536000000);\n\t\t  var expires = "expires="+d.toUTCString();\n\t\t  return "visitorId=" + visitorId + ";" + expires + ";domain=.target.com;path=/";\n\t  }\n\n\t  if (getVisitorIdCookie() === "") {\n\t\t  var session, sessionId, visitorId;\n\t\t  visitorId = getVisitorId();\n\t\t  document.cookie = createVisitorIdCookie(visitorId);\n\t\t  \n\t\t  // init firefly session\n\t\t  sessionId = (Math.floor(Math.random() * (9007199254740960 - 11184840)) + 11184840).toString(16);\n\t\t  session = {\n\t\t  \t\'newGuest\': \'true\',\n\t\t  \t\'sessionHash\': sessionId\n\t\t  };\n\t\t  document.cookie = "ffsession=" + JSON.stringify(session) + ";domain=.target.com;path=/";\n\t  }\n  })();\n\n  if (!isSecure && !noSeoCall) {\n    (function(){\n    var seoApi = (true && window.location.protocol == "http:") ? "http://content-delivery.target.com/content-publish/taxonomy/v1/seo?" : "https://content-delivery-secure.target.com/content-publish/taxonomy/v1/seo?";\n    var appPath = window.location.pathname.replace(\'home\',\'\') + ((false)?"": window.location.search)\n        seoApi = seoApi + \'url=\' + encodeURIComponent(appPath) + \'&children=true&breadcrumbs=true\';\n\n        if (false) {\n          // below changes are to give preference to effective date url parameter\n          var regex = new RegExp("[\\\\?&]" + \'effective_date\' + "=([^&#]*)");\n          var results = regex.exec(location.search);\n          var effectiveDate = results == null ? "" : decodeURIComponent(results[1].replace(/\\+/g, " "));\n          if(effectiveDate){\n            dateSearchParam = \'&effective_date=\' + effectiveDate;\n            document.getElementById(\'previewDate\').value = effectiveDate.replace(\'Z\',\'\');\n          }else{\n            dateSearchParam = \'&effective_date=\' + document.getElementById(\'previewDate\').value + \'Z\';\n          }\n          if(dateSearchParam){\n              seoApi = seoApi + dateSearchParam;\n          }\n\n        }\n        seoHttpRequest = new XMLHttpRequest();\n        seoHttpRequest.onreadystatechange = function(){\n          if(seoHttpRequest.readyState == 4 && seoReadyStateHandler){\n            seoReadyStateHandler();\n          }\n        };\n        seoHttpRequest.open("GET", seoApi, true);\n        seoHttpRequest.send();\n      })();\n    }\n</script>\n<meta name="google-site-verification" content="1rmXsZRZGP3uOmdg4qvP1A0zVaAKoxvrWtBavkX0LCE" />\n    <link  href="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/css/patlab/global.css" media="all" rel="stylesheet" type="text/css" />\n\n\t<script id="domains" type="text/javascript">\n\n\t\tif(tabletDomain.indexOf(window.location.hostname.replace(/origin.{3}-/,"")) != -1 || tabletSecureDomain.indexOf(window.location.hostname.replace(/origin.{3}-/,"")) != -1 ){\n\t\tdomain = tabletDomain;\n\t\tsecure_domain = tabletSecureDomain;\n\t\t}else{\n\t\tdomain = mobileDomain;\n\t\tsecure_domain = mobileSecureDomain;\n\t\t}\n\n\t\timg_domain = "http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01";\n\t\timageSerURL="http://img3.targetimg3.com/wcsstore/marketing";\n\t\twcs_server="http://www-int.att.target.com/wcs/resources";\n\t\twcs_secure_server="https://www-int.att.target.com/wcs/resources";\n\t\t\n\t\t\t\tisSecure = false;\n\t\t\t</script>\n\n\n\n    <script>\n\t\tvar FF_GEO_FEATURE = \'ON\';\n\t\tvar FF_PRG_2  = \'true\';\n\t\tvar defualtPickupWindow = \'false\';\n\t\tvar sfsenable = (\'true\'===\'true\');\n\t\tvar rushDelByAddress = \'on\';\n\t\tvar IS_REPROMISE_ENABLE =  \'true\';\n\t\tvar USE_ORDER_ITEM_ID =  \'true\';\n\t\tvar formFactor=\'tablet\'||"phone";\n\t\tvar useV1OrderDetails=\'false\';\n\t\tvar showCreateACcount=\'true\';\n\t\tvar STORE_RESULT_LIMIT=\'20\';\n\t\tvar prodAvailCount = \'10\';\n\t\tvar redCard_new = \'true\';\n\t\tvar plugins_mod = \'http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/plugins.mod.js\';\n\t\tvar mod_0 = \'http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/browse.mod.js\';\n\t\tvar mod_1 = \'http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/non-browse.mod.js\';\n\t</script>\n\t\n    <script type="text/javascript" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/plugins.mod.js" ></script>\n\t\t\t<script type="text/javascript" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/browse.mod.js" ></script>\n\t\t<script type="text/javascript" src="//nexus.ensighten.com/target/tcom-ui-prod/Bootstrap.js"></script>\n\t\t<script>\n\t  var scr = document.createElement("script");\n\t  scr.src = configJSON.imageServerDomain + configJSON.imageIncludes + \'/foresee2/foresee-trigger.js\';\n    scr.async = true;\n\t  document.getElementsByTagName("head")[0].appendChild(scr);\n\t</script>\n<script id="dvm" type="text/javascript">\n\tvar gptadslots=[];\n\tvar googletag = googletag || {};\n\tgoogletag.cmd = googletag.cmd || [];\n\t(function(){ var gads = document.createElement(\'script\');\n\t\tgads.async = true; gads.type = \'text/javascript\';\n\t\tvar useSSL = \'https:\' == document.location.protocol;\n\t\tgads.src = (useSSL ? \'https:\' : \'http:\') + \'//www.googletagservices.com/tag/js/gpt.js\';\n\t\tvar node = document.getElementsByTagName(\'script\')[0];\n\t\tnode.parentNode.insertBefore(gads, node);\n\t})();\n</script>\n<script type="text/javascript">\n      if ((/iphone|ipod|ipad.*os /gi).test(navigator.appVersion)) {\n        window.onpageshow = function(evt) {\n          // If persisted then it is in the page cache, force a reload of the page.\n          if (evt.persisted) {\n    \t    window.location.reload();\n          }\n        };\n      }\n</script>\n</head>\n  <body id="home" ontouchstart="">\n  <div tabindex="-1" class="TGTloading" style="display: none">\n    <div class="loading-container">\n      <div class="loading-spinner"></div>\n      <div class="loading-message"></div>\n    </div>\n  </div>\n\t<div id="viewport">\n\t\t\t\t<div id="pageStart"></div>\n\t\t\t</div>\n\t\t<script id="page-meta" type="application/json">\n\t\t{\n  "img_domain" : "http://img3.targetimg3.com",\n  "img_secure_domain" : "https://img3-secure.targetimg3.com",\n  "generated_time" : "Thu Mar 24 02:32:56 EDT 2016",\n  "build_number" : "716-03162016-01",\n  "page_name" : "mProduct",\n  "view_def" : {\n    "header" : [ {\n      "path" : "http://img3.targetimg3.com/wcsstore/marketing/com/mobile/includes/template/header_v2.html",\n      "position" : 1\n    } ],\n    "nav" : [ {\n      "path" : "http://img3.targetimg3.com/wcsstore/marketing/com/mobile/includes/template/header_v2.html",\n      "position" : 1\n    } ],\n    "main_body" : [ {\n      "path" : "mCommonProductPage",\n      "position" : 2,\n      "attribute" : [ {\n        "name" : "rrpcStaticLink",\n        "value" : "/spot/terms/return-policy"\n      }, {\n        "name" : "isNewCheckOut",\n        "value" : "Y"\n      } ]\n    } ],\n    "footer" : [ {\n      "path" : "http://img3.targetimg3.com/wcsstore/marketing/com/mobile/includes/template/header_v2.html",\n      "position" : 1\n    } ]\n  },\n  "page_grid" : "<div id=\\"header\\" class=\\"l-sticky\\" data-name=\\"views/tablet/common/header.view\\"></div><div id=\\"nav\\" data-name=\\"views/tablet/common/nav.view\\"></div><div id=\\"pdp\\" class=\\"main-content l-container-fixed\\" data-page=\\"product details page\\" data-name=\\"views/tablet/browse/pdp.view\\" itemscope=\\"\\" itemtype=\\"http://schema.org/Product\\"></div><div id=\\"fiats\\" data-name=\\"views/tablet/common/fiats.view\\"></div><div id=\\"footer\\" class=\\"footer\\" data-name=\\"views/tablet/common/footer.view\\"></div>",\n  "tracking" : {\n    "attribute" : [ {\n      "name" : "s.prop1",\n      "value" : "product details"\n    }, {\n      "name" : "s.prop4",\n      "value" : "mobile"\n    } ]\n  },\n  "device_info" : {\n    "attribute" : [ {\n      "name" : "deviceType"\n    }, {\n      "name" : "formFactor",\n      "value" : "tablet"\n    } ]\n  },\n  "meta_tags" : {\n    "attribute" : [ {\n      "name" : "title",\n      "value" : "16849119 at Mobile Target"\n    }, {\n      "name" : "description",\n      "value" : "Shop for 16849119 at Mobile Target"\n    }, {\n      "name" : "keywords",\n      "value" : "16849119, 16849119 online, Mobile Target"\n    } ]\n  },\n  "banners" : [ {\n    "id" : "13186697",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/tent-6-person-13186697.html"\n  }, {\n    "id" : "13186698",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/tent-9-person-13186698.html"\n  }, {\n    "id" : "14432134",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/20130414_kate.html"\n  } ],\n  "title" : "",\n  "processing_time" : 73,\n  "jsfiles" : [ {\n    "jsfile" : "http://img3.targetimg3.com/wcsstore/marketing/com/mobile/js/template/productDetail_minified.js"\n  } ],\n  "cssfiles" : [ ],\n  "feature" : {\n    "FORESEE" : "false",\n    "TEA_LEAF" : "false",\n    "SECURE_TEA_LEAF" : "false",\n    "FF_ENABLE" : "true",\n    "BV_ENABLED" : "true",\n    "TRACKER" : "false",\n    "SFS_ENABLE" : "true",\n    "FF_PRG_2" : "true",\n    "REGISTRY_RESET_FLAG" : "false",\n    "TNL_COOKIE" : "false",\n    "IS_REPROMISE_ENABLE" : "true",\n    "SHOW_MODAL_BOX" : "true",\n    "ONE_PAGE_CHECKOUT_ENABLE" : "true",\n    "ONE_PAGE_CHECKOUT_ENABLE_FOR_IPAD" : "true",\n    "REVIEW_PAGE_ENABLE_CRTE_ACCT" : "false",\n    "IS_DUMMY_THANK_YOU" : "true",\n    "SEARCH_OPT_FLAG" : "false",\n    "USE_ORDER_ITEM_ID" : "true",\n    "DVM" : "true",\n    "SHIPPING_LIMITED_OFFER" : "false",\n    "PREVIEW_ENABLE" : "false",\n    "ORDER_DETAIL_V1" : "false",\n    "SHOW_CREATE_ACCOUNT" : "true",\n    "SUBSCRIPTION_ENABLED" : "true",\n    "STS_ENABLE" : "true",\n    "SUBS_SHIP_PROMO_MODALMSG" : "true",\n    "PRZ_ENABLE" : "true",\n    "CHKOUT_EXP_ELIGBLE" : "true",\n    "PEAK_HOURS_FLAG" : "false",\n    "THREAT_METRICS_ENABLE" : "true",\n    "ORD_PRZ_ENABLE" : "true",\n    "REDCARD_NEW" : "true",\n    "SLINGSHOT_ENABLED" : "true",\n    "EXPERIAN_EMAIL_SERVICE" : "true",\n    "CART_GET_DEALS" : "false",\n    "APPLE_GIFTCARD_MERCH_CLASS" : "true",\n    "SLING_SHOT_PREVIEW_ENABLE" : "false",\n    "SLINGSHOT_SERVER_CONTROLE" : "false",\n    "IS_CARDINAL" : "false",\n    "ADVANCE_ORDER_CROSSOVER" : "false",\n    "ADVANCE_ORDER_ENABLE" : "true",\n    "MOBILE_ONLY_CHANNEL" : "true",\n    "DELIVERY_DISPLAY_PRICE_ENABLE" : "false",\n    "SITESKIN_ENABLED" : "false",\n    "SUBSCRIPTION_MOD_ENDPOINT" : "true",\n    "SUBSCRIPTION_UI_DISABLED" : "false",\n    "NONSECURE_SIGNIN_OVERLAY_ENABLED" : "true",\n    "ADAPIVE_GC" : "true",\n    "FULL_ADAPTIVE" : "true",\n    "PLP_TO_PDP_PARTIAL_LOAD" : "false",\n    "LIMITED_QTY_ENABLED" : "false",\n    "OBGB_ENABLED" : "true",\n    "ENABLE_TRACKJS" : "false",\n    "REORDER_TWO_TAP_OVERLAY" : "true",\n    "DELIVERY_EMAIL_VALIDATION" : "false",\n    "PAGE_SCRIPT_ENABLE" : "false",\n    "STORE_LIMITED_QTY_ENABLED" : "true",\n    "REPROMISE_OPTIMIZATION_ENABLE" : "true",\n    "WXS_LIMITED_QTY_ENABLED" : "true",\n    "AISLEINFOSERVICE_ENABLE" : "true",\n    "TAG_PAGE_ENABLED" : "true",\n    "CATEGORY_SLINGSHOT_ENABLED" : "true",\n    "SLINGSHOT_HTTP_ENABLED" : "true",\n    "STORE_LOCATOR_SEO_URL" : "true",\n    "CART_PROMO_CODE_ENTRY" : "true",\n    "FF_V3_TO_ATP_ENABLE" : "true",\n    "CRUSH_ACTIVE" : "true",\n    "REFRESH_JOB" : "false",\n    "BROWSE_BY_CATEGORIES_SLINGSHOT" : "true",\n    "FIREFLY_ENABLED" : "true",\n    "REPOPULATE_GEO_COOKIE" : "true",\n    "DEFAULT_TABLET_VIEW" : "true",\n    "PDP_DYNAMIC_PRICING" : "true",\n    "GET_THIS_PHONE" : "true",\n    "GIFT_REGISTRY_RENAME" : "true",\n    "CRUSH_FEED_CURATION" : "true",\n    "EMPTY_CART_DVM_FLAG" : "true",\n    "ENABLE_FORESEE" : "true",\n    "IS_VIEWCART_OPTIMIZED" : "true",\n    "PAYMENT_SERVICES_ENABLED" : "true",\n    "GIFTCARD_ACTIVATION_MSG_ENABLE" : "false",\n    "SUB_RECO" : "false",\n    "PROMO_INJECTION_ENABLED" : "false",\n    "SECURITY_FIX_ENABLED" : "true",\n    "EXPRESS_CHECKOUT" : "true",\n    "OBGB_MSG_ON_LISTING_PAGES" : "true",\n    "FGC_FIX_ENABLE" : "false",\n    "SFS_BACKORDER" : "false",\n    "SHOW_ORDER_OVERLAY" : "true",\n    "USE_MOD_ORDERS" : "false",\n    "PHARMACY_INTERSTITIAL" : "true",\n    "ENABLE_WRITE_REVIEW" : "true",\n    "ENABLE_CRITICAL_REVIEW" : "true",\n    "DISABLE_MOBILE_GC" : "true",\n    "SUBSCRIPTION_FLYOUT" : "true",\n    "SEARCH_INSTEAD_FOR" : "false",\n    "DID_YOU_MEAN" : "false",\n    "ATC_RECOMMANDATIONS" : "false",\n    "SAPPHIRE" : "false",\n    "STORE_LOCATOR_ACCORDION_FIX" : "true",\n    "GAM_REPROMISE_FLYOUT" : "true",\n    "SSX_ENABLED" : "false",\n    "EnableSFL" : "true",\n    "FF_GEO_FEATURE" : "ON",\n    "DEFAULT_PICKUP_WINDOW" : "4",\n    "RELATED_CATEGORY" : "Y",\n    "CATEGORY_FEATURE_BRAND" : "Y",\n    "CATEGORY_GOOGLE_ADS" : "Y",\n    "CATEGORY_DVM_ADS" : "Y",\n    "DVM_CHANNLE_ID" : "mtarget",\n    "TABLET_DVM_CHANNLE_ID" : "target",\n    "SEARCH_OPT_RESP_GROUP" : "VariationSummary,Items",\n    "RUSH_DELIVERY_RADIUS" : "10",\n    "STORE_FINDER" : "100",\n    "RUSH_DEL_BY_ADDR" : "on",\n    "AVAILABILITY_SERVICE_PROD_COUNT" : "10",\n    "STORE_RESULT_LIMIT" : "20",\n    "THREAT_METRICS_ORG_ID" : "9p00aymw",\n    "SLINGSHOT_CATG_ID" : "/slingshot/category/2222222",\n    "FREE_SHIPPING_THRESHHOLD_VALUE" : "25",\n    "AO_MAX_STORES" : "5",\n    "ORD_HISTORY_DAY_LIMIT" : "1",\n    "ORD_HISTORY_COUNT_LIMIT" : "100",\n    "AO_STORES_RADIUS" : "25",\n    "GAM_DASH_ORDERS_LIMIT_COUNT" : "3",\n    "HOOK_LOGIC_KEY" : "764937a9-7afb-4cf1-8631-d8a5edca8f36",\n    "HOOK_LOGIC_ID" : "[CS]v1|2AC0BE5905079201-6000010B000429CD[CE]",\n    "TRACKJS_APPID" : "mobileweb",\n    "TRACKJS_TOKEN" : "913e59b71ca34b21aa95bc55121a0871",\n    "STORE_LIMITED_QTY" : "5",\n    "EVENT_TYPE" : "star",\n    "EVENT_STORES" : "4,61,64,90,93,199,215,221,230,246,301,320,346,348,351,359,361,617,627,636,676,686,687,755,766,769,794,810,818,822,824,827,830,844,861,870,885,911,935,937,938,942,969,992,995,1010,1018,1021,1025,1029,1034,1043,1056,1058,1092,1102,1107,1139,1140,1150,1153,1163,1166,1182,1191,1207,1224,1238,1244,1249,1252,1254,1257,1261,1266,1268,1275,1285,1306,1338,1339,1347,1350,1351,1354,1355,1357,1363,1364,1367,1368,1370,1376,1377,1384,1391,1397,1408,1409,1427,1431,1439,1443,1445,1449,1453,1455,1473,1476,1478,1481,1483,1501,1502,1505,1506,1510,1518,1541,1751,1755,1756,1767,1768,1774,1783,1787,1795,1797,1799,1806,1820,1821,1822,1856,1858,1869,1874,1883,1895,1903,1912,1916,1921,1930,1932,1934,1944,1954,1961,1965,1981,2014,2019,2022,2031,2034,2035,2036,2051,2093,2101,2105,2106,2108,2124,2129,2138,2170,2176,2189,2190,2205,2208,2210,2227,2244,2266,2271,2303,2313,2322,2338,2339,2348,2350,2356,2360,2371,2372,2373,2403,2410,2429,2473,2532,2542,2572,2682,2737,2757,2760,2764,2767,2771,2824,2843",\n    "CRUSH_URL_PROD" : "https://gnc-secure.target.com/guestpreference",\n    "FEED_URL_PROD" : "https://prz-secure.target.com/recommendations/v1?",\n    "MOD_INTEG_BUILD_NUMBER" : "12345",\n    "CRUSH_FEED_MAX" : "96",\n    "ITUNES_MERCH_CLASS" : "PREPAID CARDS, ENTERTAINMENT CARDS, ITUNES, DIGITAL CONTENT, VERIZON CONTRACT, BATTERIES",\n    "INVALID_CALLOUTS" : "testCallOut",\n    "GET_THIS_PHONEURL" : "https://mobile.target.com/web/controller/landing.php?",\n    "DLP_PARAMS" : "[\\"AFID\\",\\"CPNG\\",\\"KID\\",\\"LID\\",\\"LNM\\",\\"MT\\",\\"N\\",\\"gclid\\",\\"ref\\",\\"adgroup\\",\\"network\\",\\"device\\",\\"querystring\\",\\"location\\",\\"gclsrc\\",\\"emseq\\",\\"link\\",\\"tp\\"]",\n    "DYNAMIC_PROMO_VAL" : "TGTA39R9",\n    "PRIVACY_UPDATED_DATE" : "2015-10-26",\n    "ATP_SERVICE_PAYLOAD_MAX_PRODUCTS" : "20",\n    "GIFTCARD_PURCHASED_TODAY_ACTIVATION_24HOURS" : "If you purchased a Target GiftCard on December 20, your gift card will be activated on December 21.",\n    "MERCH_SUBCLASS_ARRAY" : "[{\\"DPCI\\":\\"255-02\\",\\"content\\":\\"atnt\\",\\"corpId\\":\\"596\\"},{\\"DPCI\\":\\"255-04\\",\\"content\\":\\"verizon\\",\\"corpId\\":\\"660\\"},{\\"DPCI\\":\\"255-08\\",\\"content\\":\\"sprint\\",\\"corpId\\":\\"545\\"},{\\"DPCI\\":\\"255-14\\",\\"content\\":\\"iphones\\",\\"corpId\\":\\"731\\"}]",\n    "ORD_HISTORY_RECENT_LIMIT" : "30",\n    "ORD_HISTORY_ALL_LIMIT" : "365",\n    "SERVICE_CALL_DATA_TYPE" : "jsonp",\n    "WHITE_LIST_MERCH_CONTENT" : "merchandizingSlot1"\n  },\n  "datacenter" : "SCS"\n}</script>\n  </body>\n</html>\n\n'
>>> soup2 = BeautifulSoup(d.page_source, "html.parser", parse_only=SoupStrainer('div', {'id':'pdpMainContainer'}))
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    soup2 = BeautifulSoup(d.page_source, "html.parser", parse_only=SoupStrainer('div', {'id':'pdpMainContainer'}))
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 464, in page_source
    return self.execute(Command.GET_PAGE_SOURCE)['value']
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py", line 199, in execute
    response = self.command_executor.execute(driver_command, params)
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/remote_connection.py", line 395, in execute
    return self._request(command_info[0], url, body=data)
  File "/home/ramakrishna/anaconda3/lib/python3.5/site-packages/selenium/webdriver/remote/remote_connection.py", line 425, in _request
    self._conn.request(method, parsed_url.path, body, headers)
  File "/home/ramakrishna/anaconda3/lib/python3.5/http/client.py", line 1083, in request
    self._send_request(method, url, body, headers)
  File "/home/ramakrishna/anaconda3/lib/python3.5/http/client.py", line 1128, in _send_request
    self.endheaders(body)
  File "/home/ramakrishna/anaconda3/lib/python3.5/http/client.py", line 1079, in endheaders
    self._send_output(message_body)
  File "/home/ramakrishna/anaconda3/lib/python3.5/http/client.py", line 911, in _send_output
    self.send(msg)
  File "/home/ramakrishna/anaconda3/lib/python3.5/http/client.py", line 854, in send
    self.connect()
  File "/home/ramakrishna/anaconda3/lib/python3.5/http/client.py", line 826, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "/home/ramakrishna/anaconda3/lib/python3.5/socket.py", line 711, in create_connection
    raise err
  File "/home/ramakrishna/anaconda3/lib/python3.5/socket.py", line 702, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [Errno 111] Connection refused
>>> b'<!DOCTYPE html>\n<html lang="en" class="no-js">\n  <head>\n\t\t<meta charset="utf-8" />\n<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n<meta name="viewport" content="width=device-width, maximum-scale=1, minimum-scale=1, user-scalable=no" />\n<link id="favicon" rel="shortcut icon" type="image/png" href="//static.targetimg1.com/mobile-config/favicon.ico" />\n<link rel="apple-touch-icon-precomposed" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/apple-touch-icon-precomposed.png" />\n<link rel="icon" type="image/png" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/apple-touch-icon-precomposed.png" sizes="192x192">\n<link rel="icon" type="image/png" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/favicon-96x96.png" sizes="96x96">\t\n<link rel="icon" type="image/png" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/favicon-32x32.png" sizes="32x32">\n<link rel="icon" type="image/png" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/favicon-16x16.png" sizes="16x16">\n<meta name="msapplication-TileColor" content="#cc0000">\n<meta name="msapplication-TileImage" content="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/android-chrome-192x192.png">\n<meta name="format-detection" content="telephone=no" />\n<script>document.createElement("picture");</script>\n<script>\n\t(function(){if(window.BOOMR&&window.BOOMR.version){return}var dom,doc,where,iframe=document.createElement(\'iframe\');iframe.src="javascript:false";iframe.title="";iframe.role="presentation";(iframe.frameElement||iframe).style.cssText="width:0;height:0;border:0;display:none;";where=document.getElementsByTagName(\'script\')[0];where.parentNode.insertBefore(iframe,where);try{doc=iframe.contentWindow.document}catch(e){dom=document.domain;iframe.src="javascript:var d=document.open();d.domain=\'"+dom+"\';void(0);";doc=iframe.contentWindow.document}doc.open()._l=function(){var js=this.createElement("script");if(dom)this.domain=dom;js.id="boomr-if-as";js.src=\'//c.go-mpulse.net/boomerang/KQTS5-4NBTD-EYGLE-64UYR-S5892\';BOOMR_lstart=new Date().getTime();this.body.appendChild(js)};doc.write(\'<body onload="document._l();">\');doc.close()})();\n\t!function(a){if(a.XMLHttpRequest&&(new XMLHttpRequest).addEventListener){var b,c=document.createElement("A"),d=XMLHttpRequest,e=[],f=["uninitialized","open","responseStart","domInteractive","responseEnd"];a.BOOMR=a.BOOMR||{},BOOMR.xhr={stop:function(c){return b=c,a.XMLHttpRequest=d,delete BOOMR.xhr,setTimeout(function(){e=[]}),e}};var g=function(){try{if("performance"in a)return function(){return Math.round(performance.now()+performance.timing.navigationStart)}}catch(b){}return Date.now||function(){return(new Date).getTime()}}();a.XMLHttpRequest=function(){var h=new d,i=h.open;return h.open=function(d,j,k){function l(){if(!n.timing.loadEventEnd){if(n.timing.loadEventEnd=g(),"performance"in a&&a.performance&&"function"==typeof a.performance.getEntriesByName){var c=a.performance.getEntriesByName(n.url),d=c&&c.length&&c[c.length-1];if(d){var f=a.performance.timing.navigationStart;0!==d.responseEnd&&(n.timing.responseEnd=Math.round(f+d.responseEnd)),0!==d.responseStart&&(n.timing.responseStart=Math.round(f+d.responseStart)),0!==d.startTime&&(n.timing.requestStart=Math.round(f+d.startTime))}}b?b(n):e.push(n)}}function m(a,b){h.addEventListener(a,function(){"readystatechange"===a?(n.timing[f[h.readyState]]=g(),4===h.readyState&&l()):(n.status=void 0===b?h.status:b,l())},!1)}c.href=j;var n={timing:{},url:c.href,method:d};k===!0?m("readystatechange"):n.synchronous=!0,m("load"),m("timeout",-1001),m("error",-998),m("abort",-999);try{i.apply(h,arguments);var o=h.send;h.send=function(){n.timing.requestStart=g(),o.apply(h,arguments)}}catch(p){n.status=-997,l()}},h}}}(window);\n</script>\n<script type="text/javascript">\n\n  var configJSON = {\n\tpreUrlMobileConstructor\t\t: "http://m.target.com/",\n\tsecurePreUrlMobileConstructor\t: "https://m-secure.target.com/",\n\tpreUrlTabletConstructor\t\t: "http://www.target.com/",\n\tsecurePreUrlTabletConstructor\t: "https://www-secure.target.com/",\n\tapiServer\t\t\t\t: {\n\t\tdomain : "http://api.target.com",\n\t\tsecuredomain : "https://secure-api.target.com",\n\t\taccesskey :"eb2551e4accc14f38cc42d32fbc2b2ea",\n\t\tsecureaccesskey : "SxR9X7XoWw2fW1PBWfXswf3q5NeIuGAu"\n\t},\n\tsearchURL\t\t\t\t: "http://tws.target.com/searchservice/item/search_results/v2/by_keyword?",\n    searchURLV2             : "http://tws.target.com/searchservice/item/search_results/v2/by_keyword?",\n    brandURL                : "http://tws.target.com/searchservice/item/brand_results/v2/by_brand?",\n    itemPriceURL            : "http://dcd-prc.target.com/item/price/v1/{tcins}?key=8cb043b2dace9afc0680e6bae5cd316f",\n\tbrowseURL\t\t\t\t: "http://tws.target.com/productservice/services/item_service/v1/by_itemid?",\n\tbrowseSecureURL\t\t\t: "https://tws-secure.target.com/productservice/services/item_service/v1/by_itemid?",\n\tbazaarVoiceURL\t\t\t: "display.ugc.bazaarvoice.com/static/targetcom/uimod/en_US/bvapi.js",\n\tdvmChannelId\t\t\t: "mtarget",\n\tpersonalizationEngineURL: "https://prz-secure.target.com/recommendations/v1",\n\tthreatMerticsURL\t\t: "https://img9.target.com",\n    redcardPromoEnabled\t\t: true,\n    useServiceController\t: false,\n\twcsTimeoutIntervel\t\t: 600,\n\tcartTimeoutIntervel\t\t: 600000,\n\tsearchTimeoutIntervel\t: 10000,\n\tbrowseTimeoutIntervel\t: 10000,\n\tglobalAjaxTimeout       : 30000,\n\tglobalATPServiceTimeout : 5000,\n\tenvMpulse\t\t\t\t: "prod",\n\tmpulseUrl\t\t\t\t: "//c.go-mpulse.net/boomerang/KQTS5-4NBTD-EYGLE-64UYR-S5892",\n\tslingshotPreviewURL\t\t: "https://content-preview-secure.target.com/content-preview",\n\tslingshotURL\t\t\t: "https://content-delivery-secure.target.com/content-publish",\n\tslingshotURL_http       : "http://content-delivery.target.com/content-publish",\n\tslingshotCategoryId\t\t: "/slingshot/category/2222222",\n\tmobileDomain\t\t\t: "http://m.target.com",\n\tmobileSecureDomain\t\t: "https://m-secure.target.com",\n\ttabletDVMChannelId\t\t: "target",\n\tsubscriptionModURL\t\t: "https://subscriptions-secure.target.com",\n\tseoApiURL\t\t\t\t: "https://content-delivery-secure.target.com/content-publish/taxonomy/v1/seo?",\n\tseoApiURL_http\t\t\t: "http://content-delivery.target.com/content-publish/taxonomy/v1/seo?",\n\thlURL\t\t\t\t\t: "http://www.hlserve.com/delivery/api",\n\thlKey\t\t\t\t\t: "764937a9-7afb-4cf1-8631-d8a5edca8f36",\n\thlId\t\t\t\t\t: "[CS]v1|2AC0BE5905079201-6000010B000429CD[CE]",\n\tsfCert\t\t\t\t\t: "",\n\tsfCID\t\t\t\t\t: "",\n\tsfURL\t\t\t\t\t: "",\n\tchkURL\t\t\t\t\t: "https://checkout-api-secure.target.com",\n\tchkWalletAPIURL\t\t\t: "https://checkout-api-secure.target.com",\n\tgamURL\t\t\t\t\t: "https://gam-api-secure.target.com",\n\tgamKey\t\t\t\t\t: "OGFiNjJhOWMtMWI4Ni00ZDJhLTlkNGItMTUwODJiYzNmMDA0OjNpSnRQamVNdkk=",\n\tmodAjaxTimeout\t\t\t: "20000",\n\ttwsDomain\t\t\t\t: "http://tws.target.com",\n\ttwsSecureDomain\t\t\t: "https://tws-secure.target.com",\n\ttreeCategoryUrl\t\t\t: "http://m.target.com/TreeCategory",\n\tsecureTreeCategoryUrl\t: "https://m-secure.target.com/TreeCategory",\n\tcategoriesXml           : "http://img1.targetimg1.com/wcsstore/marketing/com/mobile/en/xml/products/categories.xml",\n\timageIncludes\t\t\t: "/wcsstore/marketing/com/mobile/includes",\n\tbreadCrumbUrl           : "http://tws.target.com/searchservice/catalog/bread_crumb/v2/by_category_id?",\n\tfireflySchemaId         : "1184",\n\tfireflyTopic            : "firefly_estore_eventstream",\n\tfireflyHost             : "firefly.target.com",\n\tsecEnabled\t\t\t\t: "true",\n\tapiNonPCIDomain\t\t\t: "https://api.target.com",\n\tsubscriptionUrl         : "/wcsstore/marketing/com/mobile/en/html/spot/target-subscriptions_1.html",\n\tsapphireUrl: "http://sapphire.edge-csp1-e1-npe.target.com/sapphire/runtime/api/v1/qualified-experiments?",\n  typeaheadUrl: "http://typeahead.target.com/",\n  typeaheadSecureUrl: "https://typeahead-secure.target.com/",\n\tshapeJs: "//static.targetimg1.com/ssx/ssx.mod.js"\n  };\n\n\n var mobileDomain = "http://m.target.com";\n var mobileSecureDomain = "https://m-secure.target.com";\n var tabletDomain = "http://www.target.com";\n var tabletSecureDomain = "https://www-secure.target.com";\n\n  if(tabletDomain.indexOf(window.location.hostname.replace(/origin.{3}-/,"")) != -1 || tabletSecureDomain.indexOf(window.location.hostname.replace(/origin.{3}-/,"")) != -1 ){\n\t  configJSON["preUrlConstructor"] = configJSON["preUrlTabletConstructor"];\n\t  configJSON["securePreUrlConstructor"] = configJSON["securePreUrlTabletConstructor"];\n  }else{\n\t  configJSON["preUrlConstructor"] = configJSON["preUrlMobileConstructor"];\n\t  configJSON["securePreUrlConstructor"] = configJSON["securePreUrlMobileConstructor"];\n  }\n\n  // setting secure/nonsecure image server path\n  if (window.location.protocol =="https:") {\n    configJSON["imageServerDomain"] = "https://img3-secure.targetimg3.com";\n  } else {\n    configJSON["imageServerDomain"] = "http://img3.targetimg3.com";\n  }\n\n</script>\n<script type="text/javascript">\n  \n  var isSecure = (window.location.protocol !== "http:");\n  var noSeoCall = (window.location.pathname.indexOf(\'target-crush\') !== -1 || window.location.pathname.indexOf(\'mcategories\') !== -1);\n  var seoHttpRequestPromise = null;\n  var seoHttpRequest = null;\n  var seoReadyStateHandler = null;\n  var dateSearchParam = \'\';\n  var isSapphireEnabled = false;\n  // global function to getVisitorId\n  var getVisitorIdCookie = function getVisitorIdCookie() {\n    var name = "visitorId=";\n    var ca = document.cookie.split(\';\');\n    for(var i=0; i<ca.length; i++) {\n        var c = ca[i];\n        while (c.charAt(0)===\' \') c = c.substring(1);\n        if (c.indexOf(name) === 0) return c.substring(name.length,c.length);\n    }\n    return "";\n  };\n\n  // firefly vistorId changes starts here\n  (function(){\n\tfunction getByteArrayFromInteger(integer, desiredBytes) {\n        var byteValue, byteArray, index;\n\n        byteArray = [];\n\n        for (index = 0; index < desiredBytes; index++) {\n            byteValue = integer & 0xff;\n            byteArray.push(byteValue);\n            integer = (integer - byteValue) / 256;\n        }\n\n        return byteArray.reverse();\n    }\n\n\tfunction getRandomNumber(min, max) {\n        return Math.floor(Math.random() * (max - min)) + min;\n    }\n\n\tfunction getHexStringFromByte (byte) {\n        var hexCharArray, hexString;\n\n        hexCharArray = [\'0\', \'1\', \'2\', \'3\', \'4\', \'5\', \'6\', \'7\', \'8\', \'9\', \'A\', \'B\', \'C\', \'D\', \'E\', \'F\'];\n        hexString = hexCharArray[(byte >> 4) & 0x0f] + hexCharArray[byte & 0x0f];\n\n        return hexString;\n    }\n\n\tfunction getHexStringFromByteArray(byteArray) {\n        return byteArray.map(getHexStringFromByte, this).join("");\n    }\n\n    function create48BitTimeByteArray() {\n        return getByteArrayFromInteger(new Date(), 6);\n    }\n\n    function create64BitRandomByteArray() {\n        var randomValue, sixteenBitRandomValue, fortyEightBitRandomValue;\n\n        randomValue = getRandomNumber(0, 9000000000000000);\n        sixteenBitRandomValue = getByteArrayFromInteger(randomValue, 2);\n\n        randomValue = getRandomNumber(0, 9000000000000000);\n        fortyEightBitRandomValue = getByteArrayFromInteger(randomValue, 6);\n\n        return sixteenBitRandomValue.concat(fortyEightBitRandomValue);\n    }\n\n\tfunction createVisitorId(source) {\n        var byteArray, decorator, randomByteArray, source, timeByteArray;\n\n        timeByteArray = create48BitTimeByteArray();\n        randomByteArray = create64BitRandomByteArray();\n\n        byteArray = timeByteArray.concat([1, source]).concat(randomByteArray);\n\n        return getHexStringFromByteArray(byteArray);\n\t}\n\n\tfunction isMobile() {\n\t    mobile = ["Android", "webOS", "iPhone", "iPod", "BlackBerry", "Windows Phone", "Opera Mini", "IEMobile"];\n\t    for (var i = 0; i <= mobile.length - 1; i++) {\n\t        var mobilex = navigator.userAgent.indexOf(mobile[i]);\n\t        if (mobilex != -1) {\n\t            return true;\n\t            break;\n\t        }\n\t    }\n\t    return false;\n\t }\n\n\t function isPad() {\n\t     pad = ["iPad"];\n\t     for (var i = 0; i <= pad.length - 1; i++) {\n\t         var mobilex = navigator.userAgent.indexOf(pad[i]);\n\t         if (mobilex != -1) {\n\t             return true;\n\t             break;\n\t         }\n\t     }\n\t     return false;\n\t  }\n\n\t  function isDesktop() {\n\t      return !navigator.userAgent.match(/Android|BlackBerry|iPhone|iPad|iPod|Opera Mini|IEMobile|NokiaBrowser|Silk|mobile|tablet/i);\n\t  }\n\n\t  function getVisitorId() {\n          var source;\n\n          if (isDesktop()) {\n              source = 1;\n          } else if (isMobile()) {\n              source = 2;\n          } else if (isPad()) {\n              source = 3;\n          } else {\n              source = 0;\n          }\n\n          return createVisitorId(source);\n\t  }\n\n\t  function createVisitorIdCookie(visitorId) {\n\t\t  var d = new Date();\n\t\t  d.setTime(d.getTime() + 31536000000);\n\t\t  var expires = "expires="+d.toUTCString();\n\t\t  return "visitorId=" + visitorId + ";" + expires + ";domain=.target.com;path=/";\n\t  }\n\n\t  if (getVisitorIdCookie() === "") {\n\t\t  var session, sessionId, visitorId;\n\t\t  visitorId = getVisitorId();\n\t\t  document.cookie = createVisitorIdCookie(visitorId);\n\t\t  \n\t\t  // init firefly session\n\t\t  sessionId = (Math.floor(Math.random() * (9007199254740960 - 11184840)) + 11184840).toString(16);\n\t\t  session = {\n\t\t  \t\'newGuest\': \'true\',\n\t\t  \t\'sessionHash\': sessionId\n\t\t  };\n\t\t  document.cookie = "ffsession=" + JSON.stringify(session) + ";domain=.target.com;path=/";\n\t  }\n  })();\n\n  if (!isSecure && !noSeoCall) {\n    (function(){\n    var seoApi = (true && window.location.protocol == "http:") ? "http://content-delivery.target.com/content-publish/taxonomy/v1/seo?" : "https://content-delivery-secure.target.com/content-publish/taxonomy/v1/seo?";\n    var appPath = window.location.pathname.replace(\'home\',\'\') + ((false)?"": window.location.search)\n        seoApi = seoApi + \'url=\' + encodeURIComponent(appPath) + \'&children=true&breadcrumbs=true\';\n\n        if (false) {\n          // below changes are to give preference to effective date url parameter\n          var regex = new RegExp("[\\\\?&]" + \'effective_date\' + "=([^&#]*)");\n          var results = regex.exec(location.search);\n          var effectiveDate = results == null ? "" : decodeURIComponent(results[1].replace(/\\+/g, " "));\n          if(effectiveDate){\n            dateSearchParam = \'&effective_date=\' + effectiveDate;\n            document.getElementById(\'previewDate\').value = effectiveDate.replace(\'Z\',\'\');\n          }else{\n            dateSearchParam = \'&effective_date=\' + document.getElementById(\'previewDate\').value + \'Z\';\n          }\n          if(dateSearchParam){\n              seoApi = seoApi + dateSearchParam;\n          }\n\n        }\n        seoHttpRequest = new XMLHttpRequest();\n        seoHttpRequest.onreadystatechange = function(){\n          if(seoHttpRequest.readyState == 4 && seoReadyStateHandler){\n            seoReadyStateHandler();\n          }\n        };\n        seoHttpRequest.open("GET", seoApi, true);\n        seoHttpRequest.send();\n      })();\n    }\n</script>\n<meta name="google-site-verification" content="1rmXsZRZGP3uOmdg4qvP1A0zVaAKoxvrWtBavkX0LCE" />\n    <link  href="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/css/patlab/global.css" media="all" rel="stylesheet" type="text/css" />\n\n\t<script id="domains" type="text/javascript">\n\n\t\tif(tabletDomain.indexOf(window.location.hostname.replace(/origin.{3}-/,"")) != -1 || tabletSecureDomain.indexOf(window.location.hostname.replace(/origin.{3}-/,"")) != -1 ){\n\t\tdomain = tabletDomain;\n\t\tsecure_domain = tabletSecureDomain;\n\t\t}else{\n\t\tdomain = mobileDomain;\n\t\tsecure_domain = mobileSecureDomain;\n\t\t}\n\n\t\timg_domain = "http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01";\n\t\timageSerURL="http://img3.targetimg3.com/wcsstore/marketing";\n\t\twcs_server="http://www-int.att.target.com/wcs/resources";\n\t\twcs_secure_server="https://www-int.att.target.com/wcs/resources";\n\t\t\n\t\t\t\tisSecure = false;\n\t\t\t</script>\n\n\n\n    <script>\n\t\tvar FF_GEO_FEATURE = \'ON\';\n\t\tvar FF_PRG_2  = \'true\';\n\t\tvar defualtPickupWindow = \'false\';\n\t\tvar sfsenable = (\'true\'===\'true\');\n\t\tvar rushDelByAddress = \'on\';\n\t\tvar IS_REPROMISE_ENABLE =  \'true\';\n\t\tvar USE_ORDER_ITEM_ID =  \'true\';\n\t\tvar formFactor=\'tablet\'||"phone";\n\t\tvar useV1OrderDetails=\'false\';\n\t\tvar showCreateACcount=\'true\';\n\t\tvar STORE_RESULT_LIMIT=\'20\';\n\t\tvar prodAvailCount = \'10\';\n\t\tvar redCard_new = \'true\';\n\t\tvar plugins_mod = \'http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/plugins.mod.js\';\n\t\tvar mod_0 = \'http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/browse.mod.js\';\n\t\tvar mod_1 = \'http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/non-browse.mod.js\';\n\t</script>\n\t\n    <script type="text/javascript" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/plugins.mod.js" ></script>\n\t\t\t<script type="text/javascript" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/browse.mod.js" ></script>\n\t\t<script type="text/javascript" src="//nexus.ensighten.com/target/tcom-ui-prod/Bootstrap.js"></script>\n\t\t<script>\n\t  var scr = document.createElement("script");\n\t  scr.src = configJSON.imageServerDomain + configJSON.imageIncludes + \'/foresee2/foresee-trigger.js\';\n    scr.async = true;\n\t  document.getElementsByTagName("head")[0].appendChild(scr);\n\t</script>\n<script id="dvm" type="text/javascript">\n\tvar gptadslots=[];\n\tvar googletag = googletag || {};\n\tgoogletag.cmd = googletag.cmd || [];\n\t(function(){ var gads = document.createElement(\'script\');\n\t\tgads.async = true; gads.type = \'text/javascript\';\n\t\tvar useSSL = \'https:\' == document.location.protocol;\n\t\tgads.src = (useSSL ? \'https:\' : \'http:\') + \'//www.googletagservices.com/tag/js/gpt.js\';\n\t\tvar node = document.getElementsByTagName(\'script\')[0];\n\t\tnode.parentNode.insertBefore(gads, node);\n\t})();\n</script>\n<script type="text/javascript">\n      if ((/iphone|ipod|ipad.*os /gi).test(navigator.appVersion)) {\n        window.onpageshow = function(evt) {\n          // If persisted then it is in the page cache, force a reload of the page.\n          if (evt.persisted) {\n    \t    window.location.reload();\n          }\n        };\n      }\n</script>\n</head>\n  <body id="home" ontouchstart="">\n  <div tabindex="-1" class="TGTloading" style="display: none">\n    <div class="loading-container">\n      <div class="loading-spinner"></div>\n      <div class="loading-message"></div>\n    </div>\n  </div>\n\t<div id="viewport">\n\t\t\t\t<div id="pageStart"></div>\n\t\t\t</div>\n\t\t<script id="page-meta" type="application/json">\n\t\t{\n  "img_domain" : "http://img3.targetimg3.com",\n  "img_secure_domain" : "https://img3-secure.targetimg3.com",\n  "generated_time" : "Thu Mar 24 02:32:56 EDT 2016",\n  "build_number" : "716-03162016-01",\n  "page_name" : "mProduct",\n  "view_def" : {\n    "header" : [ {\n      "path" : "http://img3.targetimg3.com/wcsstore/marketing/com/mobile/includes/template/header_v2.html",\n      "position" : 1\n    } ],\n    "nav" : [ {\n      "path" : "http://img3.targetimg3.com/wcsstore/marketing/com/mobile/includes/template/header_v2.html",\n      "position" : 1\n    } ],\n    "main_body" : [ {\n      "path" : "mCommonProductPage",\n      "position" : 2,\n      "attribute" : [ {\n        "name" : "rrpcStaticLink",\n        "value" : "/spot/terms/return-policy"\n      }, {\n        "name" : "isNewCheckOut",\n        "value" : "Y"\n      } ]\n    } ],\n    "footer" : [ {\n      "path" : "http://img3.targetimg3.com/wcsstore/marketing/com/mobile/includes/template/header_v2.html",\n      "position" : 1\n    } ]\n  },\n  "page_grid" : "<div id=\\"header\\" class=\\"l-sticky\\" data-name=\\"views/tablet/common/header.view\\"></div><div id=\\"nav\\" data-name=\\"views/tablet/common/nav.view\\"></div><div id=\\"pdp\\" class=\\"main-content l-container-fixed\\" data-page=\\"product details page\\" data-name=\\"views/tablet/browse/pdp.view\\" itemscope=\\"\\" itemtype=\\"http://schema.org/Product\\"></div><div id=\\"fiats\\" data-name=\\"views/tablet/common/fiats.view\\"></div><div id=\\"footer\\" class=\\"footer\\" data-name=\\"views/tablet/common/footer.view\\"></div>",\n  "tracking" : {\n    "attribute" : [ {\n      "name" : "s.prop1",\n      "value" : "product details"\n    }, {\n      "name" : "s.prop4",\n      "value" : "mobile"\n    } ]\n  },\n  "device_info" : {\n    "attribute" : [ {\n      "name" : "deviceType"\n    }, {\n      "name" : "formFactor",\n      "value" : "tablet"\n    } ]\n  },\n  "meta_tags" : {\n    "attribute" : [ {\n      "name" : "title",\n      "value" : "16849119 at Mobile Target"\n    }, {\n      "name" : "description",\n      "value" : "Shop for 16849119 at Mobile Target"\n    }, {\n      "name" : "keywords",\n      "value" : "16849119, 16849119 online, Mobile Target"\n    } ]\n  },\n  "banners" : [ {\n    "id" : "13186697",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/tent-6-person-13186697.html"\n  }, {\n    "id" : "13186698",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/tent-9-person-13186698.html"\n  }, {\n    "id" : "14432134",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/20130414_kate.html"\n  } ],\n  "title" : "",\n  "processing_time" : 73,\n  "jsfiles" : [ {\n    "jsfile" : "http://img3.targetimg3.com/wcsstore/marketing/com/mobile/js/template/productDetail_minified.js"\n  } ],\n  "cssfiles" : [ ],\n  "feature" : {\n    "FORESEE" : "false",\n    "TEA_LEAF" : "false",\n    "SECURE_TEA_LEAF" : "false",\n    "FF_ENABLE" : "true",\n    "BV_ENABLED" : "true",\n    "TRACKER" : "false",\n    "SFS_ENABLE" : "true",\n    "FF_PRG_2" : "true",\n    "REGISTRY_RESET_FLAG" : "false",\n    "TNL_COOKIE" : "false",\n    "IS_REPROMISE_ENABLE" : "true",\n    "SHOW_MODAL_BOX" : "true",\n    "ONE_PAGE_CHECKOUT_ENABLE" : "true",\n    "ONE_PAGE_CHECKOUT_ENABLE_FOR_IPAD" : "true",\n    "REVIEW_PAGE_ENABLE_CRTE_ACCT" : "false",\n    "IS_DUMMY_THANK_YOU" : "true",\n    "SEARCH_OPT_FLAG" : "false",\n    "USE_ORDER_ITEM_ID" : "true",\n    "DVM" : "true",\n    "SHIPPING_LIMITED_OFFER" : "false",\n    "PREVIEW_ENABLE" : "false",\n    "ORDER_DETAIL_V1" : "false",\n    "SHOW_CREATE_ACCOUNT" : "true",\n    "SUBSCRIPTION_ENABLED" : "true",\n    "STS_ENABLE" : "true",\n    "SUBS_SHIP_PROMO_MODALMSG" : "true",\n    "PRZ_ENABLE" : "true",\n    "CHKOUT_EXP_ELIGBLE" : "true",\n    "PEAK_HOURS_FLAG" : "false",\n    "THREAT_METRICS_ENABLE" : "true",\n    "ORD_PRZ_ENABLE" : "true",\n    "REDCARD_NEW" : "true",\n    "SLINGSHOT_ENABLED" : "true",\n    "EXPERIAN_EMAIL_SERVICE" : "true",\n    "CART_GET_DEALS" : "false",\n    "APPLE_GIFTCARD_MERCH_CLASS" : "true",\n    "SLING_SHOT_PREVIEW_ENABLE" : "false",\n    "SLINGSHOT_SERVER_CONTROLE" : "false",\n    "IS_CARDINAL" : "false",\n    "ADVANCE_ORDER_CROSSOVER" : "false",\n    "ADVANCE_ORDER_ENABLE" : "true",\n    "MOBILE_ONLY_CHANNEL" : "true",\n    "DELIVERY_DISPLAY_PRICE_ENABLE" : "false",\n    "SITESKIN_ENABLED" : "false",\n    "SUBSCRIPTION_MOD_ENDPOINT" : "true",\n    "SUBSCRIPTION_UI_DISABLED" : "false",\n    "NONSECURE_SIGNIN_OVERLAY_ENABLED" : "true",\n    "ADAPIVE_GC" : "true",\n    "FULL_ADAPTIVE" : "true",\n    "PLP_TO_PDP_PARTIAL_LOAD" : "false",\n    "LIMITED_QTY_ENABLED" : "false",\n    "OBGB_ENABLED" : "true",\n    "ENABLE_TRACKJS" : "false",\n    "REORDER_TWO_TAP_OVERLAY" : "true",\n    "DELIVERY_EMAIL_VALIDATION" : "false",\n    "PAGE_SCRIPT_ENABLE" : "false",\n    "STORE_LIMITED_QTY_ENABLED" : "true",\n    "REPROMISE_OPTIMIZATION_ENABLE" : "true",\n    "WXS_LIMITED_QTY_ENABLED" : "true",\n    "AISLEINFOSERVICE_ENABLE" : "true",\n    "TAG_PAGE_ENABLED" : "true",\n    "CATEGORY_SLINGSHOT_ENABLED" : "true",\n    "SLINGSHOT_HTTP_ENABLED" : "true",\n    "STORE_LOCATOR_SEO_URL" : "true",\n    "CART_PROMO_CODE_ENTRY" : "true",\n    "FF_V3_TO_ATP_ENABLE" : "true",\n    "CRUSH_ACTIVE" : "true",\n    "REFRESH_JOB" : "false",\n    "BROWSE_BY_CATEGORIES_SLINGSHOT" : "true",\n    "FIREFLY_ENABLED" : "true",\n    "REPOPULATE_GEO_COOKIE" : "true",\n    "DEFAULT_TABLET_VIEW" : "true",\n    "PDP_DYNAMIC_PRICING" : "true",\n    "GET_THIS_PHONE" : "true",\n    "GIFT_REGISTRY_RENAME" : "true",\n    "CRUSH_FEED_CURATION" : "true",\n    "EMPTY_CART_DVM_FLAG" : "true",\n    "ENABLE_FORESEE" : "true",\n    "IS_VIEWCART_OPTIMIZED" : "true",\n    "PAYMENT_SERVICES_ENABLED" : "true",\n    "GIFTCARD_ACTIVATION_MSG_ENABLE" : "false",\n    "SUB_RECO" : "false",\n    "PROMO_INJECTION_ENABLED" : "false",\n    "SECURITY_FIX_ENABLED" : "true",\n    "EXPRESS_CHECKOUT" : "true",\n    "OBGB_MSG_ON_LISTING_PAGES" : "true",\n    "FGC_FIX_ENABLE" : "false",\n    "SFS_BACKORDER" : "false",\n    "SHOW_ORDER_OVERLAY" : "true",\n    "USE_MOD_ORDERS" : "false",\n    "PHARMACY_INTERSTITIAL" : "true",\n    "ENABLE_WRITE_REVIEW" : "true",\n    "ENABLE_CRITICAL_REVIEW" : "true",\n    "DISABLE_MOBILE_GC" : "true",\n    "SUBSCRIPTION_FLYOUT" : "true",\n    "SEARCH_INSTEAD_FOR" : "false",\n    "DID_YOU_MEAN" : "false",\n    "ATC_RECOMMANDATIONS" : "false",\n    "SAPPHIRE" : "false",\n    "STORE_LOCATOR_ACCORDION_FIX" : "true",\n    "GAM_REPROMISE_FLYOUT" : "true",\n    "SSX_ENABLED" : "false",\n    "EnableSFL" : "true",\n    "FF_GEO_FEATURE" : "ON",\n    "DEFAULT_PICKUP_WINDOW" : "4",\n    "RELATED_CATEGORY" : "Y",\n    "CATEGORY_FEATURE_BRAND" : "Y",\n    "CATEGORY_GOOGLE_ADS" : "Y",\n    "CATEGORY_DVM_ADS" : "Y",\n    "DVM_CHANNLE_ID" : "mtarget",\n    "TABLET_DVM_CHANNLE_ID" : "target",\n    "SEARCH_OPT_RESP_GROUP" : "VariationSummary,Items",\n    "RUSH_DELIVERY_RADIUS" : "10",\n    "STORE_FINDER" : "100",\n    "RUSH_DEL_BY_ADDR" : "on",\n    "AVAILABILITY_SERVICE_PROD_COUNT" : "10",\n    "STORE_RESULT_LIMIT" : "20",\n    "THREAT_METRICS_ORG_ID" : "9p00aymw",\n    "SLINGSHOT_CATG_ID" : "/slingshot/category/2222222",\n    "FREE_SHIPPING_THRESHHOLD_VALUE" : "25",\n    "AO_MAX_STORES" : "5",\n    "ORD_HISTORY_DAY_LIMIT" : "1",\n    "ORD_HISTORY_COUNT_LIMIT" : "100",\n    "AO_STORES_RADIUS" : "25",\n    "GAM_DASH_ORDERS_LIMIT_COUNT" : "3",\n    "HOOK_LOGIC_KEY" : "764937a9-7afb-4cf1-8631-d8a5edca8f36",\n    "HOOK_LOGIC_ID" : "[CS]v1|2AC0BE5905079201-6000010B000429CD[CE]",\n    "TRACKJS_APPID" : "mobileweb",\n    "TRACKJS_TOKEN" : "913e59b71ca34b21aa95bc55121a0871",\n    "STORE_LIMITED_QTY" : "5",\n    "EVENT_TYPE" : "star",\n    "EVENT_STORES" : "4,61,64,90,93,199,215,221,230,246,301,320,346,348,351,359,361,617,627,636,676,686,687,755,766,769,794,810,818,822,824,827,830,844,861,870,885,911,935,937,938,942,969,992,995,1010,1018,1021,1025,1029,1034,1043,1056,1058,1092,1102,1107,1139,1140,1150,1153,1163,1166,1182,1191,1207,1224,1238,1244,1249,1252,1254,1257,1261,1266,1268,1275,1285,1306,1338,1339,1347,1350,1351,1354,1355,1357,1363,1364,1367,1368,1370,1376,1377,1384,1391,1397,1408,1409,1427,1431,1439,1443,1445,1449,1453,1455,1473,1476,1478,1481,1483,1501,1502,1505,1506,1510,1518,1541,1751,1755,1756,1767,1768,1774,1783,1787,1795,1797,1799,1806,1820,1821,1822,1856,1858,1869,1874,1883,1895,1903,1912,1916,1921,1930,1932,1934,1944,1954,1961,1965,1981,2014,2019,2022,2031,2034,2035,2036,2051,2093,2101,2105,2106,2108,2124,2129,2138,2170,2176,2189,2190,2205,2208,2210,2227,2244,2266,2271,2303,2313,2322,2338,2339,2348,2350,2356,2360,2371,2372,2373,2403,2410,2429,2473,2532,2542,2572,2682,2737,2757,2760,2764,2767,2771,2824,2843",\n    "CRUSH_URL_PROD" : "https://gnc-secure.target.com/guestpreference",\n    "FEED_URL_PROD" : "https://prz-secure.target.com/recommendations/v1?",\n    "MOD_INTEG_BUILD_NUMBER" : "12345",\n    "CRUSH_FEED_MAX" : "96",\n    "ITUNES_MERCH_CLASS" : "PREPAID CARDS, ENTERTAINMENT CARDS, ITUNES, DIGITAL CONTENT, VERIZON CONTRACT, BATTERIES",\n    "INVALID_CALLOUTS" : "testCallOut",\n    "GET_THIS_PHONEURL" : "https://mobile.target.com/web/controller/landing.php?",\n    "DLP_PARAMS" : "[\\"AFID\\",\\"CPNG\\",\\"KID\\",\\"LID\\",\\"LNM\\",\\"MT\\",\\"N\\",\\"gclid\\",\\"ref\\",\\"adgroup\\",\\"network\\",\\"device\\",\\"querystring\\",\\"location\\",\\"gclsrc\\",\\"emseq\\",\\"link\\",\\"tp\\"]",\n    "DYNAMIC_PROMO_VAL" : "TGTA39R9",\n    "PRIVACY_UPDATED_DATE" : "2015-10-26",\n    "ATP_SERVICE_PAYLOAD_MAX_PRODUCTS" : "20",\n    "GIFTCARD_PURCHASED_TODAY_ACTIVATION_24HOURS" : "If you purchased a Target GiftCard on December 20, your gift card will be activated on December 21.",\n    "MERCH_SUBCLASS_ARRAY" : "[{\\"DPCI\\":\\"255-02\\",\\"content\\":\\"atnt\\",\\"corpId\\":\\"596\\"},{\\"DPCI\\":\\"255-04\\",\\"content\\":\\"verizon\\",\\"corpId\\":\\"660\\"},{\\"DPCI\\":\\"255-08\\",\\"content\\":\\"sprint\\",\\"corpId\\":\\"545\\"},{\\"DPCI\\":\\"255-14\\",\\"content\\":\\"iphones\\",\\"corpId\\":\\"731\\"}]",\n    "ORD_HISTORY_RECENT_LIMIT" : "30",\n    "ORD_HISTORY_ALL_LIMIT" : "365",\n    "SERVICE_CALL_DATA_TYPE" : "jsonp",\n    "WHITE_LIST_MERCH_CONTENT" : "merchandizingSlot1"\n  },\n  "datacenter" : "SCS"\n}</script>\n  </body>\n</html>\n\n'soup2 = BeautifulSoup(d.page_source, "html.parser", parse_only=SoupStrainer('div', {'id':'pdpMainContainer'}))
SyntaxError: invalid syntax
>>> b'<!DOCTYPE html>\n<html lang="en" class="no-js">\n  <head>\n\t\t<meta charset="utf-8" />\n<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n<meta name="viewport" content="width=device-width, maximum-scale=1, minimum-scale=1, user-scalable=no" />\n<link id="favicon" rel="shortcut icon" type="image/png" href="//static.targetimg1.com/mobile-config/favicon.ico" />\n<link rel="apple-touch-icon-precomposed" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/apple-touch-icon-precomposed.png" />\n<link rel="icon" type="image/png" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/apple-touch-icon-precomposed.png" sizes="192x192">\n<link rel="icon" type="image/png" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/favicon-96x96.png" sizes="96x96">\t\n<link rel="icon" type="image/png" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/favicon-32x32.png" sizes="32x32">\n<link rel="icon" type="image/png" href="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/favicon-16x16.png" sizes="16x16">\n<meta name="msapplication-TileColor" content="#cc0000">\n<meta name="msapplication-TileImage" content="http://img1.targetimg1.com/wcsstore/marketing/com/mobile/images/template/android-chrome-192x192.png">\n<meta name="format-detection" content="telephone=no" />\n<script>document.createElement("picture");</script>\n<script>\n\t(function(){if(window.BOOMR&&window.BOOMR.version){return}var dom,doc,where,iframe=document.createElement(\'iframe\');iframe.src="javascript:false";iframe.title="";iframe.role="presentation";(iframe.frameElement||iframe).style.cssText="width:0;height:0;border:0;display:none;";where=document.getElementsByTagName(\'script\')[0];where.parentNode.insertBefore(iframe,where);try{doc=iframe.contentWindow.document}catch(e){dom=document.domain;iframe.src="javascript:var d=document.open();d.domain=\'"+dom+"\';void(0);";doc=iframe.contentWindow.document}doc.open()._l=function(){var js=this.createElement("script");if(dom)this.domain=dom;js.id="boomr-if-as";js.src=\'//c.go-mpulse.net/boomerang/KQTS5-4NBTD-EYGLE-64UYR-S5892\';BOOMR_lstart=new Date().getTime();this.body.appendChild(js)};doc.write(\'<body onload="document._l();">\');doc.close()})();\n\t!function(a){if(a.XMLHttpRequest&&(new XMLHttpRequest).addEventListener){var b,c=document.createElement("A"),d=XMLHttpRequest,e=[],f=["uninitialized","open","responseStart","domInteractive","responseEnd"];a.BOOMR=a.BOOMR||{},BOOMR.xhr={stop:function(c){return b=c,a.XMLHttpRequest=d,delete BOOMR.xhr,setTimeout(function(){e=[]}),e}};var g=function(){try{if("performance"in a)return function(){return Math.round(performance.now()+performance.timing.navigationStart)}}catch(b){}return Date.now||function(){return(new Date).getTime()}}();a.XMLHttpRequest=function(){var h=new d,i=h.open;return h.open=function(d,j,k){function l(){if(!n.timing.loadEventEnd){if(n.timing.loadEventEnd=g(),"performance"in a&&a.performance&&"function"==typeof a.performance.getEntriesByName){var c=a.performance.getEntriesByName(n.url),d=c&&c.length&&c[c.length-1];if(d){var f=a.performance.timing.navigationStart;0!==d.responseEnd&&(n.timing.responseEnd=Math.round(f+d.responseEnd)),0!==d.responseStart&&(n.timing.responseStart=Math.round(f+d.responseStart)),0!==d.startTime&&(n.timing.requestStart=Math.round(f+d.startTime))}}b?b(n):e.push(n)}}function m(a,b){h.addEventListener(a,function(){"readystatechange"===a?(n.timing[f[h.readyState]]=g(),4===h.readyState&&l()):(n.status=void 0===b?h.status:b,l())},!1)}c.href=j;var n={timing:{},url:c.href,method:d};k===!0?m("readystatechange"):n.synchronous=!0,m("load"),m("timeout",-1001),m("error",-998),m("abort",-999);try{i.apply(h,arguments);var o=h.send;h.send=function(){n.timing.requestStart=g(),o.apply(h,arguments)}}catch(p){n.status=-997,l()}},h}}}(window);\n</script>\n<script type="text/javascript">\n\n  var configJSON = {\n\tpreUrlMobileConstructor\t\t: "http://m.target.com/",\n\tsecurePreUrlMobileConstructor\t: "https://m-secure.target.com/",\n\tpreUrlTabletConstructor\t\t: "http://www.target.com/",\n\tsecurePreUrlTabletConstructor\t: "https://www-secure.target.com/",\n\tapiServer\t\t\t\t: {\n\t\tdomain : "http://api.target.com",\n\t\tsecuredomain : "https://secure-api.target.com",\n\t\taccesskey :"eb2551e4accc14f38cc42d32fbc2b2ea",\n\t\tsecureaccesskey : "SxR9X7XoWw2fW1PBWfXswf3q5NeIuGAu"\n\t},\n\tsearchURL\t\t\t\t: "http://tws.target.com/searchservice/item/search_results/v2/by_keyword?",\n    searchURLV2             : "http://tws.target.com/searchservice/item/search_results/v2/by_keyword?",\n    brandURL                : "http://tws.target.com/searchservice/item/brand_results/v2/by_brand?",\n    itemPriceURL            : "http://dcd-prc.target.com/item/price/v1/{tcins}?key=8cb043b2dace9afc0680e6bae5cd316f",\n\tbrowseURL\t\t\t\t: "http://tws.target.com/productservice/services/item_service/v1/by_itemid?",\n\tbrowseSecureURL\t\t\t: "https://tws-secure.target.com/productservice/services/item_service/v1/by_itemid?",\n\tbazaarVoiceURL\t\t\t: "display.ugc.bazaarvoice.com/static/targetcom/uimod/en_US/bvapi.js",\n\tdvmChannelId\t\t\t: "mtarget",\n\tpersonalizationEngineURL: "https://prz-secure.target.com/recommendations/v1",\n\tthreatMerticsURL\t\t: "https://img9.target.com",\n    redcardPromoEnabled\t\t: true,\n    useServiceController\t: false,\n\twcsTimeoutIntervel\t\t: 600,\n\tcartTimeoutIntervel\t\t: 600000,\n\tsearchTimeoutIntervel\t: 10000,\n\tbrowseTimeoutIntervel\t: 10000,\n\tglobalAjaxTimeout       : 30000,\n\tglobalATPServiceTimeout : 5000,\n\tenvMpulse\t\t\t\t: "prod",\n\tmpulseUrl\t\t\t\t: "//c.go-mpulse.net/boomerang/KQTS5-4NBTD-EYGLE-64UYR-S5892",\n\tslingshotPreviewURL\t\t: "https://content-preview-secure.target.com/content-preview",\n\tslingshotURL\t\t\t: "https://content-delivery-secure.target.com/content-publish",\n\tslingshotURL_http       : "http://content-delivery.target.com/content-publish",\n\tslingshotCategoryId\t\t: "/slingshot/category/2222222",\n\tmobileDomain\t\t\t: "http://m.target.com",\n\tmobileSecureDomain\t\t: "https://m-secure.target.com",\n\ttabletDVMChannelId\t\t: "target",\n\tsubscriptionModURL\t\t: "https://subscriptions-secure.target.com",\n\tseoApiURL\t\t\t\t: "https://content-delivery-secure.target.com/content-publish/taxonomy/v1/seo?",\n\tseoApiURL_http\t\t\t: "http://content-delivery.target.com/content-publish/taxonomy/v1/seo?",\n\thlURL\t\t\t\t\t: "http://www.hlserve.com/delivery/api",\n\thlKey\t\t\t\t\t: "764937a9-7afb-4cf1-8631-d8a5edca8f36",\n\thlId\t\t\t\t\t: "[CS]v1|2AC0BE5905079201-6000010B000429CD[CE]",\n\tsfCert\t\t\t\t\t: "",\n\tsfCID\t\t\t\t\t: "",\n\tsfURL\t\t\t\t\t: "",\n\tchkURL\t\t\t\t\t: "https://checkout-api-secure.target.com",\n\tchkWalletAPIURL\t\t\t: "https://checkout-api-secure.target.com",\n\tgamURL\t\t\t\t\t: "https://gam-api-secure.target.com",\n\tgamKey\t\t\t\t\t: "OGFiNjJhOWMtMWI4Ni00ZDJhLTlkNGItMTUwODJiYzNmMDA0OjNpSnRQamVNdkk=",\n\tmodAjaxTimeout\t\t\t: "20000",\n\ttwsDomain\t\t\t\t: "http://tws.target.com",\n\ttwsSecureDomain\t\t\t: "https://tws-secure.target.com",\n\ttreeCategoryUrl\t\t\t: "http://m.target.com/TreeCategory",\n\tsecureTreeCategoryUrl\t: "https://m-secure.target.com/TreeCategory",\n\tcategoriesXml           : "http://img1.targetimg1.com/wcsstore/marketing/com/mobile/en/xml/products/categories.xml",\n\timageIncludes\t\t\t: "/wcsstore/marketing/com/mobile/includes",\n\tbreadCrumbUrl           : "http://tws.target.com/searchservice/catalog/bread_crumb/v2/by_category_id?",\n\tfireflySchemaId         : "1184",\n\tfireflyTopic            : "firefly_estore_eventstream",\n\tfireflyHost             : "firefly.target.com",\n\tsecEnabled\t\t\t\t: "true",\n\tapiNonPCIDomain\t\t\t: "https://api.target.com",\n\tsubscriptionUrl         : "/wcsstore/marketing/com/mobile/en/html/spot/target-subscriptions_1.html",\n\tsapphireUrl: "http://sapphire.edge-csp1-e1-npe.target.com/sapphire/runtime/api/v1/qualified-experiments?",\n  typeaheadUrl: "http://typeahead.target.com/",\n  typeaheadSecureUrl: "https://typeahead-secure.target.com/",\n\tshapeJs: "//static.targetimg1.com/ssx/ssx.mod.js"\n  };\n\n\n var mobileDomain = "http://m.target.com";\n var mobileSecureDomain = "https://m-secure.target.com";\n var tabletDomain = "http://www.target.com";\n var tabletSecureDomain = "https://www-secure.target.com";\n\n  if(tabletDomain.indexOf(window.location.hostname.replace(/origin.{3}-/,"")) != -1 || tabletSecureDomain.indexOf(window.location.hostname.replace(/origin.{3}-/,"")) != -1 ){\n\t  configJSON["preUrlConstructor"] = configJSON["preUrlTabletConstructor"];\n\t  configJSON["securePreUrlConstructor"] = configJSON["securePreUrlTabletConstructor"];\n  }else{\n\t  configJSON["preUrlConstructor"] = configJSON["preUrlMobileConstructor"];\n\t  configJSON["securePreUrlConstructor"] = configJSON["securePreUrlMobileConstructor"];\n  }\n\n  // setting secure/nonsecure image server path\n  if (window.location.protocol =="https:") {\n    configJSON["imageServerDomain"] = "https://img3-secure.targetimg3.com";\n  } else {\n    configJSON["imageServerDomain"] = "http://img3.targetimg3.com";\n  }\n\n</script>\n<script type="text/javascript">\n  \n  var isSecure = (window.location.protocol !== "http:");\n  var noSeoCall = (window.location.pathname.indexOf(\'target-crush\') !== -1 || window.location.pathname.indexOf(\'mcategories\') !== -1);\n  var seoHttpRequestPromise = null;\n  var seoHttpRequest = null;\n  var seoReadyStateHandler = null;\n  var dateSearchParam = \'\';\n  var isSapphireEnabled = false;\n  // global function to getVisitorId\n  var getVisitorIdCookie = function getVisitorIdCookie() {\n    var name = "visitorId=";\n    var ca = document.cookie.split(\';\');\n    for(var i=0; i<ca.length; i++) {\n        var c = ca[i];\n        while (c.charAt(0)===\' \') c = c.substring(1);\n        if (c.indexOf(name) === 0) return c.substring(name.length,c.length);\n    }\n    return "";\n  };\n\n  // firefly vistorId changes starts here\n  (function(){\n\tfunction getByteArrayFromInteger(integer, desiredBytes) {\n        var byteValue, byteArray, index;\n\n        byteArray = [];\n\n        for (index = 0; index < desiredBytes; index++) {\n            byteValue = integer & 0xff;\n            byteArray.push(byteValue);\n            integer = (integer - byteValue) / 256;\n        }\n\n        return byteArray.reverse();\n    }\n\n\tfunction getRandomNumber(min, max) {\n        return Math.floor(Math.random() * (max - min)) + min;\n    }\n\n\tfunction getHexStringFromByte (byte) {\n        var hexCharArray, hexString;\n\n        hexCharArray = [\'0\', \'1\', \'2\', \'3\', \'4\', \'5\', \'6\', \'7\', \'8\', \'9\', \'A\', \'B\', \'C\', \'D\', \'E\', \'F\'];\n        hexString = hexCharArray[(byte >> 4) & 0x0f] + hexCharArray[byte & 0x0f];\n\n        return hexString;\n    }\n\n\tfunction getHexStringFromByteArray(byteArray) {\n        return byteArray.map(getHexStringFromByte, this).join("");\n    }\n\n    function create48BitTimeByteArray() {\n        return getByteArrayFromInteger(new Date(), 6);\n    }\n\n    function create64BitRandomByteArray() {\n        var randomValue, sixteenBitRandomValue, fortyEightBitRandomValue;\n\n        randomValue = getRandomNumber(0, 9000000000000000);\n        sixteenBitRandomValue = getByteArrayFromInteger(randomValue, 2);\n\n        randomValue = getRandomNumber(0, 9000000000000000);\n        fortyEightBitRandomValue = getByteArrayFromInteger(randomValue, 6);\n\n        return sixteenBitRandomValue.concat(fortyEightBitRandomValue);\n    }\n\n\tfunction createVisitorId(source) {\n        var byteArray, decorator, randomByteArray, source, timeByteArray;\n\n        timeByteArray = create48BitTimeByteArray();\n        randomByteArray = create64BitRandomByteArray();\n\n        byteArray = timeByteArray.concat([1, source]).concat(randomByteArray);\n\n        return getHexStringFromByteArray(byteArray);\n\t}\n\n\tfunction isMobile() {\n\t    mobile = ["Android", "webOS", "iPhone", "iPod", "BlackBerry", "Windows Phone", "Opera Mini", "IEMobile"];\n\t    for (var i = 0; i <= mobile.length - 1; i++) {\n\t        var mobilex = navigator.userAgent.indexOf(mobile[i]);\n\t        if (mobilex != -1) {\n\t            return true;\n\t            break;\n\t        }\n\t    }\n\t    return false;\n\t }\n\n\t function isPad() {\n\t     pad = ["iPad"];\n\t     for (var i = 0; i <= pad.length - 1; i++) {\n\t         var mobilex = navigator.userAgent.indexOf(pad[i]);\n\t         if (mobilex != -1) {\n\t             return true;\n\t             break;\n\t         }\n\t     }\n\t     return false;\n\t  }\n\n\t  function isDesktop() {\n\t      return !navigator.userAgent.match(/Android|BlackBerry|iPhone|iPad|iPod|Opera Mini|IEMobile|NokiaBrowser|Silk|mobile|tablet/i);\n\t  }\n\n\t  function getVisitorId() {\n          var source;\n\n          if (isDesktop()) {\n              source = 1;\n          } else if (isMobile()) {\n              source = 2;\n          } else if (isPad()) {\n              source = 3;\n          } else {\n              source = 0;\n          }\n\n          return createVisitorId(source);\n\t  }\n\n\t  function createVisitorIdCookie(visitorId) {\n\t\t  var d = new Date();\n\t\t  d.setTime(d.getTime() + 31536000000);\n\t\t  var expires = "expires="+d.toUTCString();\n\t\t  return "visitorId=" + visitorId + ";" + expires + ";domain=.target.com;path=/";\n\t  }\n\n\t  if (getVisitorIdCookie() === "") {\n\t\t  var session, sessionId, visitorId;\n\t\t  visitorId = getVisitorId();\n\t\t  document.cookie = createVisitorIdCookie(visitorId);\n\t\t  \n\t\t  // init firefly session\n\t\t  sessionId = (Math.floor(Math.random() * (9007199254740960 - 11184840)) + 11184840).toString(16);\n\t\t  session = {\n\t\t  \t\'newGuest\': \'true\',\n\t\t  \t\'sessionHash\': sessionId\n\t\t  };\n\t\t  document.cookie = "ffsession=" + JSON.stringify(session) + ";domain=.target.com;path=/";\n\t  }\n  })();\n\n  if (!isSecure && !noSeoCall) {\n    (function(){\n    var seoApi = (true && window.location.protocol == "http:") ? "http://content-delivery.target.com/content-publish/taxonomy/v1/seo?" : "https://content-delivery-secure.target.com/content-publish/taxonomy/v1/seo?";\n    var appPath = window.location.pathname.replace(\'home\',\'\') + ((false)?"": window.location.search)\n        seoApi = seoApi + \'url=\' + encodeURIComponent(appPath) + \'&children=true&breadcrumbs=true\';\n\n        if (false) {\n          // below changes are to give preference to effective date url parameter\n          var regex = new RegExp("[\\\\?&]" + \'effective_date\' + "=([^&#]*)");\n          var results = regex.exec(location.search);\n          var effectiveDate = results == null ? "" : decodeURIComponent(results[1].replace(/\\+/g, " "));\n          if(effectiveDate){\n            dateSearchParam = \'&effective_date=\' + effectiveDate;\n            document.getElementById(\'previewDate\').value = effectiveDate.replace(\'Z\',\'\');\n          }else{\n            dateSearchParam = \'&effective_date=\' + document.getElementById(\'previewDate\').value + \'Z\';\n          }\n          if(dateSearchParam){\n              seoApi = seoApi + dateSearchParam;\n          }\n\n        }\n        seoHttpRequest = new XMLHttpRequest();\n        seoHttpRequest.onreadystatechange = function(){\n          if(seoHttpRequest.readyState == 4 && seoReadyStateHandler){\n            seoReadyStateHandler();\n          }\n        };\n        seoHttpRequest.open("GET", seoApi, true);\n        seoHttpRequest.send();\n      })();\n    }\n</script>\n<meta name="google-site-verification" content="1rmXsZRZGP3uOmdg4qvP1A0zVaAKoxvrWtBavkX0LCE" />\n    <link  href="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/css/patlab/global.css" media="all" rel="stylesheet" type="text/css" />\n\n\t<script id="domains" type="text/javascript">\n\n\t\tif(tabletDomain.indexOf(window.location.hostname.replace(/origin.{3}-/,"")) != -1 || tabletSecureDomain.indexOf(window.location.hostname.replace(/origin.{3}-/,"")) != -1 ){\n\t\tdomain = tabletDomain;\n\t\tsecure_domain = tabletSecureDomain;\n\t\t}else{\n\t\tdomain = mobileDomain;\n\t\tsecure_domain = mobileSecureDomain;\n\t\t}\n\n\t\timg_domain = "http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01";\n\t\timageSerURL="http://img3.targetimg3.com/wcsstore/marketing";\n\t\twcs_server="http://www-int.att.target.com/wcs/resources";\n\t\twcs_secure_server="https://www-int.att.target.com/wcs/resources";\n\t\t\n\t\t\t\tisSecure = false;\n\t\t\t</script>\n\n\n\n    <script>\n\t\tvar FF_GEO_FEATURE = \'ON\';\n\t\tvar FF_PRG_2  = \'true\';\n\t\tvar defualtPickupWindow = \'false\';\n\t\tvar sfsenable = (\'true\'===\'true\');\n\t\tvar rushDelByAddress = \'on\';\n\t\tvar IS_REPROMISE_ENABLE =  \'true\';\n\t\tvar USE_ORDER_ITEM_ID =  \'true\';\n\t\tvar formFactor=\'tablet\'||"phone";\n\t\tvar useV1OrderDetails=\'false\';\n\t\tvar showCreateACcount=\'true\';\n\t\tvar STORE_RESULT_LIMIT=\'20\';\n\t\tvar prodAvailCount = \'10\';\n\t\tvar redCard_new = \'true\';\n\t\tvar plugins_mod = \'http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/plugins.mod.js\';\n\t\tvar mod_0 = \'http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/browse.mod.js\';\n\t\tvar mod_1 = \'http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/non-browse.mod.js\';\n\t</script>\n\t\n    <script type="text/javascript" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/plugins.mod.js" ></script>\n\t\t\t<script type="text/javascript" src="http://img3.targetimg3.com/wcsstore/marketing/com/uimod/716-03162016-01/js/browse.mod.js" ></script>\n\t\t<script type="text/javascript" src="//nexus.ensighten.com/target/tcom-ui-prod/Bootstrap.js"></script>\n\t\t<script>\n\t  var scr = document.createElement("script");\n\t  scr.src = configJSON.imageServerDomain + configJSON.imageIncludes + \'/foresee2/foresee-trigger.js\';\n    scr.async = true;\n\t  document.getElementsByTagName("head")[0].appendChild(scr);\n\t</script>\n<script id="dvm" type="text/javascript">\n\tvar gptadslots=[];\n\tvar googletag = googletag || {};\n\tgoogletag.cmd = googletag.cmd || [];\n\t(function(){ var gads = document.createElement(\'script\');\n\t\tgads.async = true; gads.type = \'text/javascript\';\n\t\tvar useSSL = \'https:\' == document.location.protocol;\n\t\tgads.src = (useSSL ? \'https:\' : \'http:\') + \'//www.googletagservices.com/tag/js/gpt.js\';\n\t\tvar node = document.getElementsByTagName(\'script\')[0];\n\t\tnode.parentNode.insertBefore(gads, node);\n\t})();\n</script>\n<script type="text/javascript">\n      if ((/iphone|ipod|ipad.*os /gi).test(navigator.appVersion)) {\n        window.onpageshow = function(evt) {\n          // If persisted then it is in the page cache, force a reload of the page.\n          if (evt.persisted) {\n    \t    window.location.reload();\n          }\n        };\n      }\n</script>\n</head>\n  <body id="home" ontouchstart="">\n  <div tabindex="-1" class="TGTloading" style="display: none">\n    <div class="loading-container">\n      <div class="loading-spinner"></div>\n      <div class="loading-message"></div>\n    </div>\n  </div>\n\t<div id="viewport">\n\t\t\t\t<div id="pageStart"></div>\n\t\t\t</div>\n\t\t<script id="page-meta" type="application/json">\n\t\t{\n  "img_domain" : "http://img3.targetimg3.com",\n  "img_secure_domain" : "https://img3-secure.targetimg3.com",\n  "generated_time" : "Thu Mar 24 02:32:56 EDT 2016",\n  "build_number" : "716-03162016-01",\n  "page_name" : "mProduct",\n  "view_def" : {\n    "header" : [ {\n      "path" : "http://img3.targetimg3.com/wcsstore/marketing/com/mobile/includes/template/header_v2.html",\n      "position" : 1\n    } ],\n    "nav" : [ {\n      "path" : "http://img3.targetimg3.com/wcsstore/marketing/com/mobile/includes/template/header_v2.html",\n      "position" : 1\n    } ],\n    "main_body" : [ {\n      "path" : "mCommonProductPage",\n      "position" : 2,\n      "attribute" : [ {\n        "name" : "rrpcStaticLink",\n        "value" : "/spot/terms/return-policy"\n      }, {\n        "name" : "isNewCheckOut",\n        "value" : "Y"\n      } ]\n    } ],\n    "footer" : [ {\n      "path" : "http://img3.targetimg3.com/wcsstore/marketing/com/mobile/includes/template/header_v2.html",\n      "position" : 1\n    } ]\n  },\n  "page_grid" : "<div id=\\"header\\" class=\\"l-sticky\\" data-name=\\"views/tablet/common/header.view\\"></div><div id=\\"nav\\" data-name=\\"views/tablet/common/nav.view\\"></div><div id=\\"pdp\\" class=\\"main-content l-container-fixed\\" data-page=\\"product details page\\" data-name=\\"views/tablet/browse/pdp.view\\" itemscope=\\"\\" itemtype=\\"http://schema.org/Product\\"></div><div id=\\"fiats\\" data-name=\\"views/tablet/common/fiats.view\\"></div><div id=\\"footer\\" class=\\"footer\\" data-name=\\"views/tablet/common/footer.view\\"></div>",\n  "tracking" : {\n    "attribute" : [ {\n      "name" : "s.prop1",\n      "value" : "product details"\n    }, {\n      "name" : "s.prop4",\n      "value" : "mobile"\n    } ]\n  },\n  "device_info" : {\n    "attribute" : [ {\n      "name" : "deviceType"\n    }, {\n      "name" : "formFactor",\n      "value" : "tablet"\n    } ]\n  },\n  "meta_tags" : {\n    "attribute" : [ {\n      "name" : "title",\n      "value" : "16849119 at Mobile Target"\n    }, {\n      "name" : "description",\n      "value" : "Shop for 16849119 at Mobile Target"\n    }, {\n      "name" : "keywords",\n      "value" : "16849119, 16849119 online, Mobile Target"\n    } ]\n  },\n  "banners" : [ {\n    "id" : "13186697",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/tent-6-person-13186697.html"\n  }, {\n    "id" : "13186698",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/tent-9-person-13186698.html"\n  }, {\n    "id" : "14432134",\n    "position" : "1",\n    "path" : "/com/mobile/en/html/products/20130414_kate.html"\n  } ],\n  "title" : "",\n  "processing_time" : 73,\n  "jsfiles" : [ {\n    "jsfile" : "http://img3.targetimg3.com/wcsstore/marketing/com/mobile/js/template/productDetail_minified.js"\n  } ],\n  "cssfiles" : [ ],\n  "feature" : {\n    "FORESEE" : "false",\n    "TEA_LEAF" : "false",\n    "SECURE_TEA_LEAF" : "false",\n    "FF_ENABLE" : "true",\n    "BV_ENABLED" : "true",\n    "TRACKER" : "false",\n    "SFS_ENABLE" : "true",\n    "FF_PRG_2" : "true",\n    "REGISTRY_RESET_FLAG" : "false",\n    "TNL_COOKIE" : "false",\n    "IS_REPROMISE_ENABLE" : "true",\n    "SHOW_MODAL_BOX" : "true",\n    "ONE_PAGE_CHECKOUT_ENABLE" : "true",\n    "ONE_PAGE_CHECKOUT_ENABLE_FOR_IPAD" : "true",\n    "REVIEW_PAGE_ENABLE_CRTE_ACCT" : "false",\n    "IS_DUMMY_THANK_YOU" : "true",\n    "SEARCH_OPT_FLAG" : "false",\n    "USE_ORDER_ITEM_ID" : "true",\n    "DVM" : "true",\n    "SHIPPING_LIMITED_OFFER" : "false",\n    "PREVIEW_ENABLE" : "false",\n    "ORDER_DETAIL_V1" : "false",\n    "SHOW_CREATE_ACCOUNT" : "true",\n    "SUBSCRIPTION_ENABLED" : "true",\n    "STS_ENABLE" : "true",\n    "SUBS_SHIP_PROMO_MODALMSG" : "true",\n    "PRZ_ENABLE" : "true",\n    "CHKOUT_EXP_ELIGBLE" : "true",\n    "PEAK_HOURS_FLAG" : "false",\n    "THREAT_METRICS_ENABLE" : "true",\n    "ORD_PRZ_ENABLE" : "true",\n    "REDCARD_NEW" : "true",\n    "SLINGSHOT_ENABLED" : "true",\n    "EXPERIAN_EMAIL_SERVICE" : "true",\n    "CART_GET_DEALS" : "false",\n    "APPLE_GIFTCARD_MERCH_CLASS" : "true",\n    "SLING_SHOT_PREVIEW_ENABLE" : "false",\n    "SLINGSHOT_SERVER_CONTROLE" : "false",\n    "IS_CARDINAL" : "false",\n    "ADVANCE_ORDER_CROSSOVER" : "false",\n    "ADVANCE_ORDER_ENABLE" : "true",\n    "MOBILE_ONLY_CHANNEL" : "true",\n    "DELIVERY_DISPLAY_PRICE_ENABLE" : "false",\n    "SITESKIN_ENABLED" : "false",\n    "SUBSCRIPTION_MOD_ENDPOINT" : "true",\n    "SUBSCRIPTION_UI_DISABLED" : "false",\n    "NONSECURE_SIGNIN_OVERLAY_ENABLED" : "true",\n    "ADAPIVE_GC" : "true",\n    "FULL_ADAPTIVE" : "true",\n    "PLP_TO_PDP_PARTIAL_LOAD" : "false",\n    "LIMITED_QTY_ENABLED" : "false",\n    "OBGB_ENABLED" : "true",\n    "ENABLE_TRACKJS" : "false",\n    "REORDER_TWO_TAP_OVERLAY" : "true",\n    "DELIVERY_EMAIL_VALIDATION" : "false",\n    "PAGE_SCRIPT_ENABLE" : "false",\n    "STORE_LIMITED_QTY_ENABLED" : "true",\n    "REPROMISE_OPTIMIZATION_ENABLE" : "true",\n    "WXS_LIMITED_QTY_ENABLED" : "true",\n    "AISLEINFOSERVICE_ENABLE" : "true",\n    "TAG_PAGE_ENABLED" : "true",\n    "CATEGORY_SLINGSHOT_ENABLED" : "true",\n    "SLINGSHOT_HTTP_ENABLED" : "true",\n    "STORE_LOCATOR_SEO_URL" : "true",\n    "CART_PROMO_CODE_ENTRY" : "true",\n    "FF_V3_TO_ATP_ENABLE" : "true",\n    "CRUSH_ACTIVE" : "true",\n    "REFRESH_JOB" : "false",\n    "BROWSE_BY_CATEGORIES_SLINGSHOT" : "true",\n    "FIREFLY_ENABLED" : "true",\n    "REPOPULATE_GEO_COOKIE" : "true",\n    "DEFAULT_TABLET_VIEW" : "true",\n    "PDP_DYNAMIC_PRICING" : "true",\n    "GET_THIS_PHONE" : "true",\n    "GIFT_REGISTRY_RENAME" : "true",\n    "CRUSH_FEED_CURATION" : "true",\n    "EMPTY_CART_DVM_FLAG" : "true",\n    "ENABLE_FORESEE" : "true",\n    "IS_VIEWCART_OPTIMIZED" : "true",\n    "PAYMENT_SERVICES_ENABLED" : "true",\n    "GIFTCARD_ACTIVATION_MSG_ENABLE" : "false",\n    "SUB_RECO" : "false",\n    "PROMO_INJECTION_ENABLED" : "false",\n    "SECURITY_FIX_ENABLED" : "true",\n    "EXPRESS_CHECKOUT" : "true",\n    "OBGB_MSG_ON_LISTING_PAGES" : "true",\n    "FGC_FIX_ENABLE" : "false",\n    "SFS_BACKORDER" : "false",\n    "SHOW_ORDER_OVERLAY" : "true",\n    "USE_MOD_ORDERS" : "false",\n    "PHARMACY_INTERSTITIAL" : "true",\n    "ENABLE_WRITE_REVIEW" : "true",\n    "ENABLE_CRITICAL_REVIEW" : "true",\n    "DISABLE_MOBILE_GC" : "true",\n    "SUBSCRIPTION_FLYOUT" : "true",\n    "SEARCH_INSTEAD_FOR" : "false",\n    "DID_YOU_MEAN" : "false",\n    "ATC_RECOMMANDATIONS" : "false",\n    "SAPPHIRE" : "false",\n    "STORE_LOCATOR_ACCORDION_FIX" : "true",\n    "GAM_REPROMISE_FLYOUT" : "true",\n    "SSX_ENABLED" : "false",\n    "EnableSFL" : "true",\n    "FF_GEO_FEATURE" : "ON",\n    "DEFAULT_PICKUP_WINDOW" : "4",\n    "RELATED_CATEGORY" : "Y",\n    "CATEGORY_FEATURE_BRAND" : "Y",\n    "CATEGORY_GOOGLE_ADS" : "Y",\n    "CATEGORY_DVM_ADS" : "Y",\n    "DVM_CHANNLE_ID" : "mtarget",\n    "TABLET_DVM_CHANNLE_ID" : "target",\n    "SEARCH_OPT_RESP_GROUP" : "VariationSummary,Items",\n    "RUSH_DELIVERY_RADIUS" : "10",\n    "STORE_FINDER" : "100",\n    "RUSH_DEL_BY_ADDR" : "on",\n    "AVAILABILITY_SERVICE_PROD_COUNT" : "10",\n    "STORE_RESULT_LIMIT" : "20",\n    "THREAT_METRICS_ORG_ID" : "9p00aymw",\n    "SLINGSHOT_CATG_ID" : "/slingshot/category/2222222",\n    "FREE_SHIPPING_THRESHHOLD_VALUE" : "25",\n    "AO_MAX_STORES" : "5",\n    "ORD_HISTORY_DAY_LIMIT" : "1",\n    "ORD_HISTORY_COUNT_LIMIT" : "100",\n    "AO_STORES_RADIUS" : "25",\n    "GAM_DASH_ORDERS_LIMIT_COUNT" : "3",\n    "HOOK_LOGIC_KEY" : "764937a9-7afb-4cf1-8631-d8a5edca8f36",\n    "HOOK_LOGIC_ID" : "[CS]v1|2AC0BE5905079201-6000010B000429CD[CE]",\n    "TRACKJS_APPID" : "mobileweb",\n    "TRACKJS_TOKEN" : "913e59b71ca34b21aa95bc55121a0871",\n    "STORE_LIMITED_QTY" : "5",\n    "EVENT_TYPE" : "star",\n    "EVENT_STORES" : "4,61,64,90,93,199,215,221,230,246,301,320,346,348,351,359,361,617,627,636,676,686,687,755,766,769,794,810,818,822,824,827,830,844,861,870,885,911,935,937,938,942,969,992,995,1010,1018,1021,1025,1029,1034,1043,1056,1058,1092,1102,1107,1139,1140,1150,1153,1163,1166,1182,1191,1207,1224,1238,1244,1249,1252,1254,1257,1261,1266,1268,1275,1285,1306,1338,1339,1347,1350,1351,1354,1355,1357,1363,1364,1367,1368,1370,1376,1377,1384,1391,1397,1408,1409,1427,1431,1439,1443,1445,1449,1453,1455,1473,1476,1478,1481,1483,1501,1502,1505,1506,1510,1518,1541,1751,1755,1756,1767,1768,1774,1783,1787,1795,1797,1799,1806,1820,1821,1822,1856,1858,1869,1874,1883,1895,1903,1912,1916,1921,1930,1932,1934,1944,1954,1961,1965,1981,2014,2019,2022,2031,2034,2035,2036,2051,2093,2101,2105,2106,2108,2124,2129,2138,2170,2176,2189,2190,2205,2208,2210,2227,2244,2266,2271,2303,2313,2322,2338,2339,2348,2350,2356,2360,2371,2372,2373,2403,2410,2429,2473,2532,2542,2572,2682,2737,2757,2760,2764,2767,2771,2824,2843",\n    "CRUSH_URL_PROD" : "https://gnc-secure.target.com/guestpreference",\n    "FEED_URL_PROD" : "https://prz-secure.target.com/recommendations/v1?",\n    "MOD_INTEG_BUILD_NUMBER" : "12345",\n    "CRUSH_FEED_MAX" : "96",\n    "ITUNES_MERCH_CLASS" : "PREPAID CARDS, ENTERTAINMENT CARDS, ITUNES, DIGITAL CONTENT, VERIZON CONTRACT, BATTERIES",\n    "INVALID_CALLOUTS" : "testCallOut",\n    "GET_THIS_PHONEURL" : "https://mobile.target.com/web/controller/landing.php?",\n    "DLP_PARAMS" : "[\\"AFID\\",\\"CPNG\\",\\"KID\\",\\"LID\\",\\"LNM\\",\\"MT\\",\\"N\\",\\"gclid\\",\\"ref\\",\\"adgroup\\",\\"network\\",\\"device\\",\\"querystring\\",\\"location\\",\\"gclsrc\\",\\"emseq\\",\\"link\\",\\"tp\\"]",\n    "DYNAMIC_PROMO_VAL" : "TGTA39R9",\n    "PRIVACY_UPDATED_DATE" : "2015-10-26",\n    "ATP_SERVICE_PAYLOAD_MAX_PRODUCTS" : "20",\n    "GIFTCARD_PURCHASED_TODAY_ACTIVATION_24HOURS" : "If you purchased a Target GiftCard on December 20, your gift card will be activated on December 21.",\n    "MERCH_SUBCLASS_ARRAY" : "[{\\"DPCI\\":\\"255-02\\",\\"content\\":\\"atnt\\",\\"corpId\\":\\"596\\"},{\\"DPCI\\":\\"255-04\\",\\"content\\":\\"verizon\\",\\"corpId\\":\\"660\\"},{\\"DPCI\\":\\"255-08\\",\\"content\\":\\"sprint\\",\\"corpId\\":\\"545\\"},{\\"DPCI\\":\\"255-14\\",\\"content\\":\\"iphones\\",\\"corpId\\":\\"731\\"}]",\n    "ORD_HISTORY_RECENT_LIMIT" : "30",\n    "ORD_HISTORY_ALL_LIMIT" : "365",\n    "SERVICE_CALL_DATA_TYPE" : "jsonp",\n    "WHITE_LIST_MERCH_CONTENT" : "merchandizingSlot1"\n  },\n  "datacenter" : "SCS"\n}</script>\n  </body>\n</html>\n\n'soup2 = BeautifulSoup(d.page_source, "html.parser", parse_only=SoupStrainer('div', {'id':'pdpMainContainer'}))
SyntaxError: invalid syntax
>>> soup2 = BeautifulSoup(r.content, "html.parser", parse_only=SoupStrainer('div', {'id':'pdpMainContainer'}))
>>> soup2.find('span', {'itemprop', 'breadcrumb'})
>>> soup2.find('span', {'itemprop', 'breadcrumb'}).text
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    soup2.find('span', {'itemprop', 'breadcrumb'}).text
AttributeError: 'NoneType' object has no attribute 'text'
>>> import socks, socket
>>> socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9150)
>>> socket.socket = socks.socksocket
>>> d = webdriver.Firefox()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
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

>>> from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
>>> dc = DesiredCapabilities.FIREFOX
>>> d = webdriver.Firefox()
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
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

>>> import requests
>>> headers = {'User-Agent': 'Mozilla/5.0'}
>>> 
>>> s = requests.session()
>>> url = 'http://shop.mywebgrocer.com/Browse.aspx?&strid=5F3D126398&catL0=570&catL1=572&catL2=616&catL3=-1&HasProducts=1'
>>> r = s.get(url, headers=headers)
>>> r.status_code
200
>>> soup = BeautifulSoup(r.content, "html.parser", parse_only=SoupStrainer('body'))
>>> soup.find('b', {'class':'ProductDetail-Brand'}).text.replace("\n","").strip()
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    soup.find('b', {'class':'ProductDetail-Brand'}).text.replace("\n","").strip()
AttributeError: 'NoneType' object has no attribute 'text'
>>> len(soup)
1
>>> soup
<body>
<form action="Whoops.aspx?strid=5F3D126398&amp;strid=5F3D126398&amp;wrid=4&amp;wreferrer=http%3a%2f%2fshop.mywebgrocer.com%2fBrowse.aspx%3f&amp;catL0=570&amp;catL1=572&amp;catL2=616&amp;catL3=-1&amp;HasProducts=1" id="frmWhoops" method="post" name="frmWhoops">
<input name="PostBack" type="hidden" value="1"/>
<div style="width:1000px;margin:2px;">
<div style="border:2px solid #000066;">
<table>
<tr>
<td style="background-color:#000066;vertical-align:text-top;">
<img alt="http://mywebgrocer.com" src="i/common/whoops_left.jpg" style="border:none;"/>
</td>
<td>
<div style="color:#000;font-size:12px;font-family:Verdana,arial,helvetica;">
<h1>We are sorry, a problem has occurred  - Invalid Browser</h1>
<p>You have reached this page because we've identified your browser as Unknown v0.0 which is currently unsupported by our application. Please upgrade your browser using one of the links below. Keep in mind that you may need to <i>install</i> a newer version of your browser. </p>
<p style="font-family:Verdana,arial,helvetica;">Additional things to try:</p><ul style="font-family:Verdana,arial,helvetica;"><li>Deleting the browser's Temporary Internet Files and Cookies</li><li>Close your browser (if you have more than one open please close them all)</li><li>Open a browser and start from your store's home page and navigate to the Online Shopping Service again</li></ul>
<div style="width:850px;margin:0 auto;text-align:center;">
<style type="text/css">
  #sbv { font-family: Verdana, "Lucida Grande" ,Tahoma,Helvetica,sans-serif; font-size: 11px; background: #fff; width: 480px; border-collapse: collapse; text-align: left; }
  #sbv caption { padding-bottom: 1em; text-align: center; font-size: 1.4em; font-weight: normal; text-transform: uppercase; letter-spacing: .6em; color: #039; }
  #sbv th { font-size: 12px; font-weight: normal; color: #039; padding: 8px 8px; border-bottom: 2px solid #6678b1; }
  #sbv td { color: #669; border-bottom: 1px solid #ccc; padding: 6px 8px; }
</style>
<table id="sbv" summary="Supported Browser Versions">
<caption>Supported Windows Browsers</caption>
<thead>
<tr>
<th scope="col">Browser</th>
<th scope="col">Minimum<br/>Supported</th>
<th scope="col">Recommended</th>
<th scope="col">Link</th>
</tr>
</thead>
<tbody>
<tr>
<td>Internet Explorer</td>
<td>9.0</td>
<td>11.0</td>
<td><a href="http://windows.microsoft.com/en-us/internet-explorer/download-ie" target="_blank">Download</a></td>
</tr>
<tr>
<td>Firefox</td>
<td>24.0</td>
<td>27.0</td>
<td><a href="http://mozilla.org/firefox" target="_blank">Download</a></td>
</tr>
<tr>
<td>Chrome</td>
<td>29.0</td>
<td>32.0</td>
<td><a href="http://www.google.com/chrome/" target="_blank">Download</a></td>
</tr>
</tbody>
</table>
</div>
</div>
<br/>
<div style="color:#000;font-size:12px;font-family:Verdana,arial,helvetica;font-weight:bold;">
<p>
              If you are still experiencing difficulties, please complete the information below so that a technical 
              representative may provide you with assistance.
              </p>
<table style="border:none;width:850px;margin:0 auto;">
<tr>
<td style="text-align:right;">First Name:</td>
<td><input maxlength="50" name="FName" size="50" type="text" value=""/></td>
</tr>
<tr>
<td style="text-align:right;">Last Name:</td>
<td><input maxlength="50" name="LName" size="50" type="text" value=""/></td>
</tr>
<tr>
<td style="text-align:right;">Which Store?</td>
<td><input maxlength="50" name="StoreName" size="50" type="text" value=""/></td>
</tr>
<tr>
<td style="text-align:right;">Email Address:</td>
<td><input maxlength="200" name="Email" size="50" type="text" value=""/></td>
</tr>
<tr>
<td style="text-align:right;">Phone Number:</td>
<td><input maxlength="50" name="Phone" size="50" type="text" value=""/></td>
</tr>
<tr>
<td style="text-align:right;vertical-align:text-top;">Description of Problem:</td>
<td><textarea cols="50" name="Problem" rows="4"></textarea></td>
</tr>
<tr>
<td style="text-align:right;">Connection Type?</td>
<td>
<input name="Connection" type="radio" value="Dial-up-modem"/>Dial-up modem  
                    <input name="Connection" type="radio" value="Cable-modem"/>Cable modem  
                    <input name="Connection" type="radio" value="Network"/>Network  
                    <input name="Connection" type="radio" value="DSL-Line"/>DSL  
                    <input name="Connection" type="radio" value="Other"/>Other
                  </td>
</tr>
</table>
</div>
<div style="width:850px;margin:0 auto;text-align:center;">
<input id="btnSubmit" name="btnSubmit" type="submit" value="Submit Information"/>
</div>
</td>
</tr>
</table>
</div>
</div>
</form>
<script type="text/javascript">
    var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
    document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
  </script>
<script type="text/javascript">
    try {
      //individual
      var pageTracker = _gat._getTracker("UA-5496062-33");
      pageTracker._trackPageview();

      //global
      var globalTracker = _gat._getTracker("UA-3893611-1");
      globalTracker._trackPageview();
    }
    catch (err) { }
  </script>
</body>
>>> r.url
'https://shop.mywebgrocer.com/whoops.aspx?strid=5F3D126398&strid=5F3D126398&wrid=4&wreferrer=http%3a%2f%2fshop.mywebgrocer.com%2fBrowse.aspx%3f&catL0=570&catL1=572&catL2=616&catL3=-1&HasProducts=1'
>>> url = 'http://www.savannahstate.edu/utilities/SuggestedSearchService.asmx/Find?keyword=%25a%25&numberOfPosts=200&type=employee&subtype=student'
>>> r = s.get(url, headers=headers)
>>> r.content
b'<?xml version="1.0" encoding="utf-8"?>\r\n<ArrayOfSearchResult xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://www.savannahstate.edu">\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaliyah J. Lindquist</LinkText>\r\n    <LinkURL>mailto:alindqui@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alindqui@student.savannahstate.edu"&gt;alindqui@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaliyah Q. Heggs</LinkText>\r\n    <LinkURL>mailto:aheggs@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aheggs@student.savannahstate.edu"&gt;aheggs@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaliyah S. Smith</LinkText>\r\n    <LinkURL>mailto:asmit173@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit173@student.savannahstate.edu"&gt;asmit173@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaren O. Green</LinkText>\r\n    <LinkURL>mailto:agreen36@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agreen36@student.savannahstate.edu"&gt;agreen36@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aarian J. Little</LinkText>\r\n    <LinkURL>mailto:alittle6@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alittle6@student.savannahstate.edu"&gt;alittle6@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron A. McKinnon</LinkText>\r\n    <LinkURL>mailto:amckinn9@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amckinn9@student.savannahstate.edu"&gt;amckinn9@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron D. Hunt</LinkText>\r\n    <LinkURL>mailto:ahunt3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahunt3@student.savannahstate.edu"&gt;ahunt3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron G. Deas</LinkText>\r\n    <LinkURL>mailto:adeas2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adeas2@student.savannahstate.edu"&gt;adeas2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron Grant</LinkText>\r\n    <LinkURL>mailto:agrant19@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agrant19@student.savannahstate.edu"&gt;agrant19@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron J. Mason</LinkText>\r\n    <LinkURL>mailto:amason8@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amason8@student.savannahstate.edu"&gt;amason8@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron J. Udell</LinkText>\r\n    <LinkURL>mailto:audell@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:audell@student.savannahstate.edu"&gt;audell@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn145@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn145@student.savannahstate.edu"&gt;ajohn145@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron M. Polite</LinkText>\r\n    <LinkURL>mailto:apolite4@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apolite4@student.savannahstate.edu"&gt;apolite4@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron P. Odum</LinkText>\r\n    <LinkURL>mailto:aodum@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aodum@student.savannahstate.edu"&gt;aodum@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron Thomas</LinkText>\r\n    <LinkURL>mailto:athoma85@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:athoma85@student.savannahstate.edu"&gt;athoma85@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron X. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn126@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn126@student.savannahstate.edu"&gt;ajohn126@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaryn M. McDade</LinkText>\r\n    <LinkURL>mailto:amcdade1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amcdade1@student.savannahstate.edu"&gt;amcdade1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Abel Reyes</LinkText>\r\n    <LinkURL>mailto:areyes2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:areyes2@student.savannahstate.edu"&gt;areyes2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Abigaile K. Naslund</LinkText>\r\n    <LinkURL>mailto:anaslund@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:anaslund@student.savannahstate.edu"&gt;anaslund@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>A\'bria K. McDonald</LinkText>\r\n    <LinkURL>mailto:amcdona5@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amcdona5@student.savannahstate.edu"&gt;amcdona5@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Acadia D. Plummer</LinkText>\r\n    <LinkURL>mailto:aplumme3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aplumme3@student.savannahstate.edu"&gt;aplumme3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Acasia L. Turner</LinkText>\r\n    <LinkURL>mailto:aturne25@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aturne25@student.savannahstate.edu"&gt;aturne25@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adam A. Walden</LinkText>\r\n    <LinkURL>mailto:awalden3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awalden3@student.savannahstate.edu"&gt;awalden3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adam C. Smith</LinkText>\r\n    <LinkURL>mailto:asmit155@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit155@student.savannahstate.edu"&gt;asmit155@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adam K. Wilkerson</LinkText>\r\n    <LinkURL>mailto:awilkers@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awilkers@student.savannahstate.edu"&gt;awilkers@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adam M. Hower</LinkText>\r\n    <LinkURL>mailto:ahower@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahower@student.savannahstate.edu"&gt;ahower@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adara K. Butts</LinkText>\r\n    <LinkURL>mailto:abutts3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abutts3@student.savannahstate.edu"&gt;abutts3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adarian D. Dunmeyer</LinkText>\r\n    <LinkURL>mailto:adunmeye@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adunmeye@student.savannahstate.edu"&gt;adunmeye@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adayshia L. Carlis</LinkText>\r\n    <LinkURL>mailto:acarlis@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acarlis@student.savannahstate.edu"&gt;acarlis@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Addie Daniels</LinkText>\r\n    <LinkURL>mailto:adanie21@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adanie21@student.savannahstate.edu"&gt;adanie21@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adeola E. Gbadebo</LinkText>\r\n    <LinkURL>mailto:agbadebo@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agbadebo@student.savannahstate.edu"&gt;agbadebo@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adia D. Gilbert</LinkText>\r\n    <LinkURL>mailto:agilbe12@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agilbe12@student.savannahstate.edu"&gt;agilbe12@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adidasheonna N. Sloan</LinkText>\r\n    <LinkURL>mailto:asloan2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asloan2@student.savannahstate.edu"&gt;asloan2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adjani Donald</LinkText>\r\n    <LinkURL>mailto:adonald8@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adonald8@student.savannahstate.edu"&gt;adonald8@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adrainna A. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn212@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn212@student.savannahstate.edu"&gt;ajohn212@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adrian D. Gaither</LinkText>\r\n    <LinkURL>mailto:agaithe1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agaithe1@student.savannahstate.edu"&gt;agaithe1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adrian M. English</LinkText>\r\n    <LinkURL>mailto:aenglis2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aenglis2@student.savannahstate.edu"&gt;aenglis2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adriana J. Thomas</LinkText>\r\n    <LinkURL>mailto:athom101@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:athom101@student.savannahstate.edu"&gt;athom101@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adriana S. Mann</LinkText>\r\n    <LinkURL>mailto:amann1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amann1@student.savannahstate.edu"&gt;amann1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adrianna R. Dawkins</LinkText>\r\n    <LinkURL>mailto:adawkin2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adawkin2@student.savannahstate.edu"&gt;adawkin2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adrienne Kilgore</LinkText>\r\n    <LinkURL>mailto:akilgore@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:akilgore@student.savannahstate.edu"&gt;akilgore@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Afolabi A. Ayangbayi</LinkText>\r\n    <LinkURL>mailto:aayangba@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aayangba@student.savannahstate.edu"&gt;aayangba@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ahkanyala J. Jordan</LinkText>\r\n    <LinkURL>mailto:ajorda15@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajorda15@student.savannahstate.edu"&gt;ajorda15@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ahmaad M. Green</LinkText>\r\n    <LinkURL>mailto:agreen29@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agreen29@student.savannahstate.edu"&gt;agreen29@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ahmad J. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn190@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn190@student.savannahstate.edu"&gt;ajohn190@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ahmir S. Green</LinkText>\r\n    <LinkURL>mailto:agreen51@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agreen51@student.savannahstate.edu"&gt;agreen51@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ahmord O. Rivers</LinkText>\r\n    <LinkURL>mailto:arivers8@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arivers8@student.savannahstate.edu"&gt;arivers8@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aiesha Rankin</LinkText>\r\n    <LinkURL>mailto:arankin@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arankin@student.savannahstate.edu"&gt;arankin@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Airese R. Moss</LinkText>\r\n    <LinkURL>mailto:amoss3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amoss3@student.savannahstate.edu"&gt;amoss3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Airianne T. Wright</LinkText>\r\n    <LinkURL>mailto:awrigh74@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awrigh74@student.savannahstate.edu"&gt;awrigh74@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aisha D. Ross</LinkText>\r\n    <LinkURL>mailto:aross17@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aross17@student.savannahstate.edu"&gt;aross17@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aisha S. Mack</LinkText>\r\n    <LinkURL>mailto:amack13@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amack13@student.savannahstate.edu"&gt;amack13@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aisha Z. Gamble</LinkText>\r\n    <LinkURL>mailto:agamble7@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agamble7@student.savannahstate.edu"&gt;agamble7@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aiyannah C. Peal</LinkText>\r\n    <LinkURL>mailto:apeal@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apeal@student.savannahstate.edu"&gt;apeal@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aja J. Smith</LinkText>\r\n    <LinkURL>mailto:asmit160@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit160@student.savannahstate.edu"&gt;asmit160@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akeem E. Love</LinkText>\r\n    <LinkURL>mailto:alove3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alove3@student.savannahstate.edu"&gt;alove3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akeem H. White</LinkText>\r\n    <LinkURL>mailto:awhite27@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awhite27@student.savannahstate.edu"&gt;awhite27@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akeem J. Williams</LinkText>\r\n    <LinkURL>mailto:awill248@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awill248@student.savannahstate.edu"&gt;awill248@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akeya S. Hurt</LinkText>\r\n    <LinkURL>mailto:ahurt2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahurt2@student.savannahstate.edu"&gt;ahurt2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akira T. Warren</LinkText>\r\n    <LinkURL>mailto:awarren4@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awarren4@student.savannahstate.edu"&gt;awarren4@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akirya R. Blair</LinkText>\r\n    <LinkURL>mailto:ablair2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ablair2@student.savannahstate.edu"&gt;ablair2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akivia M. Blue</LinkText>\r\n    <LinkURL>mailto:ablue4@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ablue4@student.savannahstate.edu"&gt;ablue4@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alacia D. Platts</LinkText>\r\n    <LinkURL>mailto:aplatts@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aplatts@student.savannahstate.edu"&gt;aplatts@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>A\'laija S. Gardner</LinkText>\r\n    <LinkURL>mailto:agardn11@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agardn11@student.savannahstate.edu"&gt;agardn11@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alaina P. Monroe</LinkText>\r\n    <LinkURL>mailto:amonroe1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amonroe1@student.savannahstate.edu"&gt;amonroe1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alakenisa R. Thorpe</LinkText>\r\n    <LinkURL>mailto:athorpe@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:athorpe@student.savannahstate.edu"&gt;athorpe@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alana M. Harris</LinkText>\r\n    <LinkURL>mailto:aharr100@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aharr100@student.savannahstate.edu"&gt;aharr100@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alana S. Reese</LinkText>\r\n    <LinkURL>mailto:areese13@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:areese13@student.savannahstate.edu"&gt;areese13@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alana V. Green</LinkText>\r\n    <LinkURL>mailto:agreen30@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agreen30@student.savannahstate.edu"&gt;agreen30@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alanna M. Puzzuoli</LinkText>\r\n    <LinkURL>mailto:apuzzuol@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apuzzuol@student.savannahstate.edu"&gt;apuzzuol@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alannah N. Jackson</LinkText>\r\n    <LinkURL>mailto:ajacks82@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajacks82@student.savannahstate.edu"&gt;ajacks82@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alayna P. Stovall</LinkText>\r\n    <LinkURL>mailto:astovall@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:astovall@student.savannahstate.edu"&gt;astovall@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alaysia S. Brown-Kelly</LinkText>\r\n    <LinkURL>mailto:abrownke@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrownke@student.savannahstate.edu"&gt;abrownke@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Albert C. Rumph</LinkText>\r\n    <LinkURL>mailto:arumph1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arumph1@student.savannahstate.edu"&gt;arumph1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Albrena J. Jelks</LinkText>\r\n    <LinkURL>mailto:ajelks@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajelks@student.savannahstate.edu"&gt;ajelks@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alec J. Brown</LinkText>\r\n    <LinkURL>mailto:abrow118@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrow118@student.savannahstate.edu"&gt;abrow118@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aleeyah L. Hardwick</LinkText>\r\n    <LinkURL>mailto:ahardwi1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahardwi1@student.savannahstate.edu"&gt;ahardwi1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alerie T. Roberts</LinkText>\r\n    <LinkURL>mailto:arober34@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arober34@student.savannahstate.edu"&gt;arober34@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alescia S. Washington</LinkText>\r\n    <LinkURL>mailto:awashi40@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awashi40@student.savannahstate.edu"&gt;awashi40@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alesha M. Boles-Johnson</LinkText>\r\n    <LinkURL>mailto:abolesjo@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abolesjo@student.savannahstate.edu"&gt;abolesjo@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alesha M. Moore</LinkText>\r\n    <LinkURL>mailto:amoore48@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amoore48@student.savannahstate.edu"&gt;amoore48@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex A. Fulks</LinkText>\r\n    <LinkURL>mailto:afulksjr@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:afulksjr@student.savannahstate.edu"&gt;afulksjr@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex Brown</LinkText>\r\n    <LinkURL>mailto:abrown63@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrown63@student.savannahstate.edu"&gt;abrown63@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex J. Simmons</LinkText>\r\n    <LinkURL>mailto:asimmo12@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asimmo12@student.savannahstate.edu"&gt;asimmo12@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex J. Wright</LinkText>\r\n    <LinkURL>mailto:awrigh76@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awrigh76@student.savannahstate.edu"&gt;awrigh76@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex M. Koonce</LinkText>\r\n    <LinkURL>mailto:akoonce@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:akoonce@student.savannahstate.edu"&gt;akoonce@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex M. Nichols</LinkText>\r\n    <LinkURL>mailto:anichol7@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:anichol7@student.savannahstate.edu"&gt;anichol7@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex R. Weaver</LinkText>\r\n    <LinkURL>mailto:aweaver5@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aweaver5@student.savannahstate.edu"&gt;aweaver5@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex T. Pierce</LinkText>\r\n    <LinkURL>mailto:apierc18@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apierc18@student.savannahstate.edu"&gt;apierc18@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex W. Barrett</LinkText>\r\n    <LinkURL>mailto:abarret6@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abarret6@student.savannahstate.edu"&gt;abarret6@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexander A. Reid</LinkText>\r\n    <LinkURL>mailto:areid10@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:areid10@student.savannahstate.edu"&gt;areid10@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexander A. Taul</LinkText>\r\n    <LinkURL>mailto:ataul@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ataul@student.savannahstate.edu"&gt;ataul@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexander Q. Grier</LinkText>\r\n    <LinkURL>mailto:agrier1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agrier1@student.savannahstate.edu"&gt;agrier1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexander V. Ontivero</LinkText>\r\n    <LinkURL>mailto:aontiver@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aontiver@student.savannahstate.edu"&gt;aontiver@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexander Y. Holcey</LinkText>\r\n    <LinkURL>mailto:aholcey@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aholcey@student.savannahstate.edu"&gt;aholcey@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexanderia N. Dixon</LinkText>\r\n    <LinkURL>mailto:adixon12@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adixon12@student.savannahstate.edu"&gt;adixon12@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexandra I. Kinney</LinkText>\r\n    <LinkURL>mailto:akinney@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:akinney@student.savannahstate.edu"&gt;akinney@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexandra X. Cabell</LinkText>\r\n    <LinkURL>mailto:acabell@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acabell@student.savannahstate.edu"&gt;acabell@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexandrea L. Vereen</LinkText>\r\n    <LinkURL>mailto:avereen1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:avereen1@student.savannahstate.edu"&gt;avereen1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexandrea Mann</LinkText>\r\n    <LinkURL>mailto:amann3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amann3@student.savannahstate.edu"&gt;amann3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexandria Ambrose</LinkText>\r\n    <LinkURL>mailto:aambros1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aambros1@student.savannahstate.edu"&gt;aambros1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex-Aundryah Duporte</LinkText>\r\n    <LinkURL>mailto:aduporte@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aduporte@student.savannahstate.edu"&gt;aduporte@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexcia G. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn181@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn181@student.savannahstate.edu"&gt;ajohn181@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexcia R. Cooper</LinkText>\r\n    <LinkURL>mailto:acoope22@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acoope22@student.savannahstate.edu"&gt;acoope22@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexi K. Gaboriault</LinkText>\r\n    <LinkURL>mailto:agaboria@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agaboria@student.savannahstate.edu"&gt;agaboria@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexia L. Singleton</LinkText>\r\n    <LinkURL>mailto:asingl13@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asingl13@student.savannahstate.edu"&gt;asingl13@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexia T. Ewell</LinkText>\r\n    <LinkURL>mailto:aewell@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aewell@student.savannahstate.edu"&gt;aewell@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis B. Brown</LinkText>\r\n    <LinkURL>mailto:abrow124@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrow124@student.savannahstate.edu"&gt;abrow124@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis B. Haynes</LinkText>\r\n    <LinkURL>mailto:ahaynes9@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahaynes9@student.savannahstate.edu"&gt;ahaynes9@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis C. Flowers</LinkText>\r\n    <LinkURL>mailto:aflower4@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aflower4@student.savannahstate.edu"&gt;aflower4@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis C. McIver</LinkText>\r\n    <LinkURL>mailto:amciver1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amciver1@student.savannahstate.edu"&gt;amciver1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis C. Zeigler</LinkText>\r\n    <LinkURL>mailto:azeigler@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:azeigler@student.savannahstate.edu"&gt;azeigler@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis D. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn179@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn179@student.savannahstate.edu"&gt;ajohn179@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis D. Webb</LinkText>\r\n    <LinkURL>mailto:awebb6@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awebb6@student.savannahstate.edu"&gt;awebb6@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis E. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn213@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn213@student.savannahstate.edu"&gt;ajohn213@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis F. Richard</LinkText>\r\n    <LinkURL>mailto:aricha29@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aricha29@student.savannahstate.edu"&gt;aricha29@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis I. Fleming</LinkText>\r\n    <LinkURL>mailto:aflemin4@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aflemin4@student.savannahstate.edu"&gt;aflemin4@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis J. Abollo</LinkText>\r\n    <LinkURL>mailto:aabollo@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aabollo@student.savannahstate.edu"&gt;aabollo@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis J. Gilmore</LinkText>\r\n    <LinkURL>mailto:agilmor2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agilmor2@student.savannahstate.edu"&gt;agilmor2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis K. Glenn</LinkText>\r\n    <LinkURL>mailto:aglenn2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aglenn2@student.savannahstate.edu"&gt;aglenn2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis K. Pointer</LinkText>\r\n    <LinkURL>mailto:apointer@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apointer@student.savannahstate.edu"&gt;apointer@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis L. Crawford</LinkText>\r\n    <LinkURL>mailto:acrawf19@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acrawf19@student.savannahstate.edu"&gt;acrawf19@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis L. Wade</LinkText>\r\n    <LinkURL>mailto:awade3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awade3@student.savannahstate.edu"&gt;awade3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis L. Washington</LinkText>\r\n    <LinkURL>mailto:awashi44@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awashi44@student.savannahstate.edu"&gt;awashi44@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis N. Baird</LinkText>\r\n    <LinkURL>mailto:abaird1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abaird1@student.savannahstate.edu"&gt;abaird1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis N. Singleton</LinkText>\r\n    <LinkURL>mailto:asingl11@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asingl11@student.savannahstate.edu"&gt;asingl11@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis N. Smith</LinkText>\r\n    <LinkURL>mailto:asmit125@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit125@student.savannahstate.edu"&gt;asmit125@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis N. Williams</LinkText>\r\n    <LinkURL>mailto:awill265@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awill265@student.savannahstate.edu"&gt;awill265@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis P. Collado</LinkText>\r\n    <LinkURL>mailto:acollado@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acollado@student.savannahstate.edu"&gt;acollado@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis Parker</LinkText>\r\n    <LinkURL>mailto:aparke26@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aparke26@student.savannahstate.edu"&gt;aparke26@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis R. Robinson</LinkText>\r\n    <LinkURL>mailto:arobin46@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arobin46@student.savannahstate.edu"&gt;arobin46@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis S. Arnold</LinkText>\r\n    <LinkURL>mailto:aarnol14@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aarnol14@student.savannahstate.edu"&gt;aarnol14@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis S. Evans</LinkText>\r\n    <LinkURL>mailto:aevans27@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aevans27@student.savannahstate.edu"&gt;aevans27@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis S. Tuggle</LinkText>\r\n    <LinkURL>mailto:atuggle2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:atuggle2@student.savannahstate.edu"&gt;atuggle2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis T. Halston</LinkText>\r\n    <LinkURL>mailto:ahalston@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahalston@student.savannahstate.edu"&gt;ahalston@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis T. Thompson</LinkText>\r\n    <LinkURL>mailto:athomp41@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:athomp41@student.savannahstate.edu"&gt;athomp41@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis T. Watts</LinkText>\r\n    <LinkURL>mailto:awatts9@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awatts9@student.savannahstate.edu"&gt;awatts9@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis V. Washington</LinkText>\r\n    <LinkURL>mailto:awashi45@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awashi45@student.savannahstate.edu"&gt;awashi45@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis V. Williams</LinkText>\r\n    <LinkURL>mailto:awillima@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awillima@student.savannahstate.edu"&gt;awillima@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexsia C. McClary</LinkText>\r\n    <LinkURL>mailto:amcclary@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amcclary@student.savannahstate.edu"&gt;amcclary@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexsia D. Brown</LinkText>\r\n    <LinkURL>mailto:abrow120@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrow120@student.savannahstate.edu"&gt;abrow120@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexsis Q. Martin</LinkText>\r\n    <LinkURL>mailto:amarti37@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amarti37@student.savannahstate.edu"&gt;amarti37@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus B. Collins</LinkText>\r\n    <LinkURL>mailto:acolli23@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acolli23@student.savannahstate.edu"&gt;acolli23@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus D. Byrd</LinkText>\r\n    <LinkURL>mailto:abyrd12@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abyrd12@student.savannahstate.edu"&gt;abyrd12@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus D. Robinson</LinkText>\r\n    <LinkURL>mailto:arobin52@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arobin52@student.savannahstate.edu"&gt;arobin52@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus E. Cannon</LinkText>\r\n    <LinkURL>mailto:acannon2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acannon2@student.savannahstate.edu"&gt;acannon2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus E. Reed</LinkText>\r\n    <LinkURL>mailto:areed16@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:areed16@student.savannahstate.edu"&gt;areed16@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus I. Flores</LinkText>\r\n    <LinkURL>mailto:aflores1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aflores1@student.savannahstate.edu"&gt;aflores1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus M. Neal</LinkText>\r\n    <LinkURL>mailto:aneal6@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aneal6@student.savannahstate.edu"&gt;aneal6@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus S. Bryant</LinkText>\r\n    <LinkURL>mailto:abryan27@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abryan27@student.savannahstate.edu"&gt;abryan27@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus S. Holley</LinkText>\r\n    <LinkURL>mailto:aholley3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aholley3@student.savannahstate.edu"&gt;aholley3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus S. Stone</LinkText>\r\n    <LinkURL>mailto:astone3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:astone3@student.savannahstate.edu"&gt;astone3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus S. Williams</LinkText>\r\n    <LinkURL>mailto:awill130@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awill130@student.savannahstate.edu"&gt;awill130@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus S. Williams</LinkText>\r\n    <LinkURL>mailto:awill242@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awill242@student.savannahstate.edu"&gt;awill242@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus T. Hampton</LinkText>\r\n    <LinkURL>mailto:ahampto7@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahampto7@student.savannahstate.edu"&gt;ahampto7@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexxa Jernigan</LinkText>\r\n    <LinkURL>mailto:ajernig3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajernig3@student.savannahstate.edu"&gt;ajernig3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alfatine A. Gardner</LinkText>\r\n    <LinkURL>mailto:agardne9@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agardne9@student.savannahstate.edu"&gt;agardne9@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alfonzo D. Berry</LinkText>\r\n    <LinkURL>mailto:aberry6@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aberry6@student.savannahstate.edu"&gt;aberry6@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ali S. Steed</LinkText>\r\n    <LinkURL>mailto:asteed@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asteed@student.savannahstate.edu"&gt;asteed@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alia D. Tascoe El</LinkText>\r\n    <LinkURL>mailto:atascoee@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:atascoee@student.savannahstate.edu"&gt;atascoee@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alia K. Hill</LinkText>\r\n    <LinkURL>mailto:ahill45@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahill45@student.savannahstate.edu"&gt;ahill45@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alia N. Hawes</LinkText>\r\n    <LinkURL>mailto:ahawes2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahawes2@student.savannahstate.edu"&gt;ahawes2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia Blain</LinkText>\r\n    <LinkURL>mailto:ablain@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ablain@student.savannahstate.edu"&gt;ablain@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia D. Tanner</LinkText>\r\n    <LinkURL>mailto:atanner1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:atanner1@student.savannahstate.edu"&gt;atanner1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia E. Lambert</LinkText>\r\n    <LinkURL>mailto:alamber3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alamber3@student.savannahstate.edu"&gt;alamber3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia K. Lawton</LinkText>\r\n    <LinkURL>mailto:alawton1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alawton1@student.savannahstate.edu"&gt;alawton1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia L. Frontera</LinkText>\r\n    <LinkURL>mailto:afronter@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:afronter@student.savannahstate.edu"&gt;afronter@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia Montgomery</LinkText>\r\n    <LinkURL>mailto:amontgo5@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amontgo5@student.savannahstate.edu"&gt;amontgo5@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alisa A. Baker</LinkText>\r\n    <LinkURL>mailto:abaker10@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abaker10@student.savannahstate.edu"&gt;abaker10@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alisa B. Ellis</LinkText>\r\n    <LinkURL>mailto:aellis8@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aellis8@student.savannahstate.edu"&gt;aellis8@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alison Hill</LinkText>\r\n    <LinkURL>mailto:ahill42@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahill42@student.savannahstate.edu"&gt;ahill42@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alison J. Morgan</LinkText>\r\n    <LinkURL>mailto:amorga10@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amorga10@student.savannahstate.edu"&gt;amorga10@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliya D. Barkley</LinkText>\r\n    <LinkURL>mailto:abarkle2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abarkle2@student.savannahstate.edu"&gt;abarkle2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliya N. Wharton</LinkText>\r\n    <LinkURL>mailto:awharton@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awharton@student.savannahstate.edu"&gt;awharton@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah C. Davis</LinkText>\r\n    <LinkURL>mailto:adavis94@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adavis94@student.savannahstate.edu"&gt;adavis94@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah C. Moore</LinkText>\r\n    <LinkURL>mailto:amoore41@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amoore41@student.savannahstate.edu"&gt;amoore41@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah D. Moultrie</LinkText>\r\n    <LinkURL>mailto:amoultr3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amoultr3@student.savannahstate.edu"&gt;amoultr3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah J. Duffey</LinkText>\r\n    <LinkURL>mailto:aduffey@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aduffey@student.savannahstate.edu"&gt;aduffey@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah M. Lewis</LinkText>\r\n    <LinkURL>mailto:alewis49@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alewis49@student.savannahstate.edu"&gt;alewis49@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah M. Toney</LinkText>\r\n    <LinkURL>mailto:atoney1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:atoney1@student.savannahstate.edu"&gt;atoney1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah R. Smith</LinkText>\r\n    <LinkURL>mailto:asmit131@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit131@student.savannahstate.edu"&gt;asmit131@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah S. Bryant</LinkText>\r\n    <LinkURL>mailto:abryan37@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abryan37@student.savannahstate.edu"&gt;abryan37@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah Y. Parker</LinkText>\r\n    <LinkURL>mailto:aparke19@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aparke19@student.savannahstate.edu"&gt;aparke19@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allante R. Smith</LinkText>\r\n    <LinkURL>mailto:asmith86@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmith86@student.savannahstate.edu"&gt;asmith86@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allea E. Campbell</LinkText>\r\n    <LinkURL>mailto:acampb15@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acampb15@student.savannahstate.edu"&gt;acampb15@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allegria T. Hutchins</LinkText>\r\n    <LinkURL>mailto:ahutchi2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahutchi2@student.savannahstate.edu"&gt;ahutchi2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allen C. Robinson</LinkText>\r\n    <LinkURL>mailto:arobin58@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arobin58@student.savannahstate.edu"&gt;arobin58@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allen E. Bell</LinkText>\r\n    <LinkURL>mailto:abell19@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abell19@student.savannahstate.edu"&gt;abell19@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allen M. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn139@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn139@student.savannahstate.edu"&gt;ajohn139@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allendria T. Brown</LinkText>\r\n    <LinkURL>mailto:abrow152@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrow152@student.savannahstate.edu"&gt;abrow152@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alliyah M. Lowder</LinkText>\r\n    <LinkURL>mailto:alowder1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alowder1@student.savannahstate.edu"&gt;alowder1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allye A. Sneed</LinkText>\r\n    <LinkURL>mailto:asneed2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asneed2@student.savannahstate.edu"&gt;asneed2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alma B. Sapateh</LinkText>\r\n    <LinkURL>mailto:asapateh@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asapateh@student.savannahstate.edu"&gt;asapateh@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Al\'neisha J. Randall</LinkText>\r\n    <LinkURL>mailto:arandal3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arandal3@student.savannahstate.edu"&gt;arandal3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alneka K. Smith</LinkText>\r\n    <LinkURL>mailto:asmit149@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit149@student.savannahstate.edu"&gt;asmit149@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alonna D. Preyer</LinkText>\r\n    <LinkURL>mailto:apreyer@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apreyer@student.savannahstate.edu"&gt;apreyer@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alonzo A. Francis</LinkText>\r\n    <LinkURL>mailto:afranci3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:afranci3@student.savannahstate.edu"&gt;afranci3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alonzo Baker</LinkText>\r\n    <LinkURL>mailto:abaker23@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abaker23@student.savannahstate.edu"&gt;abaker23@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Altonnett E. Guyton</LinkText>\r\n    <LinkURL>mailto:aguyton2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aguyton2@student.savannahstate.edu"&gt;aguyton2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alysha M. Wright</LinkText>\r\n    <LinkURL>mailto:awrigh63@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awrigh63@student.savannahstate.edu"&gt;awrigh63@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n</ArrayOfSearchResult>'
>>> from xml.dom.minidom import parse
>>> import xml.dom.minidom
>>> DOMTree = xml.dom.minidom.parse(r.content)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    DOMTree = xml.dom.minidom.parse(r.content)
  File "/home/ramakrishna/anaconda3/lib/python3.5/xml/dom/minidom.py", line 1958, in parse
    return expatbuilder.parse(file)
  File "/home/ramakrishna/anaconda3/lib/python3.5/xml/dom/expatbuilder.py", line 913, in parse
    result = builder.parseFile(file)
  File "/home/ramakrishna/anaconda3/lib/python3.5/xml/dom/expatbuilder.py", line 204, in parseFile
    buffer = file.read(16*1024)
AttributeError: 'bytes' object has no attribute 'read'
>>> r.text
'<?xml version="1.0" encoding="utf-8"?>\r\n<ArrayOfSearchResult xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://www.savannahstate.edu">\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaliyah J. Lindquist</LinkText>\r\n    <LinkURL>mailto:alindqui@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alindqui@student.savannahstate.edu"&gt;alindqui@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaliyah Q. Heggs</LinkText>\r\n    <LinkURL>mailto:aheggs@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aheggs@student.savannahstate.edu"&gt;aheggs@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaliyah S. Smith</LinkText>\r\n    <LinkURL>mailto:asmit173@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit173@student.savannahstate.edu"&gt;asmit173@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaren O. Green</LinkText>\r\n    <LinkURL>mailto:agreen36@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agreen36@student.savannahstate.edu"&gt;agreen36@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aarian J. Little</LinkText>\r\n    <LinkURL>mailto:alittle6@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alittle6@student.savannahstate.edu"&gt;alittle6@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron A. McKinnon</LinkText>\r\n    <LinkURL>mailto:amckinn9@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amckinn9@student.savannahstate.edu"&gt;amckinn9@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron D. Hunt</LinkText>\r\n    <LinkURL>mailto:ahunt3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahunt3@student.savannahstate.edu"&gt;ahunt3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron G. Deas</LinkText>\r\n    <LinkURL>mailto:adeas2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adeas2@student.savannahstate.edu"&gt;adeas2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron Grant</LinkText>\r\n    <LinkURL>mailto:agrant19@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agrant19@student.savannahstate.edu"&gt;agrant19@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron J. Mason</LinkText>\r\n    <LinkURL>mailto:amason8@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amason8@student.savannahstate.edu"&gt;amason8@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron J. Udell</LinkText>\r\n    <LinkURL>mailto:audell@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:audell@student.savannahstate.edu"&gt;audell@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn145@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn145@student.savannahstate.edu"&gt;ajohn145@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron M. Polite</LinkText>\r\n    <LinkURL>mailto:apolite4@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apolite4@student.savannahstate.edu"&gt;apolite4@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron P. Odum</LinkText>\r\n    <LinkURL>mailto:aodum@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aodum@student.savannahstate.edu"&gt;aodum@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron Thomas</LinkText>\r\n    <LinkURL>mailto:athoma85@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:athoma85@student.savannahstate.edu"&gt;athoma85@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron X. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn126@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn126@student.savannahstate.edu"&gt;ajohn126@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaryn M. McDade</LinkText>\r\n    <LinkURL>mailto:amcdade1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amcdade1@student.savannahstate.edu"&gt;amcdade1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Abel Reyes</LinkText>\r\n    <LinkURL>mailto:areyes2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:areyes2@student.savannahstate.edu"&gt;areyes2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Abigaile K. Naslund</LinkText>\r\n    <LinkURL>mailto:anaslund@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:anaslund@student.savannahstate.edu"&gt;anaslund@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>A\'bria K. McDonald</LinkText>\r\n    <LinkURL>mailto:amcdona5@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amcdona5@student.savannahstate.edu"&gt;amcdona5@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Acadia D. Plummer</LinkText>\r\n    <LinkURL>mailto:aplumme3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aplumme3@student.savannahstate.edu"&gt;aplumme3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Acasia L. Turner</LinkText>\r\n    <LinkURL>mailto:aturne25@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aturne25@student.savannahstate.edu"&gt;aturne25@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adam A. Walden</LinkText>\r\n    <LinkURL>mailto:awalden3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awalden3@student.savannahstate.edu"&gt;awalden3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adam C. Smith</LinkText>\r\n    <LinkURL>mailto:asmit155@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit155@student.savannahstate.edu"&gt;asmit155@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adam K. Wilkerson</LinkText>\r\n    <LinkURL>mailto:awilkers@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awilkers@student.savannahstate.edu"&gt;awilkers@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adam M. Hower</LinkText>\r\n    <LinkURL>mailto:ahower@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahower@student.savannahstate.edu"&gt;ahower@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adara K. Butts</LinkText>\r\n    <LinkURL>mailto:abutts3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abutts3@student.savannahstate.edu"&gt;abutts3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adarian D. Dunmeyer</LinkText>\r\n    <LinkURL>mailto:adunmeye@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adunmeye@student.savannahstate.edu"&gt;adunmeye@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adayshia L. Carlis</LinkText>\r\n    <LinkURL>mailto:acarlis@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acarlis@student.savannahstate.edu"&gt;acarlis@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Addie Daniels</LinkText>\r\n    <LinkURL>mailto:adanie21@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adanie21@student.savannahstate.edu"&gt;adanie21@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adeola E. Gbadebo</LinkText>\r\n    <LinkURL>mailto:agbadebo@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agbadebo@student.savannahstate.edu"&gt;agbadebo@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adia D. Gilbert</LinkText>\r\n    <LinkURL>mailto:agilbe12@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agilbe12@student.savannahstate.edu"&gt;agilbe12@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adidasheonna N. Sloan</LinkText>\r\n    <LinkURL>mailto:asloan2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asloan2@student.savannahstate.edu"&gt;asloan2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adjani Donald</LinkText>\r\n    <LinkURL>mailto:adonald8@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adonald8@student.savannahstate.edu"&gt;adonald8@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adrainna A. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn212@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn212@student.savannahstate.edu"&gt;ajohn212@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adrian D. Gaither</LinkText>\r\n    <LinkURL>mailto:agaithe1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agaithe1@student.savannahstate.edu"&gt;agaithe1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adrian M. English</LinkText>\r\n    <LinkURL>mailto:aenglis2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aenglis2@student.savannahstate.edu"&gt;aenglis2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adriana J. Thomas</LinkText>\r\n    <LinkURL>mailto:athom101@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:athom101@student.savannahstate.edu"&gt;athom101@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adriana S. Mann</LinkText>\r\n    <LinkURL>mailto:amann1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amann1@student.savannahstate.edu"&gt;amann1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adrianna R. Dawkins</LinkText>\r\n    <LinkURL>mailto:adawkin2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adawkin2@student.savannahstate.edu"&gt;adawkin2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adrienne Kilgore</LinkText>\r\n    <LinkURL>mailto:akilgore@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:akilgore@student.savannahstate.edu"&gt;akilgore@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Afolabi A. Ayangbayi</LinkText>\r\n    <LinkURL>mailto:aayangba@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aayangba@student.savannahstate.edu"&gt;aayangba@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ahkanyala J. Jordan</LinkText>\r\n    <LinkURL>mailto:ajorda15@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajorda15@student.savannahstate.edu"&gt;ajorda15@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ahmaad M. Green</LinkText>\r\n    <LinkURL>mailto:agreen29@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agreen29@student.savannahstate.edu"&gt;agreen29@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ahmad J. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn190@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn190@student.savannahstate.edu"&gt;ajohn190@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ahmir S. Green</LinkText>\r\n    <LinkURL>mailto:agreen51@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agreen51@student.savannahstate.edu"&gt;agreen51@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ahmord O. Rivers</LinkText>\r\n    <LinkURL>mailto:arivers8@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arivers8@student.savannahstate.edu"&gt;arivers8@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aiesha Rankin</LinkText>\r\n    <LinkURL>mailto:arankin@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arankin@student.savannahstate.edu"&gt;arankin@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Airese R. Moss</LinkText>\r\n    <LinkURL>mailto:amoss3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amoss3@student.savannahstate.edu"&gt;amoss3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Airianne T. Wright</LinkText>\r\n    <LinkURL>mailto:awrigh74@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awrigh74@student.savannahstate.edu"&gt;awrigh74@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aisha D. Ross</LinkText>\r\n    <LinkURL>mailto:aross17@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aross17@student.savannahstate.edu"&gt;aross17@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aisha S. Mack</LinkText>\r\n    <LinkURL>mailto:amack13@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amack13@student.savannahstate.edu"&gt;amack13@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aisha Z. Gamble</LinkText>\r\n    <LinkURL>mailto:agamble7@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agamble7@student.savannahstate.edu"&gt;agamble7@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aiyannah C. Peal</LinkText>\r\n    <LinkURL>mailto:apeal@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apeal@student.savannahstate.edu"&gt;apeal@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aja J. Smith</LinkText>\r\n    <LinkURL>mailto:asmit160@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit160@student.savannahstate.edu"&gt;asmit160@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akeem E. Love</LinkText>\r\n    <LinkURL>mailto:alove3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alove3@student.savannahstate.edu"&gt;alove3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akeem H. White</LinkText>\r\n    <LinkURL>mailto:awhite27@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awhite27@student.savannahstate.edu"&gt;awhite27@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akeem J. Williams</LinkText>\r\n    <LinkURL>mailto:awill248@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awill248@student.savannahstate.edu"&gt;awill248@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akeya S. Hurt</LinkText>\r\n    <LinkURL>mailto:ahurt2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahurt2@student.savannahstate.edu"&gt;ahurt2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akira T. Warren</LinkText>\r\n    <LinkURL>mailto:awarren4@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awarren4@student.savannahstate.edu"&gt;awarren4@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akirya R. Blair</LinkText>\r\n    <LinkURL>mailto:ablair2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ablair2@student.savannahstate.edu"&gt;ablair2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akivia M. Blue</LinkText>\r\n    <LinkURL>mailto:ablue4@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ablue4@student.savannahstate.edu"&gt;ablue4@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alacia D. Platts</LinkText>\r\n    <LinkURL>mailto:aplatts@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aplatts@student.savannahstate.edu"&gt;aplatts@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>A\'laija S. Gardner</LinkText>\r\n    <LinkURL>mailto:agardn11@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agardn11@student.savannahstate.edu"&gt;agardn11@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alaina P. Monroe</LinkText>\r\n    <LinkURL>mailto:amonroe1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amonroe1@student.savannahstate.edu"&gt;amonroe1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alakenisa R. Thorpe</LinkText>\r\n    <LinkURL>mailto:athorpe@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:athorpe@student.savannahstate.edu"&gt;athorpe@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alana M. Harris</LinkText>\r\n    <LinkURL>mailto:aharr100@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aharr100@student.savannahstate.edu"&gt;aharr100@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alana S. Reese</LinkText>\r\n    <LinkURL>mailto:areese13@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:areese13@student.savannahstate.edu"&gt;areese13@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alana V. Green</LinkText>\r\n    <LinkURL>mailto:agreen30@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agreen30@student.savannahstate.edu"&gt;agreen30@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alanna M. Puzzuoli</LinkText>\r\n    <LinkURL>mailto:apuzzuol@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apuzzuol@student.savannahstate.edu"&gt;apuzzuol@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alannah N. Jackson</LinkText>\r\n    <LinkURL>mailto:ajacks82@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajacks82@student.savannahstate.edu"&gt;ajacks82@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alayna P. Stovall</LinkText>\r\n    <LinkURL>mailto:astovall@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:astovall@student.savannahstate.edu"&gt;astovall@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alaysia S. Brown-Kelly</LinkText>\r\n    <LinkURL>mailto:abrownke@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrownke@student.savannahstate.edu"&gt;abrownke@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Albert C. Rumph</LinkText>\r\n    <LinkURL>mailto:arumph1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arumph1@student.savannahstate.edu"&gt;arumph1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Albrena J. Jelks</LinkText>\r\n    <LinkURL>mailto:ajelks@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajelks@student.savannahstate.edu"&gt;ajelks@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alec J. Brown</LinkText>\r\n    <LinkURL>mailto:abrow118@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrow118@student.savannahstate.edu"&gt;abrow118@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aleeyah L. Hardwick</LinkText>\r\n    <LinkURL>mailto:ahardwi1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahardwi1@student.savannahstate.edu"&gt;ahardwi1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alerie T. Roberts</LinkText>\r\n    <LinkURL>mailto:arober34@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arober34@student.savannahstate.edu"&gt;arober34@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alescia S. Washington</LinkText>\r\n    <LinkURL>mailto:awashi40@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awashi40@student.savannahstate.edu"&gt;awashi40@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alesha M. Boles-Johnson</LinkText>\r\n    <LinkURL>mailto:abolesjo@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abolesjo@student.savannahstate.edu"&gt;abolesjo@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alesha M. Moore</LinkText>\r\n    <LinkURL>mailto:amoore48@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amoore48@student.savannahstate.edu"&gt;amoore48@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex A. Fulks</LinkText>\r\n    <LinkURL>mailto:afulksjr@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:afulksjr@student.savannahstate.edu"&gt;afulksjr@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex Brown</LinkText>\r\n    <LinkURL>mailto:abrown63@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrown63@student.savannahstate.edu"&gt;abrown63@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex J. Simmons</LinkText>\r\n    <LinkURL>mailto:asimmo12@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asimmo12@student.savannahstate.edu"&gt;asimmo12@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex J. Wright</LinkText>\r\n    <LinkURL>mailto:awrigh76@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awrigh76@student.savannahstate.edu"&gt;awrigh76@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex M. Koonce</LinkText>\r\n    <LinkURL>mailto:akoonce@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:akoonce@student.savannahstate.edu"&gt;akoonce@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex M. Nichols</LinkText>\r\n    <LinkURL>mailto:anichol7@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:anichol7@student.savannahstate.edu"&gt;anichol7@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex R. Weaver</LinkText>\r\n    <LinkURL>mailto:aweaver5@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aweaver5@student.savannahstate.edu"&gt;aweaver5@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex T. Pierce</LinkText>\r\n    <LinkURL>mailto:apierc18@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apierc18@student.savannahstate.edu"&gt;apierc18@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex W. Barrett</LinkText>\r\n    <LinkURL>mailto:abarret6@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abarret6@student.savannahstate.edu"&gt;abarret6@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexander A. Reid</LinkText>\r\n    <LinkURL>mailto:areid10@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:areid10@student.savannahstate.edu"&gt;areid10@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexander A. Taul</LinkText>\r\n    <LinkURL>mailto:ataul@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ataul@student.savannahstate.edu"&gt;ataul@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexander Q. Grier</LinkText>\r\n    <LinkURL>mailto:agrier1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agrier1@student.savannahstate.edu"&gt;agrier1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexander V. Ontivero</LinkText>\r\n    <LinkURL>mailto:aontiver@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aontiver@student.savannahstate.edu"&gt;aontiver@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexander Y. Holcey</LinkText>\r\n    <LinkURL>mailto:aholcey@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aholcey@student.savannahstate.edu"&gt;aholcey@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexanderia N. Dixon</LinkText>\r\n    <LinkURL>mailto:adixon12@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adixon12@student.savannahstate.edu"&gt;adixon12@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexandra I. Kinney</LinkText>\r\n    <LinkURL>mailto:akinney@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:akinney@student.savannahstate.edu"&gt;akinney@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexandra X. Cabell</LinkText>\r\n    <LinkURL>mailto:acabell@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acabell@student.savannahstate.edu"&gt;acabell@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexandrea L. Vereen</LinkText>\r\n    <LinkURL>mailto:avereen1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:avereen1@student.savannahstate.edu"&gt;avereen1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexandrea Mann</LinkText>\r\n    <LinkURL>mailto:amann3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amann3@student.savannahstate.edu"&gt;amann3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexandria Ambrose</LinkText>\r\n    <LinkURL>mailto:aambros1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aambros1@student.savannahstate.edu"&gt;aambros1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex-Aundryah Duporte</LinkText>\r\n    <LinkURL>mailto:aduporte@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aduporte@student.savannahstate.edu"&gt;aduporte@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexcia G. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn181@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn181@student.savannahstate.edu"&gt;ajohn181@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexcia R. Cooper</LinkText>\r\n    <LinkURL>mailto:acoope22@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acoope22@student.savannahstate.edu"&gt;acoope22@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexi K. Gaboriault</LinkText>\r\n    <LinkURL>mailto:agaboria@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agaboria@student.savannahstate.edu"&gt;agaboria@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexia L. Singleton</LinkText>\r\n    <LinkURL>mailto:asingl13@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asingl13@student.savannahstate.edu"&gt;asingl13@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexia T. Ewell</LinkText>\r\n    <LinkURL>mailto:aewell@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aewell@student.savannahstate.edu"&gt;aewell@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis B. Brown</LinkText>\r\n    <LinkURL>mailto:abrow124@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrow124@student.savannahstate.edu"&gt;abrow124@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis B. Haynes</LinkText>\r\n    <LinkURL>mailto:ahaynes9@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahaynes9@student.savannahstate.edu"&gt;ahaynes9@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis C. Flowers</LinkText>\r\n    <LinkURL>mailto:aflower4@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aflower4@student.savannahstate.edu"&gt;aflower4@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis C. McIver</LinkText>\r\n    <LinkURL>mailto:amciver1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amciver1@student.savannahstate.edu"&gt;amciver1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis C. Zeigler</LinkText>\r\n    <LinkURL>mailto:azeigler@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:azeigler@student.savannahstate.edu"&gt;azeigler@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis D. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn179@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn179@student.savannahstate.edu"&gt;ajohn179@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis D. Webb</LinkText>\r\n    <LinkURL>mailto:awebb6@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awebb6@student.savannahstate.edu"&gt;awebb6@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis E. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn213@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn213@student.savannahstate.edu"&gt;ajohn213@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis F. Richard</LinkText>\r\n    <LinkURL>mailto:aricha29@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aricha29@student.savannahstate.edu"&gt;aricha29@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis I. Fleming</LinkText>\r\n    <LinkURL>mailto:aflemin4@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aflemin4@student.savannahstate.edu"&gt;aflemin4@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis J. Abollo</LinkText>\r\n    <LinkURL>mailto:aabollo@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aabollo@student.savannahstate.edu"&gt;aabollo@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis J. Gilmore</LinkText>\r\n    <LinkURL>mailto:agilmor2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agilmor2@student.savannahstate.edu"&gt;agilmor2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis K. Glenn</LinkText>\r\n    <LinkURL>mailto:aglenn2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aglenn2@student.savannahstate.edu"&gt;aglenn2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis K. Pointer</LinkText>\r\n    <LinkURL>mailto:apointer@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apointer@student.savannahstate.edu"&gt;apointer@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis L. Crawford</LinkText>\r\n    <LinkURL>mailto:acrawf19@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acrawf19@student.savannahstate.edu"&gt;acrawf19@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis L. Wade</LinkText>\r\n    <LinkURL>mailto:awade3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awade3@student.savannahstate.edu"&gt;awade3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis L. Washington</LinkText>\r\n    <LinkURL>mailto:awashi44@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awashi44@student.savannahstate.edu"&gt;awashi44@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis N. Baird</LinkText>\r\n    <LinkURL>mailto:abaird1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abaird1@student.savannahstate.edu"&gt;abaird1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis N. Singleton</LinkText>\r\n    <LinkURL>mailto:asingl11@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asingl11@student.savannahstate.edu"&gt;asingl11@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis N. Smith</LinkText>\r\n    <LinkURL>mailto:asmit125@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit125@student.savannahstate.edu"&gt;asmit125@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis N. Williams</LinkText>\r\n    <LinkURL>mailto:awill265@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awill265@student.savannahstate.edu"&gt;awill265@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis P. Collado</LinkText>\r\n    <LinkURL>mailto:acollado@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acollado@student.savannahstate.edu"&gt;acollado@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis Parker</LinkText>\r\n    <LinkURL>mailto:aparke26@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aparke26@student.savannahstate.edu"&gt;aparke26@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis R. Robinson</LinkText>\r\n    <LinkURL>mailto:arobin46@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arobin46@student.savannahstate.edu"&gt;arobin46@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis S. Arnold</LinkText>\r\n    <LinkURL>mailto:aarnol14@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aarnol14@student.savannahstate.edu"&gt;aarnol14@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis S. Evans</LinkText>\r\n    <LinkURL>mailto:aevans27@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aevans27@student.savannahstate.edu"&gt;aevans27@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis S. Tuggle</LinkText>\r\n    <LinkURL>mailto:atuggle2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:atuggle2@student.savannahstate.edu"&gt;atuggle2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis T. Halston</LinkText>\r\n    <LinkURL>mailto:ahalston@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahalston@student.savannahstate.edu"&gt;ahalston@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis T. Thompson</LinkText>\r\n    <LinkURL>mailto:athomp41@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:athomp41@student.savannahstate.edu"&gt;athomp41@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis T. Watts</LinkText>\r\n    <LinkURL>mailto:awatts9@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awatts9@student.savannahstate.edu"&gt;awatts9@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis V. Washington</LinkText>\r\n    <LinkURL>mailto:awashi45@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awashi45@student.savannahstate.edu"&gt;awashi45@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis V. Williams</LinkText>\r\n    <LinkURL>mailto:awillima@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awillima@student.savannahstate.edu"&gt;awillima@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexsia C. McClary</LinkText>\r\n    <LinkURL>mailto:amcclary@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amcclary@student.savannahstate.edu"&gt;amcclary@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexsia D. Brown</LinkText>\r\n    <LinkURL>mailto:abrow120@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrow120@student.savannahstate.edu"&gt;abrow120@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexsis Q. Martin</LinkText>\r\n    <LinkURL>mailto:amarti37@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amarti37@student.savannahstate.edu"&gt;amarti37@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus B. Collins</LinkText>\r\n    <LinkURL>mailto:acolli23@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acolli23@student.savannahstate.edu"&gt;acolli23@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus D. Byrd</LinkText>\r\n    <LinkURL>mailto:abyrd12@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abyrd12@student.savannahstate.edu"&gt;abyrd12@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus D. Robinson</LinkText>\r\n    <LinkURL>mailto:arobin52@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arobin52@student.savannahstate.edu"&gt;arobin52@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus E. Cannon</LinkText>\r\n    <LinkURL>mailto:acannon2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acannon2@student.savannahstate.edu"&gt;acannon2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus E. Reed</LinkText>\r\n    <LinkURL>mailto:areed16@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:areed16@student.savannahstate.edu"&gt;areed16@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus I. Flores</LinkText>\r\n    <LinkURL>mailto:aflores1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aflores1@student.savannahstate.edu"&gt;aflores1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus M. Neal</LinkText>\r\n    <LinkURL>mailto:aneal6@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aneal6@student.savannahstate.edu"&gt;aneal6@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus S. Bryant</LinkText>\r\n    <LinkURL>mailto:abryan27@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abryan27@student.savannahstate.edu"&gt;abryan27@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus S. Holley</LinkText>\r\n    <LinkURL>mailto:aholley3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aholley3@student.savannahstate.edu"&gt;aholley3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus S. Stone</LinkText>\r\n    <LinkURL>mailto:astone3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:astone3@student.savannahstate.edu"&gt;astone3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus S. Williams</LinkText>\r\n    <LinkURL>mailto:awill130@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awill130@student.savannahstate.edu"&gt;awill130@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus S. Williams</LinkText>\r\n    <LinkURL>mailto:awill242@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awill242@student.savannahstate.edu"&gt;awill242@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus T. Hampton</LinkText>\r\n    <LinkURL>mailto:ahampto7@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahampto7@student.savannahstate.edu"&gt;ahampto7@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexxa Jernigan</LinkText>\r\n    <LinkURL>mailto:ajernig3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajernig3@student.savannahstate.edu"&gt;ajernig3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alfatine A. Gardner</LinkText>\r\n    <LinkURL>mailto:agardne9@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agardne9@student.savannahstate.edu"&gt;agardne9@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alfonzo D. Berry</LinkText>\r\n    <LinkURL>mailto:aberry6@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aberry6@student.savannahstate.edu"&gt;aberry6@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ali S. Steed</LinkText>\r\n    <LinkURL>mailto:asteed@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asteed@student.savannahstate.edu"&gt;asteed@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alia D. Tascoe El</LinkText>\r\n    <LinkURL>mailto:atascoee@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:atascoee@student.savannahstate.edu"&gt;atascoee@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alia K. Hill</LinkText>\r\n    <LinkURL>mailto:ahill45@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahill45@student.savannahstate.edu"&gt;ahill45@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alia N. Hawes</LinkText>\r\n    <LinkURL>mailto:ahawes2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahawes2@student.savannahstate.edu"&gt;ahawes2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia Blain</LinkText>\r\n    <LinkURL>mailto:ablain@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ablain@student.savannahstate.edu"&gt;ablain@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia D. Tanner</LinkText>\r\n    <LinkURL>mailto:atanner1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:atanner1@student.savannahstate.edu"&gt;atanner1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia E. Lambert</LinkText>\r\n    <LinkURL>mailto:alamber3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alamber3@student.savannahstate.edu"&gt;alamber3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia K. Lawton</LinkText>\r\n    <LinkURL>mailto:alawton1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alawton1@student.savannahstate.edu"&gt;alawton1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia L. Frontera</LinkText>\r\n    <LinkURL>mailto:afronter@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:afronter@student.savannahstate.edu"&gt;afronter@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia Montgomery</LinkText>\r\n    <LinkURL>mailto:amontgo5@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amontgo5@student.savannahstate.edu"&gt;amontgo5@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alisa A. Baker</LinkText>\r\n    <LinkURL>mailto:abaker10@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abaker10@student.savannahstate.edu"&gt;abaker10@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alisa B. Ellis</LinkText>\r\n    <LinkURL>mailto:aellis8@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aellis8@student.savannahstate.edu"&gt;aellis8@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alison Hill</LinkText>\r\n    <LinkURL>mailto:ahill42@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahill42@student.savannahstate.edu"&gt;ahill42@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alison J. Morgan</LinkText>\r\n    <LinkURL>mailto:amorga10@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amorga10@student.savannahstate.edu"&gt;amorga10@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliya D. Barkley</LinkText>\r\n    <LinkURL>mailto:abarkle2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abarkle2@student.savannahstate.edu"&gt;abarkle2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliya N. Wharton</LinkText>\r\n    <LinkURL>mailto:awharton@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awharton@student.savannahstate.edu"&gt;awharton@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah C. Davis</LinkText>\r\n    <LinkURL>mailto:adavis94@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adavis94@student.savannahstate.edu"&gt;adavis94@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah C. Moore</LinkText>\r\n    <LinkURL>mailto:amoore41@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amoore41@student.savannahstate.edu"&gt;amoore41@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah D. Moultrie</LinkText>\r\n    <LinkURL>mailto:amoultr3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amoultr3@student.savannahstate.edu"&gt;amoultr3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah J. Duffey</LinkText>\r\n    <LinkURL>mailto:aduffey@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aduffey@student.savannahstate.edu"&gt;aduffey@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah M. Lewis</LinkText>\r\n    <LinkURL>mailto:alewis49@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alewis49@student.savannahstate.edu"&gt;alewis49@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah M. Toney</LinkText>\r\n    <LinkURL>mailto:atoney1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:atoney1@student.savannahstate.edu"&gt;atoney1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah R. Smith</LinkText>\r\n    <LinkURL>mailto:asmit131@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit131@student.savannahstate.edu"&gt;asmit131@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah S. Bryant</LinkText>\r\n    <LinkURL>mailto:abryan37@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abryan37@student.savannahstate.edu"&gt;abryan37@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah Y. Parker</LinkText>\r\n    <LinkURL>mailto:aparke19@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aparke19@student.savannahstate.edu"&gt;aparke19@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allante R. Smith</LinkText>\r\n    <LinkURL>mailto:asmith86@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmith86@student.savannahstate.edu"&gt;asmith86@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allea E. Campbell</LinkText>\r\n    <LinkURL>mailto:acampb15@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acampb15@student.savannahstate.edu"&gt;acampb15@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allegria T. Hutchins</LinkText>\r\n    <LinkURL>mailto:ahutchi2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahutchi2@student.savannahstate.edu"&gt;ahutchi2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allen C. Robinson</LinkText>\r\n    <LinkURL>mailto:arobin58@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arobin58@student.savannahstate.edu"&gt;arobin58@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allen E. Bell</LinkText>\r\n    <LinkURL>mailto:abell19@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abell19@student.savannahstate.edu"&gt;abell19@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allen M. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn139@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn139@student.savannahstate.edu"&gt;ajohn139@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allendria T. Brown</LinkText>\r\n    <LinkURL>mailto:abrow152@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrow152@student.savannahstate.edu"&gt;abrow152@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alliyah M. Lowder</LinkText>\r\n    <LinkURL>mailto:alowder1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alowder1@student.savannahstate.edu"&gt;alowder1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allye A. Sneed</LinkText>\r\n    <LinkURL>mailto:asneed2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asneed2@student.savannahstate.edu"&gt;asneed2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alma B. Sapateh</LinkText>\r\n    <LinkURL>mailto:asapateh@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asapateh@student.savannahstate.edu"&gt;asapateh@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Al\'neisha J. Randall</LinkText>\r\n    <LinkURL>mailto:arandal3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arandal3@student.savannahstate.edu"&gt;arandal3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alneka K. Smith</LinkText>\r\n    <LinkURL>mailto:asmit149@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit149@student.savannahstate.edu"&gt;asmit149@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alonna D. Preyer</LinkText>\r\n    <LinkURL>mailto:apreyer@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apreyer@student.savannahstate.edu"&gt;apreyer@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alonzo A. Francis</LinkText>\r\n    <LinkURL>mailto:afranci3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:afranci3@student.savannahstate.edu"&gt;afranci3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alonzo Baker</LinkText>\r\n    <LinkURL>mailto:abaker23@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abaker23@student.savannahstate.edu"&gt;abaker23@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Altonnett E. Guyton</LinkText>\r\n    <LinkURL>mailto:aguyton2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aguyton2@student.savannahstate.edu"&gt;aguyton2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alysha M. Wright</LinkText>\r\n    <LinkURL>mailto:awrigh63@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awrigh63@student.savannahstate.edu"&gt;awrigh63@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n</ArrayOfSearchResult>'
>>> DOMTree = xml.dom.minidom.parse(r.text)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    DOMTree = xml.dom.minidom.parse(r.text)
  File "/home/ramakrishna/anaconda3/lib/python3.5/xml/dom/minidom.py", line 1958, in parse
    return expatbuilder.parse(file)
  File "/home/ramakrishna/anaconda3/lib/python3.5/xml/dom/expatbuilder.py", line 910, in parse
    with open(file, 'rb') as fp:
OSError: [Errno 36] File name too long: '<?xml version="1.0" encoding="utf-8"?>\r\n<ArrayOfSearchResult xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://www.savannahstate.edu">\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaliyah J. Lindquist</LinkText>\r\n    <LinkURL>mailto:alindqui@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alindqui@student.savannahstate.edu"&gt;alindqui@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaliyah Q. Heggs</LinkText>\r\n    <LinkURL>mailto:aheggs@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aheggs@student.savannahstate.edu"&gt;aheggs@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaliyah S. Smith</LinkText>\r\n    <LinkURL>mailto:asmit173@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit173@student.savannahstate.edu"&gt;asmit173@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaren O. Green</LinkText>\r\n    <LinkURL>mailto:agreen36@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agreen36@student.savannahstate.edu"&gt;agreen36@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aarian J. Little</LinkText>\r\n    <LinkURL>mailto:alittle6@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alittle6@student.savannahstate.edu"&gt;alittle6@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron A. McKinnon</LinkText>\r\n    <LinkURL>mailto:amckinn9@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amckinn9@student.savannahstate.edu"&gt;amckinn9@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron D. Hunt</LinkText>\r\n    <LinkURL>mailto:ahunt3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahunt3@student.savannahstate.edu"&gt;ahunt3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron G. Deas</LinkText>\r\n    <LinkURL>mailto:adeas2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adeas2@student.savannahstate.edu"&gt;adeas2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron Grant</LinkText>\r\n    <LinkURL>mailto:agrant19@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agrant19@student.savannahstate.edu"&gt;agrant19@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron J. Mason</LinkText>\r\n    <LinkURL>mailto:amason8@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amason8@student.savannahstate.edu"&gt;amason8@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron J. Udell</LinkText>\r\n    <LinkURL>mailto:audell@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:audell@student.savannahstate.edu"&gt;audell@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn145@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn145@student.savannahstate.edu"&gt;ajohn145@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron M. Polite</LinkText>\r\n    <LinkURL>mailto:apolite4@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apolite4@student.savannahstate.edu"&gt;apolite4@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron P. Odum</LinkText>\r\n    <LinkURL>mailto:aodum@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aodum@student.savannahstate.edu"&gt;aodum@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron Thomas</LinkText>\r\n    <LinkURL>mailto:athoma85@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:athoma85@student.savannahstate.edu"&gt;athoma85@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaron X. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn126@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn126@student.savannahstate.edu"&gt;ajohn126@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aaryn M. McDade</LinkText>\r\n    <LinkURL>mailto:amcdade1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amcdade1@student.savannahstate.edu"&gt;amcdade1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Abel Reyes</LinkText>\r\n    <LinkURL>mailto:areyes2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:areyes2@student.savannahstate.edu"&gt;areyes2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Abigaile K. Naslund</LinkText>\r\n    <LinkURL>mailto:anaslund@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:anaslund@student.savannahstate.edu"&gt;anaslund@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>A\'bria K. McDonald</LinkText>\r\n    <LinkURL>mailto:amcdona5@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amcdona5@student.savannahstate.edu"&gt;amcdona5@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Acadia D. Plummer</LinkText>\r\n    <LinkURL>mailto:aplumme3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aplumme3@student.savannahstate.edu"&gt;aplumme3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Acasia L. Turner</LinkText>\r\n    <LinkURL>mailto:aturne25@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aturne25@student.savannahstate.edu"&gt;aturne25@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adam A. Walden</LinkText>\r\n    <LinkURL>mailto:awalden3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awalden3@student.savannahstate.edu"&gt;awalden3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adam C. Smith</LinkText>\r\n    <LinkURL>mailto:asmit155@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit155@student.savannahstate.edu"&gt;asmit155@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adam K. Wilkerson</LinkText>\r\n    <LinkURL>mailto:awilkers@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awilkers@student.savannahstate.edu"&gt;awilkers@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adam M. Hower</LinkText>\r\n    <LinkURL>mailto:ahower@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahower@student.savannahstate.edu"&gt;ahower@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adara K. Butts</LinkText>\r\n    <LinkURL>mailto:abutts3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abutts3@student.savannahstate.edu"&gt;abutts3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adarian D. Dunmeyer</LinkText>\r\n    <LinkURL>mailto:adunmeye@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adunmeye@student.savannahstate.edu"&gt;adunmeye@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adayshia L. Carlis</LinkText>\r\n    <LinkURL>mailto:acarlis@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acarlis@student.savannahstate.edu"&gt;acarlis@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Addie Daniels</LinkText>\r\n    <LinkURL>mailto:adanie21@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adanie21@student.savannahstate.edu"&gt;adanie21@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adeola E. Gbadebo</LinkText>\r\n    <LinkURL>mailto:agbadebo@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agbadebo@student.savannahstate.edu"&gt;agbadebo@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adia D. Gilbert</LinkText>\r\n    <LinkURL>mailto:agilbe12@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agilbe12@student.savannahstate.edu"&gt;agilbe12@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adidasheonna N. Sloan</LinkText>\r\n    <LinkURL>mailto:asloan2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asloan2@student.savannahstate.edu"&gt;asloan2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adjani Donald</LinkText>\r\n    <LinkURL>mailto:adonald8@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adonald8@student.savannahstate.edu"&gt;adonald8@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adrainna A. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn212@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn212@student.savannahstate.edu"&gt;ajohn212@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adrian D. Gaither</LinkText>\r\n    <LinkURL>mailto:agaithe1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agaithe1@student.savannahstate.edu"&gt;agaithe1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adrian M. English</LinkText>\r\n    <LinkURL>mailto:aenglis2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aenglis2@student.savannahstate.edu"&gt;aenglis2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adriana J. Thomas</LinkText>\r\n    <LinkURL>mailto:athom101@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:athom101@student.savannahstate.edu"&gt;athom101@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adriana S. Mann</LinkText>\r\n    <LinkURL>mailto:amann1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amann1@student.savannahstate.edu"&gt;amann1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adrianna R. Dawkins</LinkText>\r\n    <LinkURL>mailto:adawkin2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adawkin2@student.savannahstate.edu"&gt;adawkin2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Adrienne Kilgore</LinkText>\r\n    <LinkURL>mailto:akilgore@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:akilgore@student.savannahstate.edu"&gt;akilgore@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Afolabi A. Ayangbayi</LinkText>\r\n    <LinkURL>mailto:aayangba@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aayangba@student.savannahstate.edu"&gt;aayangba@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ahkanyala J. Jordan</LinkText>\r\n    <LinkURL>mailto:ajorda15@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajorda15@student.savannahstate.edu"&gt;ajorda15@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ahmaad M. Green</LinkText>\r\n    <LinkURL>mailto:agreen29@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agreen29@student.savannahstate.edu"&gt;agreen29@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ahmad J. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn190@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn190@student.savannahstate.edu"&gt;ajohn190@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ahmir S. Green</LinkText>\r\n    <LinkURL>mailto:agreen51@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agreen51@student.savannahstate.edu"&gt;agreen51@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ahmord O. Rivers</LinkText>\r\n    <LinkURL>mailto:arivers8@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arivers8@student.savannahstate.edu"&gt;arivers8@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aiesha Rankin</LinkText>\r\n    <LinkURL>mailto:arankin@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arankin@student.savannahstate.edu"&gt;arankin@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Airese R. Moss</LinkText>\r\n    <LinkURL>mailto:amoss3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amoss3@student.savannahstate.edu"&gt;amoss3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Airianne T. Wright</LinkText>\r\n    <LinkURL>mailto:awrigh74@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awrigh74@student.savannahstate.edu"&gt;awrigh74@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aisha D. Ross</LinkText>\r\n    <LinkURL>mailto:aross17@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aross17@student.savannahstate.edu"&gt;aross17@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aisha S. Mack</LinkText>\r\n    <LinkURL>mailto:amack13@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amack13@student.savannahstate.edu"&gt;amack13@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aisha Z. Gamble</LinkText>\r\n    <LinkURL>mailto:agamble7@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agamble7@student.savannahstate.edu"&gt;agamble7@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aiyannah C. Peal</LinkText>\r\n    <LinkURL>mailto:apeal@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apeal@student.savannahstate.edu"&gt;apeal@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aja J. Smith</LinkText>\r\n    <LinkURL>mailto:asmit160@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit160@student.savannahstate.edu"&gt;asmit160@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akeem E. Love</LinkText>\r\n    <LinkURL>mailto:alove3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alove3@student.savannahstate.edu"&gt;alove3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akeem H. White</LinkText>\r\n    <LinkURL>mailto:awhite27@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awhite27@student.savannahstate.edu"&gt;awhite27@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akeem J. Williams</LinkText>\r\n    <LinkURL>mailto:awill248@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awill248@student.savannahstate.edu"&gt;awill248@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akeya S. Hurt</LinkText>\r\n    <LinkURL>mailto:ahurt2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahurt2@student.savannahstate.edu"&gt;ahurt2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akira T. Warren</LinkText>\r\n    <LinkURL>mailto:awarren4@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awarren4@student.savannahstate.edu"&gt;awarren4@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akirya R. Blair</LinkText>\r\n    <LinkURL>mailto:ablair2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ablair2@student.savannahstate.edu"&gt;ablair2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Akivia M. Blue</LinkText>\r\n    <LinkURL>mailto:ablue4@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ablue4@student.savannahstate.edu"&gt;ablue4@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alacia D. Platts</LinkText>\r\n    <LinkURL>mailto:aplatts@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aplatts@student.savannahstate.edu"&gt;aplatts@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>A\'laija S. Gardner</LinkText>\r\n    <LinkURL>mailto:agardn11@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agardn11@student.savannahstate.edu"&gt;agardn11@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alaina P. Monroe</LinkText>\r\n    <LinkURL>mailto:amonroe1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amonroe1@student.savannahstate.edu"&gt;amonroe1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alakenisa R. Thorpe</LinkText>\r\n    <LinkURL>mailto:athorpe@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:athorpe@student.savannahstate.edu"&gt;athorpe@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alana M. Harris</LinkText>\r\n    <LinkURL>mailto:aharr100@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aharr100@student.savannahstate.edu"&gt;aharr100@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alana S. Reese</LinkText>\r\n    <LinkURL>mailto:areese13@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:areese13@student.savannahstate.edu"&gt;areese13@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alana V. Green</LinkText>\r\n    <LinkURL>mailto:agreen30@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agreen30@student.savannahstate.edu"&gt;agreen30@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alanna M. Puzzuoli</LinkText>\r\n    <LinkURL>mailto:apuzzuol@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apuzzuol@student.savannahstate.edu"&gt;apuzzuol@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alannah N. Jackson</LinkText>\r\n    <LinkURL>mailto:ajacks82@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajacks82@student.savannahstate.edu"&gt;ajacks82@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alayna P. Stovall</LinkText>\r\n    <LinkURL>mailto:astovall@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:astovall@student.savannahstate.edu"&gt;astovall@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alaysia S. Brown-Kelly</LinkText>\r\n    <LinkURL>mailto:abrownke@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrownke@student.savannahstate.edu"&gt;abrownke@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Albert C. Rumph</LinkText>\r\n    <LinkURL>mailto:arumph1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arumph1@student.savannahstate.edu"&gt;arumph1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Albrena J. Jelks</LinkText>\r\n    <LinkURL>mailto:ajelks@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajelks@student.savannahstate.edu"&gt;ajelks@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alec J. Brown</LinkText>\r\n    <LinkURL>mailto:abrow118@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrow118@student.savannahstate.edu"&gt;abrow118@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aleeyah L. Hardwick</LinkText>\r\n    <LinkURL>mailto:ahardwi1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahardwi1@student.savannahstate.edu"&gt;ahardwi1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alerie T. Roberts</LinkText>\r\n    <LinkURL>mailto:arober34@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arober34@student.savannahstate.edu"&gt;arober34@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alescia S. Washington</LinkText>\r\n    <LinkURL>mailto:awashi40@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awashi40@student.savannahstate.edu"&gt;awashi40@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alesha M. Boles-Johnson</LinkText>\r\n    <LinkURL>mailto:abolesjo@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abolesjo@student.savannahstate.edu"&gt;abolesjo@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alesha M. Moore</LinkText>\r\n    <LinkURL>mailto:amoore48@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amoore48@student.savannahstate.edu"&gt;amoore48@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex A. Fulks</LinkText>\r\n    <LinkURL>mailto:afulksjr@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:afulksjr@student.savannahstate.edu"&gt;afulksjr@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex Brown</LinkText>\r\n    <LinkURL>mailto:abrown63@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrown63@student.savannahstate.edu"&gt;abrown63@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex J. Simmons</LinkText>\r\n    <LinkURL>mailto:asimmo12@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asimmo12@student.savannahstate.edu"&gt;asimmo12@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex J. Wright</LinkText>\r\n    <LinkURL>mailto:awrigh76@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awrigh76@student.savannahstate.edu"&gt;awrigh76@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex M. Koonce</LinkText>\r\n    <LinkURL>mailto:akoonce@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:akoonce@student.savannahstate.edu"&gt;akoonce@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex M. Nichols</LinkText>\r\n    <LinkURL>mailto:anichol7@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:anichol7@student.savannahstate.edu"&gt;anichol7@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex R. Weaver</LinkText>\r\n    <LinkURL>mailto:aweaver5@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aweaver5@student.savannahstate.edu"&gt;aweaver5@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex T. Pierce</LinkText>\r\n    <LinkURL>mailto:apierc18@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apierc18@student.savannahstate.edu"&gt;apierc18@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex W. Barrett</LinkText>\r\n    <LinkURL>mailto:abarret6@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abarret6@student.savannahstate.edu"&gt;abarret6@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexander A. Reid</LinkText>\r\n    <LinkURL>mailto:areid10@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:areid10@student.savannahstate.edu"&gt;areid10@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexander A. Taul</LinkText>\r\n    <LinkURL>mailto:ataul@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ataul@student.savannahstate.edu"&gt;ataul@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexander Q. Grier</LinkText>\r\n    <LinkURL>mailto:agrier1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agrier1@student.savannahstate.edu"&gt;agrier1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexander V. Ontivero</LinkText>\r\n    <LinkURL>mailto:aontiver@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aontiver@student.savannahstate.edu"&gt;aontiver@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexander Y. Holcey</LinkText>\r\n    <LinkURL>mailto:aholcey@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aholcey@student.savannahstate.edu"&gt;aholcey@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexanderia N. Dixon</LinkText>\r\n    <LinkURL>mailto:adixon12@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adixon12@student.savannahstate.edu"&gt;adixon12@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexandra I. Kinney</LinkText>\r\n    <LinkURL>mailto:akinney@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:akinney@student.savannahstate.edu"&gt;akinney@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexandra X. Cabell</LinkText>\r\n    <LinkURL>mailto:acabell@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acabell@student.savannahstate.edu"&gt;acabell@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexandrea L. Vereen</LinkText>\r\n    <LinkURL>mailto:avereen1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:avereen1@student.savannahstate.edu"&gt;avereen1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexandrea Mann</LinkText>\r\n    <LinkURL>mailto:amann3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amann3@student.savannahstate.edu"&gt;amann3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexandria Ambrose</LinkText>\r\n    <LinkURL>mailto:aambros1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aambros1@student.savannahstate.edu"&gt;aambros1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alex-Aundryah Duporte</LinkText>\r\n    <LinkURL>mailto:aduporte@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aduporte@student.savannahstate.edu"&gt;aduporte@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexcia G. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn181@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn181@student.savannahstate.edu"&gt;ajohn181@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexcia R. Cooper</LinkText>\r\n    <LinkURL>mailto:acoope22@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acoope22@student.savannahstate.edu"&gt;acoope22@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexi K. Gaboriault</LinkText>\r\n    <LinkURL>mailto:agaboria@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agaboria@student.savannahstate.edu"&gt;agaboria@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexia L. Singleton</LinkText>\r\n    <LinkURL>mailto:asingl13@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asingl13@student.savannahstate.edu"&gt;asingl13@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexia T. Ewell</LinkText>\r\n    <LinkURL>mailto:aewell@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aewell@student.savannahstate.edu"&gt;aewell@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis B. Brown</LinkText>\r\n    <LinkURL>mailto:abrow124@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrow124@student.savannahstate.edu"&gt;abrow124@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis B. Haynes</LinkText>\r\n    <LinkURL>mailto:ahaynes9@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahaynes9@student.savannahstate.edu"&gt;ahaynes9@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis C. Flowers</LinkText>\r\n    <LinkURL>mailto:aflower4@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aflower4@student.savannahstate.edu"&gt;aflower4@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis C. McIver</LinkText>\r\n    <LinkURL>mailto:amciver1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amciver1@student.savannahstate.edu"&gt;amciver1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis C. Zeigler</LinkText>\r\n    <LinkURL>mailto:azeigler@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:azeigler@student.savannahstate.edu"&gt;azeigler@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis D. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn179@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn179@student.savannahstate.edu"&gt;ajohn179@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis D. Webb</LinkText>\r\n    <LinkURL>mailto:awebb6@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awebb6@student.savannahstate.edu"&gt;awebb6@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis E. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn213@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn213@student.savannahstate.edu"&gt;ajohn213@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis F. Richard</LinkText>\r\n    <LinkURL>mailto:aricha29@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aricha29@student.savannahstate.edu"&gt;aricha29@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis I. Fleming</LinkText>\r\n    <LinkURL>mailto:aflemin4@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aflemin4@student.savannahstate.edu"&gt;aflemin4@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis J. Abollo</LinkText>\r\n    <LinkURL>mailto:aabollo@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aabollo@student.savannahstate.edu"&gt;aabollo@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis J. Gilmore</LinkText>\r\n    <LinkURL>mailto:agilmor2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agilmor2@student.savannahstate.edu"&gt;agilmor2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis K. Glenn</LinkText>\r\n    <LinkURL>mailto:aglenn2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aglenn2@student.savannahstate.edu"&gt;aglenn2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis K. Pointer</LinkText>\r\n    <LinkURL>mailto:apointer@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apointer@student.savannahstate.edu"&gt;apointer@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis L. Crawford</LinkText>\r\n    <LinkURL>mailto:acrawf19@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acrawf19@student.savannahstate.edu"&gt;acrawf19@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis L. Wade</LinkText>\r\n    <LinkURL>mailto:awade3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awade3@student.savannahstate.edu"&gt;awade3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis L. Washington</LinkText>\r\n    <LinkURL>mailto:awashi44@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awashi44@student.savannahstate.edu"&gt;awashi44@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis N. Baird</LinkText>\r\n    <LinkURL>mailto:abaird1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abaird1@student.savannahstate.edu"&gt;abaird1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis N. Singleton</LinkText>\r\n    <LinkURL>mailto:asingl11@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asingl11@student.savannahstate.edu"&gt;asingl11@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis N. Smith</LinkText>\r\n    <LinkURL>mailto:asmit125@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit125@student.savannahstate.edu"&gt;asmit125@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis N. Williams</LinkText>\r\n    <LinkURL>mailto:awill265@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awill265@student.savannahstate.edu"&gt;awill265@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis P. Collado</LinkText>\r\n    <LinkURL>mailto:acollado@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acollado@student.savannahstate.edu"&gt;acollado@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis Parker</LinkText>\r\n    <LinkURL>mailto:aparke26@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aparke26@student.savannahstate.edu"&gt;aparke26@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis R. Robinson</LinkText>\r\n    <LinkURL>mailto:arobin46@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arobin46@student.savannahstate.edu"&gt;arobin46@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis S. Arnold</LinkText>\r\n    <LinkURL>mailto:aarnol14@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aarnol14@student.savannahstate.edu"&gt;aarnol14@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis S. Evans</LinkText>\r\n    <LinkURL>mailto:aevans27@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aevans27@student.savannahstate.edu"&gt;aevans27@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis S. Tuggle</LinkText>\r\n    <LinkURL>mailto:atuggle2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:atuggle2@student.savannahstate.edu"&gt;atuggle2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis T. Halston</LinkText>\r\n    <LinkURL>mailto:ahalston@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahalston@student.savannahstate.edu"&gt;ahalston@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis T. Thompson</LinkText>\r\n    <LinkURL>mailto:athomp41@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:athomp41@student.savannahstate.edu"&gt;athomp41@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis T. Watts</LinkText>\r\n    <LinkURL>mailto:awatts9@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awatts9@student.savannahstate.edu"&gt;awatts9@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis V. Washington</LinkText>\r\n    <LinkURL>mailto:awashi45@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awashi45@student.savannahstate.edu"&gt;awashi45@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexis V. Williams</LinkText>\r\n    <LinkURL>mailto:awillima@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awillima@student.savannahstate.edu"&gt;awillima@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexsia C. McClary</LinkText>\r\n    <LinkURL>mailto:amcclary@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amcclary@student.savannahstate.edu"&gt;amcclary@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexsia D. Brown</LinkText>\r\n    <LinkURL>mailto:abrow120@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrow120@student.savannahstate.edu"&gt;abrow120@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexsis Q. Martin</LinkText>\r\n    <LinkURL>mailto:amarti37@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amarti37@student.savannahstate.edu"&gt;amarti37@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus B. Collins</LinkText>\r\n    <LinkURL>mailto:acolli23@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acolli23@student.savannahstate.edu"&gt;acolli23@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus D. Byrd</LinkText>\r\n    <LinkURL>mailto:abyrd12@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abyrd12@student.savannahstate.edu"&gt;abyrd12@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus D. Robinson</LinkText>\r\n    <LinkURL>mailto:arobin52@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arobin52@student.savannahstate.edu"&gt;arobin52@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus E. Cannon</LinkText>\r\n    <LinkURL>mailto:acannon2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acannon2@student.savannahstate.edu"&gt;acannon2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus E. Reed</LinkText>\r\n    <LinkURL>mailto:areed16@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:areed16@student.savannahstate.edu"&gt;areed16@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus I. Flores</LinkText>\r\n    <LinkURL>mailto:aflores1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aflores1@student.savannahstate.edu"&gt;aflores1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus M. Neal</LinkText>\r\n    <LinkURL>mailto:aneal6@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aneal6@student.savannahstate.edu"&gt;aneal6@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus S. Bryant</LinkText>\r\n    <LinkURL>mailto:abryan27@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abryan27@student.savannahstate.edu"&gt;abryan27@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus S. Holley</LinkText>\r\n    <LinkURL>mailto:aholley3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aholley3@student.savannahstate.edu"&gt;aholley3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus S. Stone</LinkText>\r\n    <LinkURL>mailto:astone3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:astone3@student.savannahstate.edu"&gt;astone3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus S. Williams</LinkText>\r\n    <LinkURL>mailto:awill130@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awill130@student.savannahstate.edu"&gt;awill130@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus S. Williams</LinkText>\r\n    <LinkURL>mailto:awill242@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awill242@student.savannahstate.edu"&gt;awill242@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexus T. Hampton</LinkText>\r\n    <LinkURL>mailto:ahampto7@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahampto7@student.savannahstate.edu"&gt;ahampto7@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alexxa Jernigan</LinkText>\r\n    <LinkURL>mailto:ajernig3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajernig3@student.savannahstate.edu"&gt;ajernig3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alfatine A. Gardner</LinkText>\r\n    <LinkURL>mailto:agardne9@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:agardne9@student.savannahstate.edu"&gt;agardne9@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alfonzo D. Berry</LinkText>\r\n    <LinkURL>mailto:aberry6@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aberry6@student.savannahstate.edu"&gt;aberry6@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Ali S. Steed</LinkText>\r\n    <LinkURL>mailto:asteed@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asteed@student.savannahstate.edu"&gt;asteed@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alia D. Tascoe El</LinkText>\r\n    <LinkURL>mailto:atascoee@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:atascoee@student.savannahstate.edu"&gt;atascoee@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alia K. Hill</LinkText>\r\n    <LinkURL>mailto:ahill45@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahill45@student.savannahstate.edu"&gt;ahill45@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alia N. Hawes</LinkText>\r\n    <LinkURL>mailto:ahawes2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahawes2@student.savannahstate.edu"&gt;ahawes2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia Blain</LinkText>\r\n    <LinkURL>mailto:ablain@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ablain@student.savannahstate.edu"&gt;ablain@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia D. Tanner</LinkText>\r\n    <LinkURL>mailto:atanner1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:atanner1@student.savannahstate.edu"&gt;atanner1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia E. Lambert</LinkText>\r\n    <LinkURL>mailto:alamber3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alamber3@student.savannahstate.edu"&gt;alamber3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia K. Lawton</LinkText>\r\n    <LinkURL>mailto:alawton1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alawton1@student.savannahstate.edu"&gt;alawton1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia L. Frontera</LinkText>\r\n    <LinkURL>mailto:afronter@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:afronter@student.savannahstate.edu"&gt;afronter@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alicia Montgomery</LinkText>\r\n    <LinkURL>mailto:amontgo5@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amontgo5@student.savannahstate.edu"&gt;amontgo5@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alisa A. Baker</LinkText>\r\n    <LinkURL>mailto:abaker10@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abaker10@student.savannahstate.edu"&gt;abaker10@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alisa B. Ellis</LinkText>\r\n    <LinkURL>mailto:aellis8@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aellis8@student.savannahstate.edu"&gt;aellis8@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alison Hill</LinkText>\r\n    <LinkURL>mailto:ahill42@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahill42@student.savannahstate.edu"&gt;ahill42@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alison J. Morgan</LinkText>\r\n    <LinkURL>mailto:amorga10@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amorga10@student.savannahstate.edu"&gt;amorga10@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliya D. Barkley</LinkText>\r\n    <LinkURL>mailto:abarkle2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abarkle2@student.savannahstate.edu"&gt;abarkle2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliya N. Wharton</LinkText>\r\n    <LinkURL>mailto:awharton@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awharton@student.savannahstate.edu"&gt;awharton@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah C. Davis</LinkText>\r\n    <LinkURL>mailto:adavis94@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:adavis94@student.savannahstate.edu"&gt;adavis94@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah C. Moore</LinkText>\r\n    <LinkURL>mailto:amoore41@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amoore41@student.savannahstate.edu"&gt;amoore41@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah D. Moultrie</LinkText>\r\n    <LinkURL>mailto:amoultr3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:amoultr3@student.savannahstate.edu"&gt;amoultr3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah J. Duffey</LinkText>\r\n    <LinkURL>mailto:aduffey@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aduffey@student.savannahstate.edu"&gt;aduffey@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah M. Lewis</LinkText>\r\n    <LinkURL>mailto:alewis49@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alewis49@student.savannahstate.edu"&gt;alewis49@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah M. Toney</LinkText>\r\n    <LinkURL>mailto:atoney1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:atoney1@student.savannahstate.edu"&gt;atoney1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah R. Smith</LinkText>\r\n    <LinkURL>mailto:asmit131@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit131@student.savannahstate.edu"&gt;asmit131@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah S. Bryant</LinkText>\r\n    <LinkURL>mailto:abryan37@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abryan37@student.savannahstate.edu"&gt;abryan37@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Aliyah Y. Parker</LinkText>\r\n    <LinkURL>mailto:aparke19@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aparke19@student.savannahstate.edu"&gt;aparke19@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allante R. Smith</LinkText>\r\n    <LinkURL>mailto:asmith86@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmith86@student.savannahstate.edu"&gt;asmith86@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allea E. Campbell</LinkText>\r\n    <LinkURL>mailto:acampb15@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:acampb15@student.savannahstate.edu"&gt;acampb15@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allegria T. Hutchins</LinkText>\r\n    <LinkURL>mailto:ahutchi2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ahutchi2@student.savannahstate.edu"&gt;ahutchi2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allen C. Robinson</LinkText>\r\n    <LinkURL>mailto:arobin58@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arobin58@student.savannahstate.edu"&gt;arobin58@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allen E. Bell</LinkText>\r\n    <LinkURL>mailto:abell19@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abell19@student.savannahstate.edu"&gt;abell19@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allen M. Johnson</LinkText>\r\n    <LinkURL>mailto:ajohn139@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:ajohn139@student.savannahstate.edu"&gt;ajohn139@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allendria T. Brown</LinkText>\r\n    <LinkURL>mailto:abrow152@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abrow152@student.savannahstate.edu"&gt;abrow152@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alliyah M. Lowder</LinkText>\r\n    <LinkURL>mailto:alowder1@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:alowder1@student.savannahstate.edu"&gt;alowder1@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Allye A. Sneed</LinkText>\r\n    <LinkURL>mailto:asneed2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asneed2@student.savannahstate.edu"&gt;asneed2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alma B. Sapateh</LinkText>\r\n    <LinkURL>mailto:asapateh@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asapateh@student.savannahstate.edu"&gt;asapateh@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Al\'neisha J. Randall</LinkText>\r\n    <LinkURL>mailto:arandal3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:arandal3@student.savannahstate.edu"&gt;arandal3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alneka K. Smith</LinkText>\r\n    <LinkURL>mailto:asmit149@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:asmit149@student.savannahstate.edu"&gt;asmit149@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alonna D. Preyer</LinkText>\r\n    <LinkURL>mailto:apreyer@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:apreyer@student.savannahstate.edu"&gt;apreyer@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alonzo A. Francis</LinkText>\r\n    <LinkURL>mailto:afranci3@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:afranci3@student.savannahstate.edu"&gt;afranci3@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alonzo Baker</LinkText>\r\n    <LinkURL>mailto:abaker23@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:abaker23@student.savannahstate.edu"&gt;abaker23@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Altonnett E. Guyton</LinkText>\r\n    <LinkURL>mailto:aguyton2@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:aguyton2@student.savannahstate.edu"&gt;aguyton2@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n  <SearchResult>\r\n    <CategoryName>student</CategoryName>\r\n    <LinkText>Alysha M. Wright</LinkText>\r\n    <LinkURL>mailto:awrigh63@student.savannahstate.edu</LinkURL>\r\n    <AdditionalInfo>&lt;a href="mailto:awrigh63@student.savannahstate.edu"&gt;awrigh63@student.savannahstate.edu&lt;/a&gt;</AdditionalInfo>\r\n  </SearchResult>\r\n</ArrayOfSearchResult>'
>>> DOMTree = xml.dom.minidom.parseString(r.text)
>>> collection = DOMTree.documentElement
>>> results = collection.getElementsByTagName("SearchResult")
>>> len(results)
200
>>> results[0]
<DOM Element: SearchResult at 0x7f1db4a19c28>
>>> results[0].getElementsByTagName('LinkText')[0]
<DOM Element: LinkText at 0x7f1db4a19210>
>>> name = results[0].getElementsByTagName('LinkText')[0]
>>> name.childNodes[0].data
'Aaliyah J. Lindquist'
>>> results[0].getElementsByTagName('LinkURL')[0].childNodes[0].data
'mailto:alindqui@student.savannahstate.edu'
>>> results[0].getElementsByTagName('LinkURL')[0].childNodes[0].data.replace("mailto:", "")
'alindqui@student.savannahstate.edu'
>>> 
