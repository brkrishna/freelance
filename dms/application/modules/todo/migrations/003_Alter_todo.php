<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Migration_Alter_todo extends Migration{
    
    public function up(){
        
       $this->dbforge->add_column('todo', array(
                'status'	=> array(
                'type'	=> 'VARCHAR',
                'constraint'	=> 255,
                'default'		=> NULL
            )
        ));        
    }
    
    public function down(){
        $this->dbforge->drop_column('todo', 'status');                
    }
}