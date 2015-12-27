<?php

$num_columns	= 2;
$can_delete	= $this->auth->has_permission('Vendor_Products.Content.Delete');
$can_edit		= $this->auth->has_permission('Vendor_Products.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class="admin-box">
	<h3>Vendor Products</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>Vendor</th>
					<th>Product</th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('vendor_products_delete_confirm'))); ?>')" />
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
						foreach($products as $product){
							if($product->id == $record->product_id){
								$product_name = $product->name . ' - ' . $product->desc;
							}
						}
					endif;

					$vendor_name = null;
					if (isset($vendors)):
						foreach($vendors as $vendor){
							if($vendor->id == $record->vendor_id){
								$vendor_name = $vendor->name;
							}
						}
					endif;

				?>					                
				<tr>
					<?php if ($can_delete) : ?>
					<td class="column-check"><input type="checkbox" name="checked[]" value="<?php echo $record->id; ?>" /></td>
					<?php endif;?>
					
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/vendor_products/edit/' . $record->id, '<span class="icon-pencil"></span>' .  $vendor_name); ?></td>
				<?php else : ?>
					<td><?php e($vendor_name); ?></td>
				<?php endif; ?>
					<td><?php e($product_name) ?></td>
				</tr>
				<?php
					endforeach;
				else:
				?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">No records found that match your selection.</td>
				</tr>
				<?php endif; ?>
			</tbody>
		</table>
	<?php echo form_close(); ?>
    <?php echo $this->pagination->create_links(); ?>
</div>