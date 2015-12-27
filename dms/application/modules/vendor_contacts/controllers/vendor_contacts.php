<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * vendor_contacts controller
 */
class vendor_contacts extends Front_Controller
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
		$this->load->model('vendor_contacts_model', null, true);
		$this->lang->load('vendor_contacts');
		

		Assets::add_module_js('vendor_contacts', 'vendor_contacts.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->vendor_contacts_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------
	public function get_vendor_contacts(){

        $profile_id = NULL;
        
        if (isset($this->curr_user_profile['id'])){
            $profile_id = $this->curr_user_profile['id'];
        }
        
		$records = $this->vendor_contacts_model->get_vendor_contacts($profile_id);

        $data = array('records' => $records);    
        return $this->load->view('content/vendor_contacts', $data, true);    
	}



}