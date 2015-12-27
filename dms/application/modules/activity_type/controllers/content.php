<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * content controller
 */
class content extends Admin_Controller
{

	//--------------------------------------------------------------------


	/**
	 * Constructor
	 *
	 * @return void
	 */
	public function __construct()
	{
		parent::__construct();

		$this->auth->restrict('Activity_Type.Content.View');
		$this->load->model('activity_type_model', null, true);
		$this->lang->load('activity_type');
		
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('activity_type', 'activity_type.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		// Deleting anything?
		if (isset($_POST['delete']))
		{
			$checked = $this->input->post('checked');

			if (is_array($checked) && count($checked))
			{
				$result = FALSE;
				foreach ($checked as $pid)
				{
					$result = $this->activity_type_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('activity_type_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('activity_type_delete_failure') . $this->activity_type_model->error, 'error');
				}
			}
		}

		$records = $this->activity_type_model->find_all();
        $total = $this->activity_type_model->count_all();
 
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
 
        $this->pager['base_url']          = current_url() .'?';
        $this->pager['total_rows']            = $total;
        $this->pager['per_page']          = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
 
        Template::set('records', $this->activity_type_model->limit($limit, $offset)->find_all());


		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Activity Type');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Activity Type object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Activity_Type.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_activity_type())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('activity_type_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'activity_type');

				Template::set_message(lang('activity_type_create_success'), 'success');
				redirect(SITE_AREA .'/content/activity_type');
			}
			else
			{
				Template::set_message(lang('activity_type_create_failure') . $this->activity_type_model->error, 'error');
			}
		}
		Assets::add_module_js('activity_type', 'activity_type.js');

		Template::set('toolbar_title', lang('activity_type_create') . ' Activity Type');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Activity Type data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('activity_type_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/activity_type');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Activity_Type.Content.Edit');

			if ($this->save_activity_type('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('activity_type_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'activity_type');

				Template::set_message(lang('activity_type_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('activity_type_edit_failure') . $this->activity_type_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Activity_Type.Content.Delete');

			if ($this->activity_type_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('activity_type_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'activity_type');

				Template::set_message(lang('activity_type_delete_success'), 'success');

				redirect(SITE_AREA .'/content/activity_type');
			}
			else
			{
				Template::set_message(lang('activity_type_delete_failure') . $this->activity_type_model->error, 'error');
			}
		}
		Template::set('activity_type', $this->activity_type_model->find($id));
		Template::set('toolbar_title', lang('activity_type_edit') .' Activity Type');
		Template::render();
	}

	//--------------------------------------------------------------------

	//--------------------------------------------------------------------
	// !PRIVATE METHODS
	//--------------------------------------------------------------------

	/**
	 * Summary
	 *
	 * @param String $type Either "insert" or "update"
	 * @param Int	 $id	The ID of the record to update, ignored on inserts
	 *
	 * @return Mixed    An INT id for successful inserts, TRUE for successful updates, else FALSE
	 */
	private function save_activity_type($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['name']        = $this->input->post('activity_type_name');
        $data['code']        = $this->input->post('activity_type_code');

		if ($type == 'insert')
		{
			$id = $this->activity_type_model->insert($data);

			if (is_numeric($id))
			{
				$return = $id;
			}
			else
			{
				$return = FALSE;
			}
		}
		elseif ($type == 'update')
		{
			$return = $this->activity_type_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}