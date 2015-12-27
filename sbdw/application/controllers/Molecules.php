<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Molecules extends MY_Controller {

	function Molecules(){
		
		parent::__construct();
		
		$this->load->model('molecules_model');
	}	
    
	public function index($type = 'dd', $offset = 0)
	{
        $this->limit = 1;
        
        $uri_segment = 4;
        
        if($this->uri->segment($uri_segment)){
            $offset = $this->uri->segment($uri_segment);           
        }
        
		//Generate pagination
		$this->load->library('pagination');
		$config['base_url'] = site_url('index.php/Molecules/index/' . $type . '/');
        $config['total_rows'] = $this->molecules_model->count_all();
        $config['per_page'] = $this->limit;
        $config['uri_segment'] = $uri_segment;
        
        $config = $this->set_pager_style($config);    

        $this->pagination->initialize($config);
        $this->data['pagination'] = $this->pagination->create_links();		
        
        $this->data['records'] = $this->molecules_model->get_paged_mol_list($this->limit, $offset);     
        $this->data['record_count'] = $this->molecules_model->count_all();
        $this->data['unique_src_family'] = $this->molecules_model->unique_src_family();
        $src_type_count = $this->molecules_model->top_5_src_family();
        $options = array();
        $maximum = 0;
        foreach($src_type_count->result() as $s){
            if ($s->src_type_count > $maximum) { $maximum = $s->src_type_count; }
            $options[] = array('term' => $s->src_type, 'counter'=>$s->src_type_count);
        }
        
        $this->data['terms'] = $options;
        $this->data['data'] = array(4, 8, 16, 32, 46, 76);
        $this->data['maximum'] = $maximum;
        
        $this->load->view('molecules', $this->data);
        
	}
    public function counts(){
        
    }
}
