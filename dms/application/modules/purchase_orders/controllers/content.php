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

		$this->auth->restrict('Purchase_Orders.Content.View');
		$this->load->model('purchase_orders_model', null, true);
        $this->load->model(array('uom/uom_model', 'customers/customers_model', 'product/product_model'));
		$this->lang->load('purchase_orders');
		
		Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
		Assets::add_js('jquery-ui-1.8.13.min.js');
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('purchase_orders', 'purchase_orders.js');
        
		$uoms_select = $this->uom_model->get_uoms_select();
		Template::set('uoms_select', $uoms_select);

		$uoms = $this->uom_model->get_uoms();
		Template::set('uoms', $uoms);        
        
		$customers_select = $this->customers_model->get_customers_select();
		Template::set('customers_select', $customers_select);

		$customers = $this->customers_model->get_customers();
		Template::set('customers', $customers);        
        
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
					$result = $this->purchase_orders_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('purchase_orders_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('purchase_orders_delete_failure') . $this->purchase_orders_model->error, 'error');
				}
			}
		}

		$records = $this->purchase_orders_model->find_all();
        $total = $this->purchase_orders_model->count_all();
        
        //pagination
        $this->load->library('pagination');
        $offset = $this->input->get('per_page');
        
        $limit = '10';
        
        $this->pager['base_url'] = current_url() .'?';
        $this->pager['total_rows'] = $total;
        $this->pager['per_page'] = $limit;
        $this->pager['page_query_string'] = TRUE;
        
        $this->pagination->initialize($this->pager);
        
        Template::set('records', $this->purchase_orders_model->limit($limit, $offset)->find_all());

		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Purchase Orders');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Purchase Orders object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Purchase_Orders.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_purchase_orders())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('purchase_orders_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'purchase_orders');

				Template::set_message(lang('purchase_orders_create_success'), 'success');
				redirect(SITE_AREA .'/content/purchase_orders');
			}
			else
			{
				Template::set_message(lang('purchase_orders_create_failure') . $this->purchase_orders_model->error, 'error');
			}
		}
		Assets::add_module_js('purchase_orders', 'purchase_orders.js');

		Template::set('toolbar_title', lang('purchase_orders_create') . ' Purchase Orders');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Purchase Orders data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('purchase_orders_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/purchase_orders');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Purchase_Orders.Content.Edit');

			if ($this->save_purchase_orders('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('purchase_orders_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'purchase_orders');

				Template::set_message(lang('purchase_orders_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('purchase_orders_edit_failure') . $this->purchase_orders_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Purchase_Orders.Content.Delete');

			if ($this->purchase_orders_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('purchase_orders_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'purchase_orders');

				Template::set_message(lang('purchase_orders_delete_success'), 'success');

				redirect(SITE_AREA .'/content/purchase_orders');
			}
			else
			{
				Template::set_message(lang('purchase_orders_delete_failure') . $this->purchase_orders_model->error, 'error');
			}
		}
		Template::set('purchase_orders', $this->purchase_orders_model->find($id));
		Template::set('toolbar_title', lang('purchase_orders_edit') .' Purchase Orders');
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
	private function save_purchase_orders($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['po_no']        = $this->input->post('purchase_orders_po_no');
		$data['po_dt']        = $this->input->post('purchase_orders_po_dt') ? $this->input->post('purchase_orders_po_dt') : '0000-00-00';
		$data['product_id']        = $this->input->post('purchase_orders_product_id');
		$data['qty']        = $this->input->post('purchase_orders_qty');
		$data['uom_id']        = $this->input->post('purchase_orders_uom_id');
		$data['rate']        = $this->input->post('purchase_orders_rate');
		$data['packing_mode']        = $this->input->post('purchase_orders_packing_mode');
		$data['no_of_units']        = $this->input->post('purchase_orders_no_of_units');
		$data['created_by']        = $this->current_user->id;
		$data['customer_id']        = $this->input->post('purchase_orders_customer_id');
		$data['status_id']        = $this->input->post('purchase_orders_status_id');
		$data['comments']        = $this->input->post('purchase_orders_comments');

		if ($type == 'insert')
		{
			$id = $this->purchase_orders_model->insert($data);

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
			$return = $this->purchase_orders_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------

    public function po_details(){

        $data = array();
        
        $id = $this->uri->segment(5);
        
        $this->auth->restrict('Purchase_Orders.Content.View');
        
        if ($id == NULL){
        	$data = '';
        }else{
            
            $records = $this->purchase_orders_model->get_po_tracker($id);
            $data['po_details'] = $records;	
            
            $records = $this->purchase_orders_model->get_po_doc($id);
            $data['po_docs'] = $records;
        }
        
		Template::set('records', $data);
		Template::set('toolbar_title', 'PO Details');
		Template::render();
        
     	//return $this->load->view('content/vendor_status', $data, true);       
    }
    //--------------------------------------------------------------------
        

}