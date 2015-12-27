<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Botan_structure controller
 */
class Botan_structure extends Front_Controller
{
    protected $permissionCreate = 'Botan_structure.Botan_structure.Create';
    protected $permissionDelete = 'Botan_structure.Botan_structure.Delete';
    protected $permissionEdit   = 'Botan_structure.Botan_structure.Edit';
    protected $permissionView   = 'Botan_structure.Botan_structure.View';

    /**
	 * Constructor
	 *
	 * @return void
	 */
	public function __construct()
	{
		parent::__construct();
		
		$this->load->model('botan_structure/botan_structure_model');
        $this->lang->load('botan_structure');
		
        

		Assets::add_module_js('botan_structure', 'botan_structure.js');
	}

	/**
	 * Display a list of Botan Structure data.
	 *
	 * @return void
	 */
	public function index()
	{
        
        
        
        
		$records = $this->botan_structure_model->find_all();

		Template::set('records', $records);
        

		Template::render();
	}
    
}