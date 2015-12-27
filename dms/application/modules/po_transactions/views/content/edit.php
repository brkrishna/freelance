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

if (isset($po_transactions))
{
	$po_transactions = (array) $po_transactions;
}
$id = isset($po_transactions['id']) ? $po_transactions['id'] : '';

?>
<div class="admin-box">
	<h3>PO Transactions</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<?php // Change the values in this array to populate your dropdown as required
				if (is_array($po_ref_select) && count($po_ref_select)) :		
					echo form_dropdown('po_transactions_po_ref', $po_ref_select, set_value('po_transactions_po_ref', isset($po_transaactions['po_ref']) ? $po_transactions['po_ref'] : ''), 'Po Ref'. lang('bf_form_label_required'));
				endif;
			?>

			<?php // Change the values in this array to populate your dropdown as required
			     $options = array(
					'Inbound' => 'Inbound',
					'Outbound' => 'Outbound',
					
				);

            
            echo form_dropdown('po_transactions_trans_type', $options, set_value('po_transactions_trans_type', isset($po_transactions['trans_type']) ? $po_transactions['trans_type'] : ''), 'Trans Type'. lang('bf_form_label_required'));
			?>

			<div class="control-group <?php echo form_error('remit_date') ? 'error' : ''; ?>">
				<?php echo form_label('Date Remitted', 'po_transactions_remit_date', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='po_transactions_remit_date' type='text' name='po_transactions_remit_date'  value="<?php echo set_value('po_transactions_remit_date', isset($po_transactions['remit_date']) ? $po_transactions['remit_date'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('remit_date'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('rcvd_date') ? 'error' : ''; ?>">
				<?php echo form_label('Date Received', 'po_transactions_rcvd_date', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='po_transactions_rcvd_date' type='text' name='po_transactions_rcvd_date'  value="<?php echo set_value('po_transactions_rcvd_date', isset($po_transactions['rcvd_date']) ? $po_transactions['rcvd_date'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('rcvd_date'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('amount') ? 'error' : ''; ?>">
				<?php echo form_label('Amount', 'po_transactions_amount', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='po_transactions_amount' type='text' name='po_transactions_amount' maxlength="19" value="<?php echo set_value('po_transactions_amount', isset($po_transactions['amount']) ? $po_transactions['amount'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('amount'); ?></span>
				</div>
			</div>

			 <?php // Change the values in this array to populate your dropdown as required
                        if (is_array($vendors_select) && count($vendors_select)) :
                            echo form_dropdown('po_transactions_vendor_id', $vendors_select, set_value('po_transactions_vendor_id', isset($po_transactions['vendor_id']) ? $po_transactions['vendor_id'] : ''), 'Vendor'. lang('bf_form_label_required'), 'tabindex="1"');
                        endif;
                    ?>


			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('po_transactions_action_edit'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/po_transactions', lang('po_transactions_cancel'), 'class="btn btn-warning"'); ?>
				
			<?php if ($this->auth->has_permission('PO_Transactions.Content.Delete')) : ?>
				or
				<button type="submit" name="delete" class="btn btn-danger" id="delete-me" onclick="return confirm('<?php e(js_escape(lang('po_transactions_delete_confirm'))); ?>'); ">
					<span class="icon-trash icon-white"></span>&nbsp;<?php echo lang('po_transactions_delete_record'); ?>
				</button>
			<?php endif; ?>
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>