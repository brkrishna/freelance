<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Content controller
 */
class Content extends Admin_Controller
{
    protected $permissionCreate = 'Product_documents.Content.Create';
    protected $permissionDelete = 'Product_documents.Content.Delete';
    protected $permissionEdit   = 'Product_documents.Content.Edit';
    protected $permissionView   = 'Product_documents.Content.View';

    /**
	 * Constructor
	 *
	 * @return void
	 */
	public function __construct()
	{
		parent::__construct();
		
        $this->auth->restrict($this->permissionView);
		$this->load->model('product_documents/product_documents_model');
		$this->load->model(array('products/products_model'));
        $this->lang->load('product_documents');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');
            $this->form_validation->set_error_delimiters("<span class='error'>", "</span>");
        
		$products_select = $this->products_model->get_products_select();
		Template::set('products_select', $products_select);

		$products = $this->products_model->get_products();
		Template::set('products', $products);

		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('product_documents', 'product_documents.js');
	}

	/**
	 * Display a list of Product Documents data.
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
					$deleted = $this->product_documents_model->delete($pid);
                    if ($deleted == false) {
                        $result = false;
                    }
				}
				if ($result) {
					Template::set_message(count($checked) . ' ' . lang('product_documents_delete_success'), 'success');
				} else {
					Template::set_message(lang('product_documents_delete_failure') . $this->product_documents_model->error, 'error');
				}
			}
		}
        $pagerUriSegment = 5;
        $pagerBaseUrl = site_url(SITE_AREA . '/content/product_documents/index') . '/';
        
        $limit  = $this->settings_lib->item('site.list_limit') ?: 15;

        $this->load->library('pagination');
        $pager['base_url']    = $pagerBaseUrl;
        $pager['total_rows']  = $this->product_documents_model->count_all();
        $pager['per_page']    = $limit;
        $pager['uri_segment'] = $pagerUriSegment;

        $this->pagination->initialize($pager);
        $this->product_documents_model->limit($limit, $offset);
        
		$records = $this->product_documents_model->find_all();

		Template::set('records', $records);
        
    Template::set('toolbar_title', lang('product_documents_manage'));

		Template::render();
	}
    
    /**
	 * Create a Product Documents object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict($this->permissionCreate);
        
		if (isset($_POST['save'])) {
			if ($insert_id = $this->save_product_documents()) {
				log_activity($this->auth->user_id(), lang('product_documents_act_create_record') . ': ' . $insert_id . ' : ' . $this->input->ip_address(), 'product_documents');
				Template::set_message(lang('product_documents_create_success'), 'success');

				redirect(SITE_AREA . '/content/product_documents');
			}

            // Not validation error
			if ( ! empty($this->product_documents_model->error)) {
				Template::set_message(lang('product_documents_create_failure') . $this->product_documents_model->error, 'error');
            }
		}

		Template::set('toolbar_title', lang('product_documents_action_create'));

		Template::render();
	}
	/**
	 * Allows editing of Product Documents data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);
		if (empty($id)) {
			Template::set_message(lang('product_documents_invalid_id'), 'error');

			redirect(SITE_AREA . '/content/product_documents');
		}
        
		if (isset($_POST['save'])) {
			$this->auth->restrict($this->permissionEdit);

			if ($this->save_product_documents('update', $id)) {
				log_activity($this->auth->user_id(), lang('product_documents_act_edit_record') . ': ' . $id . ' : ' . $this->input->ip_address(), 'product_documents');
				Template::set_message(lang('product_documents_edit_success'), 'success');
				redirect(SITE_AREA . '/content/product_documents');
			}

            // Not validation error
            if ( ! empty($this->product_documents_model->error)) {
                Template::set_message(lang('product_documents_edit_failure') . $this->product_documents_model->error, 'error');
			}
		}
        
		elseif (isset($_POST['delete'])) {
			$this->auth->restrict($this->permissionDelete);

			if ($this->product_documents_model->delete($id)) {
				log_activity($this->auth->user_id(), lang('product_documents_act_delete_record') . ': ' . $id . ' : ' . $this->input->ip_address(), 'product_documents');
				Template::set_message(lang('product_documents_delete_success'), 'success');

				redirect(SITE_AREA . '/content/product_documents');
			}

            Template::set_message(lang('product_documents_delete_failure') . $this->product_documents_model->error, 'error');
		}
        
        Template::set('product_documents', $this->product_documents_model->find($id));

		Template::set('toolbar_title', lang('product_documents_edit_heading'));
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
	private function save_product_documents($type = 'insert', $id = 0)
	{
		if ($type == 'update') {
			$_POST['id'] = $id;
		}

        // Validate the data
        //$this->form_validation->set_rules($this->product_documents_model->get_validation_rules());
        //if ($this->form_validation->run() === false) {
        //    return false;
        //}

		// Make sure we only pass in the fields we want

		//$data = $this->product_documents_model->prep_data($this->input->post());

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

        $data['product_id']	= $this->input->post('product_documents_product_id');
        $data['doc_name']	= $this->input->post('doc_name');
        $data['comments']	= $this->input->post('comments');
        $data['archive']	= $this->input->post('archive');
		$data['rcvd_on']	= $this->input->post('rcvd_on') ? $this->input->post('rcvd_on') : '0000-00-00';

        $return = false;
		if ($type == 'insert') {
			$id = $this->product_documents_model->insert($data);

			if (is_numeric($id)) {
				$return = $id;
			}
		} elseif ($type == 'update') {
			$return = $this->product_documents_model->update($id, $data);
		}

		return $return;
	}
}