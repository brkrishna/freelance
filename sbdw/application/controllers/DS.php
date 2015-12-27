<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class DS extends MY_Controller {

	function DS(){
		
		parent::__construct();
	}	
    
	public function index($content = 'dsvcs')
	{
		$this->load->view($content, $this->data);
	}
}
