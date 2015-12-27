<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Migration_Install_po_fulfillment extends Migration
{
	/**
	 * The name of the database table
	 *
	 * @var String
	 */
	private $table_name = 'po_fulfillment';

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
		'po_no' => array(
			'type' => 'VARCHAR',
			'constraint' => 255,
			'null' => FALSE,
		),
		'vendor_id' => array(
			'type' => 'INT',
			'null' => FALSE,
		),
		'product_id' => array(
			'type' => 'INT',
			'null' => FALSE,
		),
		'qty' => array(
			'type' => 'DECIMAL',
			'constraint' => '18,3',
			'null' => FALSE,
		),
		'uom_id' => array(
			'type' => 'INT',
			'null' => FALSE,
		),
		'rate' => array(
			'type' => 'DECIMAL',
			'constraint' => '18,3',
			'null' => FALSE,
		),
		'supply_from' => array(
			'type' => 'VARCHAR',
			'constraint' => 255,
			'null' => FALSE,
		),
		'dest_port' => array(
			'type' => 'VARCHAR',
			'constraint' => 255,
			'null' => FALSE,
		),
		'packing_mode' => array(
			'type' => 'VARCHAR',
			'constraint' => 255,
			'null' => FALSE,
		),
		'no_of_units' => array(
			'type' => 'DECIMAL',
			'constraint' => '18,3',
			'null' => FALSE,
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