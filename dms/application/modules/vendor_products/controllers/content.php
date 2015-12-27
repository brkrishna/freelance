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

		$this->auth->restrict('Vendor_Products.Content.View');
		$this->load->model('vendor_products_model', null, true);
        $this->load->model(array('vendor_profile/vendor_profile_model', 'product/product_model'));
		$this->lang->load('vendor_products');
		
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('vendor_products', 'vendor_products.js');
        
        $profile_id = NULL;
        
        if (isset($this->curr_user_profile['id'])) {
            $profile_id = $this->curr_user_profile['id'];
        }
        
		$vendors_select = $this->vendor_profile_model->get_vendors_select($profile_id);
		Template::set('vendors_select', $vendors_select);

		$vendors = $this->vendor_profile_model->get_vendors($profile_id);
		Template::set('vendors', $vendors);

		$products_select = $this->product_model->get_products_select();
		Template::set('products_select', $products_select);

		$products = $this->product_model->get_products();
		Template::set('products', $products);
        
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
					$result = $this->vendor_products_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('vendor_products_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('vendor_products_delete_failure') . $this->vendor_products_model->error, 'error');
				}
			}
		}

        $profile_id = NULL;
        
        if (isset($this->curr_user_profile['id'])) {
            $profile_id = $this->curr_user_profile['id'];
        }
        
		$records = $this->vendor_products_model->find_all($profile_id);
         $total = $this->vendor_products_model->count_all();
 
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
 
        $this->pager['base_url']          = current_url() .'?';
        $this->pager['total_rows']            = $total;
        $this->pager['per_page']          = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
 
        Template::set('records', $this->vendor_products_model->limit($limit, $offset)->find_all());

		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Vendor Products');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Vendor Products object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Vendor_Products.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_vendor_products())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('vendor_products_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'vendor_products');

				Template::set_message(lang('vendor_products_create_success'), 'success');
				redirect(SITE_AREA .'/content/vendor_products');
			}
			else
			{
				Template::set_message(lang('vendor_products_create_failure') . $this->vendor_products_model->error, 'error');
			}
		}
		Assets::add_module_js('vendor_products', 'vendor_products.js');

		Template::set('toolbar_title', lang('vendor_products_create') . ' Vendor Products');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Vendor Products data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('vendor_products_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/vendor_products');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Vendor_Products.Content.Edit');

			if ($this->save_vendor_products('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('vendor_products_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'vendor_products');

				Template::set_message(lang('vendor_products_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('vendor_products_edit_failure') . $this->vendor_products_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Vendor_Products.Content.Delete');

			if ($this->vendor_products_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('vendor_products_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'vendor_products');

				Template::set_message(lang('vendor_products_delete_success'), 'success');

				redirect(SITE_AREA .'/content/vendor_products');
			}
			else
			{
				Template::set_message(lang('vendor_products_delete_failure') . $this->vendor_products_model->error, 'error');
			}
		}
		Template::set('vendor_products', $this->vendor_products_model->find($id));
		Template::set('toolbar_title', lang('vendor_products_edit') .' Vendor Products');
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
	private function save_vendor_products($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['vendor_id']        = $this->input->post('vendor_products_vendor_id');
		$data['product_id']        = $this->input->post('vendor_products_product_id');
		$data['comments']        = $this->input->post('vendor_products_comments');
		$data['created_by']        = $this->current_user->id;
        
        if (isset($this->curr_user_profile) && isset($this->curr_user_profile['id'])){
            $data['profile_id']        = $this->curr_user_profile['id'];    
        }else{
            $data['profile_id']        = NULL;    
        }	

		if ($type == 'insert')
		{
			$id = $this->vendor_products_model->insert($data);

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
			$return = $this->vendor_products_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}