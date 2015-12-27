<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Todo_model extends BF_Model {

	protected $table_name	= "todo";
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
			"field"		=> "todo_list_id",
			"label"		=> "List",
			"rules"		=> "required|is_natural_no_zero"
		),
		array(
			"field"		=> "todo_name",
			"label"		=> "Subject",
			"rules"		=> "required|trim|max_length[255]"
		),
		array(
			"field"		=> "todo_notes",
			"label"		=> "Notes",
			"rules"		=> "trim|max_length[4000]"
		),
		array(
			"field"		=> "todo_created_by",
			"label"		=> "Created By",
			"rules"		=> ""
		),
		array(
			"field"		=> "todo_assigned_to",
			"label"		=> "Assigned To",
			"rules"		=> "required|trim|is_natural_no_zero|max_length[11]"
		),
		array(
			"field"		=> "todo_due_by",
			"label"		=> "Due By",
			"rules"		=> "required"
		),
		array(
			"field"		=> "todo_orig_due_by",
			"label"		=> "Original Due By",
			"rules"		=> ""
		),
		array(
			"field"		=> "todo_comments_thread_id",
			"label"		=> "Comments Thread Id",
			"rules"		=> ""
		),
	);
	protected $insert_validation_rules 	= array();
	protected $skip_validation 			= FALSE;

	//--------------------------------------------------------------------

	public function get_top_todos($top = 10){

		$query = $this->db->select('t.id, t.list_id, tl.name list_name, t.name, t.notes, t.created_by, t.created_on, t.due_by, t.orig_due_by, t.assigned_to, t.attachment, t.modified_on, a.display_name assigned_name')
							->from('todo t')
                            ->join('todo_list tl', 't.list_id = tl.id')
							->join('users c', 't.created_by = c.id')
                            ->join('users a', 't.assigned_to = a.id')
                            ->where('t.deleted', 0)
                            ->where('t.status', 'Active')
                            ->order_by('t.list_id, t.due_by');

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
