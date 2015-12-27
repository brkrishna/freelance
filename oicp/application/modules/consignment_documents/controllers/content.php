<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Content controller
 */
class Content extends Admin_Controller
{
    protected $permissionCreate = 'Consignment_documents.Content.Create';
    protected $permissionDelete = 'Consignment_documents.Content.Delete';
    protected $permissionEdit   = 'Consignment_documents.Content.Edit';
    protected $permissionView   = 'Consignment_documents.Content.View';

    /**
	 * Constructor
	 *
	 * @return void
	 */
	public function __construct()
	{
		parent::__construct();
		
        $this->auth->restrict($this->permissionView);
		$this->load->model('consignment_documents/consignment_documents_model');
		$this->load->model('consignment/consignment_model');
        $this->lang->load('consignment_documents');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');
            $this->form_validation->set_error_delimiters("<span class='error'>", "</span>");
        
        $consign_select = $this->consignment_model->get_consign_select();
		Template::set('consign_select', $consign_select);

		$consign = $this->consignment_model->get_consign();
		Template::set('consign', $consign);

		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('consignment_documents', 'consignment_documents.js');
	}

	/**
	 * Display a list of Consignment Documents data.
	 *
	 * @return void
	 */
	public function index()
	{
        // Deleting anything?
		if (isset($_POST['delete'])) {
            $this->auth->restrict($this->permissionDelete);
			$checked = $this->input->post('checked');
			if (is_array($checked) && count($checked)) {

                // If any of the deletions fail, set the result to false, so
                // failure message is set if any of the attempts fail, not just
                // the last attempt

				$result = true;
				foreach ($checked as $pid) {
					$deleted = $this->consignment_documents_model->delete($pid);
                    if ($deleted == false) {
                        $result = false;
                    }
				}
				if ($result) {
					Template::set_message(count($checked) . ' ' . lang('consignment_documents_delete_success'), 'success');
				} else {
					Template::set_message(lang('consignment_documents_delete_failure') . $this->consignment_documents_model->error, 'error');
				}
			}
		}
        
        
        
		$records = $this->consignment_documents_model->find_all();

		Template::set('records', $records);
        
    Template::set('toolbar_title', lang('consignment_documents_manage'));

		Template::render();
	}
    
    /**
	 * Create a Consignment Documents object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict($this->permissionCreate);
        
		if (isset($_POST['save'])) {
			if ($insert_id = $this->save_consignment_documents()) {
				log_activity($this->auth->user_id(), lang('consignment_documents_act_create_record') . ': ' . $insert_id . ' : ' . $this->input->ip_address(), 'consignment_documents');
				Template::set_message(lang('consignment_documents_create_success'), 'success');

				redirect(SITE_AREA . '/content/consignment_documents');
			}

            // Not validation error
			if ( ! empty($this->consignment_documents_model->error)) {
				Template::set_message(lang('consignment_documents_create_failure') . $this->consignment_documents_model->error, 'error');
            }
		}

		Template::set('toolbar_title', lang('consignment_documents_action_create'));

		Template::render();
	}
	/**
	 * Allows editing of Consignment Documents data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);
		if (empty($id)) {
			Template::set_message(lang('consignment_documents_invalid_id'), 'error');

			redirect(SITE_AREA . '/content/consignment_documents');
		}
        
		if (isset($_POST['save'])) {
			$this->auth->restrict($this->permissionEdit);

			if ($this->save_consignment_documents('update', $id)) {
				log_activity($this->auth->user_id(), lang('consignment_documents_act_edit_record') . ': ' . $id . ' : ' . $this->input->ip_address(), 'consignment_documents');
				Template::set_message(lang('consignment_documents_edit_success'), 'success');
				redirect(SITE_AREA . '/content/consignment_documents');
			}

            // Not validation error
            if ( ! empty($this->consignment_documents_model->error)) {
                Template::set_message(lang('consignment_documents_edit_failure') . $this->consignment_documents_model->error, 'error');
			}
		}
        
		elseif (isset($_POST['delete'])) {
			$this->auth->restrict($this->permissionDelete);

			if ($this->consignment_documents_model->delete($id)) {
				log_activity($this->auth->user_id(), lang('consignment_documents_act_delete_record') . ': ' . $id . ' : ' . $this->input->ip_address(), 'consignment_documents');
				Template::set_message(lang('consignment_documents_delete_success'), 'success');

				redirect(SITE_AREA . '/content/consignment_documents');
			}

            Template::set_message(lang('consignment_documents_delete_failure') . $this->consignment_documents_model->error, 'error');
		}
        
        Template::set('consignment_documents', $this->consignment_documents_model->find($id));

		Template::set('toolbar_title', lang('consignment_documents_edit_heading'));
		Template::render();
	}

	//--------------------------------------------------------------------
	// !PRIVATE METHODS
	//--------------------------------------------------------------------

	/**
	 * Save the data.
	 *
	 * @param string $type Either 'insert' or 'update'.
	 * @param int	 $id	The ID of the record to update, ignored on inserts.
	 *
	 * @return bool|int An int ID for successful inserts, true for successful
     * updates, else false.
	 */
	private function save_consignment_documents($type = 'insert', $id = 0)
	{
		if ($type == 'update') {
			$_POST['id'] = $id;
		}

        // Validate the data
        //$this->form_validation->set_rules($this->consignment_documents_model->get_validation_rules());
        //if ($this->form_validation->run() === false) {
        //    return false;
        //}

		// Make sure we only pass in the fields we want
		
		//$data = $this->consignment_documents_model->prep_data($this->input->post());

        // Additional handling for default values should be added below,
        // or in the model's prep_data() method
        
		$data = array();

		//$data = $this->party_documents_model->prep_data($this->input->post());

		if (isset($_FILES['doc_file']) && is_array($_FILES['doc_file']) && $_FILES['doc_file']['error'] != 4)
        {
			// make sure we only pass in the fields we want
			$file_path = $this->config->item('upload_dir');

			$config['upload_path']		= $file_path;
			$config['allowed_types']	= 'pdf|jpeg|gif|docx|doc|xlsx|xls';

			$this->load->library('upload', $config);
			
			if ( ! $this->upload->do_upload('doc_file'))
			{
				return array('error'=>$this->upload->display_errors());
			}else{
				$data['doc_file'] = serialize($this->upload->data());			
			}		

		}

        $data['ref_no']	= $this->input->post('ref_no');
        $data['doc_name']	= $this->input->post('doc_name');
		$data['rcvd_on']	= $this->input->post('rcvd_on') ? $this->input->post('rcvd_on') : '0000-00-00';
		$data['comments']	= $this->input->post('comments');
		$data['archive']	= $this->input->post('archive');
		
        $return = false;
		if ($type == 'insert') {
			$id = $this->consignment_documents_model->insert($data);

			if (is_numeric($id)) {
				$return = $id;
			}
		} elseif ($type == 'update') {
			$return = $this->consignment_documents_model->update($id, $data);
		}

		return $return;
	}


}