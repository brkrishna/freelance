<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Content controller
 */
class Content extends Admin_Controller
{
    protected $permissionCreate = 'Ingredients.Content.Create';
    protected $permissionDelete = 'Ingredients.Content.Delete';
    protected $permissionEdit   = 'Ingredients.Content.Edit';
    protected $permissionView   = 'Ingredients.Content.View';

    /**
	 * Constructor
	 *
	 * @return void
	 */
	public function __construct()
	{
		parent::__construct();
		
        $this->auth->restrict($this->permissionView);
		$this->load->model('ingredients/ingredients_model');
        $this->lang->load('ingredients');
		
            $this->form_validation->set_error_delimiters("<span class='error'>", "</span>");
        
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('ingredients', 'ingredients.js');
	}

	/**
	 * Display a list of Ingredients data.
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
					$deleted = $this->ingredients_model->delete($pid);
                    if ($deleted == false) {
                        $result = false;
                    }
				}
				if ($result) {
					Template::set_message(count($checked) . ' ' . lang('ingredients_delete_success'), 'success');
				} else {
					Template::set_message(lang('ingredients_delete_failure') . $this->ingredients_model->error, 'error');
				}
			}
		}
        $pagerUriSegment = 5;
        $pagerBaseUrl = site_url(SITE_AREA . '/content/ingredients/index') . '/';
        
        $limit  = $this->settings_lib->item('site.list_limit') ?: 15;

        $this->load->library('pagination');
        $pager['base_url']    = $pagerBaseUrl;
        $pager['total_rows']  = $this->ingredients_model->count_all();
        $pager['per_page']    = $limit;
        $pager['uri_segment'] = $pagerUriSegment;

        $this->pagination->initialize($pager);
        $this->ingredients_model->limit($limit, $offset);
        
		$records = $this->ingredients_model->find_all();

		Template::set('records', $records);
        
    Template::set('toolbar_title', lang('ingredients_manage'));

		Template::render();
	}
    
    /**
	 * Create a Ingredients object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict($this->permissionCreate);
        
		if (isset($_POST['save'])) {
			if ($insert_id = $this->save_ingredients()) {
				log_activity($this->auth->user_id(), lang('ingredients_act_create_record') . ': ' . $insert_id . ' : ' . $this->input->ip_address(), 'ingredients');
				Template::set_message(lang('ingredients_create_success'), 'success');

				redirect(SITE_AREA . '/content/ingredients');
			}

            // Not validation error
			if ( ! empty($this->ingredients_model->error)) {
				Template::set_message(lang('ingredients_create_failure') . $this->ingredients_model->error, 'error');
            }
		}

		Template::set('toolbar_title', lang('ingredients_action_create'));

		Template::render();
	}
	/**
	 * Allows editing of Ingredients data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);
		if (empty($id)) {
			Template::set_message(lang('ingredients_invalid_id'), 'error');

			redirect(SITE_AREA . '/content/ingredients');
		}
        
		if (isset($_POST['save'])) {
			$this->auth->restrict($this->permissionEdit);

			if ($this->save_ingredients('update', $id)) {
				log_activity($this->auth->user_id(), lang('ingredients_act_edit_record') . ': ' . $id . ' : ' . $this->input->ip_address(), 'ingredients');
				Template::set_message(lang('ingredients_edit_success'), 'success');
				redirect(SITE_AREA . '/content/ingredients');
			}

            // Not validation error
            if ( ! empty($this->ingredients_model->error)) {
                Template::set_message(lang('ingredients_edit_failure') . $this->ingredients_model->error, 'error');
			}
		}
        
		elseif (isset($_POST['delete'])) {
			$this->auth->restrict($this->permissionDelete);

			if ($this->ingredients_model->delete($id)) {
				log_activity($this->auth->user_id(), lang('ingredients_act_delete_record') . ': ' . $id . ' : ' . $this->input->ip_address(), 'ingredients');
				Template::set_message(lang('ingredients_delete_success'), 'success');

				redirect(SITE_AREA . '/content/ingredients');
			}

            Template::set_message(lang('ingredients_delete_failure') . $this->ingredients_model->error, 'error');
		}
        
        Template::set('ingredients', $this->ingredients_model->find($id));

		Template::set('toolbar_title', lang('ingredients_edit_heading'));
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
	private function save_ingredients($type = 'insert', $id = 0)
	{
		if ($type == 'update') {
			$_POST['id'] = $id;
		}

        // Validate the data
        $this->form_validation->set_rules($this->ingredients_model->get_validation_rules());
        if ($this->form_validation->run() === false) {
            return false;
        }

		// Make sure we only pass in the fields we want
		
		$data = $this->ingredients_model->prep_data($this->input->post());

        // Additional handling for default values should be added below,
        // or in the model's prep_data() method
        

        $return = false;
		if ($type == 'insert') {
			$id = $this->ingredients_model->insert($data);

			if (is_numeric($id)) {
				$return = $id;
			}
		} elseif ($type == 'update') {
			$return = $this->ingredients_model->update($id, $data);
		}

		return $return;
	}
}