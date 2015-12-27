<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Vendors_model extends BF_Model {

	protected $table_name	= "vendors";
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
			"field"		=> "vendors_name",
			"label"		=> "Name",
			"rules"		=> "required|unique[bf_vendors.name,bf_vendors.id]|max_length[255]"
		),
		array(
			"field"		=> "vendors_contact_name",
			"label"		=> "Contact Name",
			"rules"		=> "required|max_length[255]"
		),
		array(
			"field"		=> "vendors_contact_phone",
			"label"		=> "Contact Phone",
			"rules"		=> "required|max_length[255]"
		),
		array(
			"field"		=> "vendors_address1",
			"label"		=> "Address1",
			"rules"		=> "max_length[255]"
		),
		array(
			"field"		=> "vendors_address2",
			"label"		=> "Address2",
			"rules"		=> "max_length[255]"
		),
		array(
			"field"		=> "vendors_city",
			"label"		=> "City",
			"rules"		=> "max_length[255]"
		),
		array(
			"field"		=> "vendors_country",
			"label"		=> "Country",
			"rules"		=> "required"
		),
		array(
			"field"		=> "vendors_work_phones",
			"label"		=> "Office Phones",
			"rules"		=> "max_length[255]"
		),
		array(
			"field"		=> "vendors_contact_email",
			"label"		=> "contact_email",
			"rules"		=> "valid_email|max_length[255]"
		),
		array(
			"field"		=> "vendors_website_url",
			"label"		=> "Website URL",
			"rules"		=> "max_length[255]"
		),
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;

	//--------------------------------------------------------------------
	public function get_vendors_select ( )
	{
		$query = $this->db->select('id, name')->get('vendors');

		if ( $query->num_rows() <= 0 )
			return '';

		$option = array();
		$option['-1'] = 'Select one';
		foreach ($query->result() as $row)
		{
			$option[$row->id] = $row->name;
		}

		$query->free_result();

		return $option;
	}

	//--------------------------------------------------------------------

	public function get_vendors()
	{
		$query = $this->db->select('id, name')->get('vendors');

		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
	}

	//--------------------------------------------------------------------
}
