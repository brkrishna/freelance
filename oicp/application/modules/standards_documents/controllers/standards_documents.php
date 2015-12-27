<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Content controller
 */
class Standards_Documents extends Admin_Controller
{
    protected $permissionCreate = 'Standards_documents.Content.Create';
    protected $permissionDelete = 'Standards_documents.Content.Delete';
    protected $permissionEdit   = 'Standards_documents.Content.Edit';
    protected $permissionView   = 'Standards_documents.Content.View';

    /**
     * Constructor
     *
     * @return void
     */
    public function __construct()
    {
        parent::__construct();
        
        $this->auth->restrict($this->permissionView);
        $this->load->model('standards_documents/standards_documents_model');
        $this->lang->load('standards_documents');
        
            $this->form_validation->set_error_delimiters("<span class='error'>", "</span>");
        
        Template::set_block('sub_nav', 'content/_sub_nav');

        Assets::add_module_js('standards_documents', 'standards_documents.js');
    }

    /**
     * Display a list of Standards Documents data.
     *
     * @return void
     */

    public function listing(){

        $records = $this->standards_documents_model->get_std_documents();

        $data = array('records' => $records);

        return $this->load->view('content/listing', $data, true);

    }    
}