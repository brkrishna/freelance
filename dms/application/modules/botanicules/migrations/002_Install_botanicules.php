<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Migration_Install_botanicules extends Migration
{
	/**
	 * The name of the database table
	 *
	 * @var String
	 */
	private $table_name = 'botanicules';

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
		'structure' => array(
			'type' => 'MEDIUMBLOB',
			'null' => FALSE,
		),
		'mol_weight' => array(
			'type' => 'DECIMAL',
			'constraint' => '18,3',
			'null' => FALSE,
		),
		'formula' => array(
			'type' => 'VARCHAR',
			'constraint' => 255,
			'null' => FALSE,
		),
		'compound_name' => array(
			'type' => 'VARCHAR',
			'constraint' => 1000,
			'null' => FALSE,
		),
		'mol_name' => array(
			'type' => 'VARCHAR',
			'constraint' => 1000,
			'null' => FALSE,
		),
		'ref' => array(
			'type' => 'VARCHAR',
			'constraint' => 1000,
			'null' => FALSE,
		),
		'src_ref' => array(
			'type' => 'VARCHAR',
			'constraint' => 1000,
			'null' => FALSE,
		),
		'mol_type' => array(
			'type' => 'VARCHAR',
			'constraint' => 1000,
			'null' => FALSE,
		),
		'therapeutic_catg' => array(
			'type' => 'VARCHAR',
			'constraint' => 255,
			'null' => FALSE,
		),
		'iupac_name' => array(
			'type' => 'VARCHAR',
			'constraint' => 1000,
			'null' => FALSE,
		),
		'src_type' => array(
			'type' => 'VARCHAR',
			'constraint' => 1000,
			'null' => FALSE,
		),
		'src_family' => array(
			'type' => 'VARCHAR',
			'constraint' => 1000,
			'null' => FALSE,
		),
		'qc_status' => array(
			'type' => 'VARCHAR',
			'constraint' => 15,
			'null' => FALSE,
		),
		'pdf_avail' => array(
			'type' => 'VARCHAR',
			'constraint' => 15,
			'null' => FALSE,
		),
		'parts_of_isol' => array(
			'type' => 'VARCHAR',
			'constraint' => 1000,
			'null' => FALSE,
		),
		'user_id' => array(
			'type' => 'INT',
			'constraint' => 11,
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