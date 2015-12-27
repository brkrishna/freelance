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

		$this->auth->restrict('Activity_Documents.Content.View');
		$this->load->model('activity_documents_model', null, true);
        $this->load->model(array('activity_type/activity_type_model', 'document_types/document_types_model', 'product/product_model'));
		$this->lang->load('activity_documents');
		
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('activity_documents', 'activity_documents.js');
        
		$activity_types_select = $this->activity_type_model->get_activity_types_select();
		Template::set('activity_types_select', $activity_types_select);

		$activity_types = $this->activity_type_model->get_activity_types();
		Template::set('activity_types', $activity_types);
        
		$doc_types_select = $this->document_types_model->get_doc_types_select();
		Template::set('doc_types_select', $doc_types_select);

		$doc_types = $this->document_types_model->get_doc_types();
		Template::set('doc_types', $doc_types);
        
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
					$result = $this->activity_documents_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('activity_documents_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('activity_documents_delete_failure') . $this->activity_documents_model->error, 'error');
				}
			}
		}

		$records = $this->activity_documents_model->find_all();
        $total = $this->activity_documents_model->count_all();
 
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
 
        $this->pager['base_url']          = current_url() .'?';
        $this->pager['total_rows']            = $total;
        $this->pager['per_page']          = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
 
        Template::set('records', $this->activity_documents_model->limit($limit, $offset)->find_all());

		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Activity Documents');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Activity Documents object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Activity_Documents.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_activity_documents())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('activity_documents_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'activity_documents');

				Template::set_message(lang('activity_documents_create_success'), 'success');
				redirect(SITE_AREA .'/content/activity_documents');
			}
			else
			{
				Template::set_message(lang('activity_documents_create_failure') . $this->activity_documents_model->error, 'error');
			}
		}
		Assets::add_module_js('activity_documents', 'activity_documents.js');

		Template::set('toolbar_title', lang('activity_documents_create') . ' Activity Documents');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Activity Documents data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('activity_documents_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/activity_documents');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Activity_Documents.Content.Edit');

			if ($this->save_activity_documents('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('activity_documents_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'activity_documents');

				Template::set_message(lang('activity_documents_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('activity_documents_edit_failure') . $this->activity_documents_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Activity_Documents.Content.Delete');

			if ($this->activity_documents_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('activity_documents_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'activity_documents');

				Template::set_message(lang('activity_documents_delete_success'), 'success');

				redirect(SITE_AREA .'/content/activity_documents');
			}
			else
			{
				Template::set_message(lang('activity_documents_delete_failure') . $this->activity_documents_model->error, 'error');
			}
		}
		Template::set('activity_documents', $this->activity_documents_model->find($id));
		Template::set('toolbar_title', lang('activity_documents_edit') .' Activity Documents');
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
	private function save_activity_documents($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['activity_code']      = $this->input->post('activity_documents_activity_code');
        $data['product_id']         = $this->input->post('activity_documents_product_id');
		$data['document_id']        = $this->input->post('activity_documents_document_id');
        $data['sno']                = $this->input->post('activity_documents_sno');

		if ($type == 'insert')
		{
			$id = $this->activity_documents_model->insert($data);

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
			$return = $this->activity_documents_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------


}