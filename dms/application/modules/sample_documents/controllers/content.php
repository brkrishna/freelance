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

		$this->auth->restrict('Sample_Documents.Content.View');
		$this->load->model('sample_documents_model', null, true);
        $this->load->model(array('document_types/document_types_model', 'samples/samples_model'));
		$this->lang->load('sample_documents');
		
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('sample_documents', 'sample_documents.js');
        
		$doc_types_select = $this->document_types_model->get_doc_types_select();
		Template::set('doc_types_select', $doc_types_select);

		$doc_types = $this->document_types_model->get_doc_types();
		Template::set('doc_types', $doc_types);
        
		$samples_select = $this->samples_model->get_samples_select();
		Template::set('samples_select', $samples_select);

		$samples = $this->samples_model->get_samples();
		Template::set('samples', $samples);
        
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
        $total = $this->sample_documents_model->count_all();
 
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
 
        $this->pager['base_url']          = current_url() .'?';
        $this->pager['total_rows']            = $total;
        $this->pager['per_page']          = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
 
        Template::set('records', $this->sample_documents_model->limit($limit, $offset)->find_all());

		//Template::set('records', $records);
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
		$this->auth->restrict('Sample_Documents.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_sample_documents())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('sample_documents_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'sample_documents');

				Template::set_message(lang('sample_documents_create_success'), 'success');
				redirect(SITE_AREA .'/content/sample_documents');
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
			redirect(SITE_AREA .'/content/sample_documents');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Sample_Documents.Content.Edit');

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
			$this->auth->restrict('Sample_Documents.Content.Delete');

			if ($this->sample_documents_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('sample_documents_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'sample_documents');

				Template::set_message(lang('sample_documents_delete_success'), 'success');

				redirect(SITE_AREA .'/content/sample_documents');
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
        
		if (isset($_FILES['sample_documents_attachment']) && is_array($_FILES['sample_documents_attachment']) && $_FILES['sample_documents_attachment']['error'] != 4)
        {
			// make sure we only pass in the fields we want
			$file_path = $this->config->item('upload_dir');

			$config['upload_path']		= $file_path;
			$config['allowed_types']	= 'pdf';

			$this->load->library('upload', $config);
			echo "hree";
			if ( ! $this->upload->do_upload('sample_documents_attachment'))
			{
				return array('error'=>$this->upload->display_errors());
			}else{
				$data['attachment'] = serialize($this->upload->data());			
			}		

		}
        
		$data['doc_type']        = $this->input->post('sample_documents_doc_type');
		$data['sample_id']        = $this->input->post('sample_documents_sample_id');
		
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
     public function remove_attachment()
	{
		$id = $this->uri->segment(5);

		$success = false;

		// Handle a single-user purge
		if (!empty($id) && is_numeric($id))
		{
			$sample_document = $this->sample_documents_model->find($id);
			if (isset($sample_document) && isset($sample_document->attachment))
			{
                echo 'calling delete attachment';
				$this->delete_attachments ( $sample_document->attachment );
                echo 'here';
				$data = array('attachment'=>'');
				$success = $this->sample_documents_model->update($id, $data);
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