<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * customers controller
 */
class customers extends Front_Controller
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
		$this->load->model('customers_model', null, true);
		$this->lang->load('customers');
		

		Assets::add_module_js('customers', 'customers.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->customers_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------



}