<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * product_documents controller
 */
class product_documents extends Front_Controller
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
		$this->load->model('product_documents_model', null, true);
		$this->lang->load('product_documents');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');

		Assets::add_module_js('product_documents', 'product_documents.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->product_documents_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------
	public function get_product_docs_def(){

        $profile_id = NULL;
        
        if (isset($this->curr_user_profile['id'])){
            $profile_id = $this->curr_user_profile['id'];
        }
        
		$records = $this->product_documents_model->get_product_docs_def($profile_id);
        $docs = $this->product_documents_model->get_product_docs($profile_id);

        $data = array('records' => $records, 'docs'=>$docs);    
        return $this->load->view('content/product_documents', $data, true);    
	}



}