<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Content controller
 */
class Party_Documents extends Admin_Controller
{
    protected $permissionCreate = 'Party_documents.Content.Create';
    protected $permissionDelete = 'Party_documents.Content.Delete';
    protected $permissionEdit   = 'Party_documents.Content.Edit';
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
        $this->load->model(array('products/products_model', 'party/party_model', 'ingredients/ingredients_model'));
        $this->lang->load('party_documents');
        
        Assets::add_js('jquery-ui-1.8.13.min.js');
        $this->form_validation->set_error_delimiters("<span class='error'>", "</span>");
        
        Template::set_block('sub_nav', 'content/_sub_nav');

        Assets::add_module_js('party_documents', 'party_documents.js');

        $products_select = $this->products_model->get_products_select();
        Template::set('products_select', $products_select);

        $products = $this->products_model->get_products();
        Template::set('products', $products);

        $party_select = $this->party_model->get_party_select();
        Template::set('party_select', $party_select);

        $party = $this->party_model->get_party();
        Template::set('party', $party);

        $ingredients_select = $this->ingredients_model->get_ingredients_select();
        Template::set('ingredients_select', $ingredients_select);

        $ingredients = $this->ingredients_model->get_ingredients();
        Template::set('ingredients', $ingredients);
    }

    /**
     * Display a list of Party Documents data.
     *
     * @return void
     */

}