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

		$this->auth->restrict('Containers.Content.View');
		$this->load->model('containers_model', null, true);
		$this->load->model(array('purchase_orders/purchase_orders_model', 'countries_model', 'product/product_model', 'uom/uom_model',));
		$this->lang->load('containers');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('containers', 'containers.js');

		$po_refs_select = $this->purchase_orders_model->get_po_ref_select();
		Template::set('po_refs_select', $po_refs_select);

		$po_refs = $this->purchase_orders_model->get_po_refs();
		Template::set('po_refs', $po_refs);

		$countries_select = $this->countries_model->get_countries_select();
		Template::set('countries_select', $countries_select);

		$countries = $this->countries_model->get_countries();
		Template::set('countries', $countries);

		$uoms_select = $this->uom_model->get_uoms_select();
		Template::set('uoms_select', $uoms_select);

		$uoms = $this->uom_model->get_uoms();
		Template::set('uoms', $uoms);

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
					$result = $this->containers_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('containers_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('containers_delete_failure') . $this->containers_model->error, 'error');
				}
			}
		}

		$records = $this->containers_model->find_all();
        $total = $this->containers_model->count_all();
 
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
 
        $this->pager['base_url']          = current_url() .'?';
        $this->pager['total_rows']            = $total;
        $this->pager['per_page']          = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
 
        Template::set('records', $this->containers_model->limit($limit, $offset)->find_all());



		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Containers');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Containers object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Containers.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_containers())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('containers_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'containers');

				Template::set_message(lang('containers_create_success'), 'success');
				redirect(SITE_AREA .'/content/containers');
			}
			else
			{
				Template::set_message(lang('containers_create_failure') . $this->containers_model->error, 'error');
			}
		}
		Assets::add_module_js('containers', 'containers.js');

		Template::set('toolbar_title', lang('containers_create') . ' Containers');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Containers data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('containers_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/containers');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Containers.Content.Edit');

			if ($this->save_containers('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('containers_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'containers');

				Template::set_message(lang('containers_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('containers_edit_failure') . $this->containers_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Containers.Content.Delete');

			if ($this->containers_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('containers_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'containers');

				Template::set_message(lang('containers_delete_success'), 'success');

				redirect(SITE_AREA .'/content/containers');
			}
			else
			{
				Template::set_message(lang('containers_delete_failure') . $this->containers_model->error, 'error');
			}
		}
		Template::set('containers', $this->containers_model->find($id));
		Template::set('toolbar_title', lang('containers_edit') .' Containers');
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
	private function save_containers($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['po_ref']        = $this->input->post('containers_po_ref');
		$data['container_no']        = $this->input->post('containers_container_no');
		$data['seal']        = $this->input->post('containers_seal');
		$data['origin']        = $this->input->post('containers_origin');
		$data['batch_nos']        = $this->input->post('containers_batch_nos');
		$data['product_id']        = $this->input->post('containers_product_id');
		$data['quantity']        = $this->input->post('containers_quantity');
		$data['uom_id']        = $this->input->post('containers_uom_id');
		$data['status']        = $this->input->post('containers_status');
		$data['started_on']        = $this->input->post('containers_started_on') ? $this->input->post('containers_started_on') : '0000-00-00';
		$data['arrived_on']        = $this->input->post('containers_arrived_on') ? $this->input->post('containers_arrived_on') : '0000-00-00';

		if ($type == 'insert')
		{
			$id = $this->containers_model->insert($data);

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
			$return = $this->containers_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}