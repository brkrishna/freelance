<?php defined('BASEPATH') || exit('No direct script access allowed');

class Party_documents_model extends BF_Model
{
    protected $table_name	= 'party_documents';
	protected $key			= 'id';
	protected $date_format	= 'datetime';

	protected $log_user 	= false;
	protected $set_created	= false;
	protected $set_modified = false;
	protected $soft_deletes	= false;


	// Customize the operations of the model without recreating the insert,
    // update, etc. methods by adding the method names to act as callbacks here.
	protected $before_insert 	= array();
	protected $after_insert 	= array();
	protected $before_update 	= array();
	protected $after_update 	= array();
	protected $before_find 	    = array();
	protected $after_find 		= array();
	protected $before_delete 	= array();
	protected $after_delete 	= array();

	// For performance reasons, you may require your model to NOT return the id
	// of the last inserted row as it is a bit of a slow method. This is
    // primarily helpful when running big loops over data.
	protected $return_insert_id = true;

	// The default type for returned row data.
	protected $return_type = 'object';

	// Items that are always removed from data prior to inserts or updates.
	protected $protected_attributes = array();

	// You may need to move certain rules (like required) into the
	// $insert_validation_rules array and out of the standard validation array.
	// That way it is only required during inserts, not updates which may only
	// be updating a portion of the data.
	protected $validation_rules 		= array(
		array(
			'field' => 'party_id',
			'label' => 'lang:party_documents_field_party_id',
			'rules' => 'required|is_natural_no_zero',
		),
		array(
			'field' => 'product_id',
			'label' => 'lang:party_documents_field_product_id',
			'rules' => 'required|is_natural_no_zero',
		),
        array(
            'field' => 'catg',
            'label' => 'lang:party_documents_field_catg',
            'rules' => 'trim|max_length[255]',
        ),    
        array(
            'field' => 'cert_type',
            'label' => 'lang:party_documents_field_cert_type',
            'rules' => 'trim|max_length[255]',
        ),
		array(
			'field' => 'doc_name',
			'label' => 'lang:party_documents_field_doc_name',
			'rules' => 'required|trim|max_length[255]',
		),
		array(
			'field' => 'doc_file',
			'label' => 'lang:party_documents_field_doc_file',
			'rules' => 'required|max_length[4000]',
		),
		array(
			'field' => 'rcvd_on',
			'label' => 'lang:party_documents_field_rcvd_on',
			'rules' => 'required|max_length[50]',
		),
		array(
			'field' => 'comments',
			'label' => 'lang:party_documents_field_comments',
			'rules' => 'trim|max_length[4000]',
		),
		array(
			'field' => 'archive',
			'label' => 'lang:party_documents_field_archive',
			'rules' => 'required|trim|max_length[25]',
		),
	);
	protected $insert_validation_rules  = array();
	protected $skip_validation 			= false;

    /**
     * Constructor
     *
     * @return void
     */
    public function __construct()
    {
        parent::__construct();
    }

	//--------------------------------------------------------------------

	public function get_product_docs($product_id = 0)
	{
		if ($product_id != 0){
			$query = $this->db->select('p.id, p.type, p.org_name, i.name ing_name, pr.name prod_name, pd.doc_name, pd.doc_file, pd.rcvd_on, pd.comments')
					->from('party p')
					->join('party_documents pd', 'p.id = pd.party_id')	
					->join('products pr', 'pd.product_id = pr.id')
                    ->join('ingredients i', 'pd.ingredient_id = i.id', 'LEFT')
					->where('pd.product_id', $product_id)
					->order_by('p.type, p.org_name, pd.doc_name');

			$query = $this->db->get();
		}else{
			return 0;
		}
		
		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
	}

	//--------------------------------------------------------------------    

    public function get_party_docs($party_id = 0)
    {
        if ($party_id != 0){
            $query = $this->db->select('p.id, p.type, p.org_name, p.address, p.city, p.pincode, p.country, i.name ing_name, pr.name prod_name, pd.doc_name, pd.doc_file, pd.rcvd_on, pd.comments')
                    ->from('party p')
                    ->join('party_documents pd', 'p.id = pd.party_id')  
                    ->join('products pr', 'pd.product_id = pr.id')
                    ->join('ingredients i', 'pd.ingredient_id = i.id', 'LEFT')
                    ->where('pd.party_id', $party_id)
                    ->order_by('p.type, p.org_name, pd.doc_name');

            $query = $this->db->get();
        }else{
            return 0;
        }
        
        if ($query->num_rows() > 0)
        {
            return $query->result();
        } else {
            return null;
        }
    }

    //--------------------------------------------------------------------    

    public function get_ingre_docs($ingre_id = 0)
    {
        if ($ingre_id != 0){
            $query = $this->db->select('p.type, p.org_name, i.name ing_name, pr.name prod_name, pd.doc_name, pd.doc_file, pd.rcvd_on, pd.comments')
                    ->from('party p')
                    ->join('party_documents pd', 'p.id = pd.party_id')  
                    ->join('products pr', 'pd.product_id = pr.id')
                    ->join('ingredients i', 'pd.ingredient_id = i.id', 'LEFT')
                    ->where('i.id', $ingre_id)
                    ->order_by('p.type, p.org_name, pd.doc_name');

            $query = $this->db->get();
        }else{
            return 0;
        }
        
        if ($query->num_rows() > 0)
        {
            return $query->result();
        } else {
            return null;
        }
    }

    //--------------------------------------------------------------------        

    public function get_report()
    {
        $query = $this->db->select('p.name prod_name, i.classification, i.name ing_name, pa.org_name, pd.catg, pd.cert_type, pd.doc_name, pd.doc_file, pd.rcvd_on, pd.comments, pd.archive')
                ->from('products p')
                ->join('product_ingredients pi', 'p.id = pi.product_id', 'LEFT')  
                ->join('ingredients i', 'pi.ingredient_id = i.id', 'LEFT')
                ->join('party_documents pd', 'pi.product_id = pd.product_id and pi.ingredient_id = pd.ingredient_id and pd.doc_name = "Scope Certificate"', 'LEFT')
                ->join('party pa', 'pd.party_id = pa.id', 'LEFT')
                ->where('p.name <> "NA"')
                ->order_by('p.name, i.classification, i.name, pa.org_name, pd.catg, pd.cert_type, pd.doc_name');

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