<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class products_model extends MY_Model{

   function products_model(){
	   parent::__construct();
	   $this->tbl = 'cell_products';
        
   }
    
   function count_by($column, $match){
       $this->db->like($column, $match);
       $this->db->where('id', $id);
       $this->db->from($this->tbl);    
       return $this->db->count_all_results();
   } 
    //cells
   function get_products($category = 'cells', $limit = 1, $offset = 1){
	    $this->db->where('category', $category)->order_by('product_code', 'asc');
		return $this->db->get($this->tbl, $limit, $offset);
    }

    function count_results($category = 'cells'){
	    $this->db->where('category', $category)->order_by('id', 'asc');
		return $this->db->get($this->tbl)->num_rows();
    }

    function count_records($category = 'cells', $subcat = NULL){
      if ($subcat != NULL){
        $this->db->where('category', $category)->where('subcategory', $subcat)->order_by('id', 'asc');
      }else{
        $this->db->where('category', $category)->order_by('id', 'asc');
      }
    return $this->db->get($this->tbl)->num_rows();
    }


    function get_product_details($content = 'product_dtls', $id){
       $this->db->where('id', $id);
       $this->db->from($this->tbl);    
       return $this->db->get();
   }
    
}
?>
