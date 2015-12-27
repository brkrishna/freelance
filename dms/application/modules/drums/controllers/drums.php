<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * drums controller
 */
class drums extends Front_Controller
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
		$this->load->model('drums_model', null, true);
		$this->lang->load('drums');
		

		Assets::add_module_js('drums', 'drums.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->drums_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------



}