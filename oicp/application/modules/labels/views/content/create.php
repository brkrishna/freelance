<?php

$validation_errors = validation_errors();

if ($validation_errors) :
?>
<div class='alert alert-block alert-error fade in'>
	<a class='close' data-dismiss='alert'>&times;</a>
	<h4 class='alert-heading'>
		<?php echo lang('labels_errors_message'); ?>
	</h4>
	<?php echo $validation_errors; ?>
</div>
<?php
endif;

$id = isset($labels->id) ? $labels->id : '';

?>
<div class='admin-box'>
	<h3>Labels</h3>
	<?php echo form_open_multipart($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>
            

			<?php // Change the values in this array to populate your dropdown as required
				if (is_array($products_select) && count($products_select)) :	
					echo form_dropdown(array('name' => 'product_id', 'required' => 'required'), $products_select, set_value('product_id', isset($labels->product_id) ? $labels->product_id : ''), 'Product' . lang('bf_form_label_required'));
				endif;			
			?>

			<div class="control-group<?php echo form_error('label') ? ' error' : ''; ?>">
				<?php echo form_label('Label'. lang('bf_form_label_required'), 'label', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='label' type='text' required='required' name='label' maxlength='255' value="<?php echo set_value('label', isset($labels->label) ? $labels->label : ''); ?>" />
					<span class='help-inline'><?php echo form_error('label'); ?></span>
				</div>
			</div>

			<div class="control-group<?php echo form_error('doc_name') ? ' error' : ''; ?>">
				<?php echo form_label('Document'. lang('bf_form_label_required'), 'doc_name', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='doc_name' type='text' required='required' name='doc_name' maxlength='255' value="<?php echo set_value('doc_name', isset($labels->doc_name) ? $labels->doc_name : ''); ?>" />
					<span class='help-inline'><?php echo form_error('doc_name'); ?></span>
				</div>
			</div>

			<!--Document -->
            <?php if(isset($labels) && isset($labels['doc_file']) && !empty($labels['doc_file'])) : $attachment = unserialize($labels['doc_file']);
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
                                <p><?php echo anchor(SITE_AREA.'/content/party_documents/remove_attachment/'.$party_documents['id'],'Remove', 'class="btn btn-small btn-danger"'); ?></p>
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
				<?php echo form_label('Received on', 'rcvd_on', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='rcvd_on' type='text' name='rcvd_on' maxlength='25' value="<?php echo set_value('rcvd_on', isset($labels->rcvd_on) ? $labels->rcvd_on : ''); ?>" />
					<span class='help-inline'><?php echo form_error('rcvd_on'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'No' => 'No',
					'Yes' => 'Yes'
				);
				echo form_dropdown(array('name' => 'archive'), $options, set_value('archive', isset($labels->archive) ? $labels->archive : ''), 'Archive');
			?>
        </fieldset>
		<fieldset class='form-actions'>
			<input type='submit' name='save' class='btn btn-primary' value="<?php echo lang('labels_action_create'); ?>" />
			<?php echo lang('bf_or'); ?>
			<?php echo anchor(SITE_AREA . '/content/labels', lang('labels_cancel'), 'class="btn btn-warning"'); ?>
			
		</fieldset>
    <?php echo form_close(); ?>
</div>