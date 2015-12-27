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

		$this->auth->restrict('Product.Content.View');
		$this->load->model('product_model', null, true);
		$this->lang->load('product');
		
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('product', 'product.js');
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
					$result = $this->product_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('product_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('product_delete_failure') . $this->product_model->error, 'error');
				}
			}
		}

		$records = $this->product_model->find_all();
        
        $total = $this->product_model->count_all();
 
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
 
        $this->pager['base_url']          = current_url() .'?';
        $this->pager['total_rows']            = $total;
        $this->pager['per_page']          = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
 
        Template::set('records', $this->product_model->limit($limit, $offset)->find_all_by('deleted', '0'));

        
		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Product');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Product object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Product.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_product())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('product_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'product');

				Template::set_message(lang('product_create_success'), 'success');
				redirect(SITE_AREA .'/content/product');
			}
			else
			{
				Template::set_message(lang('product_create_failure') . $this->product_model->error, 'error');
			}
		}
		Assets::add_module_js('product', 'product.js');

		Template::set('toolbar_title', lang('product_create') . ' Product');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Product data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('product_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/product');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Product.Content.Edit');

			if ($this->save_product('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('product_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'product');

				Template::set_message(lang('product_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('product_edit_failure') . $this->product_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Product.Content.Delete');

			if ($this->product_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('product_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'product');

				Template::set_message(lang('product_delete_success'), 'success');

				redirect(SITE_AREA .'/content/product');
			}
			else
			{
				Template::set_message(lang('product_delete_failure') . $this->product_model->error, 'error');
			}
		}
		Template::set('product', $this->product_model->find($id));
		Template::set('toolbar_title', lang('product_edit') .' Product');
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
	private function save_product($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['name']        = $this->input->post('product_name');
		$data['desc']        = $this->input->post('product_desc');

		if ($type == 'insert')
		{
			$id = $this->product_model->insert($data);

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
			$return = $this->product_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}