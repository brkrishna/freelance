<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * vendor_address controller
 */
class vendor_address extends Front_Controller
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
		$this->load->model('vendor_address_model', null, true);
		$this->lang->load('vendor_address');
		

		Assets::add_module_js('vendor_address', 'vendor_address.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->vendor_address_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------
	public function get_vendor_address(){

        $profile_id = NULL;
        
        if (isset($this->curr_user_profile['id'])){
            $profile_id = $this->curr_user_profile['id'];
        }
        
		$records = $this->vendor_address_model->get_vendor_address($profile_id);

        $data = array('records' => $records);    
        return $this->load->view('content/vendor_address', $data, true);    
	}


}