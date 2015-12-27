<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * containers controller
 */
class containers extends Front_Controller
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
		$this->load->model('containers_model', null, true);
		$this->lang->load('containers');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');

		Assets::add_module_js('containers', 'containers.js');

	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->containers_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------

	public function top_containers(){

		$records = $this->containers_model->get_top_containers();

		$data = array('records' => $records);

		return $this->load->view('content/top_containers', $data, true);

	}

}