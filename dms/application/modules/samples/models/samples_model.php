<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Samples_model extends BF_Model {

	protected $table_name	= "samples";
	protected $key			= "id";
	protected $soft_deletes	= true;
	protected $date_format	= "datetime";

	protected $log_user 	= FALSE;

	protected $set_created	= true;
	protected $set_modified = true;
	protected $created_field = "created_on";
	protected $modified_field = "modified_on";

	/*
		Customize the operations of the model without recreating the insert, update,
		etc methods by adding the method names to act as callbacks here.
	 */
	protected $before_insert 	= array();
	protected $after_insert 	= array();
	protected $before_update 	= array();
	protected $after_update 	= array();
	protected $before_find 		= array();
	protected $after_find 		= array();
	protected $before_delete 	= array();
	protected $after_delete 	= array();

	/*
		For performance reasons, you may require your model to NOT return the
		id of the last inserted row as it is a bit of a slow method. This is
		primarily helpful when running big loops over data.
	 */
	protected $return_insert_id 	= TRUE;

	// The default type of element data is returned as.
	protected $return_type 			= "object";

	// Items that are always removed from data arrays prior to
	// any inserts or updates.
	protected $protected_attributes = array();

	/*
		You may need to move certain rules (like required) into the
		$insert_validation_rules array and out of the standard validation array.
		That way it is only required during inserts, not updates which may only
		be updating a portion of the data.
	 */
	protected $validation_rules 		= array(
		array(
			"field"		=> "samples_product_id",
			"label"		=> "Product",
			"rules"		=> "required|is_natural_no_zero"
		),
        array(
			"field"		=> "samples_po_no",
			"label"		=> "Po No",
			"rules"		=> "required|is_natural_no_zero"
		),
         array(
			"field"		=> "samples_party_type",
			"label"		=> "Party Type",
			"rules"		=> "required"
		),
         array(
			"field"		=> "samples_trans_type",
			"label"		=> "Trans Type",
			"rules"		=> "required"
		),
		array(
			"field"		=> "samples_quantity",
			"label"		=> "Quantity",
			"rules"		=> "max_length[19]|required|trim"
		),
		array(
			"field"		=> "samples_uom_id",
			"label"		=> "UOM",
			"rules"		=> "is_natural_no_zero"
		),
		array(
			"field"		=> "samples_party_name",
			"label"		=> "Party Name",
			"rules"		=> "required"
		),
		array(
			"field"		=> "samples_int_ref_num",
			"label"		=> "Internal Ref No",
			"rules"		=> "required|trim"
		),
		array(
			"field"		=> "samples_courier",
			"label"		=> "Courier",
			"rules"		=> "required|trim"
		),
		array(
			"field"		=> "samples_tracking_no",
			"label"		=> "Tracking No",
			"rules"		=> "required|trim"
		),
        array(
			"field"		=> "samples_date_received",
			"label"		=> "Date Received",
			"rules"		=> "required|trim"
		),
        array(
			"field"		=> "samples_comments",
			"label"		=> "Comments",
			"rules"		=> "trim|xss_clean"
		),        
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;

	//--------------------------------------------------------------------
	

	public function get_top_samples($top = 3){

		$query = $this->db->select('samples.id, samples.quantity, product.name product_name, product.desc product_desc, samples.date_received, vendor_profile.name vendor_profile_name, uom.name uom_name')
							->from('samples')
							->join('vendor_profile', 'samples.profile_id = profile.id')
							->join('product', 'samples.product_id = product.id')
							->join('uom', 'samples.uom_id = uom.id');


		$query = $this->db->get();
							
		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
    }	

    public function get_samples_select ( )
	{
		$query = $this->db->select('id, int_ref_num')->get('samples');

		if ( $query->num_rows() <= 0 )
			return '';

		$option = array();
		$option['-1'] = 'Select one';
		foreach ($query->result() as $row)
		{
			$option[$row->id ] = $row->int_ref_num;
		}

		$query->free_result();

		return $option;
	}

	//--------------------------------------------------------------------

	public function get_samples()
	{
		$query = $this->db->select('id, int_ref_num')->get('samples');

		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
	}

	//--------------------------------------------------------------------
	
}
