<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Content controller
 */
class Reports extends Admin_Controller
{
    protected $permissionView   = 'Party_documents.Content.View';

    /**
     * Constructor
     *
     * @return void
     */
    public function __construct()
    {
        parent::__construct();
        
        $this->auth->restrict($this->permissionView);
        $this->load->model('party_documents/party_documents_model');
        $this->lang->load('party_documents');
        
            Assets::add_js('jquery-ui-1.8.13.min.js');
            $this->form_validation->set_error_delimiters("<span class='error'>", "</span>");
        
        Template::set_block('sub_nav', 'content/_sub_nav');

        Assets::add_module_js('party_documents', 'party_documents.js');
    }

    /**
     * Display a list of Party Documents data.
     *
     * @return void
     */
    public function index($offset = 0)
    {
        // Deleting anything?
        if (isset($_POST['delete'])) {
            $this->auth->restrict($this->permissionDelete);
            $checked = $this->input->post('checked');
            if (is_array($checked) && count($checked)) {

                // If any of the deletions fail, set the result to false, so
                // failure message is set if any of the attempts fail, not just
                // the last attempt

                $result = true;
                foreach ($checked as $pid) {
                    $deleted = $this->party_documents_model->delete($pid);
                    if ($deleted == false) {
                        $result = false;
                    }
                }
                if ($result) {
                    Template::set_message(count($checked) . ' ' . lang('party_documents_delete_success'), 'success');
                } else {
                    Template::set_message(lang('party_documents_delete_failure') . $this->party_documents_model->error, 'error');
                }
            }
        }
        
        
        $pagerUriSegment = 5;
        $pagerBaseUrl = site_url(SITE_AREA . '/reports/party_documents/index') . '/';
        
        $limit  = $this->settings_lib->item('site.list_limit') ?: 15;

        $this->load->library('pagination');
        $pager['base_url']    = $pagerBaseUrl;
        $pager['total_rows']  = $this->party_documents_model->count_all();
        $pager['per_page']    = $limit;
        $pager['uri_segment'] = $pagerUriSegment;

        $this->pagination->initialize($pager);
        $this->party_documents_model->limit($limit, $offset);

        $records = $this->party_documents_model->get_report();

        Template::set('records', $records);
        
        Template::set('toolbar_title', lang('party_documents_manage'));

        Template::render();
    }
    
 
}