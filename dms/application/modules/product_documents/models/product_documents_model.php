
<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Product_documents_model extends BF_Model {

	protected $table_name	= "product_documents";
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
			"field"		=> "product_documents_vendor_id",
			"label"		=> "Vendor",
			"rules"		=> "required|trim|is_natural_no_zero"
		),
		array(
			"field"		=> "product_documents_product_id",
			"label"		=> "Product",
			"rules"		=> "required|trim|is_natural_no_zero"
		),
		array(
			"field"		=> "product_documents_document_id",
			"label"		=> "Document",
			"rules"		=> "required|trim|is_natural_no_zero"
		),
		array(
			"field"		=> "product_documents_issue_auth",
			"label"		=> "Issuing Authority",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "product_documents_issued_on",
			"label"		=> "Issued on",
			"rules"		=> "required|trim"
		),
		array(
			"field"		=> "product_documents_valid_till",
			"label"		=> "Valid Till",
			"rules"		=> "required|trim"
		),
		array(
			"field"		=> "product_documents_profile_id",
			"label"		=> "Profile Id",
			"rules"		=> ""
		),
		array(
			"field"		=> "product_documents_created_by",
			"label"		=> "Created by",
			"rules"		=> ""
		),
		array(
			"field"		=> "product_documents_place_of_origin",
			"label"		=> "Place of Origin",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "product_documents_comments",
			"label"		=> "Comments",
			"rules"		=> "max_length[4000]"
		),
		array(
			"field"		=> "attachment",
			"label"		=> "Attachment",
			"rules"		=> "required|max_length[4000]"
		),
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;

	//--------------------------------------------------------------------
/*	public function find_all($profile_id)
	{
        if ($profile_id != null){
            $query = $this->db->select('id, vendor_id, activity_code, product_id, document_id, issue_auth, issued_on, valid_till, place_of_origin, attachment, comments, created_by, profile_id')
                                ->from('product_documents')
                                ->where('profile_id', $profile_id)
                                ->where('deleted', 0);
        }else{
            $query = $this->db->select('id, vendor_id, activity_code, product_id, document_id, issue_auth, issued_on, valid_till, place_of_origin, attachment, comments, created_by, profile_id')
                                ->from('product_documents')
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
    public function get_product_documents ($profile_id)
	{
        if ($profile_id != NULL){
            $query = $this->db->select('product_documents.id, vendor_products.product_id, vendor_products.vendor_id, vendor_profile.name vendor_name, product.name product_name, product.desc product_desc')
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
    //--------------------------------------------------------------------
    public function get_product_docs_def ($profile_id)
	{
        if ($profile_id != NULL){
            $query = $this->db->select('vendor_products.id, activity_documents.document_id, activity_documents.product_id, document_types.name document_name, product.name product_name, product.desc product_desc')
                ->from('vendor_products')
                ->join('activity_documents', 'vendor_products.product_id = activity_documents.product_id', 'right outer')
                ->join('product', 'activity_documents.product_id = product.id')
                ->join('document_types', 'activity_documents.document_id = document_types.id')
                ->where('vendor_products.profile_id', $profile_id)
                ->where('activity_documents.activity_code', 'VE')
                ->order_by('activity_documents.product_id, activity_documents.document_id');
        }else{
            $query = $this->db->select('vendor_products.id, activity_documents.document_id, activity_documents.product_id, document_types.name document_name, product.name product_name, product.desc product_desc')
                ->from('vendor_products')
                ->join('activity_documents', 'vendor_products.product_id = activity_documents.product_id', 'right outer')
                ->join('product', 'activity_documents.product_id = product.id')
                ->join('document_types', 'activity_documents.document_id = document_types.id')
                ->where('activity_documents.activity_code', 'VE')
                ->order_by('activity_documents.product_id, activity_documents.document_id');
            
        }
            
        $query = $this->db->get();
		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
	}        
    //--------------------------------------------------------------------
    
    public function get_product_docs($profile_id){
        
        if ($profile_id != NULL){
            $query = $this->db->select('product_documents.id, product_documents.product_id, product_documents.vendor_id, product_documents.document_id, product_documents.attachment ')
                            ->from('product_documents')
                            ->where('product_documents.profile_id', $profile_id)
                            ->where('product_documents.deleted', 0)
                            ->order_by('product_documents.vendor_id, product_documents.product_id, product_documents.id');
            
        }else{
            $query = $this->db->select('product_documents.id, product_documents.product_id, product_documents.vendor_id, product_documents.document_id, product_documents.attachment ')
                            ->from('product_documents')
                            ->where('product_documents.deleted', 0)         
                            ->order_by('product_documents.vendor_id, product_documents.product_id, product_documents.id');
        }
        
        $query = $this->db->get();
		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
        
    }
    //--------------------------------------------------------------------
    public function get_product_docs_def_by_vendor($vendor_id)
	{
        if ($vendor_id != NULL){
            $query = $this->db->select('vendor_products.id, activity_documents.document_id, activity_documents.product_id, document_types.name document_name, product.name product_name, product.desc product_desc')
                ->from('vendor_products')
                ->join('activity_documents', 'vendor_products.product_id = activity_documents.product_id', 'right outer')
                ->join('product', 'activity_documents.product_id = product.id')
                ->join('document_types', 'activity_documents.document_id = document_types.id')
                ->where('vendor_products.vendor_id', $vendor_id)
                ->where('activity_documents.activity_code', 'VE')
                ->order_by('activity_documents.product_id, activity_documents.document_id');
        }else{
            return NULL;
        }
            
        $query = $this->db->get();
		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
	}        
    //--------------------------------------------------------------------
    public function get_product_docs_by_vendor($vendor_id){
        
        if ($vendor_id != NULL){
            $query = $this->db->select('product_documents.id, product_documents.product_id, product_documents.vendor_id, product_documents.document_id, product_documents.attachment ')
                            ->from('product_documents')
                            ->where('product_documents.vendor_id', $vendor_id)
                            ->where('product_documents.deleted', 0)
                            ->order_by('product_documents.vendor_id, product_documents.product_id, product_documents.id');
            
        }else{
            return NULL;
        }
        
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
