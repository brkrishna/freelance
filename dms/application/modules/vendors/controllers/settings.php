<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * settings controller
 */
class settings extends Admin_Controller
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

		$this->auth->restrict('Vendors.Settings.View');
		$this->load->model('vendors_model', null, true);
		$this->lang->load('vendors');
		
		Template::set_block('sub_nav', 'settings/_sub_nav');

		Assets::add_module_js('vendors', 'vendors.js');
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
					$result = $this->vendors_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('vendors_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('vendors_delete_failure') . $this->vendors_model->error, 'error');
				}
			}
		}

		$records = $this->vendors_model->find_all();

		Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Vendors');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Vendors object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Vendors.Settings.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_vendors())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('vendors_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'vendors');

				Template::set_message(lang('vendors_create_success'), 'success');
				redirect(SITE_AREA .'/settings/vendors');
			}
			else
			{
				Template::set_message(lang('vendors_create_failure') . $this->vendors_model->error, 'error');
			}
		}
		Assets::add_module_js('vendors', 'vendors.js');

		Template::set('toolbar_title', lang('vendors_create') . ' Vendors');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Vendors data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('vendors_invalid_id'), 'error');
			redirect(SITE_AREA .'/settings/vendors');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Vendors.Settings.Edit');

			if ($this->save_vendors('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('vendors_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'vendors');

				Template::set_message(lang('vendors_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('vendors_edit_failure') . $this->vendors_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Vendors.Settings.Delete');

			if ($this->vendors_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('vendors_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'vendors');

				Template::set_message(lang('vendors_delete_success'), 'success');

				redirect(SITE_AREA .'/settings/vendors');
			}
			else
			{
				Template::set_message(lang('vendors_delete_failure') . $this->vendors_model->error, 'error');
			}
		}
		Template::set('vendors', $this->vendors_model->find($id));
		Template::set('toolbar_title', lang('vendors_edit') .' Vendors');
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
	private function save_vendors($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['name']        = $this->input->post('vendors_name');
		$data['contact_name']        = $this->input->post('vendors_contact_name');
		$data['contact_phone']        = $this->input->post('vendors_contact_phone');
		$data['address1']        = $this->input->post('vendors_address1');
		$data['address2']        = $this->input->post('vendors_address2');
		$data['city']        = $this->input->post('vendors_city');
		$data['country']        = $this->input->post('vendors_country');
		$data['work_phones']        = $this->input->post('vendors_work_phones');
		$data['contact_email']        = $this->input->post('vendors_contact_email');
		$data['website_url']        = $this->input->post('vendors_website_url');

		if ($type == 'insert')
		{
			$id = $this->vendors_model->insert($data);

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
			$return = $this->vendors_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}