<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * todo_list controller
 */
class todo_list extends Front_Controller
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

		$this->load->library('form_validation');
		$this->load->model('todo_list_model', null, true);
		$this->lang->load('todo_list');
		

		Assets::add_module_js('todo_list', 'todo_list.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->todo_list_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------



}