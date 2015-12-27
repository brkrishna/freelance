<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Content controller
 */
class Content extends Admin_Controller
{
    protected $permissionCreate = 'Botan_Structure.Content.Create';
    protected $permissionDelete = 'Botan_Structure.Content.Delete';
    protected $permissionEdit   = 'Botan_Structure.Content.Edit';
    protected $permissionView   = 'Botan_Structure.Content.View';

    /**
	 * Constructor
	 *
	 * @return void
	 */
	public function __construct()
	{
		parent::__construct();
		
        $this->auth->restrict($this->permissionView);
		$this->load->model('botan_structure/botan_structure_model');
        $this->lang->load('botan_structure');
		
        $this->form_validation->set_error_delimiters("<span class='error'>", "</span>");
        
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('botan_structure', 'botan_structure.js');
	}

	/**
	 * Display a list of Botan Structure data.
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
					$deleted = $this->botan_structure_model->delete($pid);
                    if ($deleted == false) {
                        $result = false;
                    }
				}
				if ($result) {
					Template::set_message(count($checked) . ' ' . lang('botan_structure_delete_success'), 'success');
				} else {
					Template::set_message(lang('botan_structure_delete_failure') . $this->botan_structure_model->error, 'error');
				}
			}
		}
        
        
        
		$records = $this->botan_structure_model->find_all();
        $total = $this->botan_structure_model->count_all();
 
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
 
        $this->pager['base_url']          = current_url() .'?';
        $this->pager['total_rows']            = $total;
        $this->pager['per_page']          = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
 
        Template::set('records', $this->botan_structure_model->limit($limit, $offset)->find_all());


		//Template::set('records', $records);
        
        Template::set('toolbar_title', lang('botan_structure_manage'));

		Template::render();
	}
    
    /**
	 * Create a Botan Structure object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict($this->permissionCreate);
        
		if (isset($_POST['save'])) {
			if ($insert_id = $this->save_botan_structure()) {
				log_activity($this->auth->user_id(), lang('botan_structure_act_create_record') . ': ' . $insert_id . ' : ' . $this->input->ip_address(), 'botan_structure');
				Template::set_message(lang('botan_structure_create_success'), 'success');

				redirect(SITE_AREA . '/content/botan_structure');
			}

            // Not validation error
			if ( ! empty($this->botan_structure_model->error)) {
				Template::set_message(lang('botan_structure_create_failure') . $this->botan_structure_model->error, 'error');
            }
		}

		Template::set('toolbar_title', lang('botan_structure_action_create'));

		Template::render();
	}
	/**
	 * Allows editing of Botan Structure data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);
		if (empty($id)) {
			Template::set_message(lang('botan_structure_invalid_id'), 'error');

			redirect(SITE_AREA . '/content/botan_structure');
		}
        
		if (isset($_POST['save'])) {
			$this->auth->restrict($this->permissionEdit);

			if ($this->save_botan_structure('update', $id)) {
				log_activity($this->auth->user_id(), lang('botan_structure_act_edit_record') . ': ' . $id . ' : ' . $this->input->ip_address(), 'botan_structure');
				Template::set_message(lang('botan_structure_edit_success'), 'success');
				redirect(SITE_AREA . '/content/botan_structure');
			}

            // Not validation error
            if ( ! empty($this->botan_structure_model->error)) {
                Template::set_message(lang('botan_structure_edit_failure') . $this->botan_structure_model->error, 'error');
			}
		}
        
		elseif (isset($_POST['delete'])) {
			$this->auth->restrict($this->permissionDelete);

			if ($this->botan_structure_model->delete($id)) {
				log_activity($this->auth->user_id(), lang('botan_structure_act_delete_record') . ': ' . $id . ' : ' . $this->input->ip_address(), 'botan_structure');
				Template::set_message(lang('botan_structure_delete_success'), 'success');

				redirect(SITE_AREA . '/content/botan_structure');
			}

            Template::set_message(lang('botan_structure_delete_failure') . $this->botan_structure_model->error, 'error');
		}
        
        Template::set('botan_structure', $this->botan_structure_model->find($id));

		Template::set('toolbar_title', lang('botan_structure_edit_heading'));
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
	private function save_botan_structure($type = 'insert', $id = 0)
	{
		if ($type == 'update') {
			$_POST['mol_id'] = $id;
		}
        
        function is_validmol($mol) {
          $res = FALSE;
          if ((strpos($mol,'M  END') > 40) && 
             (strpos($mol,'V2000') > 30)) { $res = TRUE; }  // rather simple, for now
          return $res;
        }
		
		

        // Validate the data
        $this->form_validation->set_rules($this->botan_structure_model->get_validation_rules());
        if ($this->form_validation->run() === false) {
            return false;
        }

		// Make sure we only pass in the fields we want
		$data = array();
        echo $this->input->post('botan_structure_struc');
		echo $this->input->get('botan_structure_struc'); 
		
		$data = $this->botan_structure_model->prep_data($this->input->post());

        // Additional handling for default values should be added below,
        // or in the model's prep_data() method
        

        $return = false;
		if ($type == 'insert') {
			$id = $this->botan_structure_model->insert($data);

			if (is_numeric($id)) {
				$return = $id;
			}
		} elseif ($type == 'update') {
			$return = $this->botan_structure_model->update($id, $data);
		}

		return $return;
	}
}











































