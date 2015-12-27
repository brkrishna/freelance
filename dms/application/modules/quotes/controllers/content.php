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

		$this->auth->restrict('Quotes.Content.View');
		$this->load->model('quotes_model', null, true);
        $this->load->model(array('uom/uom_model', 'product/product_model', 'vendor_profile/vendor_profile_model'));
		$this->lang->load('quotes');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('quotes', 'quotes.js');
        
		$uoms_select = $this->uom_model->get_uoms_select();
		Template::set('uoms_select', $uoms_select);

		$uoms = $this->uom_model->get_uoms();
		Template::set('uoms', $uoms);

		$products_select = $this->product_model->get_products_select();
		Template::set('products_select', $products_select);

		$products = $this->product_model->get_products();
		Template::set('products', $products);

		/*
        $vendors_select = $this->vendors_model->get_vendors_select();
		Template::set('vendors_select', $vendors_select);

		$vendors = $this->vendors_model->get_vendors();
		Template::set('vendors', $vendors);
        */
        $vendors_select = $this->vendor_profile_model->get_vendors_select();
		Template::set('vendors_select', $vendors_select);

		$vendors = $this->vendor_profile_model->get_vendors();
		Template::set('vendors', $vendors);
        
        
        
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
					$result = $this->quotes_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('quotes_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('quotes_delete_failure') . $this->quotes_model->error, 'error');
				}
			}
		}

		$records = $this->quotes_model->find_all();
        $total = $this->quotes_model->count_all();
 
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
 
        $this->pager['base_url']          = current_url() .'?';
        $this->pager['total_rows']            = $total;
        $this->pager['per_page']          = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
 
        Template::set('records', $this->quotes_model->limit($limit, $offset)->find_all());

		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Quotes');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Quotes object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Quotes.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_quotes())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('quotes_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'quotes');

				Template::set_message(lang('quotes_create_success'), 'success');
				redirect(SITE_AREA .'/content/quotes');
			}
			else
			{
				Template::set_message(lang('quotes_create_failure') . $this->quotes_model->error, 'error');
			}
		}
		Assets::add_module_js('quotes', 'quotes.js');

		Template::set('toolbar_title', lang('quotes_create') . ' Quotes');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Quotes data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('quotes_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/quotes');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Quotes.Content.Edit');

			if ($this->save_quotes('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('quotes_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'quotes');

				Template::set_message(lang('quotes_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('quotes_edit_failure') . $this->quotes_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Quotes.Content.Delete');

			if ($this->quotes_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('quotes_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'quotes');

				Template::set_message(lang('quotes_delete_success'), 'success');

				redirect(SITE_AREA .'/content/quotes');
			}
			else
			{
				Template::set_message(lang('quotes_delete_failure') . $this->quotes_model->error, 'error');
			}
		}
		Template::set('quotes', $this->quotes_model->find($id));
		Template::set('toolbar_title', lang('quotes_edit') .' Quotes');
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
	private function save_quotes($type='insert', $id=0)
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
			$config['allowed_types']	= 'pdf';

			$this->load->library('upload', $config);
			if ( ! $this->upload->do_upload('attachment'))
			{
				return array('error'=>$this->upload->display_errors());
			}else{
				$data['attachment'] = serialize($this->upload->data());			
			}		

		}
        
		$data['ref_no']        = $this->input->post('quotes_ref_no');
		$data['quote_dt']        = $this->input->post('quotes_quote_dt') ? $this->input->post('quotes_quote_dt') : '0000-00-00';
		$data['vendor_id']        = $this->input->post('quotes_vendor_id');
		$data['product_id']        = $this->input->post('quotes_product_id');
		$data['price']        = $this->input->post('quotes_price');
		$data['tat']        = $this->input->post('quotes_tat');
		$data['quantity']        = $this->input->post('quotes_quantity');
		$data['uom_id']        = $this->input->post('quotes_uom_id');

		if ($type == 'insert')
		{
			$id = $this->quotes_model->insert($data);

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
			$return = $this->quotes_model->update($id, $data);
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
			$quote = $this->quotes_model->find($id);
			if (isset($quote) && isset($quote->attachment))
			{
                echo 'calling delete attachment';
				$this->delete_attachments ( $quote->attachment );
                echo 'here';
				$data = array('attachment'=>'');
				$success = $this->quotes_model->update($id, $data);
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