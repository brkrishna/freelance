<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Bank_details_model extends BF_Model {

	protected $table_name	= "bank_details";
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
			"field"		=> "bank_details_profile_id",
			"label"		=> "Profile Id",
			"rules"		=> ""
		),
		array(
			"field"		=> "bank_details_created_by",
			"label"		=> "Created By",
			"rules"		=> ""
		),
		array(
			"field"		=> "bank_details_bank_name",
			"label"		=> "Bank Name",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "bank_details_branch",
			"label"		=> "Address",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "bank_details_address",
			"label"		=> "Address",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "bank_details_account_type",
			"label"		=> "Account Type",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "bank_details_oper_curr",
			"label"		=> "Operating Currency",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "bank_details_accept_curr",
			"label"		=> "Accepted Currency",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "bank_details_swift_code",
			"label"		=> "Swift Code",
			"rules"		=> "max_length[255]"
		),
		array(
			"field"		=> "bank_details_micr",
			"label"		=> "MICR",
			"rules"		=> "max_length[255]"
		),
		array(
			"field"		=> "bank_details_ifsc",
			"label"		=> "IFSC",
			"rules"		=> "max_length[255]"
		),
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;

	//--------------------------------------------------------------------
	public function find_all($profile_id = NULL)
	{
        if ($profile_id != null){
            $query = $this->db->select('id, bank_name, branch, address, account_type, oper_curr, accept_curr, swift_code, micr, ifsc, created_by, profile_id')
                                ->from('bank_details')
                                ->where('profile_id', $profile_id)
                                ->where('deleted', 0);
        }else{
            $query = $this->db->select('id, bank_name, branch, address, account_type, oper_curr, accept_curr, swift_code, micr, ifsc, created_by, profile_id')
                                ->from('bank_details')
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
