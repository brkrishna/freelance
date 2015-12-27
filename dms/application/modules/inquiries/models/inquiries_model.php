<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Inquiries_model extends BF_Model {

	protected $table_name	= "inquiries";
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
			"field"		=> "inquiries_product",
			"label"		=> "Product",
			"rules"		=> "required|max_length[255]"
		),
		array(
			"field"		=> "inquiries_quantity",
			"label"		=> "Quantity",
			"rules"		=> "required|max_length[19]"
		),
		array(
			"field"		=> "inquiries_uom_id",
			"label"		=> "UOM",
			"rules"		=> "required"
		),
		array(
			"field"		=> "inquiries_required_by",
			"label"		=> "Required By",
			"rules"		=> ""
		),
		array(
			"field"		=> "inquiries_prod_spec",
			"label"		=> "Product Specifications",
			"rules"		=> "max_length[1000]"
		),
		array(
			"field"		=> "inquiries_quality_spec",
			"label"		=> "Quality Specifications",
			"rules"		=> "max_length[1000]"
		),
		array(
			"field"		=> "inquiries_packaging_spec",
			"label"		=> "Packaging Specifications",
			"rules"		=> "max_length[1000]"
		),
		array(
			"field"		=> "inquiries_priority",
			"label"		=> "Priority",
			"rules"		=> "required|max_length[50]"
		),
		array(
			"field"		=> "inquiries_status",
			"label"		=> "Status",
			"rules"		=> "max_length[50]"
		),
		array(
			"field"		=> "inquiries_comments",
			"label"		=> "Comments",
			"rules"		=> "max_length[1000]"
		),
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;

	//--------------------------------------------------------------------

	public function get_top_inquiries($top = 3){

		$query = $this->db->select('inquiries.id, inquiries.product, inquiries.quantity, uom.name uom_name, inquiries.required_by')
							->from('inquiries')
							->join('uom', 'inquiries.uom_id = uom.id')
                            ->order_by('inquiries.required_by');


		$query = $this->db->get();
							
		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
	}	    
}
