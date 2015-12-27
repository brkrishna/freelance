<?php defined('BASEPATH') || exit('No direct script access allowed');

class Labels_model extends BF_Model
{
    protected $table_name	= 'labels';
	protected $key			= 'id';
	protected $date_format	= 'datetime';

	protected $log_user 	= true;
	protected $set_created	= true;
	protected $set_modified = true;
	protected $soft_deletes	= true;

	protected $created_field     = 'created_on';
    protected $created_by_field  = 'created_by';
	protected $modified_field    = 'modified_on';
    protected $modified_by_field = 'modified_by';
    protected $deleted_field     = 'deleted';
    protected $deleted_by_field  = 'deleted_by';

	// Customize the operations of the model without recreating the insert,
    // update, etc. methods by adding the method names to act as callbacks here.
	protected $before_insert 	= array();
	protected $after_insert 	= array();
	protected $before_update 	= array();
	protected $after_update 	= array();
	protected $before_find 	    = array();
	protected $after_find 		= array();
	protected $before_delete 	= array();
	protected $after_delete 	= array();

	// For performance reasons, you may require your model to NOT return the id
	// of the last inserted row as it is a bit of a slow method. This is
    // primarily helpful when running big loops over data.
	protected $return_insert_id = true;

	// The default type for returned row data.
	protected $return_type = 'object';

	// Items that are always removed from data prior to inserts or updates.
	protected $protected_attributes = array();

	// You may need to move certain rules (like required) into the
	// $insert_validation_rules array and out of the standard validation array.
	// That way it is only required during inserts, not updates which may only
	// be updating a portion of the data.
	protected $validation_rules 		= array(
		array(
			'field' => 'product_id',
			'label' => 'lang:labels_field_product_id',
			'rules' => 'required|is_natural_no_zero|max_length[11]',
		),
		array(
			'field' => 'label',
			'label' => 'lang:labels_field_label',
			'rules' => 'required|trim|max_length[255]',
		),
		array(
			'field' => 'doc_name',
			'label' => 'lang:labels_field_doc_name',
			'rules' => 'required|trim|max_length[255]',
		),
		array(
			'field' => 'doc_file',
			'label' => 'lang:labels_field_doc_file',
			'rules' => 'max_length[4000]',
		),
		array(
			'field' => 'rcvd_on',
			'label' => 'lang:labels_field_rcvd_on',
			'rules' => 'trim|max_length[25]',
		),
		array(
			'field' => 'archive',
			'label' => 'lang:labels_field_archive',
			'rules' => 'max_length[255]',
		),
	);
	protected $insert_validation_rules  = array();
	protected $skip_validation 			= false;

    /**
     * Constructor
     *
     * @return void
     */
    public function __construct()
    {
        parent::__construct();
    }

	public function get_labels()
	{
		
		$query = $this->db->select('l.id, l.product_id, l.label, l.doc_name, l.doc_file, l.rcvd_on, p.name prod_name')
				->from('labels l')
				->join('products p', 'l.product_id = p.id')
				->order_by('l.label');

		$query = $this->db->get();

		
		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
	}    
}