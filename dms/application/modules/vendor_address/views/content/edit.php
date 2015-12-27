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

if (isset($vendor_address))
{
	$vendor_address = (array) $vendor_address;
}
$id = isset($vendor_address['id']) ? $vendor_address['id'] : '';

?>
<div class="admin-box">
	<h3>Vendor Address</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($vendors_select) && count($vendors_select)) :
				    echo form_dropdown('vendor_address_vendor_id', $vendors_select, set_value('vendor_address_vendor_id', isset($vendor_address['vendor_id']) ? $vendor_address['vendor_id'] : ''), 'Vendor');
                endif;
			?>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'Registered Office' => 'Registered Office',
                    'Branch Office' => 'Branch Office',
                    'Godown' => 'Godown',
                    'Others' => 'Others'
				);

				echo form_dropdown('vendor_address_loc_type', $options, set_value('vendor_address_loc_type', isset($vendor_address['loc_type']) ? $vendor_address['loc_type'] : ''), 'Location Type'. lang('bf_form_label_required'));
			?>

			<div class="control-group <?php echo form_error('vendor_address_address1') ? 'error' : ''; ?>">
				<?php echo form_label('Address1'. lang('bf_form_label_required'), 'vendor_address_address1', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendor_address_address1' type='text' name='vendor_address_address1' maxlength="255" value="<?php echo set_value('vendor_address_address1', isset($vendor_address['address1']) ? $vendor_address['address1'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('vendor_address_address1'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('vendor_address_address2') ? 'error' : ''; ?>">
				<?php echo form_label('Address2', 'vendor_address_address2', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendor_address_address2' type='text' name='vendor_address_address2' maxlength="255" value="<?php echo set_value('vendor_address_address2', isset($vendor_address['address2']) ? $vendor_address['address2'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('vendor_address_address2'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('vendor_address_city') ? 'error' : ''; ?>">
				<?php echo form_label('City', 'vendor_address_city', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendor_address_city' type='text' name='vendor_address_city' maxlength="255" value="<?php echo set_value('vendor_address_city', isset($vendor_address['city']) ? $vendor_address['city'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('vendor_address_city'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($countries_select) && count($countries_select)) :
				    echo form_dropdown('vendor_address_country_id', $countries_select, set_value('vendor_address_country_id', isset($vendor_address['country_id']) ? $vendor_address['country_id'] : ''), 'Country'. lang('bf_form_label_required'));
                endif;
			?>

			<div class="control-group <?php echo form_error('vendor_address_office_phones') ? 'error' : ''; ?>">
				<?php echo form_label('Office Phones', 'vendor_address_office_phones', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendor_address_office_phones' type='text' name='vendor_address_office_phones' maxlength="255" value="<?php echo set_value('vendor_address_office_phones', isset($vendor_address['office_phones']) ? $vendor_address['office_phones'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('vendor_address_office_phones'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('vendor_address_office_fax') ? 'error' : ''; ?>">
				<?php echo form_label('Website URL', 'vendor_address_office_fax', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendor_address_office_fax' type='text' name='vendor_address_office_fax' maxlength="255" value="<?php echo set_value('vendor_address_office_fax', isset($vendor_address['office_fax']) ? $vendor_address['office_fax'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('vendor_address_office_fax'); ?></span>
				</div>
			</div>

			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('vendor_address_action_edit'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/vendor_address', lang('vendor_address_cancel'), 'class="btn btn-warning"'); ?>
				
			<?php if ($this->auth->has_permission('Vendor_Address.Content.Delete')) : ?>
				or
				<button type="submit" name="delete" class="btn btn-danger" id="delete-me" onclick="return confirm('<?php e(js_escape(lang('vendor_address_delete_confirm'))); ?>'); ">
					<span class="icon-trash icon-white"></span>&nbsp;<?php echo lang('vendor_address_delete_record'); ?>
				</button>
			<?php endif; ?>
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>