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

		$this->auth->restrict('Vendor_Profile.Content.View');
		$this->load->model('vendor_profile_model', null, true);
		$this->lang->load('vendor_profile');
		
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('vendor_profile', 'vendor_profile.js');
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
					$result = $this->vendor_profile_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('vendor_profile_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('vendor_profile_delete_failure') . $this->vendor_profile_model->error, 'error');
				}
			}
		}

        $profile_id = NULL;
        
        if (isset($this->curr_user_profile['id'])) {
            $profile_id = $this->curr_user_profile['id'];
        }

		$records = $this->vendor_profile_model->find_all($profile_id);
         $total = $this->vendor_profile_model->count_all();
 
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
 
        $this->pager['base_url']          = current_url() .'?';
        $this->pager['total_rows']            = $total;
        $this->pager['per_page']          = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
 
        Template::set('records', $this->vendor_profile_model->limit($limit, $offset)->find_all());

		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Vendor Profile');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Vendor Profile object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Vendor_Profile.Content.Create');

		if (isset($_POST['save']))
		{
            //Create profile
            $data = array();
            $data['org_name']       = $this->input->post('vendor_profile_name');
            $data['created_by']     = $this->current_user->id;

            $this->load->model('profile/profile_model');
            $this->profile_model->skip_validation(TRUE);
            $this->profile_model->insert($data);
            $this->set_profile();
            //End Create profile

            if ($insert_id = $this->save_vendor_profile())
			{
                //$this->load->model('profile/profile_model');
                //$id = $this->profile_model->insert('profile', $data);
                //Events::trigger('profile_vendor', $data);
                //End Create profile
                
				// Log the activity
				log_activity($this->current_user->id, lang('vendor_profile_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'vendor_profile');

				Template::set_message(lang('vendor_profile_create_success'), 'success');
				redirect(SITE_AREA .'/content/vendor_profile');
			}
			else
			{
				Template::set_message(lang('vendor_profile_create_failure') . $this->vendor_profile_model->error, 'error');
			}
		}
		Assets::add_module_js('vendor_profile', 'vendor_profile.js');

		Template::set('toolbar_title', lang('vendor_profile_create') . ' Vendor Profile');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Vendor Profile data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('vendor_profile_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/vendor_profile');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Vendor_Profile.Content.Edit');
            
			if ($this->save_vendor_profile('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('vendor_profile_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'vendor_profile');

				Template::set_message(lang('vendor_profile_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('vendor_profile_edit_failure') . $this->vendor_profile_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Vendor_Profile.Content.Delete');

			if ($this->vendor_profile_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('vendor_profile_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'vendor_profile');

				Template::set_message(lang('vendor_profile_delete_success'), 'success');

				redirect(SITE_AREA .'/content/vendor_profile');
			}
			else
			{
				Template::set_message(lang('vendor_profile_delete_failure') . $this->vendor_profile_model->error, 'error');
			}
		}
		Template::set('vendor_profile', $this->vendor_profile_model->find($id));
		Template::set('toolbar_title', lang('vendor_profile_edit') .' Vendor Profile');
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
	private function save_vendor_profile($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['name']        = $this->input->post('vendor_profile_name');
		$data['est_type']        = $this->input->post('vendor_profile_est_type');
		$data['est_const']        = $this->input->post('vendor_profile_est_const');
		$data['est_start_yr']        = $this->input->post('vendor_profile_est_start_yr');
        $data['profile']        = $this->input->post('vendor_profile_profile');
        $data['website']        = $this->input->post('vendor_profile_website');
		$data['created_by']        = $this->current_user->id;
        
        if (isset($this->curr_user_profile) && isset($this->curr_user_profile['id'])){
            $data['profile_id']        = $this->curr_user_profile['id'];    
        }else{
            $data['profile_id']        = NULL;    
        }	

		if ($type == 'insert')
		{
			$id = $this->vendor_profile_model->insert($data);

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
			$return = $this->vendor_profile_model->update($id, $data);
		}

		return $return;
	}

   //-------------------------------------------------------------------- 
   
    public function vendor_details(){

        $data = array();
        
        $id = $this->uri->segment(5);
        
        $this->auth->restrict('Vendor_Profile.Content.Edit');
        
        if ($id == NULL){
        	$data = '';
        }else{
            $this->load->model(array('uom/uom_model', 'vendor_address/vendor_address_model', 'vendor_contacts/vendor_contacts_model', 'factory/factory_model', 'bank_details/bank_details_model', 'product_documents/product_documents_model', 'samples/samples_model'));
            
            $records = $this->vendor_profile_model->find_all_by(array('id' => $id, 'deleted' => 0));
            $data['vendor_profile'] = $records;	
            
            $records = $this->vendor_address_model->find_all_by(array('vendor_id' => $id, 'deleted' => 0));
            $data['vendor_address'] = $records;	
            
            $records = $this->vendor_contacts_model->find_all_by(array('vendor_id' => $id, 'deleted' => 0));
            $data['vendor_contacts'] = $records;	
            
            $records = $this->factory_model->find_all_by(array('vendor_id' => $id, 'deleted' => 0));
            $data['vendor_factory'] = $records;	

            $records = $this->bank_details_model->find_all_by(array('vendor_id' => $id, 'deleted' => 0));
            $data['vendor_bank'] = $records;	
            
            $records = $this->product_documents_model->get_product_docs_def_by_vendor($id);
            $data['vendor_product_docs'] = $records;
            
            $docs = $this->product_documents_model->get_product_docs_by_vendor($id);
            $data['docs'] = $docs;
            
             
           
            
            $uoms = $this->uom_model->get_uoms();
            $data['uoms'] = $uoms;

        }
        
		Template::set('records', $data);
		Template::set('toolbar_title', 'Vendor Profile');
		Template::render();
        
     	//return $this->load->view('content/vendor_status', $data, true);       
    }
}