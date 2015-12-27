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

		$this->auth->restrict('Todo.Content.View');
		$this->load->model('todo_model', null, true);
        $this->load->model(array('todo_list/todo_list_model', 'users/user_model'));
		$this->lang->load('todo');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('todo', 'todo.js');
        
        //Assets::add_js('js/angular.min.js');
        //Assets::add_module_js('todo', 'ui-bootstrap-tpls-0.10.0.min.js');
        //Assets::add_module_js('todo', 'app.js');
        //Assets::add_module_css('todo', 'bootstrap.min.css');
        
		$todo_list_select = $this->todo_list_model->get_todo_list_select();
		Template::set('todo_list_select', $todo_list_select);

		$todo_lists = $this->todo_list_model->get_todo_lists();
		Template::set('todo_lists', $todo_lists);
        
		$users_select = $this->user_model->get_users_select();
		Template::set('users_select', $users_select);

		$users = $this->user_model->get_users();
		Template::set('users', $users);
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
					$result = $this->todo_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('todo_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('todo_delete_failure') . $this->todo_model->error, 'error');
				}
			}
		}
        
        $lists = $this->todo_list_model->get_todo_lists();
        $where = array();
        
        $filter = $this->input->get('filter');
        $filter_status = NULL;
        $list_id = NULL;
        
        switch($filter){
            case 'status':
                if ($this->input->get('status') != NULL) { 
                    $filter_status = $this->input->get('status');
                    $where['status'] = $filter_status;
                    Template::set('filter_status', $filter_status); 
                }
                break;
            case 'list':
                if ($this->input->get('list') != NULL) {   
                    $list_id = $this->input->get('list');
                    $where['list_id'] = $list_id;
                    foreach($lists as $list){
                        if($list->id == $list_id){
                            Template::set('filter_list', $list->name);         
                        }
                    }
                }
                break;
            default:
                break;
        }
        
        $this->todo_model->where($where);
        $total = $this->todo_model->count_all();
 
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
        
        $this->pager['base_url']          = current_url() .'?filter=' . $filter . '&status=' . $filter_status . '&list=' . $list_id;
        $this->pager['total_rows']        = $total;
        $this->pager['per_page']          = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
        
        $statuses = array('Active' =>'Active', 'Closed'=>'Closed');

		Template::set('records', $this->todo_model->where($where)->limit($limit, $offset)->find_all_by(array('deleted' => 0)));
		Template::set('toolbar_title', 'Manage Todo');
        
        Template::set('filter', $filter);
        Template::set('statuses', $statuses);
        Template::set('lists', $lists);
        Template::set('current_url', current_url());
		Template::render();
	}

    	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index3()
	{

<<<<<<< HEAD
		// Deleting anything?
		if (isset($_POST['delete']))
		{
			$checked = $this->input->post('checked');

			if (is_array($checked) && count($checked))
			{
				$result = FALSE;
				foreach ($checked as $pid)
				{
					$result = $this->todo_model->delete($pid);
				}

				if ($result)
				{
					Template::set_message(count($checked) .' '. lang('todo_delete_success'), 'success');
				}
				else
				{
					Template::set_message(lang('todo_delete_failure') . $this->todo_model->error, 'error');
				}
			}
		}
        
        
        // Pagination
        $this->load->library('pagination');
 
        $offset = $this->input->get('per_page');
 
        $limit = 10;
        
        $this->pager['base_url']          = current_url() .'?filter=' . $filter . '&status=' . $filter_status . '&list=' . $list_id;
        $this->pager['total_rows']        = $total;
        $this->pager['per_page']          = $limit;
        $this->pager['page_query_string'] = TRUE;
 
        $this->pagination->initialize($this->pager);
        //return $this->todo_model->as_json()->find_all_by(array('deleted' => 0));
		Template::set('records', $this->todo_model->find_all_by(array('deleted' => 0)));
=======
		$records = $this->todo_model->find_all_by(array('deleted' => 0));
        $total = $this->todo_model->count_all();
        
        //pagination
        $this->load->library('pagination');
        $offset = $this->input->get('per_page');
        
        $limit = '10';
        
        $this->pager['base_url'] = current_url() .'?';
        $this->pager['total_rows'] = $total;
        $this->pager['per_page'] = $limit;
        $this->pager['page_query_string'] = TRUE;
        
        $this->pagination->initialize($this->pager);
        
        Template::set('records', $this->todo_model->limit($limit, $offset)->find_all());
       

		//Template::set('records', $records);
>>>>>>> f19371064a9ba4d3faff72c86b6ae2805aa04588
		Template::set('toolbar_title', 'Manage Todo');
        //Template::set_view('todos');
		Template::render();
	}
    
    public function get_json(){
        
        echo $this->todo_model->as_json()->find_all_by(array('deleted' => 0));
    }

	//--------------------------------------------------------------------


	/**
	 * Creates a Todo object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict('Todo.Content.Create');

		if (isset($_POST['save']))
		{
			if ($insert_id = $this->save_todo())
			{
				// Log the activity
				log_activity($this->current_user->id, lang('todo_act_create_record') .': '. $insert_id .' : '. $this->input->ip_address(), 'todo');

				Template::set_message(lang('todo_create_success'), 'success');
				redirect(SITE_AREA .'/content/todo');
			}
			else
			{
				Template::set_message(lang('todo_create_failure') . $this->todo_model->error, 'error');
			}
		}
		Assets::add_module_js('todo', 'todo.js');

		Template::set('toolbar_title', lang('todo_create') . ' Todo');
		Template::render();
	}

	//--------------------------------------------------------------------


	/**
	 * Allows editing of Todo data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);

		if (empty($id))
		{
			Template::set_message(lang('todo_invalid_id'), 'error');
			redirect(SITE_AREA .'/content/todo');
		}

		if (isset($_POST['save']))
		{
			$this->auth->restrict('Todo.Content.Edit');

			if ($this->save_todo('update', $id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('todo_act_edit_record') .': '. $id .' : '. $this->input->ip_address(), 'todo');

				Template::set_message(lang('todo_edit_success'), 'success');
			}
			else
			{
				Template::set_message(lang('todo_edit_failure') . $this->todo_model->error, 'error');
			}
		}
		else if (isset($_POST['delete']))
		{
			$this->auth->restrict('Todo.Content.Delete');

			if ($this->todo_model->delete($id))
			{
				// Log the activity
				log_activity($this->current_user->id, lang('todo_act_delete_record') .': '. $id .' : '. $this->input->ip_address(), 'todo');

				Template::set_message(lang('todo_delete_success'), 'success');

				redirect(SITE_AREA .'/content/todo');
			}
			else
			{
				Template::set_message(lang('todo_delete_failure') . $this->todo_model->error, 'error');
			}
		}
        
       // Load comment thread id attached to content 
        $todo = $this->todo_model->find($id);
        
        $comments_thread_id = $todo->comments_thread_id;
        // Test if comment module exists and if so, load parsed content
        
        $comments = (in_array('comments',module_list(true))) ?     modules::run('comments/thread_view_with_form',$comments_thread_id) : '';
        // Set content to template
        Template::set('comment_form', $comments);
        
        // Count comments
        $comment_count = (in_array('comments',module_list(true))) ? modules::run('comments/count_comments',$comments_thread_id) : '';
        Template::set('comment_count', $comment_count);
        
		Template::set('todo', $this->todo_model->find($id));
		Template::set('toolbar_title', lang('todo_edit') .' Todo');
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
	private function save_todo($type='insert', $id=0)
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
        
		$data['list_id']      = $this->input->post('todo_list_id');
		$data['name']         = $this->input->post('todo_name');
		$data['notes']        = $this->input->post('todo_notes');
		$data['assigned_to']  = $this->input->post('todo_assigned_to');
		$data['due_by']       = $this->input->post('todo_due_by') ? $this->input->post('todo_due_by') : '0000-00-00';
        
        if ($type == 'insert'){
            
            $data['orig_due_by'] = $this->input->post('todo_due_by') ? $this->input->post('todo_due_by') : '0000-00-00'; 
            
            $thread_id = 0;
            if (in_array('comments',module_list(true))) 
            {
                if(!isset($this->comments_model)) 
                {
                    $this->load->model('comments/comments_model');
                }
                $thread_id = $this->comments_model->new_comments_thread('todo');
            }
            $data = $data + array('comments_thread_id'=>$thread_id,'created_by'=>$this->current_user->id, 'status'=>'Active');
        }

		if ($type == 'insert')
		{
			$id = $this->todo_model->insert($data);

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
            $data['status'] = $this->input->post('todo_status');

			$return = $this->todo_model->update($id, $data);
		}

		return $return;
	}

    
	//--------------------------------------------------------------------
<<<<<<< HEAD

	public function remove_attachment()
	{
		$id = $this->uri->segment(5);
		$success = (bool)false;

		// Handle a single-user purge
		if (!empty($id) && is_numeric($id))
		{
			$todo = $this->todo_model->find($id);
			if (isset($todo) && isset($todo->attachment))
			{
				$this->delete_attachments ( $todo->attachment );
				$data = array('attachment'=>'');
                $this->todo_model->skip_validation(TRUE);
				$success = $this->todo_model->update($id, $data);
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
=======
>>>>>>> f19371064a9ba4d3faff72c86b6ae2805aa04588
}