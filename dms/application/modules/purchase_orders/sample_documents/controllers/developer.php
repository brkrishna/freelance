<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * developer controller
 */
class developer extends Admin_Controller
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

		$this->auth->restrict('Sample_Documents.Developer.View');
		$this->load->model('sample_documents_model', null, true);
		$this->lang->load('sample_documents');
		
		Template::set_block('sub_nav', 'developer/_sub_nav');

		Assets::add_module_js('sample_documents', 'sample_documents.js');
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
					$result = $this->sample_documents_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('sample_documents_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('sample_documents_delete_failure') . $this->sample_documents_model->error, 'error');
				}
			}
		}

		$records = $this->sample_documents_model->find_all();

		Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Sample Documents');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Sample Documents object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Sample_Documents.Developer.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_sample_documents())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('sample_documents_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'sample_documents');

				Template::set_message(lang('sample_documents_create_success'), 'success');
				redirect(SITE_AREA .'/developer/sample_documents');
			}
			else
			{
				Template::set_message(lang('sample_documents_create_failure') . $this->sample_documents_model->error, 'error');
			}
		}
		Assets::add_module_js('sample_documents', 'sample_documents.js');

		Template::set('toolbar_title', lang('sample_documents_create') . ' Sample Documents');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Sample Documents data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('sample_documents_invalid_id'), 'error');
			redirect(SITE_AREA .'/developer/sample_documents');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Sample_Documents.Developer.Edit');

			if ($this->save_sample_documents('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('sample_documents_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'sample_documents');

				Template::set_message(lang('sample_documents_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('sample_documents_edit_failure') . $this->sample_documents_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Sample_Documents.Developer.Delete');

			if ($this->sample_documents_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('sample_documents_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'sample_documents');

				Template::set_message(lang('sample_documents_delete_success'), 'success');

				redirect(SITE_AREA .'/developer/sample_documents');
			}
			else
			{
				Template::set_message(lang('sample_documents_delete_failure') . $this->sample_documents_model->error, 'error');
			}
		}
		Template::set('sample_documents', $this->sample_documents_model->find($id));
		Template::set('toolbar_title', lang('sample_documents_edit') .' Sample Documents');
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
	private function save_sample_documents($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['doc_type']        = $this->input->post('sample_documents_doc_type');
		$data['sample_id']        = $this->input->post('sample_documents_sample_id');
		$data['attachment']        = $this->input->post('sample_documents_attachment');

		if ($type == 'insert')
		{
			$id = $this->sample_documents_model->insert($data);

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
			$return = $this->sample_documents_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}