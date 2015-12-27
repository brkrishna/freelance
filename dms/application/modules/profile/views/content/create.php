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

if (isset($profile))
{
	$profile = (array) $profile;
}
$id = isset($profile['id']) ? $profile['id'] : '';

?>
<div class="admin-box span6">
	<h3>Profile</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<div class="control-group <?php echo form_error('org_name') ? 'error' : ''; ?>">
				<?php echo form_label('Organization Name'. lang('bf_form_label_required'), 'profile_org_name', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='profile_org_name' type='text' name='profile_org_name' maxlength="255" value="<?php echo set_value('profile_org_name', isset($profile['org_name']) ? $profile['org_name'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('org_name'); ?></span>
				</div>
			</div>

			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('profile_action_create'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/profile', lang('profile_cancel'), 'class="btn btn-warning"'); ?>
				
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>
<div class="span6">
    <h2>Profile - Initial Setup</h2>    
    <p>
        <span>Please provide your organization name and a few lines on the nature of your business to help us understand better</span>
    </p>
</div>