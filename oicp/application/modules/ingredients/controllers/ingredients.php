<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Content controller
 */
class Ingredients extends Admin_Controller
{
    protected $permissionCreate = 'Ingredients.Content.Create';
    protected $permissionDelete = 'Ingredients.Content.Delete';
    protected $permissionEdit   = 'Ingredients.Content.Edit';
    protected $permissionView   = 'Ingredients.Content.View';

    /**
     * Constructor
     *
     * @return void
     */
    public function __construct()
    {
        parent::__construct();
        
        $this->auth->restrict($this->permissionView);
        $this->load->model('ingredients/ingredients_model');
        $this->lang->load('ingredients');
        
            $this->form_validation->set_error_delimiters("<span class='error'>", "</span>");
        
        Template::set_block('sub_nav', 'content/_sub_nav');

        Assets::add_module_js('ingredients', 'ingredients.js');
    }

    /**
     * Display a list of Ingredients data.
     *
     * @return void
     */
    public function listing(){

        $records = $this->ingredients_model->get_ingredients_w_scope();

        $data = array('records' => $records);

        return $this->load->view('content/listing', $data, true);

    }    
}