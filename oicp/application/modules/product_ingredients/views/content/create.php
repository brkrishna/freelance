<?php

$validation_errors = validation_errors();

if ($validation_errors) :
?>
<div class='alert alert-block alert-error fade in'>
	<a class='close' data-dismiss='alert'>&times;</a>
	<h4 class='alert-heading'>
		<?php echo lang('product_ingredients_errors_message'); ?>
	</h4>
	<?php echo $validation_errors; ?>
</div>
<?php
endif;

$id = isset($product_ingredients->id) ? $product_ingredients->id : '';

?>
<div class='admin-box'>
	<h3>Product Ingredients</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>
            
			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($products_select) && count($products_select)) :	
				    echo form_dropdown('product_id', $products_select, set_value('product_id', isset($product_ingredients->product_id) ? $product_ingredients->product_id : ''), 'Product'. lang('bf_form_label_required'));
                endif;
			?>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($ingredients_select) && count($ingredients_select)) :	
				    echo form_dropdown('ingredient_id', $ingredients_select, set_value('ingredient_id', isset($product_ingredients->ingredient_id) ? $product_ingredients->ingredient_id : ''), 'Ingredient' . lang('bf_form_label_required'));
                endif;
			?>

        </fieldset>
		<fieldset class='form-actions'>
			<input type='submit' name='save' class='btn btn-primary' value="<?php echo lang('product_ingredients_action_create'); ?>" />
			<?php echo lang('bf_or'); ?>
			<?php echo anchor(SITE_AREA . '/content/product_ingredients', lang('product_ingredients_cancel'), 'class="btn btn-warning"'); ?>
			
		</fieldset>
    <?php echo form_close(); ?>
</div>