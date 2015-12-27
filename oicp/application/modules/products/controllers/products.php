<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Content controller
 */
class Products extends Admin_Controller
{
    protected $permissionCreate = 'Products.Content.Create';
    protected $permissionDelete = 'Products.Content.Delete';
    protected $permissionEdit   = 'Products.Content.Edit';
    protected $permissionView   = 'Products.Content.View';

    /**
	 * Constructor
	 *
	 * @return void
	 */
	public function __construct()
	{
		parent::__construct();
		
        $this->auth->restrict($this->permissionView);
		$this->load->model('products/products_model');
        $this->lang->load('products');
		
            $this->form_validation->set_error_delimiters("<span class='error'>", "</span>");
        
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('products', 'products.js');
	}

	/**
	 * Display a list of Products data.
	 *
	 * @return void
	 */
  

	public function listing(){

		$records = $this->products_model->get_products();

		$data = array('records' => $records);

		return $this->load->view('content/listing', $data, true);

	}    
}