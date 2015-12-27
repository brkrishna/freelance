<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Content controller
 */
class Content extends Admin_Controller
{
    protected $permissionCreate = 'Product_ingredients.Content.Create';
    protected $permissionDelete = 'Product_ingredients.Content.Delete';
    protected $permissionEdit   = 'Product_ingredients.Content.Edit';
    protected $permissionView   = 'Product_ingredients.Content.View';

    /**
	 * Constructor
	 *
	 * @return void
	 */
	public function __construct()
	{
		parent::__construct();
		
        $this->auth->restrict($this->permissionView);
		$this->load->model('product_ingredients/product_ingredients_model');
        $this->load->model(array('products/products_model', 'ingredients/ingredients_model'));
        $this->lang->load('product_ingredients');
		
            $this->form_validation->set_error_delimiters("<span class='error'>", "</span>");
        
		Template::set_block('sub_nav', 'content/_sub_nav');

		Assets::add_module_js('product_ingredients', 'product_ingredients.js');

        $products_select = $this->products_model->get_products_select();
        Template::set('products_select', $products_select);

        $products = $this->products_model->get_products();
        Template::set('products', $products);

        $ingredients_select = $this->ingredients_model->get_ingredients_select();
        Template::set('ingredients_select', $ingredients_select);

        $ingredients = $this->ingredients_model->get_ingredients();
        Template::set('ingredients', $ingredients);
	}

	/**
	 * Display a list of Product Ingredients data.
	 *
	 * @return void
	 */
	public function index()
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
					$deleted = $this->product_ingredients_model->delete($pid);
                    if ($deleted == false) {
                        $result = false;
                    }
				}
				if ($result) {
					Template::set_message(count($checked) . ' ' . lang('product_ingredients_delete_success'), 'success');
				} else {
					Template::set_message(lang('product_ingredients_delete_failure') . $this->product_ingredients_model->error, 'error');
				}
			}
		}
        
        
        
		$records = $this->product_ingredients_model->order_by('product_id, ingredient_id')->find_all();

		Template::set('records', $records);
        
    Template::set('toolbar_title', lang('product_ingredients_manage'));

		Template::render();
	}
    
    /**
	 * Create a Product Ingredients object.
	 *
	 * @return void
	 */
	public function create()
	{
		$this->auth->restrict($this->permissionCreate);
        
		if (isset($_POST['save'])) {
			if ($insert_id = $this->save_product_ingredients()) {
				log_activity($this->auth->user_id(), lang('product_ingredients_act_create_record') . ': ' . $insert_id . ' : ' . $this->input->ip_address(), 'product_ingredients');
				Template::set_message(lang('product_ingredients_create_success'), 'success');

				redirect(SITE_AREA . '/content/product_ingredients');
			}

            // Not validation error
			if ( ! empty($this->product_ingredients_model->error)) {
				Template::set_message(lang('product_ingredients_create_failure') . $this->product_ingredients_model->error, 'error');
            }
		}

		Template::set('toolbar_title', lang('product_ingredients_action_create'));

		Template::render();
	}
	/**
	 * Allows editing of Product Ingredients data.
	 *
	 * @return void
	 */
	public function edit()
	{
		$id = $this->uri->segment(5);
		if (empty($id)) {
			Template::set_message(lang('product_ingredients_invalid_id'), 'error');

			redirect(SITE_AREA . '/content/product_ingredients');
		}
        
		if (isset($_POST['save'])) {
			$this->auth->restrict($this->permissionEdit);

			if ($this->save_product_ingredients('update', $id)) {
				log_activity($this->auth->user_id(), lang('product_ingredients_act_edit_record') . ': ' . $id . ' : ' . $this->input->ip_address(), 'product_ingredients');
				Template::set_message(lang('product_ingredients_edit_success'), 'success');
				redirect(SITE_AREA . '/content/product_ingredients');
			}

            // Not validation error
            if ( ! empty($this->product_ingredients_model->error)) {
                Template::set_message(lang('product_ingredients_edit_failure') . $this->product_ingredients_model->error, 'error');
			}
		}
        
		elseif (isset($_POST['delete'])) {
			$this->auth->restrict($this->permissionDelete);

			if ($this->product_ingredients_model->delete($id)) {
				log_activity($this->auth->user_id(), lang('product_ingredients_act_delete_record') . ': ' . $id . ' : ' . $this->input->ip_address(), 'product_ingredients');
				Template::set_message(lang('product_ingredients_delete_success'), 'success');

				redirect(SITE_AREA . '/content/product_ingredients');
			}

            Template::set_message(lang('product_ingredients_delete_failure') . $this->product_ingredients_model->error, 'error');
		}
        
        Template::set('product_ingredients', $this->product_ingredients_model->find($id));

		Template::set('toolbar_title', lang('product_ingredients_edit_heading'));
		Template::render();
	}

	//--------------------------------------------------------------------
	// !PRIVATE METHODS
	//--------------------------------------------------------------------

	/**
	 * Save the data.
	 *
	 * @param string $type Either 'insert' or 'update'.
	 * @param int	 $id	The ID of the record to update, ignored on inserts.
	 *
	 * @return bool|int An int ID for successful inserts, true for successful
     * updates, else false.
	 */
	private function save_product_ingredients($type = 'insert', $id = 0)
	{
		if ($type == 'update') {
			$_POST['id'] = $id;
		}

        // Validate the data
        $this->form_validation->set_rules($this->product_ingredients_model->get_validation_rules());
        if ($this->form_validation->run() === false) {
            return false;
        }

		// Make sure we only pass in the fields we want
		
		$data = $this->product_ingredients_model->prep_data($this->input->post());

        // Additional handling for default values should be added below,
        // or in the model's prep_data() method
        

        $return = false;
		if ($type == 'insert') {
			$id = $this->product_ingredients_model->insert($data);

			if (is_numeric($id)) {
				$return = $id;
			}
		} elseif ($type == 'update') {
			$return = $this->product_ingredients_model->update($id, $data);
		}

		return $return;
	}
}