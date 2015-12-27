<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Home extends MY_Controller {

	function Home(){
		
		parent::__construct();
	}	
    
	public function index($content = 'home')
	{
		$this->load->view($content, $this->data);
	}
}
