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

if (isset($activity_type))
{
	$activity_type = (array) $activity_type;
}
$id = isset($activity_type['id']) ? $activity_type['id'] : '';

?>
<div class="admin-box">
	<h3>Activity Type</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<div class="control-group <?php echo form_error('activity_type_code') ? 'error' : ''; ?>">
				<?php echo form_label('Activity Code'. lang('bf_form_label_required'), 'activity_type_code', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='activity_type_code' type='text' name='activity_type_code' maxlength="255" value="<?php echo set_value('activity_type_code', isset($activity_type['code']) ? $activity_type['code'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('activity_type_code'); ?></span>
				</div>
			</div>

            <div class="control-group <?php echo form_error('activity_type_name') ? 'error' : ''; ?>">
				<?php echo form_label('Activity Type'. lang('bf_form_label_required'), 'activity_type_name', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='activity_type_name' type='text' name='activity_type_name' maxlength="255" value="<?php echo set_value('activity_type_name', isset($activity_type['name']) ? $activity_type['name'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('activity_type_name'); ?></span>
				</div>
			</div>

			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('activity_type_action_create'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/activity_type', lang('activity_type_cancel'), 'class="btn btn-warning"'); ?>
				
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>