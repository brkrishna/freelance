<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class CP extends MY_Controller {

	function CP(){
		
		parent::__construct();
	}	
    
	public function index($content = 'cp')
	{
		$this->load->view($content, $this->data);
	}
}
