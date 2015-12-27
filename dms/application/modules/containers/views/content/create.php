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

if (isset($containers))
{
	$containers = (array) $containers;
}
$id = isset($containers['id']) ? $containers['id'] : '';

?>
<div class="admin-box">
	<h3>Containers</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<?php // Change the values in this array to populate your dropdown as required
				if (is_array($po_refs_select) && count($po_refs_select)) :	
					echo form_dropdown('containers_po_ref', $po_refs_select, set_value('containers_po_ref', isset($containers['po_ref']) ? $containers['po_ref'] : ''), 'PO Ref'. lang('bf_form_label_required'));
				endif;
			?>

			<div class="control-group <?php echo form_error('container_no') ? 'error' : ''; ?>">
				<?php echo form_label('Container No'. lang('bf_form_label_required'), 'containers_container_no', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='containers_container_no' type='text' name='containers_container_no' maxlength="255" value="<?php echo set_value('containers_container_no', isset($containers['container_no']) ? $containers['container_no'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('container_no'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('seal') ? 'error' : ''; ?>">
				<?php echo form_label('Seal'. lang('bf_form_label_required'), 'containers_seal', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='containers_seal' type='text' name='containers_seal' maxlength="255" value="<?php echo set_value('containers_seal', isset($containers['seal']) ? $containers['seal'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('seal'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
				if (is_array($countries_select) && count($countries_select)) :	
					echo form_dropdown('containers_origin', $countries_select, set_value('containers_origin', isset($containers['origin']) ? $containers['origin'] : ''), 'Origin'. lang('bf_form_label_required'));
				endif;
			?>

			<div class="control-group <?php echo form_error('batch_nos') ? 'error' : ''; ?>">
				<?php echo form_label('Batch Numbers', 'containers_batch_nos', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='containers_batch_nos' type='text' name='containers_batch_nos' maxlength="255" value="<?php echo set_value('containers_batch_nos', isset($containers['batch_nos']) ? $containers['batch_nos'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('batch_nos'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
				if (is_array($products_select) && count($products_select)) :	
					echo form_dropdown('containers_product_id', $products_select, set_value('containers_product_id', isset($containers['product_id']) ? $containers['product_id'] : ''), 'Product'. lang('bf_form_label_required'));
				endif;
			?>

			<div class="control-group <?php echo form_error('quantity') ? 'error' : ''; ?>">
				<?php echo form_label('Quantity', 'containers_quantity', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='containers_quantity' type='text' name='containers_quantity' maxlength="19" value="<?php echo set_value('containers_quantity', isset($containers['quantity']) ? $containers['quantity'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('quantity'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
				if (is_array($uoms_select) && count($uoms_select)) :
					echo form_dropdown('containers_uom_id', $uoms_select, set_value('containers_uom_id', isset($containers['uom_id']) ? $containers['uom_id'] : ''), 'UOM');
				endif;
			?>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'Loading' => 'Loading',
					'In Transit' => 'In Transit',
					'Delivered' => 'Deliverd',
				);

				echo form_dropdown('containers_status', $options, set_value('containers_status', isset($containers['status']) ? $containers['status'] : ''), 'Status'. lang('bf_form_label_required'));
			?>

			<div class="control-group <?php echo form_error('started_on') ? 'error' : ''; ?>">
				<?php echo form_label('Started on'. lang('bf_form_label_required'), 'containers_started_on', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='containers_started_on' type='text' name='containers_started_on'  value="<?php echo set_value('containers_started_on', isset($containers['started_on']) ? $containers['started_on'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('started_on'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('arrived_on') ? 'error' : ''; ?>">
				<?php echo form_label('Arrived On', 'containers_arrived_on', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='containers_arrived_on' type='text' name='containers_arrived_on'  value="<?php echo set_value('containers_arrived_on', isset($containers['arrived_on']) ? $containers['arrived_on'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('arrived_on'); ?></span>
				</div>
			</div>

			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('containers_action_create'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/containers', lang('containers_cancel'), 'class="btn btn-warning"'); ?>
				
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>