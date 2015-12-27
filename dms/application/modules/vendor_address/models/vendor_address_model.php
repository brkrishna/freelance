<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Vendor_address_model extends BF_Model {

	protected $table_name	= "vendor_address";
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
			"field"		=> "vendor_address_vendor_id",
			"label"		=> "Vendor",
			"rules"		=> ""
		),
		array(
			"field"		=> "vendor_address_loc_type",
			"label"		=> "Location Type",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "vendor_address_address1",
			"label"		=> "Address1",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "vendor_address_address2",
			"label"		=> "Address2",
			"rules"		=> "trim|max_length[255]"
		),
		array(
			"field"		=> "vendor_address_city",
			"label"		=> "City",
			"rules"		=> "trim|max_length[255]"
		),
		array(
			"field"		=> "vendor_address_country_id",
			"label"		=> "Country",
			"rules"		=> "required|trim|max_length[2]"
		),
		array(
			"field"		=> "vendor_address_office_phones",
			"label"		=> "Office Phones",
			"rules"		=> "max_length[255]"
		),
		array(
			"field"		=> "vendor_address_office_fax",
			"label"		=> "Office Fax",
			"rules"		=> "max_length[255]"
		),
		array(
			"field"		=> "vendor_address_profile_id",
			"label"		=> "Profile Id",
			"rules"		=> ""
		),
		array(
			"field"		=> "vendor_address_created_by",
			"label"		=> "Created By",
			"rules"		=> ""
		),
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;

	//--------------------------------------------------------------------
	public function get_vendor_address($profile_id)
	{
        if ($profile_id != NULL){
            $query = $this->db->select('id, vendor_id, loc_type, address1, address2')->get_where('vendor_address', array('profile_id'=>$profile_id, 'deleted'=>0));    
        }else{
            $query = $this->db->select('id, vendor_id, loc_type, address1, address2')->get_where('vendor_address', array('deleted'=>0));    
        }
		
		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
	}
    
	//--------------------------------------------------------------------
	public function find_all($profile_id = NULL)
	{
        if ($profile_id != null){
            $query = $this->db->select('id, vendor_id, loc_type, address1, address2, city, country_id, office_fax, office_phones, created_by, profile_id')
                                ->from('vendor_address')
                                ->where('profile_id', $profile_id)
                                ->where('deleted', 0);
        }else{
            $query = $this->db->select('id, vendor_id, loc_type, address1, address2, city, country_id, office_fax, office_phones, created_by, profile_id')
                                ->from('vendor_address')
                                ->where('deleted', 0);
        }

        $query = $this->db->get();
		if (!$query->num_rows())
		{
			return FALSE;
		}else{
            return $query->result();
        }

	}//end find_all()
    
}
