<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Profile_model extends BF_Model {

	protected $table_name	= "profile";
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
			"field"		=> "profile_org_name",
			"label"		=> "Organization Name",
			"rules"		=> "required|trim|max_length[255]"
		),
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;

	//--------------------------------------------------------------------

	public function get_profile($user_id)
	{
		$query = $this->db->select('id, org_name')->get_where('profile', array('created_by'=>$user_id));

		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
	}

	//--------------------------------------------------------------------
    
	public function find_all($user_id = NULL)
	{
        if ($user_id != null){
            $query = $this->db->select('profile.id, profile.org_name, users.username created_by')
                                ->from('profile')
                                ->join('users', 'profile.created_by = users.id')
                                ->where('created_by', $user_id);
        }else{
            $query = $this->db->select('profile.id, profile.org_name, users.username created_by')
                                ->from('profile')
                                ->join('users', 'profile.created_by = users.id');
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
	public function find($user_id)
	{
        if ($user_id != null){
            $query = $this->db->select('profile.id, profile.org_name, users.username created_by')
                                ->from('profile')
                                ->join('users', 'profile.created_by = users.id')
                                ->where('created_by', $user_id);
        }else{
            return null;
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
