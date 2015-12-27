<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * profile controller
 */
class profile extends Authenticated_Controller
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
		$this->load->model('profile_model', null, true);
		//$this->lang->load('profile');
		

		Assets::add_module_js('profile', 'profile.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->profile_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------

	public function get_profile(){

		$records = $this->profile_model->get_profile($this->current_user->id);

        $data = array('records' => $records);    
        return $this->load->view('content/profile', $data, true);    
	}   
}