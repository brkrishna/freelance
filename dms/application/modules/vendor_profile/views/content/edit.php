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

if (isset($vendor_profile))
{
	$vendor_profile = (array) $vendor_profile;
}
$id = isset($vendor_profile['id']) ? $vendor_profile['id'] : '';

?>
<div class="admin-box">
	<h3>Vendor Profile</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<div class="control-group <?php echo form_error('name') ? 'error' : ''; ?>">
				<?php echo form_label('Name'. lang('bf_form_label_required'), 'vendor_profile_name', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendor_profile_name' type='text' name='vendor_profile_name' maxlength="255" value="<?php echo set_value('vendor_profile_name', isset($vendor_profile['name']) ? $vendor_profile['name'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('name'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'-1' => 'Select one',
                    'Agent' => 'Agent',
                    'Dealer' => 'Dealer',
                    'Distributor' => 'Distributor',
                    'Manufacturer' => 'Manufacturer',
                    'Trader' => 'Trader',
                    'Others' => 'Others',
				);

				echo form_dropdown('vendor_profile_est_type', $options, set_value('vendor_profile_est_type', isset($vendor_profile['est_type']) ? $vendor_profile['est_type'] : ''), 'Establishment Type'. lang('bf_form_label_required'));
			?>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'-1' => 'Select one',
                    'Proprietary' => 'Proprietary',
                    'Partnership' => 'Partnership',
                    'Private Limited' => 'Private Limited',
                    'Public Limited' => 'Public Limited',
                    'Others' => 'Others',
				);

				echo form_dropdown('vendor_profile_est_const', $options, set_value('vendor_profile_est_const', isset($vendor_profile['est_const']) ? $vendor_profile['est_const'] : ''), 'Constitution of Company'. lang('bf_form_label_required'));
			?>

			<div class="control-group <?php echo form_error('est_start_yr') ? 'error' : ''; ?>">
				<?php echo form_label('Year of Establishment'. lang('bf_form_label_required'), 'vendor_profile_est_start_yr', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendor_profile_est_start_yr' type='text' name='vendor_profile_est_start_yr'  value="<?php echo set_value('vendor_profile_est_start_yr', isset($vendor_profile['est_start_yr']) ? $vendor_profile['est_start_yr'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('est_start_yr'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('website') ? 'error' : ''; ?>">
				<?php echo form_label('Website URL', 'vendor_profile_website', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='vendor_profile_website' type='text' name='vendor_profile_website' maxlength="255" value="<?php echo set_value('vendor_profile_website', isset($vendor_profile['website']) ? $vendor_profile['website'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('website'); ?></span>
				</div>
			</div>
            
			<div class="control-group <?php echo form_error('profile') ? 'error' : ''; ?>">
				<?php echo form_label('Profile', 'vendor_profile_profile', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<?php echo form_textarea( array( 'name' => 'vendor_profile_profile', 'id' => 'vendor_profile_profile', 'rows' => '5', 'cols' => '80', 'value' => set_value('vendor_profile_profile', isset($vendor_profile['profile']) ? $vendor_profile['profile'] : '') ) ); ?>
					<span class='help-inline'><?php echo form_error('profile'); ?></span>
				</div>
			</div>
            
			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('vendor_profile_action_edit'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/vendor_profile', lang('vendor_profile_cancel'), 'class="btn btn-warning"'); ?>
				
			<?php if ($this->auth->has_permission('Vendor_Profile.Content.Delete')) : ?>
				or
				<button type="submit" name="delete" class="btn btn-danger" id="delete-me" onclick="return confirm('<?php e(js_escape(lang('vendor_profile_delete_confirm'))); ?>'); ">
					<span class="icon-trash icon-white"></span>&nbsp;<?php echo lang('vendor_profile_delete_record'); ?>
				</button>
			<?php endif; ?>
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>