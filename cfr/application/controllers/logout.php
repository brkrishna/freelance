<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class Logout extends CI_Controller {

	var $base;
	
	public function index()
	{
		parent::__construct();

		$this->load->library('session');
		$this->load->helper('url');
		
		$this->base = $this->config->item('base_url');

		$data['base'] = $this->base;
		
		$this->session->sess_destroy();

		redirect('login', 'refresh');
	}
}
?>