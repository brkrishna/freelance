<?php

$validation_errors = validation_errors();

if ($validation_errors) :
?>
<div class='alert alert-block alert-error fade in'>
	<a class='close' data-dismiss='alert'>&times;</a>
	<h4 class='alert-heading'>
		<?php echo lang('products_errors_message'); ?>
	</h4>
	<?php echo $validation_errors; ?>
</div>
<?php
endif;

$id = isset($products->id) ? $products->id : '';

?>
<div class='admin-box'>
	<h3>Products</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>
            

			<div class="control-group<?php echo form_error('name') ? ' error' : ''; ?>">
				<?php echo form_label('Name'. lang('bf_form_label_required'), 'name', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='name' type='text' required='required' name='name' maxlength='255' value="<?php echo set_value('name', isset($products->name) ? $products->name : ''); ?>" />
					<span class='help-inline'><?php echo form_error('name'); ?></span>
				</div>
			</div>

			<div class="control-group<?php echo form_error('desc') ? ' error' : ''; ?>">
				<?php echo form_label('Description', 'desc', array('class' => 'control-label')); ?>
				<div class='controls'>
					<?php echo form_textarea(array('name' => 'desc', 'id' => 'desc', 'rows' => '5', 'cols' => '80', 'value' => set_value('desc', isset($products->desc) ? $products->desc : ''))); ?>
					<span class='help-inline'><?php echo form_error('desc'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'Multi Ingredient' => 'Multi Ingredient',
                    'Single Ingredient' => 'Single Ingredient'
				);
				echo form_dropdown(array('name' => 'class', 'required' => 'required'), $options, set_value('class', isset($products->class) ? $products->class : ''), 'Classification' . lang('bf_form_label_required'));
			?>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'Processing' => 'Processing',
                    'Handling' => 'Handling'
				);
				echo form_dropdown(array('name' => 'catg', 'required' => 'required'), $options, set_value('catg', isset($products->catg) ? $products->catg : ''), 'Category' . lang('bf_form_label_required'));
			?>

        </fieldset>
		<fieldset class='form-actions'>
			<input type='submit' name='save' class='btn btn-primary' value="<?php echo lang('products_action_edit'); ?>" />
			<?php echo lang('bf_or'); ?>
			<?php echo anchor(SITE_AREA . '/content/products', lang('products_cancel'), 'class="btn btn-warning"'); ?>
			
			<?php if ($this->auth->has_permission('Products.Content.Delete')) : ?>
				<?php echo lang('bf_or'); ?>
				<button type='submit' name='delete' formnovalidate class='btn btn-danger' id='delete-me' onclick="return confirm('<?php e(js_escape(lang('products_delete_confirm'))); ?>');">
					<span class='icon-trash icon-white'></span>&nbsp;<?php echo lang('products_delete_record'); ?>
				</button>
			<?php endif; ?>
		</fieldset>
    <?php echo form_close(); ?>
</div>