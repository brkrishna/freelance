<?php

class levels_model extends MY_Model {
	
	function levels_model(){
		parent::__construct();
		$this->tbl = 'levels';
	} 	

	function get_levels(){
		$sql = "select l.id, l.code, l.name, l.parent_id, l.sort_order, count(q.id) questions, count(a.id) answers ";
		$sql = $sql . "from levels l  ";
		$sql = $sql . "left outer join questions q on l.id = q.level_id  ";	
		$sql = $sql . "left outer join answers a on q.id = a.q_id  ";	
		$sql = $sql . "group by l.id  ";
		$sql = $sql . "order by l.sort_order  ";

		return $this->db->query($sql);
	}
	
	function get_pct(){
		$sql = "select count(q.id) questions, count(a.id) answers ";
		$sql = $sql . "from levels l  ";
		$sql = $sql . "left outer join questions q on l.id = q.level_id  ";	
		$sql = $sql . "left outer join answers a on q.id = a.q_id  ";	
		$sql = $sql . "order by l.sort_order  ";

		return $this->db->query($sql);
	}

}

?>