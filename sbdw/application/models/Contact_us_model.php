<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class contact_us_model extends MY_Model{

   function contact_us_model(){
	   parent::__construct();
	   $this->tbl = 'contact_us';
   }  
}