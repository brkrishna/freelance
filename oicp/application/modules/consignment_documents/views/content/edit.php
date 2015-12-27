<?php

$validation_errors = validation_errors();

if ($validation_errors) :
?>
<div class='alert alert-block alert-error fade in'>
	<a class='close' data-dismiss='alert'>&times;</a>
	<h4 class='alert-heading'>
		<?php echo lang('consignment_documents_errors_message'); ?>
	</h4>
	<?php echo $validation_errors; ?>
</div>
<?php
endif;

$id = isset($consignment_documents->id) ? $consignment_documents->id : '';

?>
<div class='admin-box'>
	<h3>Consignment Documents</h3>
	<?php echo form_open_multipart($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>
            
			<?php // Change the values in this array to populate your dropdown as required
				if (is_array($consign_select) && count($consign_select)) :			
					echo form_dropdown(array('name' => 'ref_no', 'required' => 'required'), $consign_select, set_value('ref_no', isset($consignment_documents->ref_no) ? $consignment_documents->ref_no : ''), 'Ref No' . lang('bf_form_label_required'));
				endif;
			?>

			<div class="control-group<?php echo form_error('doc_name') ? ' error' : ''; ?>">
				<?php echo form_label('Document'. lang('bf_form_label_required'), 'doc_name', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='doc_name' type='text' required='required' name='doc_name' maxlength='255' value="<?php echo set_value('doc_name', isset($consignment_documents->doc_name) ? $consignment_documents->doc_name : ''); ?>" />
					<span class='help-inline'><?php echo form_error('doc_name'); ?></span>
				</div>
			</div>

			<!--Document -->
            <?php if(isset($consignment_documents) && isset($consignment_documents->doc_file) && !empty($consignment_documents->doc_file)) : $attachment = unserialize($consignment_documents->doc_file);
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
                                
                            </li>
                        </ul>
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

			<div class="control-group<?php echo form_error('rcvd_on') ? ' error' : ''; ?>">
				<?php echo form_label('Received on'. lang('bf_form_label_required'), 'rcvd_on', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='rcvd_on' type='text' required='required' name='rcvd_on' maxlength='25' value="<?php echo set_value('rcvd_on', isset($consignment_documents->rcvd_on) ? $consignment_documents->rcvd_on : ''); ?>" />
					<span class='help-inline'><?php echo form_error('rcvd_on'); ?></span>
				</div>
			</div>

			<div class="control-group<?php echo form_error('comments') ? ' error' : ''; ?>">
				<?php echo form_label('Comments', 'comments', array('class' => 'control-label')); ?>
				<div class='controls'>
					<?php echo form_textarea(array('name' => 'comments', 'id' => 'comments', 'rows' => '5', 'cols' => '80', 'value' => set_value('comments', isset($consignment_documents->comments) ? $consignment_documents->comments : ''))); ?>
					<span class='help-inline'><?php echo form_error('comments'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'No' => 'No',
					'Yes' => 'Yes'
				);
				echo form_dropdown(array('name' => 'archive', 'required' => 'required'), $options, set_value('archive', isset($consignment_documents->archive) ? $consignment_documents->archive : ''), 'Archive' . lang('bf_form_label_required'));
			?>
		</fieldset>
		<fieldset class='form-actions'>
			<input type='submit' name='save' class='btn btn-primary' value="<?php echo lang('consignment_documents_action_edit'); ?>" />
			<?php echo lang('bf_or'); ?>
			<?php echo anchor(SITE_AREA . '/content/consignment_documents', lang('consignment_documents_cancel'), 'class="btn btn-warning"'); ?>
			
			<?php if ($this->auth->has_permission('Consignment_Documents.Content.Delete')) : ?>
				<?php echo lang('bf_or'); ?>
				<button type='submit' name='delete' formnovalidate class='btn btn-danger' id='delete-me' onclick="return confirm('<?php e(js_escape(lang('consignment_documents_delete_confirm'))); ?>');">
					<span class='icon-trash icon-white'></span>&nbsp;<?php echo lang('consignment_documents_delete_record'); ?>
				</button>
			<?php endif; ?>
		</fieldset>
    <?php echo form_close(); ?>
</div>