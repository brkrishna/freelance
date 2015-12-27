<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class home extends MY_Controller {

	function home(){
		parent::__construct();
		$this->load->helper(array('url', 'form'));
		$this->load->model(array('levels_model', 'questions_model',));
		$this->load->library(array('session',));
	}
	
	public function index($level_id = 1, $offset = 0)
	{
		$uri_segment = 3;
		$offset = $this->uri->segment($uri_segment);

		$this->data['left_menus'] = $this->levels_model->get_levels()->result();

		$this->data['questions'] = $this->questions_model->get_questions($level_id)->result();	

		$this->data['pct'] = $this->levels_model->get_pct()->result();				

		$this->data['message'] = '';
		$this->data['content'] = 'home';
		$this->load->view('templates/default', $this->data);

	}

	public function save(){

		$user_id = $this->session->userdata('id');
		if ($user_id == ''){
			$user_id = uniqid();
			$this->session->set_userdata('id', $user_id);
		}

		foreach($this->input->post() as $key => $val)
		{
			$q_id = 0;
			if (substr($key, 0, 2) == 'q_'){
				$q_id  = substr($key, 2);
			} 

			if ($val == '-2') { continue;}

			if ($q_id > 0){
				$record = array('user_id'=>$user_id,
				                'q_id'=>$q_id,
				                'answer'=>$val,
				                );	

				$this->questions_model->upsert($record);

			}
		}

		redirect('home','refresh');
	}
}