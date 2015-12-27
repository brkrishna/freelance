<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Content controller
 */
class Party extends Admin_Controller
{
    protected $permissionCreate = 'Party.Content.Create';
    protected $permissionDelete = 'Party.Content.Delete';
    protected $permissionEdit   = 'Party.Content.Edit';
    protected $permissionView   = 'Party.Content.View';

    /**
     * Constructor
     *
     * @return void
     */
    public function __construct()
    {
        parent::__construct();
        
        $this->auth->restrict($this->permissionView);
        $this->load->model('party/party_model');
        $this->lang->load('party');
        
            $this->form_validation->set_error_delimiters("<span class='error'>", "</span>");
        
        Template::set_block('sub_nav', 'content/_sub_nav');

        Assets::add_module_js('party', 'party.js');
    }

    /**
     * Display a list of Party data.
     *
     * @return void
     */
    public function units(){

        $records = $this->party_model->find_all_by('type','Unit');

        $data = array('records' => $records);

        return $this->load->view('content/units', $data, true);

    }    

    public function vendors(){

        $records = $this->party_model->find_all_by('type','Vendor');

        $data = array('records' => $records);

        return $this->load->view('content/vendors', $data, true);

    }    

}