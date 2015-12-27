<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * sample_documents controller
 */
class sample_documents extends Front_Controller
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
		$this->load->model('sample_documents_model', null, true);
		$this->lang->load('sample_documents');
		

		Assets::add_module_js('sample_documents', 'sample_documents.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->sample_documents_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------



}