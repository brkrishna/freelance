<?php

$validation_errors = validation_errors();

if ($validation_errors) :
?>
<div class='alert alert-block alert-error fade in'>
	<a class='close' data-dismiss='alert'>&times;</a>
	<h4 class='alert-heading'>
		<?php echo lang('product_documents_errors_message'); ?>
	</h4>
	<?php echo $validation_errors; ?>
</div>
<?php
endif;

$id = isset($product_documents->id) ? $product_documents->id : '';

?>
<div class='admin-box'>
	<h3>Product Documents</h3>
	<?php echo form_open_multipart($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>
            

			<?php // Change the values in this array to populate your dropdown as required
				if (is_array($products_select) && count($products_select)) :	
					echo form_dropdown(array('name' => 'product_id', 'required' => 'required'), $products_select, set_value('product_id', isset($product_documents->product_id) ? $product_documents->product_id : ''), 'Product' . lang('bf_form_label_required'));
				endif;
			?>

			<div class="control-group<?php echo form_error('doc_name') ? ' error' : ''; ?>">
				<?php echo form_label('Document Name', 'doc_name', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='doc_name' type='text' name='doc_name' maxlength='255' value="<?php echo set_value('doc_name', isset($product_documents->doc_name) ? $product_documents->doc_name : ''); ?>" />
					<span class='help-inline'><?php echo form_error('doc_name'); ?></span>
				</div>
			</div>

			<!--Document -->
            <?php if(isset($product_documents) && isset($product_documents['doc_file']) && !empty($product_documents['doc_file'])) : $attachment = unserialize($product_documents['doc_file']);
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
                                <!--<p><?php echo anchor(SITE_AREA.'/content/product_documents/remove_attachment/'.$product_documents['id'],'Remove', 'class="btn btn-small btn-danger"'); ?></p>-->
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
					<input id='rcvd_on' type='text' name='rcvd_on' maxlength='25' value="<?php echo set_value('rcvd_on', isset($product_documents->rcvd_on) ? $product_documents->rcvd_on : ''); ?>" />
					<span class='help-inline'><?php echo form_error('rcvd_on'); ?></span>
				</div>
			</div>

			<div class="control-group<?php echo form_error('comments') ? ' error' : ''; ?>">
				<?php echo form_label('Comments', 'comments', array('class' => 'control-label')); ?>
				<div class='controls'>
					<?php echo form_textarea(array('name' => 'comments', 'id' => 'comments', 'rows' => '5', 'cols' => '80', 'value' => set_value('comments', isset($product_documents->comments) ? $product_documents->comments : ''))); ?>
					<span class='help-inline'><?php echo form_error('comments'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'No'=>'No',
					'Yes'=>'Yes'
				);
				echo form_dropdown(array('name' => 'archive', 'required' => 'required'), $options, set_value('archive', isset($product_documents->archive) ? $product_documents->archive : ''), 'Archive' . lang('bf_form_label_required'));
			?>
        </fieldset>
		<fieldset class='form-actions'>
			<input type='submit' name='save' class='btn btn-primary' value="<?php echo lang('product_documents_action_create'); ?>" />
			<?php echo lang('bf_or'); ?>
			<?php echo anchor(SITE_AREA . '/content/product_documents', lang('product_documents_cancel'), 'class="btn btn-warning"'); ?>
			
		</fieldset>
    <?php echo form_close(); ?>
</div>