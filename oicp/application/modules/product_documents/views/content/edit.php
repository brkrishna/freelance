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
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>
            

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					11 => 11,
				);
				echo form_dropdown(array('name' => 'product_id', 'required' => 'required'), $options, set_value('product_id', isset($product_documents->product_id) ? $product_documents->product_id : ''), 'Product. lang('bf_form_label_required')');
			?>

			<div class="control-group<?php echo form_error('doc_name') ? ' error' : ''; ?>">
				<?php echo form_label('Document Name', 'doc_name', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='doc_name' type='text' name='doc_name' maxlength='255' value="<?php echo set_value('doc_name', isset($product_documents->doc_name) ? $product_documents->doc_name : ''); ?>" />
					<span class='help-inline'><?php echo form_error('doc_name'); ?></span>
				</div>
			</div>

			<div class="control-group<?php echo form_error('doc_file') ? ' error' : ''; ?>">
				<?php echo form_label('File', 'doc_file', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='doc_file' type='text' name='doc_file' maxlength='4000' value="<?php echo set_value('doc_file', isset($product_documents->doc_file) ? $product_documents->doc_file : ''); ?>" />
					<span class='help-inline'><?php echo form_error('doc_file'); ?></span>
				</div>
			</div>

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
					255 => 255,
				);
				echo form_dropdown(array('name' => 'archive', 'required' => 'required'), $options, set_value('archive', isset($product_documents->archive) ? $product_documents->archive : ''), 'Archive. lang('bf_form_label_required')');
			?>
        </fieldset>
		<fieldset class='form-actions'>
			<input type='submit' name='save' class='btn btn-primary' value="<?php echo lang('product_documents_action_edit'); ?>" />
			<?php echo lang('bf_or'); ?>
			<?php echo anchor(SITE_AREA . '/content/product_documents', lang('product_documents_cancel'), 'class="btn btn-warning"'); ?>
			
			<?php if ($this->auth->has_permission('Product_Documents.Content.Delete')) : ?>
				<?php echo lang('bf_or'); ?>
				<button type='submit' name='delete' formnovalidate class='btn btn-danger' id='delete-me' onclick="return confirm('<?php e(js_escape(lang('product_documents_delete_confirm'))); ?>');">
					<span class='icon-trash icon-white'></span>&nbsp;<?php echo lang('product_documents_delete_record'); ?>
				</button>
			<?php endif; ?>
		</fieldset>
    <?php echo form_close(); ?>
</div>