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

		$this->auth->restrict('PO_Fulfillment.Content.View');
		$this->load->model('po_fulfillment_model', null, true);
        $this->load->model(array('uom/uom_model', 'vendor_profile/vendor_profile_model', 'product/product_model', 'purchase_orders/purchase_orders_model'));
		$this->lang->load('po_fulfillment');
		
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('po_fulfillment', 'po_fulfillment.js');
        
		$uoms_select = $this->uom_model->get_uoms_select();
		Template::set('uoms_select', $uoms_select);

		$uoms = $this->uom_model->get_uoms();
		Template::set('uoms', $uoms);        
        
		$vendors_select = $this->vendor_profile_model->get_vendors_select();
		Template::set('vendors_select', $vendors_select);

		$vendors = $this->vendor_profile_model->get_vendors();
		Template::set('vendors', $vendors);        
        
		$products_select = $this->product_model->get_products_select();
		Template::set('products_select', $products_select);

		$products = $this->product_model->get_products();
		Template::set('products', $products);
        
		$pos_select = $this->purchase_orders_model->get_pos_select();
		Template::set('pos_select', $pos_select);

		$pos = $this->purchase_orders_model->get_pos();
		Template::set('pos', $pos);        
        
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
					$result = $this->po_fulfillment_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('po_fulfillment_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('po_fulfillment_delete_failure') . $this->po_fulfillment_model->error, 'error');
				}
			}
		}

		$records = $this->po_fulfillment_model->find_all();

		Template::set('records', $records);
		Template::set('toolbar_title', 'Manage PO Fulfillment');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a PO Fulfillment object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('PO_Fulfillment.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_po_fulfillment())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('po_fulfillment_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'po_fulfillment');

				Template::set_message(lang('po_fulfillment_create_success'), 'success');
				redirect(SITE_AREA .'/content/po_fulfillment');
			}
			else
			{
				Template::set_message(lang('po_fulfillment_create_failure') . $this->po_fulfillment_model->error, 'error');
			}
		}
		Assets::add_module_js('po_fulfillment', 'po_fulfillment.js');

        $id = $this->uri->segment(5);
        if (!empty($id)){
            $po_data = $this->purchase_orders_model->find_by('id', $id);
            Template::set('po_data', $po_data);
        }

		Template::set('toolbar_title', lang('po_fulfillment_create') . ' PO Fulfillment');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of PO Fulfillment data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('po_fulfillment_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/po_fulfillment');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('PO_Fulfillment.Content.Edit');

			if ($this->save_po_fulfillment('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('po_fulfillment_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'po_fulfillment');

				Template::set_message(lang('po_fulfillment_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('po_fulfillment_edit_failure') . $this->po_fulfillment_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('PO_Fulfillment.Content.Delete');

			if ($this->po_fulfillment_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('po_fulfillment_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'po_fulfillment');

				Template::set_message(lang('po_fulfillment_delete_success'), 'success');

				redirect(SITE_AREA .'/content/po_fulfillment');
			}
			else
			{
				Template::set_message(lang('po_fulfillment_delete_failure') . $this->po_fulfillment_model->error, 'error');
			}
		}
		Template::set('po_fulfillment', $this->po_fulfillment_model->find($id));
		Template::set('toolbar_title', lang('po_fulfillment_edit') .' PO Fulfillment');
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
	private function save_po_fulfillment($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['po_no']        = $this->input->post('po_fulfillment_po_no');
		$data['vendor_id']        = $this->input->post('po_fulfillment_vendor_id');
		$data['product_id']        = $this->input->post('po_fulfillment_product_id');
		$data['qty']        = $this->input->post('po_fulfillment_qty');
		$data['uom_id']        = $this->input->post('po_fulfillment_uom_id');
		$data['rate']        = $this->input->post('po_fulfillment_rate');
		$data['supply_from']        = $this->input->post('po_fulfillment_supply_from');
		$data['dest_port']        = $this->input->post('po_fulfillment_dest_port');
		$data['packing_mode']        = $this->input->post('po_fulfillment_packing_mode');
		$data['no_of_units']        = $this->input->post('po_fulfillment_no_of_units');
		$data['created_by']        = $this->current_user->id;

		if ($type == 'insert')
		{
			$id = $this->po_fulfillment_model->insert($data);

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
			$return = $this->po_fulfillment_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}