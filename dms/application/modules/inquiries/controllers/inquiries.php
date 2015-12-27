<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * inquiries controller
 */
class inquiries extends Front_Controller
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
		$this->load->model('inquiries_model', null, true);
		$this->lang->load('inquiries');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');

		Assets::add_module_js('inquiries', 'inquiries.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->inquiries_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------

	public function top_inquiries(){

		$records = $this->inquiries_model->get_top_inquiries();

		$data = array('records' => $records);

		return $this->load->view('content/top_inquiries', $data, true);

	}    


}