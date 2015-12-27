<?php
require_once('../simpletest/browser.php');

$browser = new SimpleBrowser();
$browser->get('http://mentor-stereo.codio.io:3000/app/public/index.php/login');
$browser->setFieldByName('login', 'admin');
$browser->setFieldByName('login', 'admin');
$browser->clickSubmit('Log In');

?>