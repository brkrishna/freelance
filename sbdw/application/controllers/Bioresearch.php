<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Bioresearch extends MY_Controller {

	function Bioresearch(){
		
		parent::__construct();
		
		$this->load->model('bioresearch_model');
	}	
    
	public function bio($subcategory = 'bonemarrow', $offset = 0)
	{
        $this->limit = 10;
        
        $uri_segment = 4;
        
        if($this->uri->segment($uri_segment)){
            $offset = $this->uri->segment($uri_segment);           
        }
          
       //Generate pagination
		$this->load->library('pagination');
		$config['base_url'] = site_url('index.php/Bioresearch/bio/' . $subcategory . '/');
        $config['total_rows'] = $this->bioresearch_model->count_results($subcategory);
        $config['per_page'] = $this->limit;
        $config['uri_segment'] = $uri_segment;
        
        $config = $this->set_pager_style($config);    

        $this->pagination->initialize($config);
        $this->data['pagination'] = $this->pagination->create_links();		
        
        $this->data['breadcrumb'] = $this->get_breadcrumb($subcategory);
        
        $this->data['records'] = $this->bioresearch_model->get_bioresearch($subcategory, $this->limit, $offset); 
        $this->data['record_count'] = $config['total_rows'];
        
        $this->load->view('bioresearch', $this->data);
	}    
    
   /*public function product_details($content = 'product_dtls', $offset = 0)
	{
        $this->limit = 1;
        
        $uri_segment = 4;
        
        if($this->uri->segment($uri_segment)){
            $offset = $this->uri->segment($uri_segment);           
        }
        
		//Generate pagination
		$this->load->library('pagination');
		$config['base_url'] = site_url('index.php/products/product_details/' . $content . '/');
        $config['total_rows'] = $this->products_model->count_all();
        $config['per_page'] = $this->limit;
        $config['uri_segment'] = $uri_segment;
        
        $config = $this->set_pager_style($config);    

        $this->pagination->initialize($config);
        $this->data['pagination'] = $this->pagination->create_links();		
        
        $this->data['breadcrumb'] = $this->get_breadcrumb($content);
        
        $this->data['records'] = $this->products_model->get_paged_mol_list($this->limit, $offset);     
        $this->data['record_count'] = $this->products_model->count_all();
        
        
        $this->load->view('product_details', $this->data);
	} */   
    
    public function counts(){
        
    }
    
}
