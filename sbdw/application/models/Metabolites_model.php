<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class metabolites_model extends MY_Model{

    function metabolites_model(){
        parent::__construct();
        $this->tbl = 'METABOLITES';
    }

    function count_by($column, $match){
        $this->db->like($column, $match);
        $this->db->from($this->tbl);    
        return $this->db->count_all_results();
    } 

    function unique_counts($field_name){
        $this->db->distinct();
        $this->db->select($field_name);
        $this->db->where($field_name . '<>', '""');
        return $this->db->get($this->tbl)->num_rows();    
    }
     /*function get_paged_mol($limit = 1, $offset = 1){
        $this->db->order_by('cd_id', 'asc');
        return $this->db->get($this->tbl, $limit, $offset);
    }*/
    
	function get_paged_mol($substrate_id, $limit = 1, $offset = 1){
		$this->db->where('substrate_id', $substrate_id)->order_by('cd_id', 'asc');
		return $this->db->get($this->tbl, $limit, $offset);
	}
   
	function get_paged_metabolite($substrate_id, $cd_id = 1, $limit = 1, $offset = 1){
		$this->db->where('substrate_id', $substrate_id)->where('cd_id', $cd_id)->order_by('cd_id', 'asc');
		return $this->db->get($this->tbl, $limit, $offset);
	}
}
?>
