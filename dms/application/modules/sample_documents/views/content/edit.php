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
	<?php echo form_open_multipart($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($doc_types_select) && count($doc_types_select)) :
                    echo form_dropdown('sample_documents_doc_type', $doc_types_select, set_value('sample_documents_doc_type', isset($sample_documents['doc_type']) ? $sample_documents['doc_type'] : ''), 'Document Type'. lang('bf_form_label_required'));
                endif;
			?>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($samples_select) && count($samples_select)) :
				    echo form_dropdown('sample_documents_sample_id', $samples_select, set_value('sample_documents_sample_id', isset($sample_documents['sample_id']) ? $sample_documents['sample_id'] : ''), 'Sample'. lang('bf_form_label_required'));
                endif;
			?>

		<!--	<div class="control-group <?php echo form_error('attachment') ? 'error' : ''; ?>">
				<?php echo form_label('Attachment'. lang('bf_form_label_required'), 'sample_documents_attachment', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='sample_documents_attachment' type='file' name='sample_documents_attachment' />
					<span class='help-inline'><?php echo form_error('attachment'); ?></span>
				</div>
			</div>-->
            
			<!-- Current Document -->
			<!--<?php if(isset($sample_documents) && isset($sample_documents['attachment']) && !empty($sample_documents['attachment'])) :
				$attachment = unserialize($sample_documents['attachment']);
			?>-->

			<!-- Current Document Display -->
		<!--	<div class="control-group">
				<label class="control-label">Attachment</label>
				<div class="controls">
					<ul class="thumbnails">
						<li class="span6">
							<a class="lightbox" href="<?php echo base_url() . '/uploads/' . $attachment['file_name'] ?>" target="_blank" >
								<?php echo $attachment['file_name']; ?>
							</a>
							<p><?php echo anchor(SITE_AREA.'/content/sample_documents/remove_attachment/'.$sample_documents['id'],'Remove', 'class="btn btn-small btn-danger"'); ?></p>
							</div>
						</li>
					</ul>
				</div>
			</div>
			<?php endif; ?>

-->
			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('sample_documents_action_edit'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/sample_documents', lang('sample_documents_cancel'), 'class="btn btn-warning"'); ?>
				
			<?php if ($this->auth->has_permission('Sample_Documents.Content.Delete')) : ?>
				or
				<button type="submit" name="delete" class="btn btn-danger" id="delete-me" onclick="return confirm('<?php e(js_escape(lang('sample_documents_delete_confirm'))); ?>'); ">
					<span class="icon-trash icon-white"></span>&nbsp;<?php echo lang('sample_documents_delete_record'); ?>
				</button>
			<?php endif; ?>
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>