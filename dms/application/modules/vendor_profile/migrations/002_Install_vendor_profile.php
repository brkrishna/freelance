<?php if (!defined('BASEPATH')) exit('No direct script access allowed');

class Migration_Install_vendor_profile extends Migration
{
	/**
	 * The name of the database table
	 *
	 * @var String
	 */
	private $table_name = 'vendor_profile';

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
		'name' => array(
			'type' => 'VARCHAR',
			'constraint' => 255,
			'null' => FALSE,
		),
		'est_type' => array(
			'type' => 'VARCHAR',
			'constraint' => 255,
			'null' => FALSE,
		),
		'est_const' => array(
			'type' => 'VARCHAR',
			'constraint' => 255,
			'null' => FALSE,
		),
		'est_start_yr' => array(
			'type' => 'INT',
			'null' => FALSE,
		),
		'profile' => array(
			'type' => 'VARCHAR',
			'constraint' => 4000,
			'null' => TRUE,
		),
		'website' => array(
			'type' => 'VARCHAR',
			'constraint' => 255,
			'null' => TRUE,
		),
		'created_by' => array(
			'type' => 'INT',
			'null' => FALSE,
		),
		'profile_id' => array(
			'type' => 'INT',
			'null' => TRUE,
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