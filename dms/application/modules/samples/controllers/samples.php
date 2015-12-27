<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * samples controller
 */
class samples extends Front_Controller
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
		$this->load->model('samples_model', null, true);
		$this->lang->load('samples');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');

		Assets::add_module_js('samples', 'samples.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->samples_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------

	public function top_samples(){

		$records = $this->samples_model->get_top_samples();

		$data = array('records' => $records);

		return $this->load->view('content/top_samples', $data, true);

	}

}