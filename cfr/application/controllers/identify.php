
<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class identify extends MY_Controller {

	function identify(){
		parent::__construct();
		$this->load->helper(array('url', 'form'));
	}
	
	public function index()
	{
		$this->data['message'] = '';
		$this->data['content'] = 'identify';
		$this->load->view('templates/default', $this->data);
	}
	
}