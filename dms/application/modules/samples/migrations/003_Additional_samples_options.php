<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Migration_Additional_samples_options extends Migration {

    public function up()
	{
        $this->dbforge->add_column('samples', array(
                'po_no'	=> array(
                'type'	=> 'INT',
                'constraint'	=> 11,
                
            )
        ));
        $this->dbforge->add_column('samples', array(
                'party_type' => array(
                'type'	=> 'CHAR',
                'constraint'	=> 1,
            )
        ));
         $this->dbforge->add_column('samples', array(
                'trans_type' => array(
                'type'	=> 'VARCHAR',
                'constraint'	=> 200,
            )
        ));
        $this->dbforge->add_column('samples', array(
                'party_name' => array(
                'type'	=> 'VARCHAR',
                'constraint'	=> 200,
            )
        ));
    }
	
	//--------------------------------------------------------------------
	
	public function down() 
	{

        $this->dbforge->drop_column("samples","po_no");
        $this->dbforge->drop_column("samples","party_type");
        $this->dbforge->drop_column("samples","trans_type");
        $this->dbforge->drop_column("samples","party_name");
    }
	
	//--------------------------------------------------------------------
	
}