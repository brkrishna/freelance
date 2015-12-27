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

if (isset($bank_details))
{
	$bank_details = (array) $bank_details;
}
$id = isset($bank_details['id']) ? $bank_details['id'] : '';

?>
<div class="admin-box">
	<h3>Bank Details</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<div class="control-group <?php echo form_error('bank_details_bank_name') ? 'error' : ''; ?>">
				<?php echo form_label('Bank Name'. lang('bf_form_label_required'), 'bank_details_bank_name', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='bank_details_bank_name' type='text' name='bank_details_bank_name' maxlength="255" value="<?php echo set_value('bank_details_bank_name', isset($bank_details['bank_name']) ? $bank_details['bank_name'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('bank_details_bank_name'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('bank_details_branch') ? 'error' : ''; ?>">
				<?php echo form_label('Branch'. lang('bf_form_label_required'), 'bank_details_branch', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='bank_details_branch' type='text' name='bank_details_branch' maxlength="255" value="<?php echo set_value('bank_details_bank_name', isset($bank_details['bank_name']) ? $bank_details['bank_name'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('bank_details_branch'); ?></span>
				</div>
			</div>

            <div class="control-group <?php echo form_error('bank_details_address') ? 'error' : ''; ?>">
				<?php echo form_label('Address'. lang('bf_form_label_required'), 'bank_details_address', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='bank_details_address' type='text' name='bank_details_address' maxlength="255" value="<?php echo set_value('bank_details_address', isset($bank_details['address']) ? $bank_details['address'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('bank_details_address'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
				    '-1' => 'Select one',
                    'Current' => 'Current',
                    'Savings' => 'Savings',
                    'Checking' => 'Checking',
                    'Others' => 'Others',
				);

				echo form_dropdown('bank_details_account_type', $options, set_value('bank_details_account_type', isset($bank_details['account_type']) ? $bank_details['account_type'] : ''), 'Account Type'. lang('bf_form_label_required'));
			?>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'-1' => 'Select one',
                    'AUD - Australian Dollar' => 'AUD - Australian Dollar',
                    'CAD - Canada Dollar' => 'CAD - Canada Dollar',
                    'CHF - Switzerland Franc' => 'CHF - Switzerland Franc',
                    'EUR - Euro' => 'EUR - Euro',
                    'GBP - United Kingdom Pound' => 'GBP - United Kingdom Pound',
                    'HKD - Hong Kong Dollar' => 'HKD - Hong Kong Dollar',
                    'INR - Indian Rupee' => 'INR - Indian Rupee',
                    'IDR - Indonesia Rupiah' => 'IDR - Indonesia Rupiah',
                    'JPY - Japan Yen' => 'JPY - Japan Yen',
                    'LKR - Sri Lanka Rupee' => 'LKR - Sri Lanka Rupee',
                    'NZD - New Zealand Dollar' => 'NZD - New Zealand Dollar',
                    'PHP - Philippines Peso' => 'PHP - Philippines Peso',
                    'RUB - Russia Ruble' => 'RUB - Russia Ruble',
                    'SAD - Saudi Arabia Riyal' => 'SAD - Saudi Arabia Riyal',
                    'SGD - Singapore Dollar' => 'SGD - Singapore Dollar',
                    'TWD - Taiwan New Dollar' => 'TWD - Taiwan New Dollar',
                    'THB - Thailand Baht' => 'THB - Thailand Baht',
                    'USD - United States Dollar' => 'USD - United States Dollar',
				);

				echo form_dropdown('bank_details_oper_curr', $options, set_value('bank_details_oper_curr', isset($bank_details['oper_curr']) ? $bank_details['oper_curr'] : ''), 'Operating Currency'. lang('bf_form_label_required'));
			?>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'-1' => 'Select one',
                    'AUD - Australian Dollar' => 'AUD - Australian Dollar',
                    'CAD - Canada Dollar' => 'CAD - Canada Dollar',
                    'CHF - Switzerland Franc' => 'CHF - Switzerland Franc',
                    'EUR - Euro' => 'EUR - Euro',
                    'GBP - United Kingdom Pound' => 'GBP - United Kingdom Pound',
                    'HKD - Hong Kong Dollar' => 'HKD - Hong Kong Dollar',
                    'INR - Indian Rupee' => 'INR - Indian Rupee',
                    'IDR - Indonesia Rupiah' => 'IDR - Indonesia Rupiah',
                    'JPY - Japan Yen' => 'JPY - Japan Yen',
                    'LKR - Sri Lanka Rupee' => 'LKR - Sri Lanka Rupee',
                    'NZD - New Zealand Dollar' => 'NZD - New Zealand Dollar',
                    'PHP - Philippines Peso' => 'PHP - Philippines Peso',
                    'RUB - Russia Ruble' => 'RUB - Russia Ruble',
                    'SAD - Saudi Arabia Riyal' => 'SAD - Saudi Arabia Riyal',
                    'SGD - Singapore Dollar' => 'SGD - Singapore Dollar',
                    'TWD - Taiwan New Dollar' => 'TWD - Taiwan New Dollar',
                    'THB - Thailand Baht' => 'THB - Thailand Baht',
                    'USD - United States Dollar' => 'USD - United States Dollar',
				);

				echo form_dropdown('bank_details_accept_curr', $options, set_value('bank_details_accept_curr', isset($bank_details['accept_curr']) ? $bank_details['accept_curr'] : ''), 'Accepted Currency'. lang('bf_form_label_required'));
			?>

			<div class="control-group <?php echo form_error('bank_details_swift_code') ? 'error' : ''; ?>">
				<?php echo form_label('Swift Code', 'bank_details_swift_code', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='bank_details_swift_code' type='text' name='bank_details_swift_code' maxlength="255" value="<?php echo set_value('bank_details_swift_code', isset($bank_details['swift_code']) ? $bank_details['swift_code'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('bank_details_swift_code'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('bank_details_micr') ? 'error' : ''; ?>">
				<?php echo form_label('MICR (If in India)', 'bank_details_micr', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='bank_details_micr' type='text' name='bank_details_micr' maxlength="255" value="<?php echo set_value('bank_details_micr', isset($bank_details['micr']) ? $bank_details['micr'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('bank_details_micr'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('bank_details_ifsc') ? 'error' : ''; ?>">
				<?php echo form_label('IFSC (If in India)', 'bank_details_ifsc', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='bank_details_ifsc' type='text' name='bank_details_ifsc' maxlength="255" value="<?php echo set_value('bank_details_ifsc', isset($bank_details['ifsc']) ? $bank_details['ifsc'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('bank_details_ifsc'); ?></span>
				</div>
			</div>

			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('bank_details_action_edit'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/bank_details', lang('bank_details_cancel'), 'class="btn btn-warning"'); ?>
				
			<?php if ($this->auth->has_permission('Bank_Details.Content.Delete')) : ?>
				or
				<button type="submit" name="delete" class="btn btn-danger" id="delete-me" onclick="return confirm('<?php e(js_escape(lang('bank_details_delete_confirm'))); ?>'); ">
					<span class="icon-trash icon-white"></span>&nbsp;<?php echo lang('bank_details_delete_record'); ?>
				</button>
			<?php endif; ?>
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>