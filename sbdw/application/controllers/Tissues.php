<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Tissues extends MY_Controller {

	function Tissues(){
		
		parent::__construct();
		
		$this->load->model('tissues_model');
	}	
    
	public function tissue($group = 'liver', $offset = 0)
	{
        $this->limit = 10;
        
        $uri_segment = 4;
        
        if($this->uri->segment($uri_segment)){
            $offset = $this->uri->segment($uri_segment);           
        }
          
       //Generate pagination
		$this->load->library('pagination');
		$config['base_url'] = site_url('/Tissues/tissue/' . $group . '/');
        $config['total_rows'] = $this->tissues_model->count_results($group);
        $config['per_page'] = $this->limit;
        $config['uri_segment'] = $uri_segment;
        
        $config = $this->set_pager_style($config);    

        $this->pagination->initialize($config);
        $this->data['pagination'] = $this->pagination->create_links();		
        
        $this->data['breadcrumb'] = $this->get_breadcrumb($group);
        
        $this->data['records'] = $this->tissues_model->get_tissues($group, $this->limit, $offset);
        $this->data['category'] = $group;
        $this->data['record_count'] = $config['total_rows'];
        
        $this->load->view('tissues', $this->data);
	}    
    public function tissue_details($content = 'tissue_dtls', $offset = 0)
	{
        $this->limit = 1;
        
        $uri_segment = 4;
        
        if($this->uri->segment($uri_segment)){
            $offset = $this->uri->segment($uri_segment);           
        }
        
		//Generate pagination
		$this->load->library('pagination');
		$config['base_url'] = site_url('index.php/tissues/tissue_details/' . $content . '/');
        $config['total_rows'] = $this->tissues_model->count_all();
        $config['per_page'] = $this->limit;
        $config['uri_segment'] = $uri_segment;
        
        $config = $this->set_pager_style($config);    

        $this->pagination->initialize($config);
        $this->data['pagination'] = $this->pagination->create_links();		
        
        $this->data['breadcrumb'] = $this->get_breadcrumb($content);
        
        $this->data['records'] = $this->tissues_model->get_paged_mol_list($this->limit, $offset);     
        $this->data['record_count'] = $this->tissues_model->count_all();
        
        
        $this->load->view('tissue_details', $this->data);
	}    
   
    public function counts(){
        
    }
    
}
