<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

/**
 * purchase_orders controller
 */
class purchase_orders extends Front_Controller
{

	//--------------------------------------------------------------------


	/**
	 * Constructor
	 *
	 * @return void
	 */
	public function __construct()
	{
		parent::__construct();

		$this->load->library('form_validation');
		$this->load->model('purchase_orders_model', null, true);
		$this->lang->load('purchase_orders');
		
			Assets::add_css('flick/jquery-ui-1.8.13.custom.css');
			Assets::add_js('jquery-ui-1.8.13.min.js');

		Assets::add_module_js('purchase_orders', 'purchase_orders.js');
	}

	//--------------------------------------------------------------------


	/**
	 * Displays a list of form data.
	 *
	 * @return void
	 */
	public function index()
	{

		$records = $this->purchase_orders_model->find_all();

		Template::set('records', $records);
		Template::render();
	}

	//--------------------------------------------------------------------

	public function po_tracker(){

        $po_docs = $this->purchase_orders_model->get_po_docs();
        
		$records = $this->purchase_orders_model->get_po_tracker();
        $this->load->model('activity_documents/activity_documents_model');
        
        $activity_docs = $this->activity_documents_model->get_activity_docs('PO');
        
		$data = array('records' => $records, 'po_docs' => $po_docs, 'activity_docs' => $activity_docs);

		return $this->load->view('content/po_tracker', $data, true);

	}    
	//--------------------------------------------------------------------

}