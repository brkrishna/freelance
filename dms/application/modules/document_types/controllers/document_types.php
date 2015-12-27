<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * document_types controller
 */
class document_types extends Front_Controller
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
		$this->load->model('document_types_model', null, true);
		$this->lang->load('document_types');
		

		Assets::add_module_js('document_types', 'document_types.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->document_types_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------



}