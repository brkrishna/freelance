<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Purchase_orders_model extends BF_Model {

	protected $table_name	= "purchase_orders";
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
			"field"		=> "purchase_orders_po_no",
			"label"		=> "PO No",
			"rules"		=> "required|unique[bf_purchase_orders.po_no,bf_purchase_orders.id]|trim|max_length[255]"
		),
		array(
			"field"		=> "purchase_orders_po_dt",
			"label"		=> "PO Date",
			"rules"		=> "required"
		),
		array(
			"field"		=> "purchase_orders_product_id",
			"label"		=> "Product",
			"rules"		=> "required|is_natural_no_zero"
		),
		array(
			"field"		=> "purchase_orders_qty",
			"label"		=> "Quantity",
			"rules"		=> "required|is_decimal|max_length[19]"
		),
		array(
			"field"		=> "purchase_orders_uom_id",
			"label"		=> "UOM",
			"rules"		=> "required|is_natural_no_zero"
		),
		array(
			"field"		=> "purchase_orders_rate",
			"label"		=> "Rate",
			"rules"		=> "required|is_decimal|max_length[19]"
		),
		array(
			"field"		=> "purchase_orders_packing_mode",
			"label"		=> "Mode of Packing",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "purchase_orders_no_of_units",
			"label"		=> "No of Units",
			"rules"		=> "required|is_decimal|max_length[19]"
		),
		array(
			"field"		=> "purchase_orders_created_by",
			"label"		=> "Created By",
			"rules"		=> ""
		),
		array(
			"field"		=> "purchase_orders_customer_id",
			"label"		=> "Customer",
			"rules"		=> "required|is_natural_no_zero"
		),
		array(
			"field"		=> "purchase_orders_status_id",
			"label"		=> "Status",
			"rules"		=> "required|trim|max_length[50]"
		),
		array(
			"field"		=> "purchase_orders_comments",
			"label"		=> "Comments",
			"rules"		=> "max_length[4000]"
		),
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;

	//--------------------------------------------------------------------
	public function get_pos_select ( )
	{
		$query = $this->db->select('id, po_no')->get('purchase_orders');

		if ( $query->num_rows() <= 0 )
			return '';

		$option = array();
		$option['-1'] = 'Select one';
		foreach ($query->result() as $row)
		{
			$option[$row->id] = $row->po_no;
		}

		$query->free_result();

		return $option;
	}

	//--------------------------------------------------------------------

<<<<<<< HEAD
	public function get_pos()
=======
	public function get_po_ref()
>>>>>>> f19371064a9ba4d3faff72c86b6ae2805aa04588
	{
		$query = $this->db->select('id, po_no')->get('purchase_orders');

		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
	}

	//--------------------------------------------------------------------

	public function get_po_tracker($id = NULL){

        $fields = 'po.id, pc.id container_id, pf.id fulfillment_id, po.po_no, po.po_dt, po.product_id, p.name prod_name, po.packing_mode, po.no_of_units, ';
        $fields = $fields . 'po.qty, po.uom_id, u.name uom_name, po.rate, po.comments, po.status_id, ';
        $fields = $fields . 'pc.batch_no, pc.vessel, pc.container, pc.seal, ';
        $fields = $fields . 'pf.supply_from, pf.dest_port, pf.vendor_id, v.name vendor_name, ';
        $fields = $fields . 'c.name cust_name';

        if ($id == NULL) :
            $query = $this->db->select($fields)
                                ->from('purchase_orders po')
                                ->join('product p', 'po.product_id = p.id')
                                ->join('po_containers pc', 'po.id = pc.po_no' , 'right outer')
                                ->join('uom u', 'po.uom_id = u.id')
                                ->join('po_fulfillment pf', 'po.id = pf.po_no', 'right outer')
                                ->join('vendor_profile v', 'pf.vendor_id = v.id', 'right outer')
                                ->join('customers c', 'po.customer_id = c.id')
                                ->where('po.deleted', 0)
                                ->order_by('po.po_no');
        else:
            $query = $this->db->select($fields)
                                ->from('purchase_orders po')
                                ->join('product p', 'po.product_id = p.id')
                                ->join('po_containers pc', 'po.id = pc.po_no' , 'right outer')
                                ->join('uom u', 'po.uom_id = u.id')
                                ->join('po_fulfillment pf', 'po.id = pf.po_no', 'right outer')
                                ->join('vendor_profile v', 'pf.vendor_id = v.id', 'right outer')
                                ->join('customers c', 'po.customer_id = c.id')
                                ->where('po.deleted', 0)
                                ->where('po.id', $id)
                                ->order_by('po.po_no');
        endif;
        
		$query = $this->db->get();
							
		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
	}	    
	//--------------------------------------------------------------------
    public function get_po_docs()
	{
        $query = $this->db->select('po.id, po.po_no, po.applicable, po.attachment, ad.document_id, ad.product_id, p.name product_name, p.desc product_desc')
                                ->from('po_documents po')
                                ->join('activity_documents ad', 'po.product_id = ad.product_id and po.document_id = ad.document_id')
                                ->join('product p', 'ad.product_id = p.id')
                                ->where('ad.activity_code', 'PO')
                                ->order_by('ad.sno, ad.product_id, ad.document_id');
        
        $query = $this->db->get();
		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
	}        
	//--------------------------------------------------------------------
    public function get_po_doc($po_no = 1)
	{
        $query = $this->db->select('po.id, po.po_no, po.applicable, po.attachment, ad.document_id, ad.product_id, p.name product_name, p.desc product_desc, dt.name document_name')
                                ->from('po_documents po')
                                ->join('activity_documents ad', 'po.product_id = ad.product_id and po.document_id = ad.document_id', 'right outer')
                                ->join('product p', 'ad.product_id = p.id')
                                ->join('document_types dt', 'ad.document_id = dt.id')
                                ->where('ad.activity_code', 'PO')
                                ->where('po.po_no is null', null, false)
                                ->or_where('po_no', $po_no)
                                ->order_by('ad.sno, ad.product_id, ad.document_id');
        
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
