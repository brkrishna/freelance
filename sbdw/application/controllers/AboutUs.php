<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class AboutUs extends MY_Controller {

	function AboutUs(){
		
		parent::__construct();
	}	
    
	public function index($content = 'aboutus')
	{
		$this->load->view($content, $this->data);
	}
}
