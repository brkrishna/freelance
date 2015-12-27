<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class bioresearch_model extends MY_Model{

   function bioresearch_model(){
	   parent::__construct();
	   $this->tbl = 'BLOOD_CELLS';
        
   }
    
   function count_by($column, $match){
       $this->db->like($column, $match);
       $this->db->from($this->tbl);    
       return $this->db->count_all_results();
   } 
    //BLOOD_CELLS
    function get_bioresearch($subcategory = 'bonemarrow', $limit = 1, $offset = 1){
	    $this->db->where('subcategory', $subcategory)->order_by('id', 'asc');
		return $this->db->get($this->tbl, $limit, $offset);
    }
    function count_results($subcategory = 'bonemarrow'){
	    $this->db->where('subcategory', $subcategory)->order_by('id', 'asc');
		return $this->db->get($this->tbl)->num_rows();
    }
    
}
?>
