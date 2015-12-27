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

		$this->auth->restrict('UOM.Content.View');
		$this->load->model('uom_model', null, true);
		$this->lang->load('uom');
		
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('uom', 'uom.js');
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
					$result = $this->uom_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('uom_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('uom_delete_failure') . $this->uom_model->error, 'error');
				}
			}
		}

		//$records = $this->uom_model->find_all();

        $total = $this->uom_model->count_all();
 
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
 
        $this->pager['base_url']          = current_url() .'?';
        $this->pager['total_rows']            = $total;
        $this->pager['per_page']          = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
 
        Template::set('records', $this->uom_model->limit($limit, $offset)->find_all());

        
		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage UOM');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a UOM object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('UOM.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_uom())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('uom_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'uom');

				Template::set_message(lang('uom_create_success'), 'success');
				redirect(SITE_AREA .'/content/uom');
			}
			else
			{
				Template::set_message(lang('uom_create_failure') . $this->uom_model->error, 'error');
			}
		}
		Assets::add_module_js('uom', 'uom.js');

		Template::set('toolbar_title', lang('uom_create') . ' UOM');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of UOM data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('uom_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/uom');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('UOM.Content.Edit');

			if ($this->save_uom('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('uom_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'uom');

				Template::set_message(lang('uom_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('uom_edit_failure') . $this->uom_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('UOM.Content.Delete');

			if ($this->uom_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('uom_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'uom');

				Template::set_message(lang('uom_delete_success'), 'success');

				redirect(SITE_AREA .'/content/uom');
			}
			else
			{
				Template::set_message(lang('uom_delete_failure') . $this->uom_model->error, 'error');
			}
		}
		Template::set('uom', $this->uom_model->find($id));
		Template::set('toolbar_title', lang('uom_edit') .' UOM');
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
	private function save_uom($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['name']        = $this->input->post('uom_name');

		if ($type == 'insert')
		{
			$id = $this->uom_model->insert($data);

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
			$return = $this->uom_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}