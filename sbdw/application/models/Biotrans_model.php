<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class Biotrans_model extends MY_Model{

    function biotrans_model(){
        parent::__construct();
        $this->tbl = 'BIOTRANSFORMATION';
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
    
  	function get_paged_mol($substrate_id, $limit = 1, $offset = 1){
		$this->db->where('substrate_id', $substrate_id)->order_by('cd_id', 'asc');
		return $this->db->get($this->tbl, $limit, $offset);
	}

    function get_last_updated_on($tbl = 'BOTANICULE'){
        $this->tbl = $tbl;
        $sql = "select max(Date_Imported) last_updated_on from " . $tbl . " where Date_Imported is not null order by 1 desc limit 1";
        return $this->db->query($sql)->row('last_updated_on');
    }
	
}

?>
