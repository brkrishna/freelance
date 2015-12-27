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

if (isset($todo))
{
	$todo = (array) $todo;
}
$id = isset($todo['id']) ? $todo['id'] : '';

?>
<div class="admin-box">
	<h3>Todo</h3>
	<?php echo form_open_multipart($this->uri->uri_string(), 'class="form-inline"'); ?>
		<fieldset>
            <div class="span5">
                <?php // Change the values in this array to populate your dropdown as required
                    if (is_array($todo_list_select) && count($todo_list_select)) :		
                        echo form_dropdown('todo_list_id', $todo_list_select, set_value('todo_list_id', isset($todo['list_id']) ? $todo['list_id'] : ''), 'List'. lang('bf_form_label_required'));
                    endif;    
                ?>

                <div class="control-group <?php echo form_error('name') ? 'error' : ''; ?>">
                    <?php echo form_label('Subject'. lang('bf_form_label_required'), 'todo_name', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input id='todo_name' type='text' name='todo_name' maxlength="255" value="<?php echo set_value('todo_name', isset($todo['name']) ? $todo['name'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('name'); ?></span>
                    </div>
                </div>

                <div class="control-group <?php echo form_error('notes') ? 'error' : ''; ?>">
                    <?php echo form_label('Notes', 'todo_notes', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <?php echo form_textarea( array( 'name' => 'todo_notes', 'id' => 'todo_notes', 'rows' => '5', 'cols' => '80', 'value' => set_value('todo_notes', isset($todo['notes']) ? $todo['notes'] : '') ) ); ?>
                        <span class='help-inline'><?php echo form_error('notes'); ?></span>
                    </div>
                </div>

                <?php // Change the values in this array to populate your dropdown as required
                    if (is_array($users_select) && count($users_select)) :		
                        echo form_dropdown('todo_assigned_to', $users_select, set_value('todo_assigned_to', isset($todo['assigned_to']) ? $todo['assigned_to'] : ''), 'Assigned To'. lang('bf_form_label_required'));
                    endif;
                ?>

                <div class="control-group <?php echo form_error('due_by') ? 'error' : ''; ?>">
                    <?php echo form_label('Due By'. lang('bf_form_label_required'), 'todo_due_by', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input id='todo_due_by' type='text' name='todo_due_by'  value="<?php echo set_value('todo_due_by', isset($todo['due_by']) ? $todo['due_by'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('due_by'); ?></span>
                    </div>
                </div>

                <div class="control-group <?php echo form_error('attachment') ? 'error' : ''; ?>">
                    <?php echo form_label('Attachment', 'attachment', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input id='attachment' type='file' name='attachment'/>
                        <span class='help-inline'><?php echo form_error('attachment'); ?></span>
                    </div>
                </div>
                
                <div class="form-actions">
                    <input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('todo_action_edit'); ?>"  />
                    <?php echo lang('bf_or'); ?>
                    <?php echo anchor(SITE_AREA .'/content/todo', lang('todo_cancel'), 'class="btn btn-warning"'); ?>

                <?php if ($this->auth->has_permission('Todo.Content.Delete')) : ?>
                    or
                    <button type="submit" name="delete" class="btn btn-danger" id="delete-me" onclick="return confirm('<?php e(js_escape(lang('todo_delete_confirm'))); ?>'); ">
                        <span class="icon-trash icon-white"></span>&nbsp;<?php echo lang('todo_delete_record'); ?>
                    </button>
                <?php endif; ?>
                </div>

            </div>
            <div class="span7">
                <?php
                if (isset($comment_form) && !empty($comment_form)) : ?>
                        <!-- COMMENTS -->
                    <h3>Comments</h3>
                    <?php 
                    echo ($comment_form);
                elseif (isset($comment_count) && !empty($comment_count)) :
                    echo ('<h4><span class="label">'.$comment_count.'</span> Comments</h4>');
                endif;
                ?>
            </div>

		</fieldset>
    <?php echo form_close(); ?>
</div>