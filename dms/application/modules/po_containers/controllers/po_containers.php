<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * po_containers controller
 */
class po_containers extends Front_Controller
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
		$this->load->model('po_containers_model', null, true);
		$this->lang->load('po_containers');
		

		Assets::add_module_js('po_containers', 'po_containers.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->po_containers_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------



}