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

		$this->auth->restrict('Vendor_Address.Content.View');
		$this->load->model('vendor_address_model', null, true);
        $this->load->model(array('countries_model', 'vendor_profile/vendor_profile_model'));
		$this->lang->load('vendor_address');
		
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('vendor_address', 'vendor_address.js');
                           
        $profile_id = NULL;
        
        if (isset($this->curr_user_profile['id'])) {
            $profile_id = $this->curr_user_profile['id'];
        }
        
		$countries_select = $this->countries_model->get_countries_select();
		Template::set('countries_select', $countries_select);

		$countries = $this->countries_model->get_countries();
		Template::set('countries', $countries);
                           
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
					$result = $this->vendor_address_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('vendor_address_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('vendor_address_delete_failure') . $this->vendor_address_model->error, 'error');
				}
			}
		}

        $profile_id = NULL;
        
        if (isset($this->curr_user_profile['id'])) {
            $profile_id = $this->curr_user_profile['id'];
        }

		$records = $this->vendor_address_model->find_all($profile_id);
         $total = $this->vendor_address_model->count_all();
 
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
 
        $this->pager['base_url']          = current_url() .'?';
        $this->pager['total_rows']            = $total;
        $this->pager['per_page']          = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
 
        Template::set('records', $this->vendor_address_model->limit($limit, $offset)->find_all());

		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Vendor Address');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Vendor Address object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Vendor_Address.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_vendor_address())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('vendor_address_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'vendor_address');

				Template::set_message(lang('vendor_address_create_success'), 'success');
				redirect(SITE_AREA .'/content/vendor_address');
			}
			else
			{
				Template::set_message(lang('vendor_address_create_failure') . $this->vendor_address_model->error, 'error');
			}
		}
		Assets::add_module_js('vendor_address', 'vendor_address.js');

		Template::set('toolbar_title', lang('vendor_address_create') . ' Vendor Address');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Vendor Address data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('vendor_address_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/vendor_address');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Vendor_Address.Content.Edit');

			if ($this->save_vendor_address('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('vendor_address_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'vendor_address');

				Template::set_message(lang('vendor_address_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('vendor_address_edit_failure') . $this->vendor_address_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Vendor_Address.Content.Delete');

			if ($this->vendor_address_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('vendor_address_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'vendor_address');

				Template::set_message(lang('vendor_address_delete_success'), 'success');

				redirect(SITE_AREA .'/content/vendor_address');
			}
			else
			{
				Template::set_message(lang('vendor_address_delete_failure') . $this->vendor_address_model->error, 'error');
			}
		}
		Template::set('vendor_address', $this->vendor_address_model->find($id));
		Template::set('toolbar_title', lang('vendor_address_edit') .' Vendor Address');
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
	private function save_vendor_address($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['vendor_id']        = $this->input->post('vendor_address_vendor_id');
		$data['loc_type']        = $this->input->post('vendor_address_loc_type');
		$data['address1']        = $this->input->post('vendor_address_address1');
		$data['address2']        = $this->input->post('vendor_address_address2');
		$data['city']        = $this->input->post('vendor_address_city');
		$data['country_id']        = $this->input->post('vendor_address_country_id');
		$data['office_phones']        = $this->input->post('vendor_address_office_phones');
		$data['office_fax']        = $this->input->post('vendor_address_office_fax');
        
		$data['created_by']        = $this->current_user->id;
        
        if (isset($this->curr_user_profile) && isset($this->curr_user_profile['id'])){
            $data['profile_id']        = $this->curr_user_profile['id'];    
        }else{
            $data['profile_id']        = NULL;    
        }	
        
		if ($type == 'insert')
		{
			$id = $this->vendor_address_model->insert($data);

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
			$return = $this->vendor_address_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}