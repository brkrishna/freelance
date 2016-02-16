<?php
    
    $BASE_URL = 'http://www.esiergo.com';
        
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
    $res_downs = array();
    //Start

    $urls = array('http://www.esiergo.com/tables/electric-table-bases/','www.esiergo.com/tables/electric-table-bases/sp/triumph-table-base/',);

    foreach($urls as $url){
        $url_page = curlGet($url);
        $url_xpath = returnXPathObject($url_page);

        $dtl_anchors = $url_xpath->query("//div[@class='infoBox']/ul/li/a");

        //Fetching product name, desc and notes parsing html using xpath strings
        for($i = 0; $i < $dtl_anchors->length; $i++){ 
            $dtl_page = curlGet($BASE_URL . '/' . $dtl_anchors->item($i)->attributes->getNamedItem('href')->nodeValue);
            $dtl_xpath = returnXPathObject($dtl_page);         
            
            $resources = $dtl_xpath->query("//div[@id='resource']");
            $catg = $dtl_xpath->query("//div[@id='resource']//h4", $resources->item(0));

            for($j = 0; $j < $catg->length; $j++){
                $cat = str_replace("\r\n", "",$catg->item($j)->nodeValue);  
                $links = $dtl_xpath->query("//div[@id='resource']/div/div/h4[text()='" . $cat . "']/following-sibling::ul/li/a", $resources->item($j));
                for($k = 0; $k < $links->length; $k++){
                    $res_downs[] = array('catg'=>$catg->item($j)->nodeValue,
                        'name'=>$links->item($k)->nodeValue,
                        'url'=>$BASE_URL . $links->item($k)->attributes->getNamedItem('href')->nodeValue,);
                }
            }

            $product_details[] = array(
                'name'=>$dtl_xpath->query("//div[@class='right']/h2")->item(0)->nodeValue,
                'catg'=>$dtl_xpath->query("//div[@class='right']/h2/span")->item(0)->nodeValue,
                'desc'=>$dtl_xpath->query("//div[@id='feature']/div/p/span")->item(0)->nodeValue,
                'notes'=>@$dtl_xpath->query("//div[@class='right']/ul")->item(0)->nodeValue,
                'list_price'=>str_replace('List Price', '', $dtl_xpath->query("//div[@class='right']/h3")->item(0)->nodeValue),
                'img_url'=>$BASE_URL . @$dtl_xpath->query("//div[@class='slider']/div/ul/li/img/@src")->item(0)->nodeValue,
                'res_down'=>$res_downs,);  
        } 
    }

    print_r(json_encode($product_details));
?>

