<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * po_fulfillment controller
 */
class po_fulfillment extends Front_Controller
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
		$this->load->model('po_fulfillment_model', null, true);
		$this->lang->load('po_fulfillment');
		

		Assets::add_module_js('po_fulfillment', 'po_fulfillment.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->po_fulfillment_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------



}