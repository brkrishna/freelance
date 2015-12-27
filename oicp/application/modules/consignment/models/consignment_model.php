<?php defined('BASEPATH') || exit('No direct script access allowed');

class Consignment_model extends BF_Model
{
    protected $table_name	= 'consignment';
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
			'field' => 'c_date',
			'label' => 'lang:consignment_field_c_date',
			'rules' => 'required|max_length[25]',
		),
		array(
			'field' => 'ref_no',
			'label' => 'lang:consignment_field_ref_no',
			'rules' => 'required|unique[bf_consignment.ref_no,bf_consignment.id]|trim|max_length[255]',
		),
		array(
			'field' => 'narration',
			'label' => 'lang:consignment_field_narration',
			'rules' => 'trim|max_length[4000]',
		),
		array(
			'field' => 'archive',
			'label' => 'lang:consignment_field_archive',
			'rules' => 'trim|max_length[255]',
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

	//--------------------------------------------------------------------

    public function get_consign_select ( )
	{
		$query = $this->db->select('id, ref_no')->get('consignment');

		if ( $query->num_rows() <= 0 )
			return '';

		$option = array();
		$option['-1'] = 'Select one';
		foreach ($query->result() as $row)
		{
			$option[$row->id ] = $row->ref_no;
		}

		$query->free_result();

		return $option;
	}

	//--------------------------------------------------------------------

	public function get_consign()
	{
		$query = $this->db->select('id, ref_no, narration, c_date')->get('consignment');

		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
	}

	//--------------------------------------------------------------------       
}