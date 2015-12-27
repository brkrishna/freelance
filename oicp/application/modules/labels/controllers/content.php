<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Content controller
 */
class Content extends Admin_Controller
{
    protected $permissionCreate = 'Labels.Content.Create';
    protected $permissionDelete = 'Labels.Content.Delete';
    protected $permissionEdit   = 'Labels.Content.Edit';
    protected $permissionView   = 'Labels.Content.View';

    /**
	 * Constructor
	 *
	 * @return void
	 */
	public function __construct()
	{
		parent::__construct();
		
        $this->auth->restrict($this->permissionView);
		$this->load->model('labels/labels_model');
		$this->load->model(array('products/products_model', ));
        $this->lang->load('labels');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');
            $this->form_validation->set_error_delimiters("<span class='error'>", "</span>");
        
		$products_select = $this->products_model->get_products_select();
		Template::set('products_select', $products_select);

		$products = $this->products_model->get_products();
		Template::set('products', $products);
        
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('labels', 'labels.js');
	}

	/**
	 * Display a list of Labels data.
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
					$deleted = $this->labels_model->delete($pid);
                    if ($deleted == false) {
                        $result = false;
                    }
				}
				if ($result) {
					Template::set_message(count($checked) . ' ' . lang('labels_delete_success'), 'success');
				} else {
					Template::set_message(lang('labels_delete_failure') . $this->labels_model->error, 'error');
				}
			}
		}
        $pagerUriSegment = 5;
        $pagerBaseUrl = site_url(SITE_AREA . '/content/labels/index') . '/';
        
        $limit  = $this->settings_lib->item('site.list_limit') ?: 15;

        $this->load->library('pagination');
        $pager['base_url']    = $pagerBaseUrl;
        $pager['total_rows']  = $this->labels_model->count_all();
        $pager['per_page']    = $limit;
        $pager['uri_segment'] = $pagerUriSegment;

        $this->pagination->initialize($pager);
        $this->labels_model->limit($limit, $offset);
        
		$records = $this->labels_model->find_all();

		Template::set('records', $records);
        
    Template::set('toolbar_title', lang('labels_manage'));

		Template::render();
	}
    
    /**
	 * Create a Labels object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict($this->permissionCreate);
        
		if (isset($_POST['save'])) {
			if ($insert_id = $this->save_labels()) {
				log_activity($this->auth->user_id(), lang('labels_act_create_record') . ': ' . $insert_id . ' : ' . $this->input->ip_address(), 'labels');
				Template::set_message(lang('labels_create_success'), 'success');

				redirect(SITE_AREA . '/content/labels');
			}

            // Not validation error
			if ( ! empty($this->labels_model->error)) {
				Template::set_message(lang('labels_create_failure') . $this->labels_model->error, 'error');
            }
		}

		Template::set('toolbar_title', lang('labels_action_create'));

		Template::render();
	}
	/**
	 * Allows editing of Labels data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);
		if (empty($id)) {
			Template::set_message(lang('labels_invalid_id'), 'error');

			redirect(SITE_AREA . '/content/labels');
		}
        
		if (isset($_POST['save'])) {
			$this->auth->restrict($this->permissionEdit);

			if ($this->save_labels('update', $id)) {
				log_activity($this->auth->user_id(), lang('labels_act_edit_record') . ': ' . $id . ' : ' . $this->input->ip_address(), 'labels');
				Template::set_message(lang('labels_edit_success'), 'success');
				redirect(SITE_AREA . '/content/labels');
			}

            // Not validation error
            if ( ! empty($this->labels_model->error)) {
                Template::set_message(lang('labels_edit_failure') . $this->labels_model->error, 'error');
			}
		}
        
		elseif (isset($_POST['delete'])) {
			$this->auth->restrict($this->permissionDelete);

			if ($this->labels_model->delete($id)) {
				log_activity($this->auth->user_id(), lang('labels_act_delete_record') . ': ' . $id . ' : ' . $this->input->ip_address(), 'labels');
				Template::set_message(lang('labels_delete_success'), 'success');

				redirect(SITE_AREA . '/content/labels');
			}

            Template::set_message(lang('labels_delete_failure') . $this->labels_model->error, 'error');
		}
        
        Template::set('labels', $this->labels_model->find($id));

		Template::set('toolbar_title', lang('labels_edit_heading'));
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
	private function save_labels($type = 'insert', $id = 0)
	{
		if ($type == 'update') {
			$_POST['id'] = $id;
		}

        // Validate the data
        //$this->form_validation->set_rules($this->labels_model->get_validation_rules());
        //if ($this->form_validation->run() === false) {
        //    return false;
        //}

		// Make sure we only pass in the fields we want
		
		//$data = $this->labels_model->prep_data($this->input->post());

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

		$data['product_id']	= $this->input->post('product_id');
		$data['label']	= $this->input->post('label');
		$data['doc_name']	= $this->input->post('doc_name');
		$data['archive']	= $this->input->post('archive');
		$data['rcvd_on']	= $this->input->post('rcvd_on') ? $this->input->post('rcvd_on') : '0000-00-00';

        $return = false;
		if ($type == 'insert') {
			$id = $this->labels_model->insert($data);

			if (is_numeric($id)) {
				$return = $id;
			}
		} elseif ($type == 'update') {
			$return = $this->labels_model->update($id, $data);
		}

		return $return;
	}
}