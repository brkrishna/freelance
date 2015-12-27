<?php

$num_columns	= 3;
$can_delete	= $this->auth->has_permission('Product_Ingredients.Content.Delete');
$can_edit		= $this->auth->has_permission('Product_Ingredients.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

if ($can_delete) {
    $num_columns++;
}
?>
<div class='admin-box'>
	<h3>
		<?php echo lang('product_ingredients_area_title'); ?>
	</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class='table table-striped'>
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class='column-check'><input class='check-all' type='checkbox' /></th>
					<?php endif;?>

					<th><?php echo lang('product_ingredients_field_product_id'); ?></th>
					<th><?php echo lang('product_ingredients_field_ingredient_id'); ?></th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan='<?php echo $num_columns; ?>'>
						<?php echo lang('bf_with_selected'); ?>
						<input type='submit' name='delete' id='delete-me' class='btn btn-danger' value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('product_ingredients_delete_confirm'))); ?>')" />
					</td>
				</tr>
				<?php endif; ?>
			</tfoot>
			<?php endif; ?>
			<tbody>
				<?php
				if ($has_records) :
					foreach ($records as $record) :
				?>
					<?php

					$product_name = null;
					if (isset($products)):
						foreach($products as $p){
							if($p->id == $record->product_id){
								$product_name = $p->name;		
							}
						}
					endif;					

					$ingredient_name = null;
					if (isset($ingredients)):
						foreach($ingredients as $i){
							if($i->id == $record->ingredient_id){
								$ingredient_name = $i->name;		
							}
						}
					endif;					
					
					?>					

				<tr>
					<?php if ($can_delete) : ?>
					<td class='column-check'><input type='checkbox' name='checked[]' value='<?php echo $record->id; ?>' /></td>
					<?php endif;?>
					
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/product_ingredients/edit/' . $record->id, '<span class="icon-pencil"></span> ' .  $product_name); ?></td>
				<?php else : ?>
					<td><?php e($product_name); ?></td>
				<?php endif; ?>
					<td><?php e($ingredient_name); ?></td>
				</tr>
				<?php
					endforeach;
				else:
				?>
				<tr>
					<td colspan='<?php echo $num_columns; ?>'><?php echo lang('product_ingredients_records_empty'); ?></td>
				</tr>
				<?php endif; ?>
			</tbody>
		</table>
	<?php
    echo form_close();
    
    ?>
</div>