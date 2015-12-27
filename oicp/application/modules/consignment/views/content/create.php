<?php

$validation_errors = validation_errors();

if ($validation_errors) :
?>
<div class='alert alert-block alert-error fade in'>
	<a class='close' data-dismiss='alert'>&times;</a>
	<h4 class='alert-heading'>
		<?php echo lang('consignment_errors_message'); ?>
	</h4>
	<?php echo $validation_errors; ?>
</div>
<?php
endif;

$id = isset($consignment->id) ? $consignment->id : '';

?>
<div class='admin-box'>
	<h3>Consignment</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>
            

			<div class="control-group<?php echo form_error('c_date') ? ' error' : ''; ?>">
				<?php echo form_label('Date'. lang('bf_form_label_required'), 'c_date', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='c_date' type='text' required='required' name='c_date' maxlength='25' value="<?php echo set_value('c_date', isset($consignment->c_date) ? $consignment->c_date : ''); ?>" />
					<span class='help-inline'><?php echo form_error('c_date'); ?></span>
				</div>
			</div>

			<div class="control-group<?php echo form_error('ref_no') ? ' error' : ''; ?>">
				<?php echo form_label('Ref No'. lang('bf_form_label_required'), 'ref_no', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='ref_no' type='text' required='required' name='ref_no' maxlength='255' value="<?php echo set_value('ref_no', isset($consignment->ref_no) ? $consignment->ref_no : ''); ?>" />
					<span class='help-inline'><?php echo form_error('ref_no'); ?></span>
				</div>
			</div>

			<div class="control-group<?php echo form_error('narration') ? ' error' : ''; ?>">
				<?php echo form_label('Narration', 'narration', array('class' => 'control-label')); ?>
				<div class='controls'>
					<?php echo form_textarea(array('name' => 'narration', 'id' => 'narration', 'rows' => '5', 'cols' => '80', 'value' => set_value('narration', isset($consignment->narration) ? $consignment->narration : ''))); ?>
					<span class='help-inline'><?php echo form_error('narration'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'No'=>'No',
					'Yes'=>'Yes'
				);
				echo form_dropdown(array('name' => 'archive'), $options, set_value('archive', isset($consignment->archive) ? $consignment->archive : ''), 'Archive');
			?>
        </fieldset>
		<fieldset class='form-actions'>
			<input type='submit' name='save' class='btn btn-primary' value="<?php echo lang('consignment_action_create'); ?>" />
			<?php echo lang('bf_or'); ?>
			<?php echo anchor(SITE_AREA . '/content/consignment', lang('consignment_cancel'), 'class="btn btn-warning"'); ?>
			
		</fieldset>
    <?php echo form_close(); ?>
</div>