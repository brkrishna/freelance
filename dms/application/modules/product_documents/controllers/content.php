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

		$this->auth->restrict('Product_Documents.Content.View');
		$this->load->model('product_documents_model', null, true);
        $this->load->model(array('vendor_profile/vendor_profile_model', 'product/product_model', 'document_types/document_types_model'));
		$this->lang->load('product_documents');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('product_documents', 'product_documents.js');
        
        $profile_id = NULL;
        
        if (isset($this->curr_user_profile['id'])) {
            $profile_id = $this->curr_user_profile['id'];
        }
        
		$vendors_select = $this->vendor_profile_model->get_vendors_select($profile_id);
		Template::set('vendors_select', $vendors_select);

		$vendors = $this->vendor_profile_model->get_vendors($profile_id);
		Template::set('vendors', $vendors);

		$products_select = $this->product_model->get_products_select();
		Template::set('products_select', $products_select);

		$products = $this->product_model->get_products();
		Template::set('products', $products);
        
		$doc_types_select = $this->document_types_model->get_doc_types_select();
		Template::set('doc_types_select', $doc_types_select);

		$doc_types = $this->document_types_model->get_doc_types();
		Template::set('doc_types', $doc_types);

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
					$result = $this->product_documents_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('product_documents_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('product_documents_delete_failure') . $this->product_documents_model->error, 'error');
				}
			}
		}

        $profile_id = NULL;
        
        if (isset($this->curr_user_profile['id'])) {
            $profile_id = $this->curr_user_profile['id'];
        }
        
		$records = $this->product_documents_model->find_all($profile_id);
        $total = $this->product_documents_model->count_all();
 
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
 
        $this->pager['base_url'] = current_url() .'?';
        $this->pager['total_rows'] = $total;
        $this->pager['per_page'] = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
 
        Template::set('records', $this->product_documents_model->limit($limit, $offset)->find_all());
 

		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Product Documents');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Product Documents object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Product_Documents.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_product_documents())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('product_documents_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'product_documents');

				Template::set_message(lang('product_documents_create_success'), 'success');
				redirect(SITE_AREA .'/content/product_documents');
			}
			else
			{
				Template::set_message(lang('product_documents_create_failure') . $this->product_documents_model->error, 'error');
			}
		}
		Assets::add_module_js('product_documents', 'product_documents.js');

		Template::set('toolbar_title', lang('product_documents_create') . ' Product Documents');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Product Documents data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('product_documents_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/product_documents');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Product_Documents.Content.Edit');

			if ($this->save_product_documents('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('product_documents_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'product_documents');

				Template::set_message(lang('product_documents_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('product_documents_edit_failure') . $this->product_documents_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Product_Documents.Content.Delete');

			if ($this->product_documents_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('product_documents_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'product_documents');

				Template::set_message(lang('product_documents_delete_success'), 'success');

				redirect(SITE_AREA .'/content/product_documents');
			}
			else
			{
				Template::set_message(lang('product_documents_delete_failure') . $this->product_documents_model->error, 'error');
			}
		}
		Template::set('product_documents', $this->product_documents_model->find($id));
		Template::set('toolbar_title', lang('product_documents_edit') .' Product Documents');
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
	private function save_product_documents($type='insert', $id=0)
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
        
		$data['vendor_id']        = $this->input->post('product_documents_vendor_id');
		$data['activity_code']        = 'VE';
		$data['product_id']        = $this->input->post('product_documents_product_id');
		$data['document_id']        = $this->input->post('product_documents_document_id');
		$data['issue_auth']        = $this->input->post('product_documents_issue_auth');
		$data['issued_on']        = $this->input->post('product_documents_issued_on') ? $this->input->post('product_documents_issued_on') : '0000-00-00';
		$data['valid_till']        = $this->input->post('product_documents_valid_till') ? $this->input->post('product_documents_valid_till') : '0000-00-00';
		$data['place_of_origin']        = $this->input->post('product_documents_place_of_origin');
		$data['comments']        = $this->input->post('product_documents_comments');
        
		$data['created_by']        = $this->current_user->id;
        
        if (isset($this->curr_user_profile) && isset($this->curr_user_profile['id'])){
            $data['profile_id']        = $this->curr_user_profile['id'];    
        }else{
            $data['profile_id']        = NULL;    
        }	
        

		if ($type == 'insert')
		{
			$id = $this->product_documents_model->insert($data);

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
			$return = $this->product_documents_model->update($id, $data);
		}

		return $return;
	}

	//--------------------------------------------------------------------
    public function remove_attachment()
	{
		$id = $this->uri->segment(5);

		$success = false;

		// Handle a single-user purge
		if (!empty($id) && is_numeric($id))
		{
			$product_document = $this->product_documents_model->find($id);
			if (isset($product_document) && isset($product_document->attachment))
			{
                echo 'calling delete attachment';
				$this->delete_attachments ( $product_document->attachment );
                echo 'here';
				$data = array('attachment'=>'');
				$success = $this->product_documents_model->update($id, $data);
                echo 'in if - ' . $success;
			}
		}
		if (!$success)
		{
			Template::set_message('Attachment removal failed.', 'error');
		}
		else
		{
			Template::set_message('Attachment removed.', 'success');
		}
		$this->edit();

	}

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
			if ( $deleted == false )
			{
				$err = sprintf('Problem deleting attachment file: "%s"', $attachment['file_name']);
				Template::set_message($err, 'error');
				log_message('error', $err);
			}
			unset ( $deleted );
		}
	} 

}