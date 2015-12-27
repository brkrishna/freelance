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

		$this->auth->restrict('PO_Documents.Content.View');
		$this->load->model('po_documents_model', null, true);
        $this->load->model(array('vendor_profile/vendor_profile_model', 'product/product_model', 'document_types/document_types_model', 'purchase_orders/purchase_orders_model'));
		$this->lang->load('po_documents');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('po_documents', 'po_documents.js');
        
		$vendors_select = $this->vendor_profile_model->get_vendors_select();
		Template::set('vendors_select', $vendors_select);

		$vendors = $this->vendor_profile_model->get_vendors();
		Template::set('vendors', $vendors);

		$products_select = $this->product_model->get_products_select();
		Template::set('products_select', $products_select);

		$products = $this->product_model->get_products();
		Template::set('products', $products);
        
		$doc_types_select = $this->document_types_model->get_doc_types_select();
		Template::set('doc_types_select', $doc_types_select);

		$doc_types = $this->document_types_model->get_doc_types();
		Template::set('doc_types', $doc_types);
        
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
					$result = $this->po_documents_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('po_documents_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('po_documents_delete_failure') . $this->po_documents_model->error, 'error');
				}
			}
		}

		$records = $this->po_documents_model->find_all();

		Template::set('records', $records);
		Template::set('toolbar_title', 'Manage PO Documents');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a PO Documents object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('PO_Documents.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_po_documents())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('po_documents_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'po_documents');

				Template::set_message(lang('po_documents_create_success'), 'success');
				redirect(SITE_AREA .'/content/po_documents');
			}
			else
			{
				Template::set_message(lang('po_documents_create_failure') . $this->po_documents_model->error, 'error');
			}
		}
		Assets::add_module_js('po_documents', 'po_documents.js');

        $id = $this->uri->segment(5);
        if (!empty($id)){
            $po_data = $this->purchase_orders_model->find_by('id', $id);
            Template::set('po_data', $po_data);
        }
        
		Template::set('toolbar_title', lang('po_documents_create') . ' PO Documents');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of PO Documents data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('po_documents_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/po_documents');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('PO_Documents.Content.Edit');

			if ($this->save_po_documents('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('po_documents_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'po_documents');

				Template::set_message(lang('po_documents_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('po_documents_edit_failure') . $this->po_documents_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('PO_Documents.Content.Delete');

			if ($this->po_documents_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('po_documents_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'po_documents');

				Template::set_message(lang('po_documents_delete_success'), 'success');

				redirect(SITE_AREA .'/content/po_documents');
			}
			else
			{
				Template::set_message(lang('po_documents_delete_failure') . $this->po_documents_model->error, 'error');
			}
		}
		Template::set('po_documents', $this->po_documents_model->find($id));
		Template::set('toolbar_title', lang('po_documents_edit') .' PO Documents');
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
	private function save_po_documents($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
        
		if (isset($_FILES['attachment']) && is_array($_FILES['attachment']) && $_FILES['attachment']['error'] != 4)
        {
			// make sure we only pass in the fields we want
			$file_path = $this->config->item('upload_dir');

			$config['upload_path']		= $file_path;
			$config['allowed_types']	= 'pdf|jpg|gif';

			$this->load->library('upload', $config);
			if ( ! $this->upload->do_upload('attachment'))
			{
				return array('error'=>$this->upload->display_errors());
			}else{
				$data['attachment'] = serialize($this->upload->data());			
			}		

		}
        
		$data['po_no']        = $this->input->post('po_documents_po_no');
		$data['vendor_id']        = $this->input->post('po_documents_vendor_id');
		$data['product_id']        = $this->input->post('po_documents_product_id');
		$data['applicable']        = $this->input->post('po_documents_applicable');
		$data['document_id']        = $this->input->post('po_documents_document_id');
		$data['issue_auth']        = $this->input->post('po_documents_issue_auth');
		$data['issued_on']        = $this->input->post('po_documents_issued_on') ? $this->input->post('po_documents_issued_on') : '0000-00-00';
		$data['valid_till']        = $this->input->post('po_documents_valid_till') ? $this->input->post('po_documents_valid_till') : '0000-00-00';
		$data['origin_place']        = $this->input->post('po_documents_origin_place');
		$data['comments']        = $this->input->post('po_documents_comments');
		$data['created_by']        = $this->current_user->id;

		if ($type == 'insert')
		{
			$id = $this->po_documents_model->insert($data);

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
			$return = $this->po_documents_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------
	public function remove_attachment()
	{
		$id = $this->uri->segment(5);
		$success = (bool)false;

		// Handle a single-user purge
		if (!empty($id) && is_numeric($id))
		{
			$po = $this->po_documents_model->find($id);
			if (isset($po) && isset($po->attachment))
			{
				$this->delete_attachments ( $po->attachment );
				$data = array('attachment'=>'');
                $this->po_documents_model->skip_validation(TRUE);
				$success = $this->po_documents_model->update($id, $data);
			}
		}
		if (!$success)
		{
			Template::set_message('Attachment remove failed.', 'error');
		}
		else
		{
			Template::set_message('Attachment removed.', 'success');
		}
		$this->edit();

	}

	//--------------------------------------------------------------------    
	/**
	 * Deletes Attachments or dies trying to. ( Chuck Norris would just chop them off I'm sure )
	 *
	 * @param $attachment Serialized data for attachment
	 */
	private function delete_attachments( $attachment )
	{
		$attachment = unserialize( $attachment );
		$file_dir = $this->config->item('upload_dir');

		if (file_exists( $file_dir . '/' . $attachment['file_name']) )
		{
			$deleted = unlink( $file_dir . '/' .$attachment['file_name']);
            if ( $deleted === false )
			{
				$err = sprintf('Problem deleting attachment file: "%s"', $attachment['file_name']);
				Template::set_message($err, 'error');
				log_message('error', $err);
			}
			unset ( $deleted );
		}
	}

	//--------------------------------------------------------------------

}