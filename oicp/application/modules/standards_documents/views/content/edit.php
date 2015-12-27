<?php

$validation_errors = validation_errors();

if ($validation_errors) :
?>
<div class='alert alert-block alert-error fade in'>
	<a class='close' data-dismiss='alert'>&times;</a>
	<h4 class='alert-heading'>
		<?php echo lang('standards_documents_errors_message'); ?>
	</h4>
	<?php echo $validation_errors; ?>
</div>
<?php
endif;

$id = isset($standards_documents->id) ? $standards_documents->id : '';

?>
<div class='admin-box'>
	<h3>Standards Documents</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>
            

			<div class="control-group<?php echo form_error('doc_name') ? ' error' : ''; ?>">
				<?php echo form_label('Document Name'. lang('bf_form_label_required'), 'doc_name', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='doc_name' type='text' required='required' name='doc_name' maxlength='255' value="<?php echo set_value('doc_name', isset($standards_documents->doc_name) ? $standards_documents->doc_name : ''); ?>" />
					<span class='help-inline'><?php echo form_error('doc_name'); ?></span>
				</div>
			</div>

			<!--Document -->
            <?php if(isset($standards_documents) && isset($standards_documents->doc_file) && !empty($standards_documents->doc_file)) : $attachment = unserialize($standards_documents->doc_file);
            ?>

            <?php if (isset($attachment)) : ?>
                <!-- Current Document Display -->
                <div class="control-group">
                    <label class="control-label">File</label>
                    <div class="controls">
                        <ul class="thumbnails">
                            <li class="span6">
                                <a class="lightbox" href="<?php echo base_url() . '/uploads/' . $attachment['file_name'] ?>" target="_blank" >
                                    <?php echo $attachment['file_name']; ?>
                                </a>
                                <!--<p><?php echo anchor(SITE_AREA.'/content/party_documents/remove_attachment/'.$standards_documents->id,'Remove', 'class="btn btn-small btn-danger"'); ?></p>-->
                            </li>
                        </ul>
                        <input id='doc_file' type='hidden' name='doc_file' value=<?php echo($standards_documents->doc_file); ?>/>
                    </div>
                </div>
                <?php endif; ?>
            <?php else: ?>
                <div class="control-group <?php echo form_error('doc_file') ? 'error' : ''; ?>">
                    <?php echo form_label('File', 'doc_file', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input id='doc_file' type='file' name='doc_file'/>
                        <span class='help-inline'><?php echo form_error('doc_file'); ?></span>
                    </div>
                </div>
            <?php endif; ?>  

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'No'=>'No',
					'Yes'=>'Yes'
				);
				echo form_dropdown(array('name' => 'archive', 'required' => 'required'), $options, set_value('archive', isset($standards_documents->archive) ? $standards_documents->archive : ''), 'Archive' . lang('bf_form_label_required'));
			?>
        </fieldset>
		<fieldset class='form-actions'>
			<input type='submit' name='save' class='btn btn-primary' value="<?php echo lang('standards_documents_action_edit'); ?>" />
			<?php echo lang('bf_or'); ?>
			<?php echo anchor(SITE_AREA . '/content/standards_documents', lang('standards_documents_cancel'), 'class="btn btn-warning"'); ?>
			
			<?php if ($this->auth->has_permission('Standards_Documents.Content.Delete')) : ?>
				<?php echo lang('bf_or'); ?>
				<button type='submit' name='delete' formnovalidate class='btn btn-danger' id='delete-me' onclick="return confirm('<?php e(js_escape(lang('standards_documents_delete_confirm'))); ?>');">
					<span class='icon-trash icon-white'></span>&nbsp;<?php echo lang('standards_documents_delete_record'); ?>
				</button>
			<?php endif; ?>
		</fieldset>
    <?php echo form_close(); ?>
</div>