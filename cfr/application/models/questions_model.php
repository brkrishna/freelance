<?php

class questions_model extends MY_Model {
	
  function questions_model(){
		parent::__construct();
		$this->tbl = 'questions';
  } 	   

  function upsert($data){
    $sql = $this->db->insert_string('answers', $data) . ' ON DUPLICATE KEY UPDATE answer=' . $data['answer'];
    $this->db->query($sql);
    $id = $this->db->insert_id();    
  }

  function get_questions($level_id = 1){

    $sql = "select q.id, q.code, q.level_id, q.short_desc, q.parent_id, q.sort_order, q.severity, a.answer ";
    $sql = $sql . "from questions q  ";
    $sql = $sql . "left outer join answers a on q.id = a.q_id  ";
    $sql = $sql . "where q.level_id = " . $level_id . " ";
    $sql = $sql . "order by q.sort_order  ";

    return $this->db->query($sql);    
  }
}
?>
