<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Migration_Install_po_documents extends Migration
{
	/**
	 * The name of the database table
	 *
	 * @var String
	 */
	private $table_name = 'po_documents';

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
			'type' => 'INT',
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
		'applicable' => array(
			'type' => 'VARCHAR',
			'constraint' => 10,
			'null' => FALSE,
		),
		'document_id' => array(
			'type' => 'INT',
			'null' => TRUE,
		),
		'issue_auth' => array(
			'type' => 'VARCHAR',
			'constraint' => 255,
			'null' => TRUE,
		),
		'issued_on' => array(
			'type' => 'DATE',
			'null' => TRUE,
			'default' => '0000-00-00',
		),
		'valid_till' => array(
			'type' => 'DATE',
			'null' => TRUE,
			'default' => '0000-00-00',
		),
		'origin_place' => array(
			'type' => 'VARCHAR',
			'constraint' => 255,
			'null' => TRUE,
		),
		'attachment' => array(
			'type' => 'VARCHAR',
			'constraint' => 4000,
			'null' => TRUE,
		),
		'comments' => array(
			'type' => 'VARCHAR',
			'constraint' => 4000,
			'null' => TRUE,
		),
		'created_by' => array(
			'type' => 'INT',
			'null' => FALSE,
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