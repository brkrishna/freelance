<?php
class questions extends MY_Controller{
	
	function questions(){
		
		parent::__construct();
		
		$this->load->helper(array('url', 'form', 'date',));
		$this->load->library(array('form_validation', 'session'));
		
		$this->load->model(array('questions_model'));
	}	
	
	function index($offset = 0){
		
		//Content
		$uri_segment = 3;
		$offset = $this->uri->segment($uri_segment);
		
		$query_id = $this->session->userdata('query_id');

		$this->input->load_query($query_id);

		$code_s = $this->input->get('code_s');
		$name_s = $this->input->get('name_s');

		$this->data['query'] = $this->questions_model->search($code_s, $name_s, $this->limit, $offset);
		
		$page_config['base_url'] = site_url('questions/index/');
        $page_config['total_rows'] = $this->questions_model->count_results($name_s);
        $page_config['per_page'] = $this->limit;
        $page_config['uri_segment'] = $uri_segment;

        $page_config = parent::set_pager_style($page_config);

	    $this->pagination->initialize($page_config);
        
        $this->data['pagination'] = $this->pagination->create_links();		
        
		$this->data['total_rows'] = $page_config['total_rows'];
		
		$this->data['content'] = 'questions_list';
		$this->load->view('templates/default', $this->data);
		
	}
	
	function delete($id = 0){

		if ($id > 0){
			
			$result = $this->questions_model->delete($id);
			
			if($result == 1){
				redirect('contacts_journal/index');
			}
		}
	}
	

	function query($id = 0){
		
		if ($id > 0){
			
			$result = $this->questions_model->get_by_id($id);
			
			if($result != null){
				$this->data['results'] = $this->questions_model->setup($result);
				$this->data['message'] = '';
				$this->data['content'] = 'questions_input';
				$this->load->view('templates/default', $this->data);	
			}
		}
	}
	
	function input(){
		
		$this->data['results'] = $this->questions_model->setup();
		$this->data['message'] = '';
		
		$this->form_validation->set_rules('c_code', 'Code', 'trim|required|xss_clean');
		$this->form_validation->set_rules('c_name', 'Name', 'trim|required|xss_clean');

		if($this->form_validation->run() == FALSE){
			$this->data['content'] = 'questions_input';
			$this->load->view('templates/default', $this->data);
		}
		else{
			
			if($this->input->post('b_submit')){	

				$record = array(
						'chapter_id'=>$this->input->post('c_chapter_id'),
						'sub_part_id'=>$this->input->post('c_subpart_id'),
						'code'=>$this->input->post('c_code'),
						'name'=>$this->input->post('c_name'),
						'short_desc'=>$this->input->post('c_short_desc'),
						'answer_type'=>$this->input->post('c_answer_type'),
						'sort_order'=>$this->input->post('c_sort_order')
					);

				if($this->input->post('c_id') > 0){
					$record['id'] = $this->input->post('c_id');
					$ret = $this->questions_model->update($this->input->post('c_id'), $record);
				}
				else{
					$ret = $this->questions_model->save($record);
				}

				if($ret == TRUE){
					$this->data['result'] = $this->questions_model->setup(null);
					$this->data['message'] = 'Saved';
				}
				else{
					$this->data['message'] = 'Unable to save / update record';	
				}	
			}
			
			$this->data['content'] = 'questions_input';
			$this->load->view('templates/default', $this->data);		
			
		}
	}

	function search(){

		$query_array = array(
		                     'code_s' => $this->input->post('code_s'),
		                     'name_s' => $this->input->post('name_s'),
		       );

		$query_id = $this->input->save_query($query_array);

		$query_arr = array('query_id' => $query_id);

		$this->session->set_userdata($query_arr);
		
		redirect('contacts_journal/index');
	}	
}
?>