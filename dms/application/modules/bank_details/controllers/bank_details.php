<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * bank_details controller
 */
class bank_details extends Front_Controller
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
		$this->load->model('bank_details_model', null, true);
		$this->lang->load('bank_details');
		

		Assets::add_module_js('bank_details', 'bank_details.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->bank_details_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------



}