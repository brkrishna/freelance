<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Po_transactions_model extends BF_Model {

	protected $table_name	= "po_transactions";
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
			"field"		=> "po_transactions_po_ref",
			"label"		=> "PO Ref",
			"rules"		=> "required|max_length[255]"
		),
		array(
			"field"		=> "po_transactions_trans_type",
			"label"		=> "Transaction Type",
			"rules"		=> "required|max_length[255]"
		),
		array(
			"field"		=> "po_transactions_remit_date",
			"label"		=> "Date Remitted",
			"rules"		=> ""
		),
		array(
			"field"		=> "po_transactions_rcvd_date",
			"label"		=> "Date Received",
			"rules"		=> ""
		),
		array(
			"field"		=> "po_transactions_amount",
			"label"		=> "Amount",
			"rules"		=> "max_length[19]"
		),
		array(
			"field"		=> "po_transactions_vendor_id",
			"label"		=> "Vendor",
			"rules"		=> ""
		),
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;

	//--------------------------------------------------------------------

}
