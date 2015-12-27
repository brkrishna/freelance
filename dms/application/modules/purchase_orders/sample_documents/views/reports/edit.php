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

if (isset($sample_documents))
{
	$sample_documents = (array) $sample_documents;
}
$id = isset($sample_documents['id']) ? $sample_documents['id'] : '';

?>
<div class="admin-box">
	<h3>Sample Documents</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
				);

				echo form_dropdown('sample_documents_doc_type', $options, set_value('sample_documents_doc_type', isset($sample_documents['doc_type']) ? $sample_documents['doc_type'] : ''), 'Document Type'. lang('bf_form_label_required'));
			?>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
				);

				echo form_dropdown('sample_documents_sample_id', $options, set_value('sample_documents_sample_id', isset($sample_documents['sample_id']) ? $sample_documents['sample_id'] : ''), 'Sample'. lang('bf_form_label_required'));
			?>

			<div class="control-group <?php echo form_error('attachment') ? 'error' : ''; ?>">
				<?php echo form_label('Attachment'. lang('bf_form_label_required'), 'sample_documents_attachment', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='sample_documents_attachment' type='text' name='sample_documents_attachment' maxlength="4000" value="<?php echo set_value('sample_documents_attachment', isset($sample_documents['attachment']) ? $sample_documents['attachment'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('attachment'); ?></span>
				</div>
			</div>

			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('sample_documents_action_edit'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/reports/sample_documents', lang('sample_documents_cancel'), 'class="btn btn-warning"'); ?>
				
			<?php if ($this->auth->has_permission('Sample_Documents.Reports.Delete')) : ?>
				or
				<button type="submit" name="delete" class="btn btn-danger" id="delete-me" onclick="return confirm('<?php e(js_escape(lang('sample_documents_delete_confirm'))); ?>'); ">
					<span class="icon-trash icon-white"></span>&nbsp;<?php echo lang('sample_documents_delete_record'); ?>
				</button>
			<?php endif; ?>
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>