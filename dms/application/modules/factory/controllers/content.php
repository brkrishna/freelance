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

		$this->auth->restrict('Factory.Content.View');
		$this->load->model('factory_model', null, true);
        $this->load->model(array('uom/uom_model', 'vendor_profile/vendor_profile_model'));
		$this->lang->load('factory');
		
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('factory', 'factory.js');
        
		$uoms_select = $this->uom_model->get_uoms_select();
		Template::set('uoms_select', $uoms_select);

		$uoms = $this->uom_model->get_uoms();
		Template::set('uoms', $uoms);
        
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
					$result = $this->factory_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('factory_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('factory_delete_failure') . $this->factory_model->error, 'error');
				}
			}
		}

        $profile_id = NULL;
        
        if (isset($this->curr_user_profile['id'])) {
            $profile_id = $this->curr_user_profile['id'];
        }
        
		$records = $this->factory_model->find_all($profile_id);
         $total = $this->factory_model->count_all();
        
        //pagination
        $this->load->library('pagination');
        
        $offset = $this->input->get('per_page');
        
        $limit = '10';
        
        $this->pager['base_url'] = current_url() .'?';
        $this->pager['total_rows'] = $total;
        $this->pager['per_page'] = $limit;
        $this->pager['page_query_string'] = TRUE;
        
        $this->pagination->initialize($this->pager);
        
        Template::set('records', $this->factory_model->limit($limit, $offset)->find_all());


		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Factory');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Factory object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Factory.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_factory())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('factory_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'factory');

				Template::set_message(lang('factory_create_success'), 'success');
				redirect(SITE_AREA .'/content/factory');
			}
			else
			{
				Template::set_message(lang('factory_create_failure') . $this->factory_model->error, 'error');
			}
		}
		Assets::add_module_js('factory', 'factory.js');

		Template::set('toolbar_title', lang('factory_create') . ' Factory');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Factory data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('factory_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/factory');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Factory.Content.Edit');

			if ($this->save_factory('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('factory_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'factory');

				Template::set_message(lang('factory_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('factory_edit_failure') . $this->factory_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Factory.Content.Delete');

			if ($this->factory_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('factory_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'factory');

				Template::set_message(lang('factory_delete_success'), 'success');

				redirect(SITE_AREA .'/content/factory');
			}
			else
			{
				Template::set_message(lang('factory_delete_failure') . $this->factory_model->error, 'error');
			}
		}
		Template::set('factory', $this->factory_model->find($id));
		Template::set('toolbar_title', lang('factory_edit') .' Factory');
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
	private function save_factory($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['no_of_emps']        = $this->input->post('factory_no_of_emps');
        $data['name']        = $this->input->post('factory_name');
        $data['address']        = $this->input->post('factory_address');
		$data['m_cpcty']        = $this->input->post('factory_m_cpcty');
		$data['m_cpcty_uom']        = $this->input->post('factory_m_cpcty_uom');
		$data['d_cpcty']        = $this->input->post('factory_d_cpcty');
		$data['d_cpcty_uom']        = $this->input->post('factory_d_cpcty_uom');
		$data['cpcty_raw_mtrl']        = $this->input->post('factory_cpcty_raw_mtrl');
		$data['cpcty_storage']        = $this->input->post('factory_cpcty_storage');
		$data['near_port']        = $this->input->post('factory_near_port');
		$data['near_airport']        = $this->input->post('factory_near_airport');
		$data['near_city']        = $this->input->post('factory_near_city');
		$data['transport_opt']        = $this->input->post('factory_transport_opt');
		$data['courier_comp']        = $this->input->post('factory_courier_comp');
		$data['created_by']        = $this->current_user->id;
        
        if (isset($this->curr_user_profile) && isset($this->curr_user_profile['id'])){
            $data['profile_id']        = $this->curr_user_profile['id'];    
            $vendor = $this->vendor_profile_model->find_by('profile_id', $this->curr_user_profile['id']);
            if ($vendor != NULL){
                $data['vendor_id']         = $vendor->id;
            }
        }else{
            $data['profile_id']        = NULL;    
        }	

		if ($type == 'insert')
		{
			$id = $this->factory_model->insert($data);

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
			$return = $this->factory_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}