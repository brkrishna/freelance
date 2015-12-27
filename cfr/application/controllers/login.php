<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class Login extends CI_Controller {

	function Login(){
		parent::__construct();
		
		$this->load->helper(array('url', 'form'));
		$this->load->library(array('form_validation', 'session'));
		$this->load->model('login_model');
	
		//$this->output->enable_profiler(TRUE);
	}
	
	public function index($alias = 'login')
	{
		$this->data['message'] = '';
		$this->data['results'] = $this->login_model->setup();
		$this->data['content'] = 'login';
		$this->load->view('templates/nologin_default', $this->data);
	}

	function input(){

		$this->load->helper(array('url', 'form'));
		$this->load->library(array('form_validation', 'session'));
		
		$this->form_validation->set_rules('user_name', 'Username', 'trim|required|xss_clean');
		$this->form_validation->set_rules('password', 'Password', 'trim|required|xss_clean|callback_login_check');

		$this->data['results'] = $this->login_model->setup();
		$this->data['message'] = '';
		
		if ($this->form_validation->run() == FALSE){
				$this->data['content'] = 'login';
				$this->load->view('templates/nologin_default', $this->data);
			}else{
				redirect('home','refresh');
			}
		}

		function login_check($password){
			$username = $this->input->post('user_name');
			
			$result = $this->login_model->login($username, $password);
			
			$user_id = 0;

			if ($result != ''){
				foreach($result as $row){
					$user_id = $row->id;
				}
			}

			if($result){
				$sess_array = array('id'=>$user_id, 'user_name' => $username, 'logged_in' => TRUE);
				$this->session->set_userdata($sess_array);
				return TRUE;
			}else{
				$this->form_validation->set_message('login_check', 'Invalid username or password...');
				return FALSE;
			}
		}	
	}
?>