<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Vendor_products_model extends BF_Model {

	protected $table_name	= "vendor_products";
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
			"field"		=> "vendor_products_vendor_id",
			"label"		=> "Vendor Id",
			"rules"		=> ""
		),
		array(
			"field"		=> "vendor_products_product_id",
			"label"		=> "Product Id",
			"rules"		=> "required|trim|is_natural_no_zero"
		),
		array(
			"field"		=> "vendor_products_created_by",
			"label"		=> "Created By",
			"rules"		=> ""
		),
		array(
			"field"		=> "vendor_products_profile_id",
			"label"		=> "Profile Id",
			"rules"		=> ""
		),
		array(
			"field"		=> "vendor_products_comments",
			"label"		=> "Comments",
			"rules"		=> "trim|max_length[4000]"
		),
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;


    //--------------------------------------------------------------------  
/*	public function find_all($profile_id)
	{
        if ($profile_id != null){
            $query = $this->db->select('id, vendor_id, product_id, comments, created_by, profile_id')
                                ->from('vendor_products')
                                ->where('profile_id', $profile_id)
                                ->where('deleted', 0);
        }else{
            $query = $this->db->select('id, vendor_id, product_id, comments, created_by, profile_id')
                                ->from('vendor_products')
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
    */
    //--------------------------------------------------------------------    

	public function get_vendor_products_select ($profile_id)
	{
        if ($profile_id != NULL){
            $query = $this->db->select('vendor_products.id, vendor_products.product_id, vendor_products.vendor_id, vendor_profile.name vendor_name, product.name product_name, product.desc product_desc')
                            ->from('vendor_products')
                            ->join('product', 'vendor_products.product_id = product.id')
                            ->join('vendor_profile', 'vendor_products.vendor_id = vendor_profile.id')
                            ->where('vendor_products.profile_id', $profile_id)
                            ->where('vendor_products.deleted', 0);
            
        }else{
            $query = $this->db->select('vendor_products.id, vendor_products.product_id, vendor_products.vendor_id, vendor_profile.name vendor_name, product.name product_name, product.desc product_desc')
                            ->from('vendor_products')
                            ->join('product', 'vendor_products.product_id = product.id')
                            ->join('vendor_profile', 'vendor_products.vendor_id = vendor_profile.id')
                            ->where('vendor_products.deleted', 0);
        }

        $query = $this->db->get();
		if ( $query->num_rows() <= 0 )
			return '';

		$option = array();
		$option['-1'] = 'Select one';
		foreach ($query->result() as $row)
		{
			$option[$row->id] = $row->product_name . ' - ' . $row->product_desc;
		}

		$query->free_result();

		return $option;
	}

	//--------------------------------------------------------------------

	public function get_vendor_products ($profile_id)
	{
        if ($profile_id != NULL){
            $query = $this->db->select('vendor_products.id, vendor_products.product_id, vendor_products.vendor_id, vendor_profile.name vendor_name, product.name product_name, product.desc product_desc')
                            ->from('vendor_products')
                            ->join('product', 'vendor_products.product_id = product.id')
                            ->join('vendor_profile', 'vendor_products.vendor_id = vendor_profile.id')
                            ->where('vendor_products.profile_id', $profile_id)
                            ->where('vendor_products.deleted', 0);
            
        }else{
            $query = $this->db->select('vendor_products.id, vendor_products.product_id, vendor_products.vendor_id, vendor_profile.name vendor_name, product.name product_name, product.desc product_desc')
                            ->from('vendor_products')
                            ->join('product', 'vendor_products.product_id = product.id')
                            ->join('vendor_profile', 'vendor_products.vendor_id = vendor_profile.id')
                            ->where('vendor_products.deleted', 0);
        }

        $query = $this->db->get();
		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
	}
}
