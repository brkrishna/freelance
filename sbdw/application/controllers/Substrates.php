<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Substrates extends MY_Controller {

	function Substrates(){
		
		parent::__construct();
		$this->limit = 1;
		$this->load->model(array('substrates_model', 'metabolites_model', 'biotrans_model'));
	}
 
	public function molecule($content = 'substrate', $offset = 0)
	{
		
		$uri_segment = 4;
		
		if($this->uri->segment($uri_segment)){
			$offset = $this->uri->segment($uri_segment);
		}

		if ($offset > 6){
			redirect(base_url('/index.php/Contactus/inquire/' . $table));
		}

		$this->data['records'] = $this->substrates_model->get_paged_mol($this->limit, $offset);
		$this->data['record_count'] = $this->substrates_model->count_all();
		
		//Generate pagination
		$this->load->library('pagination');
		$config['base_url'] = site_url('/Substrates/molecule/' . $content . '/');
		$config['total_rows'] = $this->substrates_model->count_all();
		$config['per_page'] = $this->limit;
		$config['uri_segment'] = $uri_segment;
		
		$config = $this->set_pager_style($config);

		$this->pagination->initialize($config);
		$this->data['pagination'] = $this->pagination->create_links();
		
		$this->load->view('substrates', $this->data);
	}

	public function substrate($s_offset = 0)
	{
		if ($s_offset > 3){
			redirect(base_url('/index.php/Contactus/vinquire/BioTransformations'));
		}

		$this->data['substrate_count'] = $this->substrates_model->count_all();

		$result = $this->substrates_model->get_paged_mol($this->limit, $s_offset);
		$substrate_id = $result->row('substrate_id');
		$this->data['substrate'] = $result;
		$this->data['substrate_id'] = $substrate_id;

		$this->data['s_offset'] = $s_offset;
		$this->data['m_offset'] = 0;
		$this->data['b_offset'] = 0;

		$this->data['metabolites_count'] = $this->metabolites_model->count_by_where('substrate_id', $substrate_id);
		$this->data['metabolite'] = $this->metabolites_model->get_paged_mol($substrate_id, $this->limit);

		$this->data['biotrans_count'] = $this->biotrans_model->count_by_where('substrate_id', $substrate_id);
		$this->data['biotrans'] = $this->biotrans_model->get_paged_mol($substrate_id, $this->limit);
		
		$last_updated_on = $this->biotrans_model->get_last_updated_on('BIOTRANSFORMATION');
		$this->data['cd_timestamp_count'] = $this->biotrans_model->count_by_where('date_imported', $last_updated_on);
		
		$this->data['last_updated_on'] = $last_updated_on;

		$this->load->view('biotransform', $this->data);
	}
	
	public function metabolite($substrate_id, $s_offset = 0, $m_offset = 0)
	{
		$this->data['substrate_count'] = $this->substrates_model->count_all();
		$this->data['substrate'] = $this->substrates_model->get_paged_mol($this->limit, $s_offset);
		$this->data['substrate_id'] = $substrate_id;

		$this->data['s_offset'] = $s_offset;
		$this->data['m_offset'] = $m_offset;
		$this->data['b_offset'] = 0;
		
		$this->data['metabolites_count'] = $this->metabolites_model->count_by_where('substrate_id', $substrate_id);
		$this->data['metabolite'] = $this->metabolites_model->get_paged_mol($substrate_id, $this->limit, $m_offset);

		$this->data['biotrans_count'] = $this->biotrans_model->count_by_where('substrate_id', $substrate_id);
		$this->data['biotrans'] = $this->biotrans_model->get_paged_mol($substrate_id, $this->limit);

		$last_updated_on = $this->biotrans_model->get_last_updated_on('BIOTRANSFORMATION');
		$this->data['cd_timestamp_count'] = $this->biotrans_model->count_by_where('date_imported', $last_updated_on);
		
		$this->data['last_updated_on'] = $last_updated_on;

		$this->load->view('biotransform', $this->data);
	}
	
	public function biotrans($substrate_id, $s_offset = 0, $m_offset = 0, $b_offset)
	{
		$this->data['substrate_count'] = $this->substrates_model->count_all();
		$this->data['substrate'] = $this->substrates_model->get_paged_mol($this->limit, $s_offset);
		$this->data['substrate_id'] = $substrate_id;

		$this->data['s_offset'] = $s_offset;
		$this->data['m_offset'] = $m_offset;
		$this->data['b_offset'] = $b_offset;
		
		$this->data['metabolites_count'] = $this->metabolites_model->count_by_where('substrate_id', $substrate_id);
		$this->data['metabolite'] = $this->metabolites_model->get_paged_mol($substrate_id, $this->limit, $m_offset);

		$this->data['biotrans_count'] = $this->biotrans_model->count_by_where('substrate_id', $substrate_id);
		$this->data['biotrans'] = $this->biotrans_model->get_paged_mol($substrate_id, $this->limit, $b_offset);

		$last_updated_on = $this->biotrans_model->get_last_updated_on('BIOTRANSFORMATION');
		$this->data['cd_timestamp_count'] = $this->biotrans_model->count_by_where('date_imported', $last_updated_on);
		
		$this->data['last_updated_on'] = $last_updated_on;

		$this->load->view('biotransform', $this->data);
	}
}
