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

if (isset($product))
{
	$product = (array) $product;
}
$id = isset($product['id']) ? $product['id'] : '';

?>
<div class="admin-box">
	<h3>Product</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<div class="control-group <?php echo form_error('name') ? 'error' : ''; ?>">
				<?php echo form_label('Name'. lang('bf_form_label_required'), 'product_name', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='product_name' type='text' name='product_name' maxlength="255" value="<?php echo set_value('product_name', isset($product['name']) ? $product['name'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('name'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('desc') ? 'error' : ''; ?>">
				<?php echo form_label('Description', 'product_desc', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<?php echo form_textarea( array( 'name' => 'product_desc', 'id' => 'product_desc', 'rows' => '5', 'cols' => '80', 'value' => set_value('product_desc', isset($product['desc']) ? $product['desc'] : '') ) ); ?>
					<span class='help-inline'><?php echo form_error('desc'); ?></span>
				</div>
			</div>

			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('product_action_edit'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/product', lang('product_cancel'), 'class="btn btn-warning"'); ?>
				
			<?php if ($this->auth->has_permission('Product.Content.Delete')) : ?>
				or
				<button type="submit" name="delete" class="btn btn-danger" id="delete-me" onclick="return confirm('<?php e(js_escape(lang('product_delete_confirm'))); ?>'); ">
					<span class="icon-trash icon-white"></span>&nbsp;<?php echo lang('product_delete_record'); ?>
				</button>
			<?php endif; ?>
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>