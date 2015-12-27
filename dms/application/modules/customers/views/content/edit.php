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

if (isset($customers))
{
	$customers = (array) $customers;
}
$id = isset($customers['id']) ? $customers['id'] : '';

?>
<div class="admin-box">
	<h3>Customers</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<div class="control-group <?php echo form_error('name') ? 'error' : ''; ?>">
				<?php echo form_label('Name'. lang('bf_form_label_required'), 'customers_name', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='customers_name' type='text' name='customers_name' maxlength="255" value="<?php echo set_value('customers_name', isset($customers['name']) ? $customers['name'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('name'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('contact_name') ? 'error' : ''; ?>">
				<?php echo form_label('Contact Name'. lang('bf_form_label_required'), 'customers_contact_name', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='customers_contact_name' type='text' name='customers_contact_name' maxlength="255" value="<?php echo set_value('customers_contact_name', isset($customers['contact_name']) ? $customers['contact_name'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('contact_name'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('contact_phone') ? 'error' : ''; ?>">
				<?php echo form_label('Contact Phone', 'customers_contact_phone', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='customers_contact_phone' type='text' name='customers_contact_phone' maxlength="255" value="<?php echo set_value('customers_contact_phone', isset($customers['contact_phone']) ? $customers['contact_phone'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('contact_phone'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('contact_email') ? 'error' : ''; ?>">
				<?php echo form_label('Contact Email', 'customers_contact_email', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='customers_contact_email' type='text' name='customers_contact_email' maxlength="255" value="<?php echo set_value('customers_contact_email', isset($customers['contact_email']) ? $customers['contact_email'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('contact_email'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('address1') ? 'error' : ''; ?>">
				<?php echo form_label('Address1', 'customers_address1', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='customers_address1' type='text' name='customers_address1' maxlength="255" value="<?php echo set_value('customers_address1', isset($customers['address1']) ? $customers['address1'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('address1'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('address2') ? 'error' : ''; ?>">
				<?php echo form_label('Address2', 'customers_address2', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='customers_address2' type='text' name='customers_address2' maxlength="255" value="<?php echo set_value('customers_address2', isset($customers['address2']) ? $customers['address2'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('address2'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('city') ? 'error' : ''; ?>">
				<?php echo form_label('City', 'customers_city', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='customers_city' type='text' name='customers_city' maxlength="255" value="<?php echo set_value('customers_city', isset($customers['city']) ? $customers['city'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('city'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
				if (is_array($countries_select) && count($countries_select)) :
					echo form_dropdown('customers_country', $countries_select, set_value('customers_country', isset($customers['country']) ? $customers['country'] : ''), 'Country');
				endif;
			?>

			<div class="control-group <?php echo form_error('work_phones') ? 'error' : ''; ?>">
				<?php echo form_label('Office Phones', 'customers_work_phones', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='customers_work_phones' type='text' name='customers_work_phones' maxlength="255" value="<?php echo set_value('customers_work_phones', isset($customers['work_phones']) ? $customers['work_phones'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('work_phones'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('website_url') ? 'error' : ''; ?>">
				<?php echo form_label('Website URL', 'customers_website_url', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='customers_website_url' type='text' name='customers_website_url' maxlength="255" value="<?php echo set_value('customers_website_url', isset($customers['website_url']) ? $customers['website_url'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('website_url'); ?></span>
				</div>
			</div>

			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('customers_action_edit'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/customers', lang('customers_cancel'), 'class="btn btn-warning"'); ?>
				
			<?php if ($this->auth->has_permission('Customers.Content.Delete')) : ?>
				or
				<button type="submit" name="delete" class="btn btn-danger" id="delete-me" onclick="return confirm('<?php e(js_escape(lang('customers_delete_confirm'))); ?>'); ">
					<span class="icon-trash icon-white"></span>&nbsp;<?php echo lang('customers_delete_record'); ?>
				</button>
			<?php endif; ?>
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>