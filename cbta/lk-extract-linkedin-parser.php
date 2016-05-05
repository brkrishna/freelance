
<?php

mysql_connect("localhost", "", "") or die(mysql_error()); 

mysql_query("SET NAMES utf8;");

mysql_query("SET CHARACTER_SET utf8;");

mysql_select_db("linkedin") or die(mysql_error());


$id = ''.$_GET['id'].'';
// roger-dickie/a3/a78/946

$url = 'https://www.linkedin.com'.$id.'';
$agent= 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.0.3705; .NET CLR 1.1.4322)';

$ch = curl_init();
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($ch, CURLOPT_VERBOSE, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_USERAGENT, $agent);
curl_setopt($ch, CURLOPT_URL,$url);
$source = curl_exec($ch);



$DOM = new DOMDocument;
     libxml_use_internal_errors(true);
     if (!$DOM->loadHTML('<?xml encoding="utf-8" ?>' . $source))
     {
	     $errors="";
    	 foreach (libxml_get_errors() as $error)  {
            $errors.=$error->message."<br/>";
         }
        libxml_clear_errors();
        print "libxml errors:<br>$errors";
        return;
        }
        $xpath = new DOMXPath($DOM);
		
//	echo $source;
	echo '1';
//	error_reporting(0);	
		
	
$fullname = $xpath->query('//*[@class="profile-overview-content"]/h1[@id="name"]')->item(0);
$fullname = $fullname->textContent;
$name = explode(' ',trim($fullname));
$name[0] = mysql_escape_string(trim($name[0]));
$name[1] = mysql_escape_string(trim($name[1]));
$fullname = mysql_escape_string(trim($fullname));

$location = $xpath->query('//*[@class="locality"]')->item(0);
$location = mysql_escape_string(trim($location->textContent));

$current = $xpath->query('//*[1]/td/ol/li/span[@class="org"]/a')->item(0);
$current = mysql_escape_string(trim($current->textContent));

$test = '';
$test =  $xpath->query('//*[1]/th')->item(0);
echo $test->textContennt;
$test =  $xpath->query('//*[2]/th')->item(0);
echo $test->textContennt;
$test =  $xpath->query('//*[3]/th')->item(0);
echo $test->textContennt;

$fullprevious = mysql_escape_string(trim(implode($previous, ' ')));

$connections = $xpath->query('//*[@class="member-connections"]/strong')->item(0);
$connections = mysql_escape_string(trim($connections->textContent));

$certification = array();
foreach($xpath->query('//*[@class="certification"]/header/h4[@class="item-title"]') as $cert) {
			$cert = $cert->textContent;
			$certification[] = $cert;
					  } 

$fullcertification = mysql_escape_string(trim(implode($certification, ' | ')));

$group = array();
foreach($xpath->query('//*[@class="group"]/h4[@class="item-title"]/a') as $groups) {
			$groups = $groups->textContent;
			$group[] = $groups;
					  } 

$fullgroup = mysql_escape_string(trim(implode($group, ' | ')));

$language = array();
foreach($xpath->query('//*[@class="language"]') as $languages) {
			$languages = $languages->textContent;
			$language[] = $languages;
					  } 

$fulllanguage = mysql_escape_string(trim(implode($language, ', ')));

$summery = $xpath->query('//*[@id="summary"]/div[@class="description"]/p')->item(0);
$summery = mysql_escape_string(trim($summery->textContent));

$industry = $xpath->query('//*[@class="descriptor"]')->item(0);
$industry = mysql_escape_string(trim($industry->textContent));

$website = $xpath->query('//*[@class="websites"]/td/ol/li/a/@href')->item(0);
$website = mysql_escape_string(trim($website->textContent));

$skill = array();
foreach($xpath->query('//*[@class="skill"]') as $skills) {
			$skills = $skills->textContent;
			$skill[] = $skills;
					  } 

$fullskills = mysql_escape_string(trim(implode($skill, ', ')));

$intrest = array();
foreach($xpath->query('//*[@class="interest"]') as $intrests) {
			$intrests = $intrests->textContent;
			$intrest[] = $intrests;
					  } 

$fullintrests = mysql_escape_string(trim(implode($intrest, ', ')));


$organisation = array();
foreach($xpath->query('//*[@id="organizations"]/ul') as $organisations) {
			$organisations = $organisations->textContent;
			$organisation[] = $organisations;
					  } 

$fullorganisation = mysql_escape_string(trim(implode($organisation, ' | ')));

$headline = $xpath->query('//*[@class="headline title"]')->item(0);
$headline = mysql_escape_string(trim($headline->textContent));

$company = $xpath->query('//*[@class="org"]')->item(0);
$company = mysql_escape_string(trim($company->textContent));

$companyhref = $xpath->query('//*[@class="org"]/@href')->item(0);
$companyhref = mysql_escape_string(trim($companyhref->textContent));


$education = $xpath->query('//*[@class="extra-info"]/tbody/tr[2]/td/ol/li')->item(0);
if (isset($education)) {
			$education = mysql_escape_string(trim($education->textContent));}
			 else {
				$education = $xpath->query('//*[@class="extra-info"]/tbody/tr[3]/td')->item(0);
				$education = mysql_escape_string(trim($education->textContent));
				}


mysql_query("INSERT INTO profile SET PublicURL ='$url', fullname ='$fullname', FirstName = '$name[0]', LastName = '$name[1]',
            Location ='$location',Industry ='$industry',Headline ='$headline',Website ='$website', Education = '$education',
			Skills ='$fullskills', Current ='$current', Previous ='$fullprevious', Connections ='$connections', Certification ='$fullcertification',
			Groups ='$fullgroup', Summery ='$summery', Language ='$fulllanguage',Interests ='$fullintrests',Organisations ='$fullorganisation'") or die(mysql_error());


foreach($xpath->query('//*[@class="position"]') as $row) {
	foreach($xpath->query('header/h4[@class="item-title"]/a', $row) as $position) {
		$position = mysql_escape_string(trim($position->textContent));
		
		}
			
		foreach($xpath->query('header/h5[@class="item-subtitle"]', $row) as $companyname) {
			$companyname = mysql_escape_string(trim($companyname->textContent));
		}	
		foreach($xpath->query('header/h5[@class="item-subtitle"]/a/@href', $row) as $companyurl) {
			$companyurl = mysql_escape_string(trim($companyurl->textContent));
		}	
		foreach($xpath->query('div[@class="meta"]/span[@class="date-range"]/time[1]', $row) as $startdate) {
			$startdate = mysql_escape_string(trim($startdate->textContent));
		}
		foreach($xpath->query('div[@class="meta"]/span[@class="date-range"]/time[2]', $row) as $enddate) {
			$enddate = mysql_escape_string(trim($enddate->textContent));
		}
		foreach($xpath->query('div[@class="meta"]/span[@class="location"]', $row) as $explocation) {
			if (isset($explocation)) {
			($explocation = mysql_escape_string(trim($explocation->textContent)));}
			 else {
				$explocation = ''; }
		}
		foreach($xpath->query('p[@class="description"]', $row) as $expdescription) {
			$expdescription = mysql_escape_string(trim($expdescription->textContent));

		}
		
		
		mysql_query("INSERT INTO experience SET CompanyID ='$companyurl', ProfileID ='$url', CompanyName ='$companyname',Position ='$position'
				,StartDate ='$startdate',EndDate ='$enddate',Location ='$explocation',Description ='$expdescription'") or die(mysql_error());
}




foreach($xpath->query('//*[@class="school"]') as $edu) {
		foreach($xpath->query('header/h4[@class="item-title"]', $edu) as $row) {
			$Institute = mysql_escape_string(trim($row->textContent));
		}
		foreach($xpath->query('header/h5[@class="item-subtitle"]', $edu) as $row) {
			$Degree = mysql_escape_string(trim($row->textContent));
		}
		foreach($xpath->query('div[@class="meta"]/span[@class="date-range"]', $edu) as $row) {
			$Year = mysql_escape_string(trim($row->textContent));
		}
		foreach($xpath->query('div[@class="description"]/p', $edu) as $row) {
			$Description = mysql_escape_string(trim($row->textContent));
		}
		mysql_query("INSERT INTO education SET LinkedInURL ='$url', Institute ='$Institute',Degree ='$Degree'
				,Years ='$Year',Description ='$Description'") or die(mysql_error());
					  } 


//*[@class='school']/div[@class='description']/p


//mysql_query("INSERT INTO bahrain SET name='$name', position='$position', previouscompany='$previouscompany',location='$location', 
//industry='$industry', company='$company', image='$image', education='$education', education2='$education2', 
//companywebsite='$companywebsite', url='$url'") or die(mysql_error());
mysql_close()


?>