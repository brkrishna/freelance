<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Containers_model extends BF_Model {

	protected $table_name	= "containers";
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
			"field"		=> "containers_po_ref",
			"label"		=> "PO Ref",
			"rules"		=> "required|max_length[255]"
		),
		array(
			"field"		=> "containers_container_no",
			"label"		=> "Container No",
			"rules"		=> "required|unique[bf_containers.container_no,bf_containers.id]|max_length[255]"
		),
		array(
			"field"		=> "containers_seal",
			"label"		=> "Seal",
			"rules"		=> "required|max_length[255]"
		),
		array(
			"field"		=> "containers_origin",
			"label"		=> "Origin",
			"rules"		=> "required"
		),
		array(
			"field"		=> "containers_batch_nos",
			"label"		=> "Batch Numbers",
			"rules"		=> "max_length[255]"
		),
		array(
			"field"		=> "containers_product_id",
			"label"		=> "Product",
			"rules"		=> "required"
		),
		array(
			"field"		=> "containers_uom_id",
			"label"		=> "UOM",
			"rules"		=> "required"
		),
		array(
			"field"		=> "containers_status",
			"label"		=> "Status",
			"rules"		=> "required|max_length[255]"
		),
		array(
			"field"		=> "containers_started_on",
			"label"		=> "Started on",
			"rules"		=> "required"
		),
		array(
			"field"		=> "containers_arrived_on",
			"label"		=> "Arrived On",
			"rules"		=> ""
		),
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;

	//--------------------------------------------------------------------

	public function get_containers_select ( )
	{
		$query = $this->db->select('container_no')->get('containers');

		if ( $query->num_rows() <= 0 )
			return '';

		$option = array();
		$option['-1'] = 'Select one';
		foreach ($query->result() as $row)
		{
			$option[$row->container_no] = $row->container_no;
		}

		$query->free_result();

		return $option;
	}

	//--------------------------------------------------------------------

	public function get_containers()
	{
		$query = $this->db->select('container_no')->get('containers');

		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
	}

	//--------------------------------------------------------------------

	public function get_top_containers($top = 3){

		$query = $this->db->select('containers.id, containers.po_ref, containers.container_no, containers.seal, containers.origin, containers.batch_nos, containers.product_id, countries.name country_name, product.name product_name, document_types.name doc_type_name, purchase_order_documents.attachments')
							->from('containers')
							->join('countries', 'containers.origin = countries.iso')
							->join('product', 'containers.product_id = product.id')
							->join('purchase_order_documents', 'containers.container_no = purchase_order_documents.container')
							->join('document_types', 'purchase_order_documents.doc_type = document_types.id')
							->order_by('product.name asc, countries.name asc, containers.container_no asc, document_types.name desc');
							//->join('uom', 'samples.uom_id = uom.id');


		$query = $this->db->get();
							
		if ($query->num_rows() > 0)
		{
			return $query->result();
		} else {
			return null;
		}
	}		
}
