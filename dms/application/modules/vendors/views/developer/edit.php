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

if (isset($vendors))
{
	$vendors = (array) $vendors;
}
$id = isset($vendors['id']) ? $vendors['id'] : '';

?>
<div class="admin-box">
	<h3>Vendors</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<div class="control-group <?php echo form_error('name') ? 'error' : ''; ?>">
				<?php echo form_label('Name'. lang('bf_form_label_required'), 'vendors_name', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendors_name' type='text' name='vendors_name' maxlength="255" value="<?php echo set_value('vendors_name', isset($vendors['name']) ? $vendors['name'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('name'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('contact_name') ? 'error' : ''; ?>">
				<?php echo form_label('Contact Name'. lang('bf_form_label_required'), 'vendors_contact_name', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendors_contact_name' type='text' name='vendors_contact_name' maxlength="255" value="<?php echo set_value('vendors_contact_name', isset($vendors['contact_name']) ? $vendors['contact_name'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('contact_name'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('contact_phone') ? 'error' : ''; ?>">
				<?php echo form_label('Contact Phone'. lang('bf_form_label_required'), 'vendors_contact_phone', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendors_contact_phone' type='text' name='vendors_contact_phone' maxlength="255" value="<?php echo set_value('vendors_contact_phone', isset($vendors['contact_phone']) ? $vendors['contact_phone'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('contact_phone'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('address1') ? 'error' : ''; ?>">
				<?php echo form_label('Address1', 'vendors_address1', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendors_address1' type='text' name='vendors_address1' maxlength="255" value="<?php echo set_value('vendors_address1', isset($vendors['address1']) ? $vendors['address1'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('address1'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('address2') ? 'error' : ''; ?>">
				<?php echo form_label('Address2', 'vendors_address2', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendors_address2' type='text' name='vendors_address2' maxlength="255" value="<?php echo set_value('vendors_address2', isset($vendors['address2']) ? $vendors['address2'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('address2'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('city') ? 'error' : ''; ?>">
				<?php echo form_label('City', 'vendors_city', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendors_city' type='text' name='vendors_city' maxlength="255" value="<?php echo set_value('vendors_city', isset($vendors['city']) ? $vendors['city'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('city'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
				);

				echo form_dropdown('vendors_country', $options, set_value('vendors_country', isset($vendors['country']) ? $vendors['country'] : ''), 'Country'. lang('bf_form_label_required'));
			?>

			<div class="control-group <?php echo form_error('work_phones') ? 'error' : ''; ?>">
				<?php echo form_label('Office Phones', 'vendors_work_phones', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendors_work_phones' type='text' name='vendors_work_phones' maxlength="255" value="<?php echo set_value('vendors_work_phones', isset($vendors['work_phones']) ? $vendors['work_phones'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('work_phones'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('contact_email') ? 'error' : ''; ?>">
				<?php echo form_label('contact_email', 'vendors_contact_email', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendors_contact_email' type='text' name='vendors_contact_email' maxlength="255" value="<?php echo set_value('vendors_contact_email', isset($vendors['contact_email']) ? $vendors['contact_email'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('contact_email'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('website_url') ? 'error' : ''; ?>">
				<?php echo form_label('Website URL', 'vendors_website_url', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendors_website_url' type='text' name='vendors_website_url' maxlength="255" value="<?php echo set_value('vendors_website_url', isset($vendors['website_url']) ? $vendors['website_url'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('website_url'); ?></span>
				</div>
			</div>

			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('vendors_action_edit'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/developer/vendors', lang('vendors_cancel'), 'class="btn btn-warning"'); ?>
				
			<?php if ($this->auth->has_permission('Vendors.Developer.Delete')) : ?>
				or
				<button type="submit" name="delete" class="btn btn-danger" id="delete-me" onclick="return confirm('<?php e(js_escape(lang('vendors_delete_confirm'))); ?>'); ">
					<span class="icon-trash icon-white"></span>&nbsp;<?php echo lang('vendors_delete_record'); ?>
				</button>
			<?php endif; ?>
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>