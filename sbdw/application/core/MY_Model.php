<?php

class MY_Model extends CI_Model{
	
	public $tbl = '';
	
	function __construct(){
        // Call the Model constructor
        parent::__construct();
        $this->load->database();
    }
	
	function count_all(){
		return $this->db->count_all($this->tbl);
	}
	
    function count_by_where($column, $match){
        $this->db->where($column, $match);
        $this->db->from($this->tbl);    
        return $this->db->count_all_results();
    } 
	
    function get_by_where($column, $match){
        $this->db->where($column, $match);
        $this->db->from($this->tbl);    
        return $this->db->get();
    } 

	function get_paged_list($limit = 10, $offset = 0){
		$this->db->order_by('id', 'asc');
		return $this->db->get($this->tbl, $limit, $offset);
	}
	
	function get_paged_mol_list($limit = 1, $offset = 1){
		$this->db->order_by('cd_id', 'asc');
		return $this->db->get($this->tbl, $limit, $offset);
	}

	function get_by_id($id){
		$this->db->where('id', $id);
		return $this->db->get($this->tbl);
	}
	
	function save($data){
		$this->db->insert($this->tbl, $data);
		return $this->db->insert_id();
	}
	
	function update($id, $data){
		$this->db->where('id', $id);
		$this->db->update($this->tbl, $data);
		return $this->db->affected_rows();
	}
	
	function delete($id){
		$this->db->where($id, 'id');
		$this->db->delete($this->tbl);
		return $this->db->affected_rows();
	}	
}

?>
