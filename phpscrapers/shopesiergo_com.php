<?php
    
    $BASE_URL = 'http://www.shopesiergo.com';
        
    //Function to get request url using curl
    function curlGet($url){
        
       $options = array(
            CURLOPT_RETURNTRANSFER => true,     // return web page
            CURLOPT_HEADER         => false,    // don't return headers
            CURLOPT_FOLLOWLOCATION => true,     // follow redirects
            CURLOPT_ENCODING       => "",       // handle all encodings
            CURLOPT_USERAGENT      => "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)", // who am i
            CURLOPT_AUTOREFERER    => true,     // set referer on redirect
            CURLOPT_CONNECTTIMEOUT => 15,      // timeout on connect
            CURLOPT_TIMEOUT        => 15,      // timeout on response
            CURLOPT_MAXREDIRS      => 10,       // stop after 10 redirects
            CURLOPT_SSL_VERIFYHOST => 0, CURLOPT_SSL_VERIFYPEER => 0,
        );

        $ch = curl_init($url);
        curl_setopt_array( $ch, $options );
        $content = curl_exec( $ch );
        $err     = curl_errno( $ch );
        $errmsg  = curl_error( $ch );
        $header  = curl_getinfo( $ch,CURLINFO_EFFECTIVE_URL );
        curl_close( $ch );

        if ($errmsg)
        {
            echo "CURL:".$errmsg."<BR>";
        }
        return $content;
    }

    //Dump results into DOMdocument for quering with xpath
    function returnXPathObject($item){
        $xmlPageDom = new DomDocument();
        @$xmlPageDom->loadHTML($item);
        $xmlPagePath = new DOMXPath($xmlPageDom);
        return $xmlPagePath;
    }
    
    $product_details = array();
    
    //Start
    $urls = array('http://www.shopesiergo.com/task-lighting-s/48.htm', 'http://www.shopesiergo.com/ergonomic-monitor-arms-s/44.htm',
        'http://www.shopesiergo.com/under-cabinet-task-light-p/ledg2-24.htm',);

    foreach($urls as $url){
        $url_page = curlGet($url);
        $url_xpath = returnXPathObject($url_page);

        $dtl_anchors = $url_xpath->query("//a[@class='smalltext colors_text']");

        //Fetching product name, desc and notes parsing html using xpath strings
        for($i = 0; $i < $dtl_anchors->length; $i++){ 
            $dtl_page = curlGet($dtl_anchors->item($i)->attributes->getNamedItem('href')->nodeValue);
            $dtl_xpath = returnXPathObject($dtl_page);         
            $product_details[] = array('name'=>$dtl_xpath->query("//span[@itemprop='name']")->item(0)->nodeValue,
                'desc'=>@$dtl_xpath->query("//span[@id='product_description']/p|//span[@id='product_description']/div")->item(0)->nodeValue,
                'desc_title'=>@$dtl_xpath->query("//span[@id='product_description']/h2")->item(0)->nodeValue,
                'notes'=> @$dtl_xpath->query("//span[@itemprop='description']/ul")->item(0)->nodeValue,
                'img_url'=>$BASE_URL . $dtl_xpath->query("//img[@id='product_photo']/@src")->item(0)->nodeValue,
                'list_price'=>str_replace('List Price:', '', $dtl_xpath->query("//div[@class='product_listprice']")->item(0)->nodeValue),
                'our_price'=>$dtl_xpath->query("//span[@itemprop='price']")->item(0)->nodeValue,
                'prod_code'=>$dtl_xpath->query("//span[@class='product_code']")->item(0)->nodeValue,);  
        }   
    }

    print_r(json_encode($product_details));
?>

