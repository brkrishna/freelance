<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class users_model extends MY_Model{

   function users_model(){
	   parent::__construct();
	   $this->tbl = 'users';
   }  
   function get_activate($pass_key = 'activation_key'){
	    $this->db->where('activation_key', 'activation_key=$pass_key');
        $this->db->update('users', $activation_key = NULL); 
        return $this->db->get($this->tbl);
    }
    function count_results($pass_key = 'activation_key'){
	    $this->db->where('activation_key', 'activation_key=$pass_key');
		return $this->db->get($this->tbl)->num_rows();
    }
    
   /* public function get_activate($pass_key = 'activation_key', $is_active = 'false'){
        $this->db->where('activation_key', 'activation_key=$pass_key');
        $this->db->update('users', $activation_key = NULL); 
        return $this->db->get();

        }
     public function get_view($is_active = NULL)
     {
               
     }
 */
  }