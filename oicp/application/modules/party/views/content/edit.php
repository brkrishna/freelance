<?php

$validation_errors = validation_errors();

if ($validation_errors) :
?>
<div class='alert alert-block alert-error fade in'>
	<a class='close' data-dismiss='alert'>&times;</a>
	<h4 class='alert-heading'>
		<?php echo lang('party_errors_message'); ?>
	</h4>
	<?php echo $validation_errors; ?>
</div>
<?php
endif;

$id = isset($party->id) ? $party->id : '';

?>
<div class='admin-box'>
	<h3>Party</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>
            

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'Customer'=>'Customer',
                    'Internal'=>'Internal',
                    'Vendor'=>'Vendor',
                    'Unit'=>'Unit'
				);
				echo form_dropdown(array('name' => 'type', 'required' => 'required'), $options, set_value('type', isset($party->type) ? $party->type : ''), 'Type' . lang('bf_form_label_required'));
			?>

			<div class="control-group<?php echo form_error('org_name') ? ' error' : ''; ?>">
				<?php echo form_label('Organization Name'. lang('bf_form_label_required'), 'org_name', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='org_name' type='text' required='required' name='org_name' maxlength='255' value="<?php echo set_value('org_name', isset($party->org_name) ? $party->org_name : ''); ?>" />
					<span class='help-inline'><?php echo form_error('org_name'); ?></span>
				</div>
			</div>

			<div class="control-group<?php echo form_error('contact') ? ' error' : ''; ?>">
				<?php echo form_label('Contact Person'. lang('bf_form_label_required'), 'contact', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='contact' type='text' required='required' name='contact' maxlength='255' value="<?php echo set_value('contact', isset($party->contact) ? $party->contact : ''); ?>" />
					<span class='help-inline'><?php echo form_error('contact'); ?></span>
				</div>
			</div>

			<div class="control-group<?php echo form_error('address') ? ' error' : ''; ?>">
				<?php echo form_label('Address'. lang('bf_form_label_required'), 'address', array('class' => 'control-label')); ?>
				<div class='controls'>
					<?php echo form_textarea(array('name' => 'address', 'id' => 'address', 'rows' => '5', 'cols' => '80', 'value' => set_value('address', isset($party->address) ? $party->address : ''), 'required' => 'required')); ?>
					<span class='help-inline'><?php echo form_error('address'); ?></span>
				</div>
			</div>

			<div class="control-group<?php echo form_error('city') ? ' error' : ''; ?>">
				<?php echo form_label('City', 'city', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='city' type='text' name='city' maxlength='255' value="<?php echo set_value('city', isset($party->city) ? $party->city : ''); ?>" />
					<span class='help-inline'><?php echo form_error('city'); ?></span>
				</div>
			</div>

			<div class="control-group<?php echo form_error('pincode') ? ' error' : ''; ?>">
				<?php echo form_label('Pincode', 'pincode', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='pincode' type='text' name='pincode' maxlength='25' value="<?php echo set_value('pincode', isset($party->pincode) ? $party->pincode : ''); ?>" />
					<span class='help-inline'><?php echo form_error('pincode'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
                    'China'=>'China',
					'India'=>'India',
                    'Philippines'=>'Philippines',
                    'Sri Lanka'=>'Sri Lanka',
                    'USA'=>'USA'
				);
				echo form_dropdown(array('name' => 'country'), $options, set_value('country', isset($party->country) ? $party->country : ''), 'Country');
			?>

			<div class="control-group<?php echo form_error('phone') ? ' error' : ''; ?>">
				<?php echo form_label('Phone', 'phone', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='phone' type='text' name='phone' maxlength='255' value="<?php echo set_value('phone', isset($party->phone) ? $party->phone : ''); ?>" />
					<span class='help-inline'><?php echo form_error('phone'); ?></span>
				</div>
			</div>

			<div class="control-group<?php echo form_error('email') ? ' error' : ''; ?>">
				<?php echo form_label('Email', 'email', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='email' type='text' name='email' maxlength='255' value="<?php echo set_value('email', isset($party->email) ? $party->email : ''); ?>" />
					<span class='help-inline'><?php echo form_error('email'); ?></span>
				</div>
			</div>
        </fieldset>
		<fieldset class='form-actions'>
			<input type='submit' name='save' class='btn btn-primary' value="<?php echo lang('party_action_edit'); ?>" />
			<?php echo lang('bf_or'); ?>
			<?php echo anchor(SITE_AREA . '/content/party', lang('party_cancel'), 'class="btn btn-warning"'); ?>
			
			<?php if ($this->auth->has_permission('Party.Content.Delete')) : ?>
				<?php echo lang('bf_or'); ?>
				<button type='submit' name='delete' formnovalidate class='btn btn-danger' id='delete-me' onclick="return confirm('<?php e(js_escape(lang('party_delete_confirm'))); ?>');">
					<span class='icon-trash icon-white'></span>&nbsp;<?php echo lang('party_delete_record'); ?>
				</button>
			<?php endif; ?>
		</fieldset>
    <?php echo form_close(); ?>
</div>