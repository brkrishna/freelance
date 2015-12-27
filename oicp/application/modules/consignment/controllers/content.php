<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Content controller
 */
class Content extends Admin_Controller
{
    protected $permissionCreate = 'Consignment.Content.Create';
    protected $permissionDelete = 'Consignment.Content.Delete';
    protected $permissionEdit   = 'Consignment.Content.Edit';
    protected $permissionView   = 'Consignment.Content.View';

    /**
	 * Constructor
	 *
	 * @return void
	 */
	public function __construct()
	{
		parent::__construct();
		
        $this->auth->restrict($this->permissionView);
		$this->load->model('consignment/consignment_model');
        $this->lang->load('consignment');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');
            $this->form_validation->set_error_delimiters("<span class='error'>", "</span>");
        
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('consignment', 'consignment.js');
	}

	/**
	 * Display a list of Consignment data.
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
					$deleted = $this->consignment_model->delete($pid);
                    if ($deleted == false) {
                        $result = false;
                    }
				}
				if ($result) {
					Template::set_message(count($checked) . ' ' . lang('consignment_delete_success'), 'success');
				} else {
					Template::set_message(lang('consignment_delete_failure') . $this->consignment_model->error, 'error');
				}
			}
		}
        $pagerUriSegment = 5;
        $pagerBaseUrl = site_url(SITE_AREA . '/content/consignment/index') . '/';
        
        $limit  = $this->settings_lib->item('site.list_limit') ?: 15;

        $this->load->library('pagination');
        $pager['base_url']    = $pagerBaseUrl;
        $pager['total_rows']  = $this->consignment_model->count_all();
        $pager['per_page']    = $limit;
        $pager['uri_segment'] = $pagerUriSegment;

        $this->pagination->initialize($pager);
        $this->consignment_model->limit($limit, $offset);
        
		$records = $this->consignment_model->find_all();

		Template::set('records', $records);
        
    Template::set('toolbar_title', lang('consignment_manage'));

		Template::render();
	}
    
    /**
	 * Create a Consignment object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict($this->permissionCreate);
        
		if (isset($_POST['save'])) {
			if ($insert_id = $this->save_consignment()) {
				log_activity($this->auth->user_id(), lang('consignment_act_create_record') . ': ' . $insert_id . ' : ' . $this->input->ip_address(), 'consignment');
				Template::set_message(lang('consignment_create_success'), 'success');

				redirect(SITE_AREA . '/content/consignment');
			}

            // Not validation error
			if ( ! empty($this->consignment_model->error)) {
				Template::set_message(lang('consignment_create_failure') . $this->consignment_model->error, 'error');
            }
		}

		Template::set('toolbar_title', lang('consignment_action_create'));

		Template::render();
	}
	/**
	 * Allows editing of Consignment data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);
		if (empty($id)) {
			Template::set_message(lang('consignment_invalid_id'), 'error');

			redirect(SITE_AREA . '/content/consignment');
		}
        
		if (isset($_POST['save'])) {
			$this->auth->restrict($this->permissionEdit);

			if ($this->save_consignment('update', $id)) {
				log_activity($this->auth->user_id(), lang('consignment_act_edit_record') . ': ' . $id . ' : ' . $this->input->ip_address(), 'consignment');
				Template::set_message(lang('consignment_edit_success'), 'success');
				redirect(SITE_AREA . '/content/consignment');
			}

            // Not validation error
            if ( ! empty($this->consignment_model->error)) {
                Template::set_message(lang('consignment_edit_failure') . $this->consignment_model->error, 'error');
			}
		}
        
		elseif (isset($_POST['delete'])) {
			$this->auth->restrict($this->permissionDelete);

			if ($this->consignment_model->delete($id)) {
				log_activity($this->auth->user_id(), lang('consignment_act_delete_record') . ': ' . $id . ' : ' . $this->input->ip_address(), 'consignment');
				Template::set_message(lang('consignment_delete_success'), 'success');

				redirect(SITE_AREA . '/content/consignment');
			}

            Template::set_message(lang('consignment_delete_failure') . $this->consignment_model->error, 'error');
		}
        
        Template::set('consignment', $this->consignment_model->find($id));

		Template::set('toolbar_title', lang('consignment_edit_heading'));
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
	private function save_consignment($type = 'insert', $id = 0)
	{
		if ($type == 'update') {
			$_POST['id'] = $id;
		}

        // Validate the data
        $this->form_validation->set_rules($this->consignment_model->get_validation_rules());
        if ($this->form_validation->run() === false) {
            return false;
        }

		// Make sure we only pass in the fields we want
		
		$data = $this->consignment_model->prep_data($this->input->post());

        // Additional handling for default values should be added below,
        // or in the model's prep_data() method
        
		$data['c_date']	= $this->input->post('c_date') ? $this->input->post('c_date') : '0000-00-00';

        $return = false;
		if ($type == 'insert') {
			$id = $this->consignment_model->insert($data);

			if (is_numeric($id)) {
				$return = $id;
			}
		} elseif ($type == 'update') {
			$return = $this->consignment_model->update($id, $data);
		}

		return $return;
	}
}