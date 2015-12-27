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

		$this->auth->restrict('Document_Types.Content.View');
		$this->load->model('document_types_model', null, true);
		$this->lang->load('document_types');
		
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('document_types', 'document_types.js');
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
					$result = $this->document_types_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('document_types_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('document_types_delete_failure') . $this->document_types_model->error, 'error');
				}
			}
		}

		$records = $this->document_types_model->find_all();
        $total = $this->document_types_model->count_all();
        
        //pagination
        $this->load->library('pagination');
        
        $offset = $this->input->get('per_page');
        
        $limit = '10';
        
        $this->pager['base_url'] = current_url() .'?';
        $this->pager['total_rows'] = $total;
        $this->pager['per_page'] = $limit;
        $this->pager['page_query_string'] = TRUE;
        
        $this->pagination->initialize($this->pager);
        
        Template::set('records', $this->document_types_model->limit($limit, $offset)->find_all());

		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Document Types');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Document Types object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Document_Types.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_document_types())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('document_types_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'document_types');

				Template::set_message(lang('document_types_create_success'), 'success');
				redirect(SITE_AREA .'/content/document_types');
			}
			else
			{
				Template::set_message(lang('document_types_create_failure') . $this->document_types_model->error, 'error');
			}
		}
		Assets::add_module_js('document_types', 'document_types.js');

		Template::set('toolbar_title', lang('document_types_create') . ' Document Types');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Document Types data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('document_types_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/document_types');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Document_Types.Content.Edit');

			if ($this->save_document_types('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('document_types_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'document_types');

				Template::set_message(lang('document_types_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('document_types_edit_failure') . $this->document_types_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Document_Types.Content.Delete');

			if ($this->document_types_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('document_types_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'document_types');

				Template::set_message(lang('document_types_delete_success'), 'success');

				redirect(SITE_AREA .'/content/document_types');
			}
			else
			{
				Template::set_message(lang('document_types_delete_failure') . $this->document_types_model->error, 'error');
			}
		}
		Template::set('document_types', $this->document_types_model->find($id));
		Template::set('toolbar_title', lang('document_types_edit') .' Document Types');
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
	private function save_document_types($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['name']        = $this->input->post('document_types_name');

		if ($type == 'insert')
		{
			$id = $this->document_types_model->insert($data);

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
			$return = $this->document_types_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}