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

if (isset($po_containers))
{
	$po_containers = (array) $po_containers;
}
$id = isset($po_containers['id']) ? $po_containers['id'] : '';

?>
<div class="admin-box">
	<h3>PO Containers</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($pos_select) && count($pos_select)) :    
				    echo form_dropdown('po_containers_po_no', $pos_select, set_value('po_containers_po_no', isset($po_containers['po_no']) ? $po_containers['po_no'] : ''), 'PO No'. lang('bf_form_label_required'));
                endif;
			?>

			<div class="control-group <?php echo form_error('batch_no') ? 'error' : ''; ?>">
				<?php echo form_label('Batch No'. lang('bf_form_label_required'), 'po_containers_batch_no', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='po_containers_batch_no' type='text' name='po_containers_batch_no' maxlength="255" value="<?php echo set_value('po_containers_batch_no', isset($po_containers['batch_no']) ? $po_containers['batch_no'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('batch_no'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('vessel') ? 'error' : ''; ?>">
				<?php echo form_label('Vessel', 'po_containers_vessel', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='po_containers_vessel' type='text' name='po_containers_vessel' maxlength="255" value="<?php echo set_value('po_containers_vessel', isset($po_containers['vessel']) ? $po_containers['vessel'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('vessel'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('container') ? 'error' : ''; ?>">
				<?php echo form_label('Container', 'po_containers_container', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='po_containers_container' type='text' name='po_containers_container' maxlength="255" value="<?php echo set_value('po_containers_container', isset($po_containers['container']) ? $po_containers['container'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('container'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('seal') ? 'error' : ''; ?>">
				<?php echo form_label('Seal', 'po_containers_seal', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='po_containers_seal' type='text' name='po_containers_seal' maxlength="255" value="<?php echo set_value('po_containers_seal', isset($po_containers['seal']) ? $po_containers['seal'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('seal'); ?></span>
				</div>
			</div>

			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('po_containers_action_edit'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/po_containers', lang('po_containers_cancel'), 'class="btn btn-warning"'); ?>
				
			<?php if ($this->auth->has_permission('PO_Containers.Content.Delete')) : ?>
				or
				<button type="submit" name="delete" class="btn btn-danger" id="delete-me" onclick="return confirm('<?php e(js_escape(lang('po_containers_delete_confirm'))); ?>'); ">
					<span class="icon-trash icon-white"></span>&nbsp;<?php echo lang('po_containers_delete_record'); ?>
				</button>
			<?php endif; ?>
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>