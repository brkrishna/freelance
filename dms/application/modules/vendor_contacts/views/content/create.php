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

if (isset($vendor_contacts))
{
	$vendor_contacts = (array) $vendor_contacts;
}
$id = isset($vendor_contacts['id']) ? $vendor_contacts['id'] : '';

?>
<div class="admin-box">
	<h3>Vendor Contacts</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($vendors_select) && count($vendors_select)) :
				    echo form_dropdown('vendor_contacts_vendor_id', $vendors_select, set_value('vendor_contacts_vendor_id', isset($vendor_contacts['vendor_id']) ? $vendor_contacts['vendor_id'] : ''), 'Vendor');
                endif;
			?>
            
			<div class="control-group <?php echo form_error('name') ? 'error' : ''; ?>">
				<?php echo form_label('Name'. lang('bf_form_label_required'), 'vendor_contacts_name', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendor_contacts_name' type='text' name='vendor_contacts_name' maxlength="255" value="<?php echo set_value('vendor_contacts_name', isset($vendor_contacts['name']) ? $vendor_contacts['name'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('name'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('dsgn') ? 'error' : ''; ?>">
				<?php echo form_label('Designation', 'vendor_contacts_dsgn', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendor_contacts_dsgn' type='text' name='vendor_contacts_dsgn' maxlength="255" value="<?php echo set_value('vendor_contacts_dsgn', isset($vendor_contacts['dsgn']) ? $vendor_contacts['dsgn'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('dsgn'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('work_phone') ? 'error' : ''; ?>">
				<?php echo form_label('Office Phone', 'vendor_contacts_work_phone', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendor_contacts_work_phone' type='text' name='vendor_contacts_work_phone' maxlength="255" value="<?php echo set_value('vendor_contacts_work_phone', isset($vendor_contacts['work_phone']) ? $vendor_contacts['work_phone'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('work_phone'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('cell_phone') ? 'error' : ''; ?>">
				<?php echo form_label('Cell Phone', 'vendor_contacts_cell_phone', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendor_contacts_cell_phone' type='text' name='vendor_contacts_cell_phone' maxlength="255" value="<?php echo set_value('vendor_contacts_cell_phone', isset($vendor_contacts['cell_phone']) ? $vendor_contacts['cell_phone'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('cell_phone'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('email_id') ? 'error' : ''; ?>">
				<?php echo form_label('Email', 'vendor_contacts_email_id', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendor_contacts_email_id' type='text' name='vendor_contacts_email_id' maxlength="255" value="<?php echo set_value('vendor_contacts_email_id', isset($vendor_contacts['email_id']) ? $vendor_contacts['email_id'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('email_id'); ?></span>
				</div>
			</div>

			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('vendor_contacts_action_create'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/vendor_contacts', lang('vendor_contacts_cancel'), 'class="btn btn-warning"'); ?>
				
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>