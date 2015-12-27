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

if (isset($drums))
{
	$drums = (array) $drums;
}
$id = isset($drums['id']) ? $drums['id'] : '';

?>
<div class="admin-box">
	<h3>Drums</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<div class="control-group <?php echo form_error('po_no') ? 'error' : ''; ?>">
				<?php echo form_label('PO No'. lang('bf_form_label_required'), 'drums_po_no', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='drums_po_no' type='text' name='drums_po_no' maxlength="255" value="<?php echo set_value('drums_po_no', isset($drums['po_no']) ? $drums['po_no'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('po_no'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('container_no') ? 'error' : ''; ?>">
				<?php echo form_label('Container No'. lang('bf_form_label_required'), 'drums_container_no', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='drums_container_no' type='text' name='drums_container_no' maxlength="255" value="<?php echo set_value('drums_container_no', isset($drums['container_no']) ? $drums['container_no'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('container_no'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('seal') ? 'error' : ''; ?>">
				<?php echo form_label('Seal No'. lang('bf_form_label_required'), 'drums_seal', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='drums_seal' type='text' name='drums_seal' maxlength="255" value="<?php echo set_value('drums_seal', isset($drums['seal']) ? $drums['seal'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('seal'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('drum_no') ? 'error' : ''; ?>">
				<?php echo form_label('Drum No'. lang('bf_form_label_required'), 'drums_drum_no', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='drums_drum_no' type='text' name='drums_drum_no' maxlength="255" value="<?php echo set_value('drums_drum_no', isset($drums['drum_no']) ? $drums['drum_no'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('drum_no'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($products_select) && count($products_select)) :
				    echo form_dropdown('drums_product_id', $products_select, set_value('drums_product_id', isset($drums['product_id']) ? $drums['product_id'] : ''), 'Product'. lang('bf_form_label_required'));
                endif;
			?>

			<div class="control-group <?php echo form_error('qty') ? 'error' : ''; ?>">
				<?php echo form_label('Quantity'. lang('bf_form_label_required'), 'drums_qty', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='drums_qty' type='text' name='drums_qty' maxlength="19" value="<?php echo set_value('drums_qty', isset($drums['qty']) ? $drums['qty'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('qty'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($uoms_select) && count($uoms_select)) :
				    echo form_dropdown('drums_uom_id', $uoms_select, set_value('drums_uom_id', isset($drums['uom_id']) ? $drums['uom_id'] : ''), 'UOM'. lang('bf_form_label_required'));
                endif;
			?>

            <?php // Change the values in this array to populate your dropdown as required
                $options = array(
                    'In Packing' => 'In Packing',
                    'In Transit' => 'In Transit',
                    'Delivered' => 'Delivered',
                );
                    
                echo form_dropdown('drums_status', $options, set_value('drums_status', isset($drums['drums_status']) ? $drums['drums_status'] : ''), 'Status'. lang('bf_form_label_required'));
            ?>
           
			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('drums_action_create'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/drums', lang('drums_cancel'), 'class="btn btn-warning"'); ?>
				
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>