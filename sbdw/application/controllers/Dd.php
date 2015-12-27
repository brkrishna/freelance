<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Dd extends MY_Controller {

	function Dd(){
		
		parent::__construct();
		
		$this->load->model('molecules_model');
	}	
    
	public function index($content = 'dd')
	{
        if($content == 'npl'){
            $div_family = $this->molecules_model->src_family(20);
            $options = array();
            $maximum = 0;
            foreach($div_family->result() as $s){
                if ($s->row_count > $maximum) { $maximum = $s->row_count; }
                $options[] = array('term' => $s->family, 'counter'=>$s->row_count);
            }

            $this->data['terms'] = $options;
            $this->data['maximum'] = $maximum;
            //MIS
            $this->data['family_top'] = $this->molecules_model->src_family(5);
            $this->data['tc_top'] = $this->molecules_model->thera_catg(5);
            $this->data['family_plants'] = $this->molecules_model->family_plants(10);
        }
        
        //$this->data['breadcrumb'] = $this->get_breadcrumb($content);
		$this->load->view($content, $this->data);
	}

	public function molecules($content = 'botan', $offset = 0)
	{
        $this->limit = 1;
        
        $uri_segment = 4;
        
        if($this->uri->segment($uri_segment)){
            $offset = $this->uri->segment($uri_segment);           
        }
        
		//Generate pagination
		$this->load->library('pagination');
		$config['base_url'] = site_url('/Dd/molecules/' . $content . '/');
        $config['total_rows'] = $this->molecules_model->count_all();
        $config['per_page'] = $this->limit;
        $config['uri_segment'] = $uri_segment;
        
        $config = $this->set_pager_style($config);    

        $this->pagination->initialize($config);
        $this->data['pagination'] = $this->pagination->create_links();		
        
        //$this->data['breadcrumb'] = $this->get_breadcrumb($content);
        
        $this->data['records'] = $this->molecules_model->get_paged_mol_list($this->limit, $offset);     
        $this->data['record_count'] = $this->molecules_model->count_all();
        $this->data['src_family_count'] = $this->molecules_model->unique_counts('source_family');
        $this->data['data'] = array(4, 8, 16, 32, 46, 76);
        
        $this->load->view('molecules', $this->data);
	}    
    
    public function decade_count($content = 'botan', $offset = 0){
        
       $uri_segment = 4;
        
        if($this->uri->segment($uri_segment)){
            $offset = $this->uri->segment($uri_segment);           
        }        
        
        $this->data['breadcrumb'] = $this->get_breadcrumb($content);        
        
        $result = json_encode($this->molecules_model->decade_counts($this->limit)); 
        echo ($result);
    }
}
