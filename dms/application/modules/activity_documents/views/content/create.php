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

if (isset($activity_documents))
{
	$activity_documents = (array) $activity_documents;
}
$id = isset($activity_documents['id']) ? $activity_documents['id'] : '';

?>
<div class="admin-box">
	<h3>Activity Documents</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($activity_types_select) && count($activity_types_select)) :
				    echo form_dropdown('activity_documents_activity_code', $activity_types_select, set_value('activity_documents_activity_code', isset($activity_documents['activity_code']) ? $activity_documents['activity_code'] : ''), 'Activity Code'. lang('bf_form_label_required'));
                endif;
			?>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($products_select) && count($products_select)) :
    				echo form_dropdown('activity_documents_product_id', $products_select, set_value('activity_documents_product_id', isset($activity_documents['product_id']) ? $activity_documents['product_id'] : ''), 'Product'. lang('bf_form_label_required'));
                endif;
			?>

            <?php // Change the values in this array to populate your dropdown as required
                if (is_array($doc_types_select) && count($doc_types_select)) :
    				echo form_dropdown('activity_documents_document_id', $doc_types_select, set_value('activity_documents_document_id', isset($activity_documents['document_id']) ? $activity_documents['document_id'] : ''), 'Document'. lang('bf_form_label_required'));
                endif;
			?>
            
			<div class="control-group <?php echo form_error('activity_documents_sno') ? 'error' : ''; ?>">
				<?php echo form_label('Serial No'. lang('bf_form_label_required'), 'activity_documents_sno', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='activity_documents_sno' type='text' name='activity_documents_sno' maxlength="10" value="<?php echo set_value('activity_documents_sno', isset($activity_documents['sno']) ? $activity_documents['sno'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('activity_documents_sno'); ?></span>
				</div>
			</div>

			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('activity_documents_action_create'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/activity_documents', lang('activity_documents_cancel'), 'class="btn btn-warning"'); ?>
				
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>