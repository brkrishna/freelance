<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * activity_type controller
 */
class activity_type extends Front_Controller
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
		$this->load->model('activity_type_model', null, true);
		$this->lang->load('activity_type');
		

		Assets::add_module_js('activity_type', 'activity_type.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->activity_type_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------



}