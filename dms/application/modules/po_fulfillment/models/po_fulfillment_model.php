<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Po_fulfillment_model extends BF_Model {

	protected $table_name	= "po_fulfillment";
	protected $key			= "id";
	protected $soft_deletes	= false;
	protected $date_format	= "datetime";

	protected $log_user 	= FALSE;

	protected $set_created	= false;
	protected $set_modified = false;

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
			"field"		=> "po_fulfillment_po_no",
			"label"		=> "PO No",
			"rules"		=> "required|max_length[255]!is_natural_no_zero"
		),
		array(
			"field"		=> "po_fulfillment_vendor_id",
			"label"		=> "Vendor",
			"rules"		=> "required|is_natural_no_zero"
		),
		array(
			"field"		=> "po_fulfillment_product_id",
			"label"		=> "Product",
			"rules"		=> "required|is_natural_no_zero"
		),
		array(
			"field"		=> "po_fulfillment_qty",
			"label"		=> "Quantity",
			"rules"		=> "required|is_decimal|max_length[19]"
		),
		array(
			"field"		=> "po_fulfillment_uom_id",
			"label"		=> "UOM",
			"rules"		=> "required|is_natural_no_zero"
		),
		array(
			"field"		=> "po_fulfillment_rate",
			"label"		=> "Rate",
			"rules"		=> "required|is_decimal|max_length[19]"
		),
		array(
			"field"		=> "po_fulfillment_supply_from",
			"label"		=> "Supply from",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "po_fulfillment_dest_port",
			"label"		=> "Destination Port",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "po_fulfillment_packing_mode",
			"label"		=> "Mode of Packing",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "po_fulfillment_no_of_units",
			"label"		=> "No of Units",
			"rules"		=> "required|is_decimal|max_length[19]"
		),
		array(
			"field"		=> "po_fulfillment_created_by",
			"label"		=> "Created By",
			"rules"		=> ""
		),
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;

	//--------------------------------------------------------------------

}
