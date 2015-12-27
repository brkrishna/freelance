<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Contactus extends MY_Controller {

	function Contactus(){
		
		parent::__construct();
        $this->load->helper(array('form', 'url'));
        $this->load->library('form_validation');
		$this->load->model('contact_us_model');
	}	
    
	public function index()
	{
        $this->form_validation->set_rules('c_name', 'Name', 'required');
        $this->form_validation->set_rules('c_email', 'E Mail', 'required');
        $this->form_validation->set_rules('c_notes', 'Notes', 'required');
        
        $this->session->set_flashdata('msg', '');
        if($this->input->post()){
            
            if ($this->form_validation->run() == FALSE){
                $this->session->set_flashdata('msg', 'Please fill in required fields...');
            }else{
                //Send the email
                if($this->sendemail($_POST))
                {
                    $this->session->set_flashdata('msg', 'Thank you, we will get back to you shortly...');
                }

                //If page exists load all necessary views
                $data = array(
                        'c_name' => $this->input->post('c_name'),
                        'c_email' => $this->input->post('c_email'),
                        'c_phone' => $this->input->post('c_phone'),
                        'c_subject' => $this->input->post('c_subject'),
                        'c_notes' => $this->input->post('c_notes'),
                    );            

                $this->contact_us_model->save($data);
                //redirect(base_url('/index.php/Contactus/index'));
            }   

        }
        
        $this->load->view('contactus', $this->data);
    }
    
    public function inquire($product = 'General Inquiry')
    {
        $this->form_validation->set_rules('c_name', 'Name', 'required');
        $this->form_validation->set_rules('c_email', 'E Mail', 'required');
        $this->form_validation->set_rules('c_notes', 'Notes', 'required');
        
        $this->session->set_flashdata('msg', '');
        if($this->input->post()){
            
            if ($this->form_validation->run() == FALSE){
                $this->session->set_flashdata('msg', 'Please fill in required fields...');
            }else{
                //Send the email
                if($this->sendemail($_POST))
                {
                    $this->session->set_flashdata('msg', 'Thank you, we will get back to you shortly...');
                }

                //If page exists load all necessary views
                $data = array(
                        'c_name' => $this->input->post('c_name'),
                        'c_email' => $this->input->post('c_email'),
                        'c_phone' => $this->input->post('c_phone'),
                        'c_subject' => $this->input->post('c_subject'),
                        'c_notes' => $this->input->post('c_notes'),
                    );            

                $this->contact_us_model->save($data);
            }   

        }else{
            $this->data['subject'] = $product;    
        }
        
        $this->load->view('inquire', $this->data);
    }

    public function vinquire($product = '')
    {
        $this->form_validation->set_rules('c_name', 'Name', 'required');
        $this->form_validation->set_rules('c_email', 'E Mail', 'required');
        $this->form_validation->set_rules('c_notes', 'Notes', 'required');
        
        $this->session->set_flashdata('msg', '');
        if($this->input->post()){
            
            if ($this->form_validation->run() == FALSE){
                $this->session->set_flashdata('msg', 'Please fill in required fields...');
            }else{
                //Send the email
                if($this->sendemail($_POST))
                {
                    $this->session->set_flashdata('msg', 'Thank you, we will get back to you shortly...');
                }

                //If page exists load all necessary views
                $data = array(
                        'c_name' => $this->input->post('c_name'),
                        'c_email' => $this->input->post('c_email'),
                        'c_phone' => $this->input->post('c_phone'),
                        'c_subject' => $this->input->post('c_subject'),
                        'c_notes' => $this->input->post('c_notes'),
                    );            

                $this->contact_us_model->save($data);
            }   

        }else{
            $this->data['subject'] = $product;    
        }
        
        $this->load->view('vinquire', $this->data);
    }
    
    private function sendemail($content){

        //Load the email library

        $this->load->library('email');

        $config['protocol'] = 'smtp';
        $config['smtp_host'] = 'in5.hostgator.in';
        $config['smtp_user'] = 'info@sristibiosciences.com';
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

        $this->email->to('info@sristibiosciences.com');
        $this->email->subject('Website Enquiry');
        $this->email->message("My name is: {$content["c_name"]}<br /><br />My email address is: {$content["c_email"]}<br /><br />My telephone number is: {$content["c_phone"]}<br /><br />The enquiry is regarding: {$content["c_subject"]}<br /><br />Enquiry: {$content["c_notes"]}");

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
}
