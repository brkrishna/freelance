<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class substrates_model extends MY_Model{

    function substrates_model(){
        parent::__construct();
        $this->tbl = 'SUBSTRATES';
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
     function get_paged_mol($limit = 1, $offset = 1){
        $this->db->order_by('cd_id', 'asc');
        return $this->db->get($this->tbl, $limit, $offset);
    }
     function get_count(){
        return $this->db->count_all_results();
    }
    
}
?>
