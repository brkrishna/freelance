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

		$this->auth->restrict('Botanicules.Content.View');
		$this->load->model('botanicules_model', null, true);
		$this->lang->load('botanicules');
		
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('botanicules', 'botanicules.js');
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
					$result = $this->botanicules_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('botanicules_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('botanicules_delete_failure') . $this->botanicules_model->error, 'error');
				}
			}
		}

		$records = $this->botanicules_model->find_all();

		Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Botanicules');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Botanicules object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Botanicules.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_botanicules())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('botanicules_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'botanicules');

				Template::set_message(lang('botanicules_create_success'), 'success');
				redirect(SITE_AREA .'/content/botanicules');
			}
			else
			{
				Template::set_message(lang('botanicules_create_failure') . $this->botanicules_model->error, 'error');
			}
		}
		Assets::add_module_js('botanicules', 'botanicules.js');

		Template::set('toolbar_title', lang('botanicules_create') . ' Botanicules');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Botanicules data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('botanicules_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/botanicules');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Botanicules.Content.Edit');

			if ($this->save_botanicules('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('botanicules_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'botanicules');

				Template::set_message(lang('botanicules_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('botanicules_edit_failure') . $this->botanicules_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Botanicules.Content.Delete');

			if ($this->botanicules_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('botanicules_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'botanicules');

				Template::set_message(lang('botanicules_delete_success'), 'success');

				redirect(SITE_AREA .'/content/botanicules');
			}
			else
			{
				Template::set_message(lang('botanicules_delete_failure') . $this->botanicules_model->error, 'error');
			}
		}
		Template::set('botanicules', $this->botanicules_model->find($id));
		Template::set('toolbar_title', lang('botanicules_edit') .' Botanicules');
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
	private function save_botanicules($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['structure']        = $this->input->post('botanicules_structure');
		$data['mol_weight']        = $this->input->post('botanicules_mol_weight');
		$data['formula']        = $this->input->post('botanicules_formula');
		$data['compound_name']        = $this->input->post('botanicules_compound_name');
		$data['mol_name']        = $this->input->post('botanicules_mol_name');
		$data['ref']        = $this->input->post('botanicules_ref');
		$data['src_ref']        = $this->input->post('botanicules_src_ref');
		$data['mol_type']        = $this->input->post('botanicules_mol_type');
		$data['therapeutic_catg']        = $this->input->post('botanicules_therapeutic_catg');
		$data['iupac_name']        = $this->input->post('botanicules_iupac_name');
		$data['src_type']        = $this->input->post('botanicules_src_type');
		$data['src_family']        = $this->input->post('botanicules_src_family');
		$data['qc_status']        = $this->input->post('botanicules_qc_status');
		$data['pdf_avail']        = $this->input->post('botanicules_pdf_avail');
		$data['parts_of_isol']        = $this->input->post('botanicules_parts_of_isol');
		$data['user_id']        = $this->current_user->id;

		if ($type == 'insert')
		{
			$id = $this->botanicules_model->insert($data);

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
			$return = $this->botanicules_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}