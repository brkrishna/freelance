<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class intro extends MY_Controller {

	function intro(){
		parent::__construct();
		$this->load->helper(array('url', 'form'));
	}
	
	public function index($alias = 'intro')
	{
		$this->data['message'] = '';
		$this->data['content'] = 'intro';
		$this->load->view('templates/default', $this->data);
	}
}