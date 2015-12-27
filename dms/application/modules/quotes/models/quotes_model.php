<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Quotes_model extends BF_Model {

	protected $table_name	= "quotes";
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
			"field"		=> "quotes_ref_no",
			"label"		=> "Reference No",
			"rules"		=> "required|max_length[255]"
		),
		array(
			"field"		=> "quotes_quote_dt",
			"label"		=> "Date Received",
			"rules"		=> "required"
		),
		array(
			"field"		=> "quotes_vendor_id",
			"label"		=> "Vendor",
			"rules"		=> "required|is_natural_no_zero"
		),
		array(
			"field"		=> "quotes_product_id",
			"label"		=> "Product",
			"rules"		=> "required|is_natural_no_zero"
		),
		array(
			"field"		=> "quotes_price",
			"label"		=> "Price",
			"rules"		=> "required|is_decimal|max_length[19]"
		),
		array(
			"field"		=> "quotes_tat",
			"label"		=> "Turn Around Time",
			"rules"		=> "required|integer"
		),
		array(
			"field"		=> "quotes_quantity",
			"label"		=> "Quantity",
			"rules"		=> "required|is_decimal|max_length[19]"
		),
		array(
			"field"		=> "quotes_uom_id",
			"label"		=> "UOM",
			"rules"		=> "required|is_natural_no_zero"
		),
		array(
			"field"		=> "quotes_attachment",
			"label"		=> "Attachment",
			"rules"		=> "max_length[4000]"
		),
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;

	//--------------------------------------------------------------------

	public function get_top_quotes($top = 3){

		$query = $this->db->select('quotes.id, quotes.ref_no, quotes.quantity, product.name product_name, product.desc product_desc, quotes.quote_dt, vendors.name vendor_name, uom.name uom_name, quotes.tat, quotes.price')
							->from('quotes')
							->join('vendors', 'quotes.vendor_id = vendors.id')
							->join('product', 'quotes.product_id = product.id')
							->join('uom', 'quotes.uom_id = uom.id');


		$query = $this->db->get();
							
		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
    }	
	
    //--------------------------------------------------------------------

}
