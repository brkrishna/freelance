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

		$this->auth->restrict('Profile.Content.Edit');
		$this->load->model('profile_model', null, true);
		$this->lang->load('profile');
		
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('profile', 'profile.js');
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
					$result = $this->profile_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('profile_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('profile_delete_failure') . $this->profile_model->error, 'error');
				}
			}
		}

        $user_id = null;    
        
        if ($this->current_user->role_id == 9){
            $user_id = $this->current_user->id;
        }
        
		$records = $this->profile_model->find_all($user_id);
        $total = $this->profile_model->count_all();
 
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
 
        $this->pager['base_url']          = current_url() .'?';
        $this->pager['total_rows']            = $total;
        $this->pager['per_page']          = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
 
        Template::set('records', $this->profile_model->limit($limit, $offset)->find_all());


		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Profile');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Profile object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Profile.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_profile())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('profile_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'profile');

				Template::set_message(lang('profile_create_success'), 'success');
				redirect(SITE_AREA .'/content/profile');
			}
			else
			{
				Template::set_message(lang('profile_create_failure') . $this->profile_model->error, 'error');
			}
		}
		Assets::add_module_js('profile', 'profile.js');

		Template::set('toolbar_title', lang('profile_create') . ' Profile');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Profile data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('profile_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/profile');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Profile.Content.Edit');

			if ($this->save_profile('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('profile_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'profile');

				Template::set_message(lang('profile_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('profile_edit_failure') . $this->profile_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Profile.Content.Delete');

			if ($this->profile_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('profile_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'profile');

				Template::set_message(lang('profile_delete_success'), 'success');

				redirect(SITE_AREA .'/content/profile');
			}
			else
			{
				Template::set_message(lang('profile_delete_failure') . $this->profile_model->error, 'error');
			}
		}
		Template::set('profile', $this->profile_model->find($id));
		Template::set('toolbar_title', lang('profile_edit') .' Profile');
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
	private function save_profile($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['org_name']        = $this->input->post('profile_org_name');
		$data['created_by']        = $this->current_user->id;

		if ($type == 'insert')
		{
			$id = $this->profile_model->insert($data);

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
			$return = $this->profile_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}