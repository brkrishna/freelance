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

if (isset($vendor_products))
{
	$vendor_products = (array) $vendor_products;
}
$id = isset($vendor_products['id']) ? $vendor_products['id'] : '';

?>
<div class="admin-box">
	<h3>Vendor Products</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($vendors_select) && count($vendors_select)) :
    				echo form_dropdown('vendor_products_vendor_id', $vendors_select, set_value('vendor_products_vendor_id', isset($vendor_products['vendor_id']) ? $vendor_products['vendor_id'] : ''), 'Vendor Id');
                endif;
			?>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($products_select) && count($products_select)) :
				    echo form_dropdown('vendor_products_product_id', $products_select, set_value('vendor_products_product_id', isset($vendor_products['product_id']) ? $vendor_products['product_id'] : ''), 'Product Id'. lang('bf_form_label_required'));
                endif;
			?>

			<div class="control-group <?php echo form_error('comments') ? 'error' : ''; ?>">
				<?php echo form_label('Comments', 'vendor_products_comments', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<?php echo form_textarea( array( 'name' => 'vendor_products_comments', 'id' => 'vendor_products_comments', 'rows' => '5', 'cols' => '80', 'value' => set_value('vendor_products_comments', isset($vendor_products['comments']) ? $vendor_products['comments'] : '') ) ); ?>
					<span class='help-inline'><?php echo form_error('comments'); ?></span>
				</div>
			</div>

			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('vendor_products_action_create'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/vendor_products', lang('vendor_products_cancel'), 'class="btn btn-warning"'); ?>
				
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>