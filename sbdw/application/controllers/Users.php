<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Users extends MY_Controller {

	function Users(){
		
		parent::__construct();
        $this->load->helper(array('form', 'url'));
        $this->load->library('form_validation');
		$this->load->model('users_model');
	}	
    
    private function sendemail($content, $activation_key = null)
    {
       
        //Load the email library

        $this->load->library('email');
          
        $config['protocol'] = 'smtp';
        $config['smtp_host'] = 'in5.hostgator.in';
        $config['smtp_user'] = 'alekhya@sristibiosciences.com';
        $config['smtp_pass'] = 'Admin@123';
        $config['smtp_port'] = '465';
        $config['smtp_crypto'] = 'ssl';
        $config['charset'] = 'iso-8859-1';
        $config['mailtype'] = 'html';
        $config['wordwrap'] = TRUE;

        $this->email->initialize($config);
        
        //Initialise the email helper and set the "from"
        $this->email->from("info@sristibiosciences.com", "Website");

        //Set the recipient, subject and message based on the page

        $this->email->to('alekhya@sristibiosciences.com');
        $this->email->subject('Email Confirmation');
        $email_body = "Thank you for Registering.A confirmation email has been sent to {$content["email"]}.Please click on the Activation link to Activate your account";
        $email_body = $email_body . "\r\n" . "<a href='http://griffin-topic.codio.io:3000/sristi/index.php/Users/activate/$activation_key'>Accept</a>";
        $this->email->message($email_body);

        //If the email is sent
        if($this->email->send())
        {
            return true;
        }
        else
        {
            return false;
        }
    }    
       
    
    public function index()
	{
        $this->form_validation->set_rules('name', 'Name', 'required');
        $this->form_validation->set_rules('org', 'Organization', 'required');
        $this->form_validation->set_rules('contact_no', 'Contact No', 'required');
        
        $this->session->set_flashdata('msg', '');
        if($this->input->post()){
            
            if ($this->form_validation->run() == FALSE){
                $this->session->set_flashdata('msg', 'Error!!');
            }else{
                //Send the email
                $activation_key = md5(uniqid(rand()));
                if($this->sendemail($_POST, $activation_key))
                {
                    $this->session->set_flashdata('msg', 'Saved');
                }

                //If page exists load all necessary views
                $data = array(
                        'name' => $this->input->post('name'),
                        'desg' => $this->input->post('desg'),
                        'org' => $this->input->post('org'),
                        'contact_no' => $this->input->post('contact_no'),
                        'email' => $this->input->post('email'),
                        'activation_key' => $activation_key, 
                        'password' => $this->input->post('password'), 
                        'confirm_password' => $this->input->post('confirm_password'), 
                      );            

                $this->users_model->save($data);
                
            }   

        }
    
      function activate($pass_key = 'activation_key')
	    {
        $this->limit = 1;
        
        $uri_segment = 4;
        
        if($this->uri->segment($uri_segment)){
            $offset = $this->uri->segment($uri_segment);           
        }
        
		//Generate pagination
		$this->load->library('pagination');
		$config['base_url'] = site_url('index.php/Users/activate/' . $pass_key . '/');
        $config['total_rows'] = $this->users_model->count_results($pass_key);
        $config['per_page'] = $this->limit;
        $config['uri_segment'] = $uri_segment;
        
        $config = $this->set_pager_style($config);    

        $this->pagination->initialize($config);
        $this->data['pagination'] = $this->pagination->create_links();
         
        $this->data['records'] = $this->users_model->get_activate($pass_key);     
        $this->data['record_count'] = $config['total_rows'];
        $this->load->view('thank', $this->data);    
     }
     $this->data['breadcrumb'] = $this->get_breadcrumb('users');
     $this->load->view('users', $this->data);
	}    
    function view($is_active = null)
        {
        
        $data['records'] = $this->users_model->get_view($is_active);

    }
     
       
    } 
