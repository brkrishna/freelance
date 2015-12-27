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

		$this->auth->restrict('Vendor_Contacts.Content.View');
		$this->load->model('vendor_contacts_model', null, true);
        $this->load->model(array('vendor_profile/vendor_profile_model'));
		$this->lang->load('vendor_contacts');
		
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('vendor_contacts', 'vendor_contacts.js');
        
        $profile_id = NULL;
        
        if (isset($this->curr_user_profile['id'])) {
            $profile_id = $this->curr_user_profile['id'];
        }

		$vendors_select = $this->vendor_profile_model->get_vendors_select($profile_id);
		Template::set('vendors_select', $vendors_select);

		$vendors = $this->vendor_profile_model->get_vendors($profile_id);
		Template::set('vendors', $vendors);
        
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
					$result = $this->vendor_contacts_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('vendor_contacts_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('vendor_contacts_delete_failure') . $this->vendor_contacts_model->error, 'error');
				}
			}
		}

        $profile_id = NULL;
        
        if (isset($this->curr_user_profile['id'])) {
            $profile_id = $this->curr_user_profile['id'];
        }
        
		$records = $this->vendor_contacts_model->find_all($profile_id);
         $total = $this->vendor_contacts_model->count_all();
 
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
 
        $this->pager['base_url']          = current_url() .'?';
        $this->pager['total_rows']            = $total;
        $this->pager['per_page']          = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
 
        Template::set('records', $this->vendor_contacts_model->limit($limit, $offset)->find_all());

		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Vendor Contacts');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Vendor Contacts object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Vendor_Contacts.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_vendor_contacts())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('vendor_contacts_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'vendor_contacts');

				Template::set_message(lang('vendor_contacts_create_success'), 'success');
				redirect(SITE_AREA .'/content/vendor_contacts');
			}
			else
			{
				Template::set_message(lang('vendor_contacts_create_failure') . $this->vendor_contacts_model->error, 'error');
			}
		}
		Assets::add_module_js('vendor_contacts', 'vendor_contacts.js');

		Template::set('toolbar_title', lang('vendor_contacts_create') . ' Vendor Contacts');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Vendor Contacts data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('vendor_contacts_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/vendor_contacts');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Vendor_Contacts.Content.Edit');

			if ($this->save_vendor_contacts('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('vendor_contacts_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'vendor_contacts');

				Template::set_message(lang('vendor_contacts_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('vendor_contacts_edit_failure') . $this->vendor_contacts_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Vendor_Contacts.Content.Delete');

			if ($this->vendor_contacts_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('vendor_contacts_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'vendor_contacts');

				Template::set_message(lang('vendor_contacts_delete_success'), 'success');

				redirect(SITE_AREA .'/content/vendor_contacts');
			}
			else
			{
				Template::set_message(lang('vendor_contacts_delete_failure') . $this->vendor_contacts_model->error, 'error');
			}
		}
		Template::set('vendor_contacts', $this->vendor_contacts_model->find($id));
		Template::set('toolbar_title', lang('vendor_contacts_edit') .' Vendor Contacts');
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
	private function save_vendor_contacts($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['vendor_id']        = $this->input->post('vendor_contacts_vendor_id');
		$data['name']        = $this->input->post('vendor_contacts_name');
		$data['dsgn']        = $this->input->post('vendor_contacts_dsgn');
		$data['work_phone']        = $this->input->post('vendor_contacts_work_phone');
		$data['cell_phone']        = $this->input->post('vendor_contacts_cell_phone');
		$data['email_id']        = $this->input->post('vendor_contacts_email_id');
		$data['created_by']        = $this->current_user->id;
        
        if (isset($this->curr_user_profile) && isset($this->curr_user_profile['id'])){
            $data['profile_id']        = $this->curr_user_profile['id'];    
        }else{
            $data['profile_id']        = NULL;    
        }	

		if ($type == 'insert')
		{
			$id = $this->vendor_contacts_model->insert($data);

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
			$return = $this->vendor_contacts_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}