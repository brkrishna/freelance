<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * uom controller
 */
class uom extends Front_Controller
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
		$this->load->model('uom_model', null, true);
		$this->lang->load('uom');
		

		Assets::add_module_js('uom', 'uom.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->uom_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------



}