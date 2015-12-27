<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * vendor_profile controller
 */
class vendor_profile extends Front_Controller
{

	//--------------------------------------------------------------------

    private $profile_id = NULL;
        

	/**
	 * Constructor
	 *
	 * @return void
	 */
	public function __construct()
	{
		parent::__construct();

		$this->load->library('form_validation');
		$this->load->model('vendor_profile_model', null, true);
		$this->lang->load('vendor_profile');
		

		Assets::add_module_js('vendor_profile', 'vendor_profile.js');
        
        if (isset($this->curr_user_profile['id'])){
            $this->profile_id = $this->curr_user_profile['id'];
        }
       
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->vendor_profile_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------

	public function get_vendor_profile(){

		$records = $this->vendor_profile_model->get_vendor_profile($this->profile_id);

        $data = array('records' => $records);    
        return $this->load->view('content/vendor_profile', $data, true);    
    }

    public function vendor_status(){

        $data = array();
        
        if ($this->profile_id == NULL){
        	$data['vendor_profile'] = '0';
        }else{
            $this->load->model(array('vendor_address/vendor_address_model', 'vendor_contacts/vendor_contacts_model', 'factory/factory_model', 'bank_details/bank_details_model'));
            
            $records = $this->vendor_profile_model->find_all_by(array('profile_id' => $this->profile_id, 'deleted' => 0));
            if ($records != NULL){
                foreach($records as $record){
                    $data['vendor_profile'] = $record->id;	
                }	
            }else{
                $data['vendor_profile'] = 0;	
            }

            
            $records = $this->vendor_address_model->find_all_by(array('profile_id' => $this->profile_id, 'deleted' => 0));

            
            foreach($records as $record){
                $data['vendor_address'] = $record->id;	
            }	
            
            $records = $this->vendor_contacts_model->find_all_by(array('profile_id' => $this->profile_id, 'deleted' => 0));
            
            if($records != NULL){
                foreach($records as $record){
                    $data['vendor_contacts'] = $record->id;	
                }	
            }else{
                $data['vendor_contacts'] = 0;
            }
            
            $records = $this->factory_model->find_all_by(array('profile_id' => $this->profile_id, 'deleted' => 0));

            if($records != NULL){
                foreach($records as $record){
                    $data['vendor_factory'] = $record->id;	
                }	
            }else{
                $data['vendor_factory'] = 0;
            }    

            $records = $this->bank_details_model->find_all_by(array('profile_id' => $this->profile_id, 'deleted' => 0));

            if ($records != NULL){
                foreach($records as $record){
                    $data['vendor_bank'] = $record->id;	
                }	
            }else{
                $data['vendor_bank'] = 0;
            }
        }
        
     	return $this->load->view('content/vendor_status', $data, true);       
    }
}