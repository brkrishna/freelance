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

		$this->auth->restrict('PO_Containers.Content.View');
		$this->load->model('po_containers_model', null, true);
        $this->load->model(array('purchase_orders/purchase_orders_model'));
		$this->lang->load('po_containers');
		
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('po_containers', 'po_containers.js');
        
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
					$result = $this->po_containers_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('po_containers_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('po_containers_delete_failure') . $this->po_containers_model->error, 'error');
				}
			}
		}

		$records = $this->po_containers_model->find_all();

		Template::set('records', $records);
		Template::set('toolbar_title', 'Manage PO Containers');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a PO Containers object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('PO_Containers.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_po_containers())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('po_containers_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'po_containers');

				Template::set_message(lang('po_containers_create_success'), 'success');
				redirect(SITE_AREA .'/content/po_containers');
			}
			else
			{
				Template::set_message(lang('po_containers_create_failure') . $this->po_containers_model->error, 'error');
			}
		}
		Assets::add_module_js('po_containers', 'po_containers.js');
        
        $id = $this->uri->segment(5);
        if (!empty($id)){
            $po_data = $this->purchase_orders_model->find_by('id', $id);
            Template::set('po_data', $po_data);
        }
        
		Template::set('toolbar_title', lang('po_containers_create') . ' PO Containers');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of PO Containers data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('po_containers_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/po_containers');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('PO_Containers.Content.Edit');

			if ($this->save_po_containers('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('po_containers_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'po_containers');

				Template::set_message(lang('po_containers_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('po_containers_edit_failure') . $this->po_containers_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('PO_Containers.Content.Delete');

			if ($this->po_containers_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('po_containers_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'po_containers');

				Template::set_message(lang('po_containers_delete_success'), 'success');

				redirect(SITE_AREA .'/content/po_containers');
			}
			else
			{
				Template::set_message(lang('po_containers_delete_failure') . $this->po_containers_model->error, 'error');
			}
		}
		Template::set('po_containers', $this->po_containers_model->find($id));
		Template::set('toolbar_title', lang('po_containers_edit') .' PO Containers');
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
	private function save_po_containers($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['po_no']        = $this->input->post('po_containers_po_no');
		$data['batch_no']        = $this->input->post('po_containers_batch_no');
		$data['vessel']        = $this->input->post('po_containers_vessel');
		$data['container']        = $this->input->post('po_containers_container');
		$data['seal']        = $this->input->post('po_containers_seal');
		$data['created_by']        = $this->current_user->id;

		if ($type == 'insert')
		{
			$id = $this->po_containers_model->insert($data);

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
			$return = $this->po_containers_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}