<?php defined('BASEPATH') || exit('No direct script access allowed');

class Migration_Install_party_documents extends Migration
{
	/**
	 * @var string The name of the database table
	 */
	private $table_name = 'party_documents';

	/**
	 * @var array The table's fields
	 */
	private $fields = array(
		'id' => array(
			'type'       => 'INT',
			'constraint' => 11,
			'auto_increment' => true,
		),
        'party_id' => array(
            'type'       => 'INT',
            'constraint' => 11,
            'null'       => false,
        ),
        'product_id' => array(
            'type'       => 'INT',
            'constraint' => 11,
            'null'       => false,
        ),
        'ingredient_id' => array(
            'type'       => 'INT',
            'constraint' => 11,
            'null'       => false,
        ),
        'doc_name' => array(
            'type'       => 'VARCHAR',
            'constraint' => 255,
            'null'       => false,
        ),
        'doc_file' => array(
            'type'       => 'TEXT',
            'null'       => true,
        ),
        'rcvd_on' => array(
            'type'       => 'DATE',
            'null'       => false,
            'default'    => '0000-00-00',
        ),
        'comments' => array(
            'type'       => 'TEXT',
            'null'       => true,
        ),
        'archive' => array(
            'type'       => 'VARCHAR',
            'constraint' => 25,
            'null'       => false,
        ),
	);

	/**
	 * Install this version
	 *
	 * @return void
	 */
	public function up()
	{
		$this->dbforge->add_field($this->fields);
		$this->dbforge->add_key('id', true);
		$this->dbforge->create_table($this->table_name);
	}

	/**
	 * Uninstall this version
	 *
	 * @return void
	 */
	public function down()
	{
		$this->dbforge->drop_table($this->table_name);
	}
}