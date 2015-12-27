<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class MY_Controller extends CI_Controller {

	public $limit = 10;
	public $tbl;
	public $data;
	
	function MY_Controller($content = 'home'){
		
		parent::__construct();
		
		//$this->output->enable_profiler(TRUE);
		
		$this->load->helper('url');
		$this->load->library('session');
		//Generate pagination
		$this->load->library('pagination');

		if($this->uri->segment(1) != NULL){
			$this->data['currentlink'] = $this->uri->segment(1);
		}
		else{
			$this->data['currentlink'] = 'home';
		}
		
		$this->data['base'] =  $this->config->item('base_url');
        
	}

	function set_pager_style($page_config){
		$page_config['full_tag_open'] = "<ul class='pagination pagination-sm'>";
		$page_config['full_tag_close'] ="</ul>";
		$page_config['num_tag_open'] = '<li>';
		$page_config['num_tag_close'] = '</li>';
		$page_config['cur_tag_open'] = "<li class='active'><a href='#'>";
		$page_config['cur_tag_close'] = "<span class='sr-only'></span></a></li>";
		$page_config['next_tag_open'] = "<li>";
		$page_config['next_tagl_close'] = "</li>";
		$page_config['prev_tag_open'] = "<li>";
		$page_config['prev_tagl_close'] = "</li>";
		$page_config['first_tag_open'] = "<li>";
		$page_config['first_tagl_close'] = "</li>";
		$page_config['first_link'] = "<<";
		$page_config['last_tag_open'] = "<li>";
		$page_config['last_tagl_close'] = "</li>";
		$page_config['last_link'] = ">>";
		return $page_config;
	}    
}

