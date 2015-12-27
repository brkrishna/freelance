<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class NP extends MY_Controller {

	function NP(){
		
		parent::__construct();
		$this->load->model('molecules_model');
	}	
    
	public function index($content = 'np')
	{
		$this->load->view($content, $this->data);
	}

	public function molecules($content = 'botan', $offset = 0)
	{
        $this->limit = 1;
        
        $uri_segment = 4;
        
        if($this->uri->segment($uri_segment)){
            $offset = $this->uri->segment($uri_segment);           
        }

        //$this->data['breadcrumb'] = $this->get_breadcrumb($content);
        if ($content == 'botan'){
            $table = 'BOTANICULE';
        }elseif ($content == 'marine') {
            $table = 'MARINICULE';
        }elseif ($content == 'micro'){
            $table = 'MICROBICULE';
        }

        if ($offset > 6){
            redirect(base_url('/index.php/Contactus/inquire/' . $table));
        }

        $this->data['records'] = $this->molecules_model->get_paged_mol($table, $this->limit, $offset);     
        $this->data['record_count'] = $this->molecules_model->count_all();
        $this->data['src_family_count'] = $this->molecules_model->unique_counts('source_family');

		//Generate pagination
		$this->load->library('pagination');
		$config['base_url'] = site_url('/NP/molecules/' . $content . '/');
        $config['total_rows'] = $this->molecules_model->count_all();
        $config['per_page'] = $this->limit;
        $config['uri_segment'] = $uri_segment;
        
        $config = $this->set_pager_style($config);    

        $this->pagination->initialize($config);
        $this->data['pagination'] = $this->pagination->create_links();		
        
        $this->load->view('molecules', $this->data);
	}    

	public function vmolecules($content = 'botan', $offset = 0)
	{
        $this->limit = 1;
        
        $uri_segment = 4;
        
        if($this->uri->segment($uri_segment)){
            $offset = $this->uri->segment($uri_segment);           
        }

        //$this->data['breadcrumb'] = $this->get_breadcrumb($content);
        if ($content == 'botan'){
            $table = 'BOTANICULE';
        }elseif ($content == 'marine') {
            $table = 'MARINICULE';
        }elseif ($content == 'micro'){
            $table = 'MICROBICULE';
        }
        
		$this->data['table'] = $table;

        if ($offset > 6){
            redirect(base_url('/index.php/Contactus/vinquire/' . $table));
        }

        $this->data['records'] = $this->molecules_model->get_paged_mol($table, $this->limit, $offset);     
        $this->data['record_count'] = $this->molecules_model->count_all();
        $this->data['src_family_count'] = $this->molecules_model->unique_counts('source_family');

		//Generate pagination
		$this->load->library('pagination');
		$config['base_url'] = site_url('/NP/vmolecules/' . $content . '/');
        $config['total_rows'] = $this->molecules_model->count_all();
        $config['per_page'] = $this->limit;
        $config['uri_segment'] = $uri_segment;
        
        $config = $this->set_pager_style($config);    

        $this->pagination->initialize($config);
        $this->data['pagination'] = $this->pagination->create_links();		
        
        $this->load->view('vmolecules', $this->data);
	}    
}
