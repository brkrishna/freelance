<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * factory controller
 */
class factory extends Front_Controller
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
		$this->load->model('factory_model', null, true);
		$this->lang->load('factory');
		

		Assets::add_module_js('factory', 'factory.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->factory_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------



}