<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Content controller
 */
class Consignment_Documents extends Admin_Controller
{
    protected $permissionCreate = 'Consignment_documents.Content.Create';
    protected $permissionDelete = 'Consignment_documents.Content.Delete';
    protected $permissionEdit   = 'Consignment_documents.Content.Edit';
    protected $permissionView   = 'Consignment_documents.Content.View';

    /**
	 * Constructor
	 *
	 * @return void
	 */
	public function __construct()
	{
		parent::__construct();
		
        $this->auth->restrict($this->permissionView);
		$this->load->model('consignment_documents/consignment_documents_model');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');
            $this->form_validation->set_error_delimiters("<span class='error'>", "</span>");
        
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('consignment_documents', 'consignment_documents.js');
	}

	/**
	 * Display a list of Consignment Documents data.
	 *
	 * @return void
	 */
    public function listing(){

        $records = $this->consignment_documents_model->get_consign_docs();

        $data = array('records' => $records);

        return $this->load->view('content/listing', $data, true);

    }    
}