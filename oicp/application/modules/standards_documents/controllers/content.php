<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Content controller
 */
class Content extends Admin_Controller
{
    protected $permissionCreate = 'Standards_documents.Content.Create';
    protected $permissionDelete = 'Standards_documents.Content.Delete';
    protected $permissionEdit   = 'Standards_documents.Content.Edit';
    protected $permissionView   = 'Standards_documents.Content.View';

    /**
	 * Constructor
	 *
	 * @return void
	 */
	public function __construct()
	{
		parent::__construct();
		
        $this->auth->restrict($this->permissionView);
		$this->load->model('standards_documents/standards_documents_model');
        $this->lang->load('standards_documents');
		
            $this->form_validation->set_error_delimiters("<span class='error'>", "</span>");
        
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('standards_documents', 'standards_documents.js');
	}

	/**
	 * Display a list of Standards Documents data.
	 *
	 * @return void
	 */
	public function index($offset = 0)
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
					$deleted = $this->standards_documents_model->delete($pid);
                    if ($deleted == false) {
                        $result = false;
                    }
				}
				if ($result) {
					Template::set_message(count($checked) . ' ' . lang('standards_documents_delete_success'), 'success');
				} else {
					Template::set_message(lang('standards_documents_delete_failure') . $this->standards_documents_model->error, 'error');
				}
			}
		}
        
        $pagerUriSegment = 5;
        $pagerBaseUrl = site_url(SITE_AREA . '/content/standards_documents/index') . '/';
        
        $limit  = $this->settings_lib->item('site.list_limit') ?: 15;

        $this->load->library('pagination');
        $pager['base_url']    = $pagerBaseUrl;
        $pager['total_rows']  = $this->standards_documents_model->count_all();
        $pager['per_page']    = $limit;
        $pager['uri_segment'] = $pagerUriSegment;

        $this->pagination->initialize($pager);
        $this->standards_documents_model->limit($limit, $offset);        
        
		$records = $this->standards_documents_model->find_all();

		Template::set('records', $records);
        
    Template::set('toolbar_title', lang('standards_documents_manage'));

		Template::render();
	}
    
    /**
	 * Create a Standards Documents object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict($this->permissionCreate);
        
		if (isset($_POST['save'])) {
			if ($insert_id = $this->save_standards_documents()) {
				log_activity($this->auth->user_id(), lang('standards_documents_act_create_record') . ': ' . $insert_id . ' : ' . $this->input->ip_address(), 'standards_documents');
				Template::set_message(lang('standards_documents_create_success'), 'success');

				redirect(SITE_AREA . '/content/standards_documents');
			}

            // Not validation error
			if ( ! empty($this->standards_documents_model->error)) {
				Template::set_message(lang('standards_documents_create_failure') . $this->standards_documents_model->error, 'error');
            }
		}

		Template::set('toolbar_title', lang('standards_documents_action_create'));

		Template::render();
	}
	/**
	 * Allows editing of Standards Documents data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);
		if (empty($id)) {
			Template::set_message(lang('standards_documents_invalid_id'), 'error');

			redirect(SITE_AREA . '/content/standards_documents');
		}
        
		if (isset($_POST['save'])) {
			$this->auth->restrict($this->permissionEdit);

			if ($this->save_standards_documents('update', $id)) {
				log_activity($this->auth->user_id(), lang('standards_documents_act_edit_record') . ': ' . $id . ' : ' . $this->input->ip_address(), 'standards_documents');
				Template::set_message(lang('standards_documents_edit_success'), 'success');
				redirect(SITE_AREA . '/content/standards_documents');
			}

            // Not validation error
            if ( ! empty($this->standards_documents_model->error)) {
                Template::set_message(lang('standards_documents_edit_failure') . $this->standards_documents_model->error, 'error');
			}
		}
        
		elseif (isset($_POST['delete'])) {
			$this->auth->restrict($this->permissionDelete);

			if ($this->standards_documents_model->delete($id)) {
				log_activity($this->auth->user_id(), lang('standards_documents_act_delete_record') . ': ' . $id . ' : ' . $this->input->ip_address(), 'standards_documents');
				Template::set_message(lang('standards_documents_delete_success'), 'success');

				redirect(SITE_AREA . '/content/standards_documents');
			}

            Template::set_message(lang('standards_documents_delete_failure') . $this->standards_documents_model->error, 'error');
		}
        
        Template::set('standards_documents', $this->standards_documents_model->find($id));

		Template::set('toolbar_title', lang('standards_documents_edit_heading'));
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
	private function save_standards_documents($type = 'insert', $id = 0)
	{
		if ($type == 'update') {
			$_POST['id'] = $id;
		}

        // Validate the data
        $this->form_validation->set_rules($this->standards_documents_model->get_validation_rules());
        if ($this->form_validation->run() === false) {
            return false;
        }

		// Make sure we only pass in the fields we want
		
		//$data = $this->standards_documents_model->prep_data($this->input->post());

        // Additional handling for default values should be added below,
        // or in the model's prep_data() method
        
        $data = array();

        //$data = $this->party_documents_model->prep_data($this->input->post());

        if (isset($_FILES['doc_file']) && is_array($_FILES['doc_file']) && $_FILES['doc_file']['error'] != 4)
        {
            // make sure we only pass in the fields we want
            $file_path = $this->config->item('upload_dir');

            $config['upload_path']      = $file_path;
            $config['allowed_types']    = 'pdf|jpeg|gif|docx|doc|xlsx|xls';

            $this->load->library('upload', $config);
            
            if ( ! $this->upload->do_upload('doc_file'))
            {
                return array('error'=>$this->upload->display_errors());
            }else{
                $data['doc_file'] = serialize($this->upload->data());           
            }       

        }

        $data['doc_name']   = $this->input->post('doc_name');
        $data['archive']    = $this->input->post('archive');
        
        $return = false;
		if ($type == 'insert') {
			$id = $this->standards_documents_model->insert($data);

			if (is_numeric($id)) {
				$return = $id;
			}
		} elseif ($type == 'update') {
			$return = $this->standards_documents_model->update($id, $data);
		}

		return $return;
	}
}