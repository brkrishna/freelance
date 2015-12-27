<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Factory_model extends BF_Model {

	protected $table_name	= "factory";
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
			"field"		=> "factory_no_of_emps",
			"label"		=> "Employee size",
			"rules"		=> "required|is_natural_no_zero"
		),
		array(
			"field"		=> "factory_name",
			"label"		=> "Name",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "factory_address",
			"label"		=> "Address",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "factory_m_cpcty",
			"label"		=> "Capacity per Month",
			"rules"		=> "required|is_natural_no_zero"
		),
		array(
			"field"		=> "factory_m_cpcty_uom",
			"label"		=> "Monthly UOM",
			"rules"		=> "required|is_natural_no_zero"
		),
		array(
			"field"		=> "factory_d_cpcty",
			"label"		=> "Capacity per Day",
			"rules"		=> "required|is_natural_no_zero"
		),
		array(
			"field"		=> "factory_d_cpcty_uom",
			"label"		=> "Daily UOM",
			"rules"		=> "required|is_natural_no_zero"
		),
		array(
			"field"		=> "factory_cpcty_raw_mtrl",
			"label"		=> "Capacity - Raw material",
			"rules"		=> "required|is_decimal|max_length[19]"
		),
		array(
			"field"		=> "factory_cpcty_storage",
			"label"		=> "Storage Capacity",
			"rules"		=> "required|is_decimal|max_length[19]"
		),
		array(
			"field"		=> "factory_near_port",
			"label"		=> "Nearest Port",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "factory_near_airport",
			"label"		=> "Nearest Airport",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "factory_near_city",
			"label"		=> "Nearest Major City",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "factory_transport_opt",
			"label"		=> "Transportation options",
			"rules"		=> ""
		),
		array(
			"field"		=> "factory_courier_comp",
			"label"		=> "Courier Company",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "factory_created_by",
			"label"		=> "Created By",
			"rules"		=> ""
		),
		array(
			"field"		=> "factory_profile_id",
			"label"		=> "Profile Id",
			"rules"		=> ""
		),
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;

	//--------------------------------------------------------------------
	public function find_all($profile_id = NULL)
	{
        if ($profile_id != null){
            $query = $this->db->select('id, name, address, no_of_emps, m_cpcty, m_cpcty_uom, d_cpcty, d_cpcty_uom, cpcty_raw_mtrl, cpcty_storage, near_port, near_city, near_airport, transport_opt, courier_comp, created_by, profile_id')
                                ->from('factory')
                                ->where('profile_id', $profile_id)
                                ->where('deleted', 0);
        }else{
            $query = $this->db->select('id, name, address, no_of_emps, m_cpcty, m_cpcty_uom, d_cpcty, d_cpcty_uom, cpcty_raw_mtrl, cpcty_storage, near_port, near_city, near_airport, transport_opt, courier_comp, created_by, profile_id')
                                ->from('factory')
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
	//--------------------------------------------------------------------

}
