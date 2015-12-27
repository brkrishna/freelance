<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class login_model extends MY_Model{

   function login_model(){
	   parent::__construct();
       $this->load->library('encrypt');
	   $this->tbl = 'a_users';
   }

   function setup(){
		
		$data['f_user_name'] = array(
								'name'=>'user_name', 
								'size'=>30,
								'type'=>'textbox',
                                'class'=>'form-control',
								'value' => $this->input->post('user_name'),
							);
		
		$data['f_password'] = array(
								'name'=>'password', 
								'size'=>30,
								'type'=>'password',
                                'class'=>'form-control',
								'value' => $this->input->post('password'),
							);

		$data['b_submit'] = array(
									'name' => 'b_submit',
									'value' => 'Login',
									'type' => 'submit',
									'content' => 'Login'
								);
		
		return $data;
	}
    
    function login($username, $password){
    	$this->db->select('id, name, password');
    	$this->db->from($this->tbl);
    	$this->db->where('name', $username);
    	$this->db->limit(1);
    	
    	$query = $this->db->get();
    	
    	if($query->num_rows() == 1){

            $result = $query->result();
            foreach($result as $row){
                $dbpass = $row->password;
                if ($dbpass == $password){
                    return $result;
                }
                elseif($this->encrypt->decode($dbpass) == $password){
                    return $result;   
                }
                else{
                    return null;
                }
            }     
    	}else{
    		return null;
    	}
    }
}
?>
