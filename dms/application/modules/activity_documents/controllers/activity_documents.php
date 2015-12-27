<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * activity_documents controller
 */
class activity_documents extends Front_Controller
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
		$this->load->model('activity_documents_model', null, true);
		$this->lang->load('activity_documents');
		

		Assets::add_module_js('activity_documents', 'activity_documents.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->activity_documents_model->find_all();
       


		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------



}