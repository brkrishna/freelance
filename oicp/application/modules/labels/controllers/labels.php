<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Content controller
 */
class Labels extends Admin_Controller
{
    protected $permissionCreate = 'Labels.Content.Create';
    protected $permissionDelete = 'Labels.Content.Delete';
    protected $permissionEdit   = 'Labels.Content.Edit';
    protected $permissionView   = 'Labels.Content.View';

    /**
	 * Constructor
	 *
	 * @return void
	 */
	public function __construct()
	{
		parent::__construct();
		
        $this->auth->restrict($this->permissionView);
		$this->load->model('labels/labels_model');
		$this->load->model(array('products/products_model', ));
        $this->lang->load('labels');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');
            $this->form_validation->set_error_delimiters("<span class='error'>", "</span>");
        
		$products_select = $this->products_model->get_products_select();
		Template::set('products_select', $products_select);

		$products = $this->products_model->get_products();
		Template::set('products', $products);
        
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('labels', 'labels.js');
	}

	/**
	 * Display a list of Labels data.
	 *
	 * @return void
	 */
    public function listing(){

        $records = $this->labels_model->get_labels();

        $data = array('records' => $records);

        return $this->load->view('content/listing', $data, true);

    }    
}