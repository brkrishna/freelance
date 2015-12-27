<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Vendor_profile_model extends BF_Model {

	protected $table_name	= "vendor_profile";
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
			"field"		=> "vendor_profile_name",
			"label"		=> "Name",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "vendor_profile_est_type",
			"label"		=> "Establishment Type",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "vendor_profile_est_const",
			"label"		=> "Constitution of Company",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "vendor_profile_est_start_yr",
			"label"		=> "Year of Establishment",
			"rules"		=> "required|is_numeric"
		),
		array(
			"field"		=> "vendor_profile_created_by",
			"label"		=> "User Id",
			"rules"		=> ""
		),
		array(
			"field"		=> "vendor_profile_profile_id",
			"label"		=> "Profile Id",
			"rules"		=> ""
		),
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;
    
    //--------------------------------------------------------------------    
    
    public function get_vendor_profile($profile_id)
	{
        if ($profile_id != NULL){
            $query = $this->db->select('id, name, est_type, est_const, est_start_yr, website, profile, ')->get_where('vendor_profile', array('profile_id'=>$profile_id, 'deleted'=>0));    
        }else{
            $query = $this->db->select('id, name, est_type, est_const, est_start_yr, website, profile, ')->get_where('vendor_profile', array('deleted'=>0));    
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
            $query = $this->db->select('id, name, est_type, est_const, est_start_yr, website, profile, created_by, profile_id')
                                ->from('vendor_profile')
                                ->where('profile_id', $profile_id)
                                ->where('deleted', 0);
        }else{
            $query = $this->db->select('id, name, est_type, est_const, est_start_yr, website, profile, created_by, profile_id')
                                ->from('vendor_profile')
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
    
	

	public function get_vendors_select ($profile_id = NULL)
	{
        if  ($profile_id != NULL){
            $query = $this->db->select('id, name')->get_where('vendor_profile', array('profile_id'=>$profile_id, 'deleted'=>0));    
        }else{
            $query = $this->db->select('id, name')->get_where('vendor_profile', array('deleted'=>0));    
        }    
		

		if ( $query->num_rows() <= 0 )
			return '';

		$option = array();
		foreach ($query->result() as $row)
		{
			$option[$row->id] = $row->name;
		}

		$query->free_result();

		return $option;
	}

	//--------------------------------------------------------------------

	public function get_vendors($profile_id = NULL)
	{
        if($profile_id != NULL){
            $query = $this->db->select('id, name')->get_where('vendor_profile', array('profile_id'=>$profile_id, 'deleted'=>0));    
        }else{
            $query = $this->db->select('id, name')->get_where('vendor_profile', array('deleted'=>0));
        }
		

		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
	}

	//--------------------------------------------------------------------
    
}
