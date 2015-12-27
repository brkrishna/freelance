<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class tissues_model extends MY_Model{

   function tissues_model(){
	   parent::__construct();
	   $this->tbl = 'MICROTISSUES';
       
   }
    
   function count_by($column, $match){
       $this->db->like($column, $match);
       $this->db->from($this->tbl);    
       return $this->db->count_all_results();
   } 
    //microtissues
   function get_tissues($group = 'liver', $limit = 1, $offset = 1){
	    $this->db->where('group', $group)->order_by('id', 'asc');
		return $this->db->get($this->tbl, $limit, $offset);
    }
    function count_results($group = 'liver'){
	    $this->db->where('group', $group)->order_by('id', 'asc');
		return $this->db->get($this->tbl)->num_rows();
    }
    
}
?>
