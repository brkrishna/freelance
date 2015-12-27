<?php

$validation_errors = validation_errors();

if ($validation_errors) :
?>
<div class="alert alert-block alert-error fade in">
	<a class="close" data-dismiss="alert">&times;</a>
	<h4 class="alert-heading">Please fix the following errors:</h4>
	<?php echo $validation_errors; ?>
</div>
<?php
endif;

if (isset($todo_list))
{
	$todo_list = (array) $todo_list;
}
$id = isset($todo_list['id']) ? $todo_list['id'] : '';

?>
<div class="admin-box">
	<h3>Todo List</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<div class="control-group <?php echo form_error('name') ? 'error' : ''; ?>">
				<?php echo form_label('Name'. lang('bf_form_label_required'), 'todo_list_name', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='todo_list_name' type='text' name='todo_list_name' maxlength="255" value="<?php echo set_value('todo_list_name', isset($todo_list['name']) ? $todo_list['name'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('name'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('notes') ? 'error' : ''; ?>">
				<?php echo form_label('Notes', 'todo_list_notes', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<?php echo form_textarea( array( 'name' => 'todo_list_notes', 'id' => 'todo_list_notes', 'rows' => '5', 'cols' => '80', 'value' => set_value('todo_list_notes', isset($todo_list['notes']) ? $todo_list['notes'] : '') ) ); ?>
					<span class='help-inline'><?php echo form_error('notes'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('sort_order') ? 'error' : ''; ?>">
				<?php echo form_label('Sort Order'. lang('bf_form_label_required'), 'todo_list_sort_order', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='todo_list_sort_order' type='text' name='todo_list_sort_order' maxlength="11" value="<?php echo set_value('todo_list_sort_order', isset($todo_list['sort_order']) ? $todo_list['sort_order'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('sort_order'); ?></span>
				</div>
			</div>

			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('todo_list_action_create'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/todo_list', lang('todo_list_cancel'), 'class="btn btn-warning"'); ?>
				
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>