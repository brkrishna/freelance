<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Migration_Install_inquiries extends Migration
{
	/**
	 * The name of the database table
	 *
	 * @var String
	 */
	private $table_name = 'inquiries';

	/**
	 * The table's fields
	 *
	 * @var Array
	 */
	private $fields = array(
		'id' => array(
			'type' => 'INT',
			'constraint' => 11,
			'auto_increment' => TRUE,
		),
		'product' => array(
			'type' => 'VARCHAR',
			'constraint' => 255,
			'null' => FALSE,
		),
		'quantity' => array(
			'type' => 'DECIMAL',
			'constraint' => '18,3',
			'null' => FALSE,
		),
		'uom_id' => array(
			'type' => 'INT',
			'null' => FALSE,
		),
		'required_by' => array(
			'type' => 'DATE',
			'null' => FALSE,
			'default' => '0000-00-00',
		),
		'prod_spec' => array(
			'type' => 'VARCHAR',
			'constraint' => 1000,
			'null' => FALSE,
		),
		'quality_spec' => array(
			'type' => 'VARCHAR',
			'constraint' => 1000,
			'null' => FALSE,
		),
		'packaging_spec' => array(
			'type' => 'VARCHAR',
			'constraint' => 1000,
			'null' => FALSE,
		),
		'priority' => array(
			'type' => 'VARCHAR',
			'constraint' => 50,
			'null' => FALSE,
		),
		'status' => array(
			'type' => 'VARCHAR',
			'constraint' => 50,
			'null' => FALSE,
		),
		'comments_thread_id' => array(
			'type' => 'INT',
			'null' => FALSE,
            'default' => '0',
		),      
        'deleted' => array(
            'type' => 'TINYINT',
            'constraint' => 1,
            'default' => '0',
        ),
		'created_on' => array(
			'type' => 'datetime',
			'default' => '0000-00-00 00:00:00',
		),
		'modified_on' => array(
			'type' => 'datetime',
			'default' => '0000-00-00 00:00:00',
		),	
		'created_by' => array(
			'type' => 'INT',
			'null' => FALSE,
		),      
	);

	/**
	 * Install this migration
	 *
	 * @return void
	 */
	public function up()
	{
		$this->dbforge->add_field($this->fields);
		$this->dbforge->add_key('id', true);
		$this->dbforge->create_table($this->table_name);
	}

	//--------------------------------------------------------------------

	/**
	 * Uninstall this migration
	 *
	 * @return void
	 */
	public function down()
	{
		$this->dbforge->drop_table($this->table_name);
	}

	//--------------------------------------------------------------------

}