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

		$this->auth->restrict('Inquiries.Content.View');
		$this->load->model('inquiries_model', null, true);
        $this->load->model('uom/uom_model');
		$this->lang->load('inquiries');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('inquiries', 'inquiries.js');
        
		$uoms_select = $this->uom_model->get_uoms_select();
		Template::set('uoms_select', $uoms_select);

		$uoms = $this->uom_model->get_uoms();
		Template::set('uoms', $uoms);        
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
					$result = $this->inquiries_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('inquiries_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('inquiries_delete_failure') . $this->inquiries_model->error, 'error');
				}
			}
		}

		$records = $this->inquiries_model->find_all();
         $total = $this->inquiries_model->count_all();
        
        //pagination
        $this->load->library('pagination');
        
        $offset = $this->input->get('per_page');
        
        $limit = '10';
        
        $this->pager['base_url'] = current_url() .'?';
        $this->pager['total_rows'] = $total;
        $this->pager['per_page'] = $limit;
        $this->pager['page_query_string'] = TRUE;
        
        $this->pagination->initialize($this->pager);
        
        Template::set('records', $this->inquiries_model->limit($limit, $offset)->find_all());


		//Template::set('records', $records);
		Template::set('toolbar_title', 'Manage Inquiries');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Creates a Inquiries object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Inquiries.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_inquiries())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('inquiries_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'inquiries');

				Template::set_message(lang('inquiries_create_success'), 'success');
				redirect(SITE_AREA .'/content/inquiries');
			}
			else
			{
				Template::set_message(lang('inquiries_create_failure') . $this->inquiries_model->error, 'error');
			}
		}
		Assets::add_module_js('inquiries', 'inquiries.js');

		Template::set('toolbar_title', lang('inquiries_create') . ' Inquiries');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Inquiries data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('inquiries_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/inquiries');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Inquiries.Content.Edit');

			if ($this->save_inquiries('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('inquiries_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'inquiries');

				Template::set_message(lang('inquiries_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('inquiries_edit_failure') . $this->inquiries_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Inquiries.Content.Delete');

			if ($this->inquiries_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('inquiries_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'inquiries');

				Template::set_message(lang('inquiries_delete_success'), 'success');

				redirect(SITE_AREA .'/content/inquiries');
			}
			else
			{
				Template::set_message(lang('inquiries_delete_failure') . $this->inquiries_model->error, 'error');
			}
		}
        
        $inquiry = $this->inquiries_model->find($id);
        
        // Load comment thread id attached to content 
        
        $comments_thread_id = $inquiry->comments_thread_id;
        // Test if comment module exists and if so, load parsed content
        
        $comments = (in_array('comments',module_list(true))) ?     modules::run('comments/thread_view_with_form',$comments_thread_id) : '';
        // Set content to template
        Template::set('comment_form', $comments);
        
        // Count comments
        $comment_count = (in_array('comments',module_list(true))) ? modules::run('comments/count_comments',$comments_thread_id) : 0;
        Template::set('comment_count', $comment_count);

        
  		Template::set('inquiries', $inquiry);
		Template::set('toolbar_title', lang('inquiries_edit') .' Inquiries');
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
	private function save_inquiries($type='insert', $id=0)
	{
		if ($type == 'update')
		{
			$_POST['id'] = $id;
		}

		// make sure we only pass in the fields we want
		
		$data = array();
		$data['product']        = $this->input->post('inquiries_product');
		$data['quantity']        = $this->input->post('inquiries_quantity');
		$data['uom_id']        = $this->input->post('inquiries_uom_id');
		$data['required_by']        = $this->input->post('inquiries_required_by') ? $this->input->post('inquiries_required_by') : '0000-00-00';
		$data['prod_spec']        = $this->input->post('inquiries_prod_spec');
		$data['quality_spec']        = $this->input->post('inquiries_quality_spec');
		$data['packaging_spec']        = $this->input->post('inquiries_packaging_spec');
		$data['priority']        = $this->input->post('inquiries_priority');
		$data['status']        = $this->input->post('inquiries_status');
        //$data['created_by']        = $this->current_user->id;

		if ($type == 'update')
		{
			$return = $this->inquiries_model->update($id, $data);
		}
        
        if ($type == 'insert')
        {
            $thread_id = 0;
            if (in_array('comments',module_list(true))) 
            {
                if(!isset($this->comments_model)) 
                {
                    $this->load->model('comments/comments_model');
                }
                $thread_id = $this->comments_model->new_comments_thread('inquiries');
            }
            $data = $data + array('comments_thread_id'=>$thread_id,'created_by'=>$this->current_user->id);
            
            return $this->inquiries_model->insert($data);
        }
        
        
	//--------------------------------------------------------------------
    }

}