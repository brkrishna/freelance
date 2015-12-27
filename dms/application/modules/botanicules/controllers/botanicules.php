<?php defined('BASEPATH') || exit('No direct script access allowed');

/**
 * Botanicules controller
 */
class Botanicules extends Front_Controller
{
    protected $permissionCreate = 'Botanicules.Botanicules.Create';
    protected $permissionDelete = 'Botanicules.Botanicules.Delete';
    protected $permissionEdit   = 'Botanicules.Botanicules.Edit';
    protected $permissionView   = 'Botanicules.Botanicules.View';

    /**
	 * Constructor
	 *
	 * @return void
	 */
	public function __construct()
	{
		parent::__construct();
		
		$this->load->model('botanicules/botanicules_model');
        $this->lang->load('botanicules');
		
        

		Assets::add_module_js('botanicules', 'botanicules.js');
	}

	/**
	 * Display a list of Botanicules data.
	 *
	 * @return void
	 */
	public function index()
	{
        
        
        
        
		$records = $this->botanicules_model->find_all();

		Template::set('records', $records);
        

		Template::render();
	}
    
}