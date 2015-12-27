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

		$this->auth->restrict('Samples.Content.View');
		$this->load->model('samples_model', null, true);
		$this->load->model(array('uom/uom_model', 'product/product_model','customers/customers_model', 'vendor_profile/vendor_profile_model'));
		$this->lang->load('samples');
		
		Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
		Assets::add_js('jquery-ui-1.8.13.min.js');
        
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('samples', 'samples.js');
        
        $profile_id = NULL;
        
        if (isset($this->curr_user_profile['id'])) {
            $profile_id = $this->curr_user_profile['id'];
        }
        

		$uoms_select = $this->uom_model->get_uoms_select();
		Template::set('uoms_select', $uoms_select);

		$uoms = $this->uom_model->get_uoms();
		Template::set('uoms', $uoms);

		$products_select = $this->product_model->get_products_select();
		Template::set('products_select', $products_select);

		$products = $this->product_model->get_products();
		Template::set('products', $products);
       
        	$party_select = $this->customers_model->get_party_select();
		Template::set('party_select', $party_select);

		$party = $this->customers_model->get_party();
		Template::set('party', $party);
        
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
					$result = $this->samples_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('samples_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('samples_delete_failure') . $this->samples_model->error, 'error');
				}
			}
		}
        
        $profile_id = NULL;
        
        if (isset($this->curr_user_profile['id'])) {
            $profile_id = $this->curr_user_profile['id'];
        }

		$records = $this->samples_model->find_all($profile_id);
        $total = $this->samples_model->count_all();
 
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
 
        $this->pager['base_url']          = current_url() .'?';
        $this->pager['total_rows']            = $total;
        $this->pager['per_page']          = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
 
        Template::set('records', $this->samples_model->limit($limit, $offset)->find_all());  

		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Samples');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Samples object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Samples.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_samples())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('samples_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'samples');

				Template::set_message(lang('samples_create_success'), 'success');
				redirect(SITE_AREA .'/content/samples');
			}
			else
			{
				Template::set_message(lang('samples_create_failure') . $this->samples_model->error, 'error');
			}
		}
		Assets::add_module_js('samples', 'samples.js');

		Template::set('toolbar_title', lang('samples_create') . ' Samples');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Samples data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('samples_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/samples');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Samples.Content.Edit');

			if ($this->save_samples('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('samples_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'samples');

				Template::set_message(lang('samples_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('samples_edit_failure') . $this->samples_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Samples.Content.Delete');

			if ($this->samples_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('samples_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'samples');

				Template::set_message(lang('samples_delete_success'), 'success');

				redirect(SITE_AREA .'/content/samples');
			}
			else
			{
				Template::set_message(lang('samples_delete_failure') . $this->samples_model->error, 'error');
			}
		}
		Template::set('samples', $this->samples_model->find($id));
		Template::set('toolbar_title', lang('samples_edit') .' Samples');
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
	private function save_samples($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['product_id'] = $this->input->post('samples_product_id');
        $data['po_no'] = $this->input->post('samples_po_no');
        
        $party_type = NULL;
        $party_name = NULL;

        $party_val =  $this->input->post('samples_party_name');
        

        
        
        if ($party_val != NULL){
            $party_type = substr($party_val, 0, 1);
            $party_name = substr($party_val, 1);
        }
        $data['party_type'] = $this->input->post('samples_party_type');
       
        
        $data['party_type'] = $party_type;
        $data['party_name'] = $party_name;
        
        $data['trans_type'] = $this->input->post('samples_trans_type');
		$data['quantity'] = $this->input->post('samples_quantity');
		$data['uom_id'] = $this->input->post('samples_uom_id');
		$data['party_name'] = $this->input->post('samples_party_name');
        $data['courier'] = $this->input->post('samples_courier');
        $data['tracking_no'] = $this->input->post('samples_tracking_no');
        $data['comments'] = $this->input->post('samples_comments');
        $data['int_ref_num'] = $this->input->post('samples_int_ref_num');
		$data['date_received'] = $this->input->post('samples_date_received') ? $this->input->post('samples_date_received') : '0000-00-00';
        
         if (isset($this->curr_user_profile) && isset($this->curr_user_profile['id'])){
            $data['profile_id'] = $this->curr_user_profile['id'];    
        }else{
            $data['profile_id'] = NULL;    
        }	
        
		if ($type == 'insert')
		{
			$id = $this->samples_model->insert($data);

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
			$return = $this->samples_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}