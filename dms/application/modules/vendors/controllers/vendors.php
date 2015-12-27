<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * vendors controller
 */
class vendors extends Front_Controller
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
		$this->load->model('vendors_model', null, true);
		$this->lang->load('vendors');
		

		Assets::add_module_js('vendors', 'vendors.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->vendors_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------



}