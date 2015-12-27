<?php defined('BASEPATH') || exit('No direct script access allowed');

class Migration_Add_Classification extends Migration
{
    /**
     * @var string The name of the database table
     */
    private $table_name = 'ingredients';

    /**
     * @var array The table's fields
     */
    private $fields = array(
        'id' => array(
            'type'       => 'VARCHAR',
            'constraint' => 255,
            'null' => true,
            )
    );

    /**
     * Install this version
     *
     * @return void
     */
    public function up()
    {
        $this->dbforge->add_column($this->table_name, array('classification' => array('type' => 'VARCHAR', 'constraint' => 255, 'null' =>  true)));
    }

    /**
     * Uninstall this version
     *
     * @return void
     */
        public function down()
    {
        $this->dbforge->drop_column($this->table_name, 'classification');
    }
}