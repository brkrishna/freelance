<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * todo controller
 */
class todo extends Front_Controller
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
		$this->load->model('todo_model', null, true);
		$this->lang->load('todo');
		
		Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
		Assets::add_js('jquery-ui-1.8.13.min.js');

		Assets::add_module_js('todo', 'todo.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->todo_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------

	public function top_todos(){

		$records = $this->todo_model->get_top_todos();

		$data = array('records' => $records);

		return $this->load->view('content/top_todos', $data, true);

	}    
	//--------------------------------------------------------------------



}