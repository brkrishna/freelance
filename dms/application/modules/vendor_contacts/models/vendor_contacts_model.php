<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Vendor_contacts_model extends BF_Model {

	protected $table_name	= "vendor_contacts";
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
			"field"		=> "vendor_contacts_vendor_id",
			"label"		=> "Vendor Id",
			"rules"		=> ""
		),
		array(
			"field"		=> "vendor_contacts_name",
			"label"		=> "Name",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "vendor_contacts_dsgn",
			"label"		=> "Designation",
			"rules"		=> "max_length[255]"
		),
		array(
			"field"		=> "vendor_contacts_work_phone",
			"label"		=> "Office Phone",
			"rules"		=> "max_length[255]"
		),
		array(
			"field"		=> "vendor_contacts_cell_phone",
			"label"		=> "Cell Phone",
			"rules"		=> "max_length[255]"
		),
		array(
			"field"		=> "vendor_contacts_email_id",
			"label"		=> "Email",
			"rules"		=> "valid_email|max_length[255]"
		),
		array(
			"field"		=> "vendor_contacts_profile_id",
			"label"		=> "Profile Id",
			"rules"		=> ""
		),
		array(
			"field"		=> "vendor_contacts_created_by",
			"label"		=> "Created By",
			"rules"		=> ""
		),
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;

	//--------------------------------------------------------------------

	public function get_vendor_contacts($profile_id)
	{
        if ($profile_id != NULL){
            $query = $this->db->select('id, vendor_id, name, dsgn, work_phone, cell_phone, email_id')->get_where('vendor_contacts', array('profile_id'=>$profile_id, 'deleted'=>0));    
        }else{
            $query = $this->db->select('id, vendor_id, name, dsgn, work_phone, cell_phone, email_id')->get_where('vendor_contacts', array('deleted'=>0));    
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
            $query = $this->db->select('id, vendor_id, name, dsgn, work_phone, cell_phone, email_id, created_by, profile_id')
                                ->from('vendor_contacts')
                                ->where('profile_id', $profile_id)
                                ->where('deleted', 0);
        }else{
            $query = $this->db->select('id, vendor_id, name, dsgn, work_phone, cell_phone, email_id, created_by, profile_id')
                                ->from('vendor_contacts')
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
