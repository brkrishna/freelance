<?php defined('BASEPATH') || exit('No direct script access allowed');

class Migration_Alter_party_documents extends Migration
{
    /**
     * @var string The name of the database table
     */
    private $table_name = 'party_documents';

    /**
     * Install this version
     *
     * @return void
     */
    public function up()
    {
        $this->dbforge->add_column($this->table_name, array('cert_type' => array('type' => 'VARCHAR', 'constraint' => 255, 'null' =>  true)));
        $this->dbforge->add_column($this->table_name, array('catg' => array('type' => 'VARCHAR', 'constraint' => 255, 'null' =>  true)));

    }

    /**
     * Uninstall this version
     *
     * @return void
     */
        public function down()
    {
        $this->dbforge->drop_column($this->table_name, 'cert_type');
        $this->dbforge->drop_column($this->table_name, 'catg');
    }
}
