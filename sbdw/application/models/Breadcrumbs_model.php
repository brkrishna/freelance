<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class breadcrumbs_model extends MY_Model{

   function breadcrumbs_model(){
	   parent::__construct();
	   $this->tbl = 'breadcrumbs';
   }
    
   function count_by($column, $match){
       $this->db->like($column, $match);
       $this->db->from($this->tbl);    
       return $this->db->count_all_results();
   }   
    
   function get_id_by_alias($alias = 'home'){
       $this->db->where('alias', $alias);
       $this->db->from($this->tbl);    
       return $this->db->get();
   }
}
?>
