<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Botanicules_model extends BF_Model {

	protected $table_name	= "botanicules";
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
			"field"		=> "botanicules_structure",
			"label"		=> "Structure",
			"rules"		=> "required|max_length[4000]"
		),
		array(
			"field"		=> "botanicules_mol_weight",
			"label"		=> "Molecular Weight",
			"rules"		=> "is_decimal|max_length[19]"
		),
		array(
			"field"		=> "botanicules_formula",
			"label"		=> "Formula",
			"rules"		=> "trim|max_length[255]"
		),
		array(
			"field"		=> "botanicules_compound_name",
			"label"		=> "Compound Name",
			"rules"		=> "trim|max_length[1000]"
		),
		array(
			"field"		=> "botanicules_mol_name",
			"label"		=> "Molecule Name",
			"rules"		=> "trim|max_length[1000]"
		),
		array(
			"field"		=> "botanicules_ref",
			"label"		=> "Reference",
			"rules"		=> "trim|max_length[1000]"
		),
		array(
			"field"		=> "botanicules_src_ref",
			"label"		=> "Source Reference",
			"rules"		=> "trim|max_length[1000]"
		),
		array(
			"field"		=> "botanicules_mol_type",
			"label"		=> "Molecule Type",
			"rules"		=> "trim|max_length[1000]"
		),
		array(
			"field"		=> "botanicules_therapeutic_catg",
			"label"		=> "Therapeutic Category",
			"rules"		=> "trim|max_length[255]"
		),
		array(
			"field"		=> "botanicules_iupac_name",
			"label"		=> "IUPAC Name",
			"rules"		=> "trim|max_length[1000]"
		),
		array(
			"field"		=> "botanicules_src_type",
			"label"		=> "Source Type",
			"rules"		=> "trim|max_length[1000]"
		),
		array(
			"field"		=> "botanicules_src_family",
			"label"		=> "Source Family",
			"rules"		=> "trim|max_length[1000]"
		),
		array(
			"field"		=> "botanicules_qc_status",
			"label"		=> "QC Status",
			"rules"		=> "trim|max_length[15]"
		),
		array(
			"field"		=> "botanicules_pdf_avail",
			"label"		=> "PDF Availability",
			"rules"		=> "trim|max_length[15]"
		),
		array(
			"field"		=> "botanicules_parts_of_isol",
			"label"		=> "Parts of Isolation",
			"rules"		=> "trim|max_length[1000]"
		),
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;

	//--------------------------------------------------------------------

}
