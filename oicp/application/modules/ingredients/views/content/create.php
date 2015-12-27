<?php

$validation_errors = validation_errors();

if ($validation_errors) :
?>
<div class='alert alert-block alert-error fade in'>
	<a class='close' data-dismiss='alert'>&times;</a>
	<h4 class='alert-heading'>
		<?php echo lang('ingredients_errors_message'); ?>
	</h4>
	<?php echo $validation_errors; ?>
</div>
<?php
endif;

$id = isset($ingredients->id) ? $ingredients->id : '';

?>
<div class='admin-box'>
	<h3>Ingredients</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>
            
			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'-1' => 'Select one',				                 	
					'Extracts'=>'Extracts',
					'Juices'=>'Juices',
					'Coconut' => 'Coconut'
				);
				echo form_dropdown(array('name' => 'classification', 'required' => 'required'), $options, set_value('archive', isset($ingredients->classification) ? $ingredients->classification : ''), 'classification' . lang('bf_form_label_required'));
			?>

			<div class="control-group<?php echo form_error('name') ? ' error' : ''; ?>">
				<?php echo form_label('Name'. lang('bf_form_label_required'), 'name', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='name' type='text' required='required' name='name' maxlength='255' value="<?php echo set_value('name', isset($ingredients->name) ? $ingredients->name : ''); ?>" />
					<span class='help-inline'><?php echo form_error('name'); ?></span>
				</div>
			</div>

			<div class="control-group<?php echo form_error('desc') ? ' error' : ''; ?>">
				<?php echo form_label('Description', 'desc', array('class' => 'control-label')); ?>
				<div class='controls'>
					<?php echo form_textarea(array('name' => 'desc', 'id' => 'desc', 'rows' => '5', 'cols' => '80', 'value' => set_value('desc', isset($ingredients->desc) ? $ingredients->desc : ''))); ?>
					<span class='help-inline'><?php echo form_error('desc'); ?></span>
				</div>
			</div>
        </fieldset>
		<fieldset class='form-actions'>
			<input type='submit' name='save' class='btn btn-primary' value="<?php echo lang('ingredients_action_create'); ?>" />
			<?php echo lang('bf_or'); ?>
			<?php echo anchor(SITE_AREA . '/content/ingredients', lang('ingredients_cancel'), 'class="btn btn-warning"'); ?>
			
		</fieldset>
    <?php echo form_close(); ?>
</div>