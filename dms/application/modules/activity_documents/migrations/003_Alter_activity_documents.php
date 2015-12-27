<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Migration_Alter_activity_documents extends Migration{
    
    public function up(){
        
       $this->dbforge->add_column('activity_documents', array(
                'sno'	=> array(
                'type'	=> 'INT',
                'constraint'	=> 11,
                'default'		=> 0
            )
        ));        
    }
    
    public function down(){
        $this->dbforge->drop_column('activity_documents', 'sno');                
    }
}