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

if (isset($samples))
{
	$samples = (array) $samples;
}
$id = isset($samples['id']) ? $samples['id'] : '';

?>
<div class="admin-box">
	<h3>Samples</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<div class="control-group <?php echo form_error('samples_int_ref_num') ? 'error' : ''; ?>">
				<?php echo form_label('Internal Ref No' . lang('bf_form_label_required'), 'samples_int_ref_num', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='samples_int_ref_num' type='text' name='samples_int_ref_num' maxlength="255" value="<?php echo set_value('samples_int_ref_num', isset($samples['int_ref_num']) ? $samples['int_ref_num'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('samples_int_ref_num'); ?></span>
				</div>
			</div>
            
			<?php // Change the values in this array to populate your dropdown as required
				if (is_array($products_select) && count($products_select)) :
					echo form_dropdown('samples_product_id', $products_select, set_value('samples_product_id', isset($samples['product_id']) ? $samples['product_id'] : ''), 'Product'. lang('bf_form_label_required'));
				endif;
			?>
            
             <div class="control-group <?php echo form_error('po_no') ? 'error' : ''; ?>">
				<?php echo form_label('Po No', 'samples_po_no', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='samples_po_no' type='int' name='samples_po_no'  value="<?php echo set_value('samples_po_no', isset($samples['po_no']) ? $samples['po_no'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('po_no'); ?></span>
				</div>
			</div>
            
             <?php // Change the values in this array to populate your dropdown as required
				if (is_array($party_select) && count($party_select)) :

				echo form_dropdown('samples_party_type', $party_select, set_value('samples_party_type', isset($samples['party_type']) ? $samples['party_type'] : ''), 'Party Type'. lang('bf_form_label_required'));
			    endif; 
			?>  
            
            <?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'Inbound' => 'Inbound',
                    'Outbound' => 'Outbound',
                   
				);

				echo form_dropdown('samples_trans_type', $options, set_value('trans_type', isset($samples['trans_type']) ? $samples['trans_type'] : ''), 'Trans Type'. lang('bf_form_label_required'));
			?>
            
			<div class="control-group <?php echo form_error('samples_quantity') ? 'error' : ''; ?>">
				<?php echo form_label('Quantity' . lang('bf_form_label_required'), 'samples_quantity', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='samples_quantity' type='text' name='samples_quantity' maxlength="19" value="<?php echo set_value('samples_quantity', isset($samples['quantity']) ? $samples['quantity'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('samples_quantity'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
				if (is_array($uoms_select) && count($uoms_select)) :
					echo form_dropdown('samples_uom_id', $uoms_select, set_value('samples_uom_id', isset($samples['uom_id']) ? $samples['uom_id'] : ''), 'UOM' . lang('bf_form_label_required'));
				endif;
			?>

			<?php // Change the values in this array to populate your dropdown as required
				if (is_array($party_select) && count($party_select)) :

				echo form_dropdown('samples_party_name', $party_select, set_value('samples_party_name', isset($samples['party_name']) ? $samples['party_name'] : ''), 'Party Name'. lang('bf_form_label_required'));
			    endif; 
			?>
            
			<div class="control-group <?php echo form_error('samples_courier') ? 'error' : ''; ?>">
				<?php echo form_label('Courier Company' . lang('bf_form_label_required'), 'samples_courier', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='samples_courier' type='text' name='samples_courier' maxlength="255" value="<?php echo set_value('samples_courier', isset($samples['courier']) ? $samples['courier'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('samples_courier'); ?></span>
				</div>
			</div>
            
			<div class="control-group <?php echo form_error('samples_tracking_no') ? 'error' : ''; ?>">
				<?php echo form_label('Tracking No' . lang('bf_form_label_required'), 'samples_tracking_no', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='samples_tracking_no' type='text' name='samples_tracking_no' maxlength="255" value="<?php echo set_value('samples_tracking_no', isset($samples['tracking_no']) ? $samples['tracking_no'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('samples_tracking_no'); ?></span>
				</div>
			</div>
            
			<div class="control-group <?php echo form_error('samples_date_received') ? 'error' : ''; ?>">
				<?php echo form_label('Date Received'  . lang('bf_form_label_required'), 'samples_date_received', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='samples_date_received' type='text' name='samples_date_received'  value="<?php echo set_value('samples_date_received', isset($samples['date_received']) ? $samples['date_received'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('samples_date_received'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('samples_comments') ? 'error' : ''; ?>">
				<?php echo form_label('Comments', 'samples_comments', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<?php echo form_textarea( array( 'name' => 'samples_comments', 'id' => 'samples_comments', 'rows' => '5', 'cols' => '80', 'value' => set_value('samples_comments', isset($samples['comments']) ? $samples['comments'] : '') ) ); ?>
					<span class='help-inline'><?php echo form_error('samples_comments'); ?></span>
				</div>
			</div>
            
            <div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('samples_action_edit'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/samples', lang('samples_cancel'), 'class="btn btn-warning"'); ?>
				
			<?php if ($this->auth->has_permission('Samples.Content.Delete')) : ?>
				or
				<button type="submit" name="delete" class="btn btn-danger" id="delete-me" onclick="return confirm('<?php e(js_escape(lang('samples_delete_confirm'))); ?>'); ">
					<span class="icon-trash icon-white"></span>&nbsp;<?php echo lang('samples_delete_record'); ?>
				</button>
			<?php endif; ?>
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>