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

		$this->auth->restrict('Bank_Details.Content.View');
		$this->load->model('bank_details_model', null, true);
        $this->load->model('vendor_profile/vendor_profile_model');
		$this->lang->load('bank_details');
		
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('bank_details', 'bank_details.js');
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
					$result = $this->bank_details_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('bank_details_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('bank_details_delete_failure') . $this->bank_details_model->error, 'error');
				}
			}
		}

        $profile_id = NULL;
        
        if (isset($this->curr_user_profile['id'])) {
            $profile_id = $this->curr_user_profile['id'];
        }
        
		$records = $this->bank_details_model->find_all($profile_id);
        $total = $this->bank_details_model->count_all();
 
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
 
        $this->pager['base_url']          = current_url() .'?';
        $this->pager['total_rows']            = $total;
        $this->pager['per_page']          = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
 
        Template::set('records', $this->bank_details_model->limit($limit, $offset)->find_all());



		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Bank Details');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Bank Details object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Bank_Details.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_bank_details())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('bank_details_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'bank_details');

				Template::set_message(lang('bank_details_create_success'), 'success');
				redirect(SITE_AREA .'/content/bank_details');
			}
			else
			{
				Template::set_message(lang('bank_details_create_failure') . $this->bank_details_model->error, 'error');
			}
		}
		Assets::add_module_js('bank_details', 'bank_details.js');

		Template::set('toolbar_title', lang('bank_details_create') . ' Bank Details');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Bank Details data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('bank_details_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/bank_details');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Bank_Details.Content.Edit');

			if ($this->save_bank_details('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('bank_details_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'bank_details');

				Template::set_message(lang('bank_details_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('bank_details_edit_failure') . $this->bank_details_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Bank_Details.Content.Delete');

			if ($this->bank_details_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('bank_details_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'bank_details');

				Template::set_message(lang('bank_details_delete_success'), 'success');

				redirect(SITE_AREA .'/content/bank_details');
			}
			else
			{
				Template::set_message(lang('bank_details_delete_failure') . $this->bank_details_model->error, 'error');
			}
		}
		Template::set('bank_details', $this->bank_details_model->find($id));
		Template::set('toolbar_title', lang('bank_details_edit') .' Bank Details');
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
	private function save_bank_details($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['bank_name']        = $this->input->post('bank_details_bank_name');
        $data['branch']        = $this->input->post('bank_details_branch');
		$data['address']        = $this->input->post('bank_details_address');
		$data['account_type']        = $this->input->post('bank_details_account_type');
		$data['oper_curr']        = $this->input->post('bank_details_oper_curr');
		$data['accept_curr']        = $this->input->post('bank_details_accept_curr');
		$data['swift_code']        = $this->input->post('bank_details_swift_code');
		$data['micr']        = $this->input->post('bank_details_micr');
		$data['ifsc']        = $this->input->post('bank_details_ifsc');
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
			$id = $this->bank_details_model->insert($data);

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
			$return = $this->bank_details_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}