<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Products extends MY_Controller {

	function Products(){
		
		parent::__construct();
		
		$this->load->model('products_model');
	}	

    public function product($category = 'cells', $offset = 0)
    {
        $this->limit = 10;
        
        $uri_segment = 4;
        
        if($this->uri->segment($uri_segment)){
            $offset = $this->uri->segment($uri_segment);           
        }

       //Generate pagination
        $this->load->library('pagination');
        $config['base_url'] = site_url('Products/product/' . $category . '/');
        $config['total_rows'] = $this->products_model->count_results($category);
        $config['per_page'] = $this->limit;
        $config['uri_segment'] = $uri_segment;
        
        $config = $this->set_pager_style($config);    

        $this->pagination->initialize($config);
        $this->data['pagination'] = $this->pagination->create_links();		
        
        $this->data['records'] = $this->products_model->get_products($category, $this->limit, $offset); 
        $this->data['record_count'] = $config['total_rows'];
        $this->data['category'] = $category;
        
        $this->load->view('products', $this->data);
    }    

    public function query($id = 0){
       if ($id > 0){
            $records = $this->products_model->get_by_id($id);
            if($records != null){
                $this->data['records'] = $this->products_model->get_paged_mol_list($records);
                $this->load->view('product_details', $this->data);	
            }
        }
    }


}
