<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * quotes controller
 */
class quotes extends Front_Controller
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
		$this->load->model('quotes_model', null, true);
		$this->lang->load('quotes');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');

		Assets::add_module_js('quotes', 'quotes.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->quotes_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------

	public function top_sample_quotes(){

		$records = $this->quotes_model->get_top_sample_quotes();

		$data = array('records' => $records);

		return $this->load->view('content/top_sample_quotes', $data, true);

	}


}