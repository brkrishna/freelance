<?php

$num_columns	= 12;
$can_delete	= $this->auth->has_permission('Quotes.Content.Delete');
$can_edit		= $this->auth->has_permission('Quotes.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class="admin-box">
	<h3>Quotes</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>Reference No</th>
					<th>Date Received</th>
					<th>Vendor</th>
					<th>Product</th>
					<th>Price</th>
					<th>Turn Around Time (days)</th>
					<th>Quantity</th>
					<th>UOM</th>
                    <!--
					<th><?php echo lang("quotes_column_deleted"); ?></th>
					<th><?php echo lang("quotes_column_created"); ?></th>
					<th><?php echo lang("quotes_column_modified"); ?></th>
                    -->
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('quotes_delete_confirm'))); ?>')" />
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
				<tr>
					<?php if ($can_delete) : ?>
					<td class="column-check"><input type="checkbox" name="checked[]" value="<?php echo $record->id; ?>" /></td>
					<?php endif;?>
					
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/quotes/edit/' . $record->id, '<span class="icon-pencil"></span>' .  $record->ref_no); ?></td>
				<?php else : ?>
					<td><?php e($record->ref_no); ?></td>
				<?php endif; ?>
				<?php
					$product_name = null;
					if (isset($products)):
						foreach($products as $product){
							if($product->id == $record->product_id){
								$product_name = $product->name . ' - ' . $product->desc;
							}
						}
					endif;

					$uom_name = null;
					if (isset($uoms)):
						foreach($uoms as $uom){
							if($uom->id == $record->uom_id){
								$uom_name = $uom->name;
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
					<td><?php e($record->quote_dt) ?></td>
					<td><?php e($vendor_name) ?></td>
					<td><?php e($product_name) ?></td>
					<td><?php e(number_format($record->price, 2)) ?></td>
					<td><?php e($record->tat) ?></td>
					<td><?php e($record->quantity) ?></td>
					<td><?php e($uom_name) ?></td>
                    <!--
					<td><?php echo $record->deleted > 0 ? lang('quotes_true') : lang('quotes_false')?></td>
					<td><?php e($record->created_on) ?></td>
					<td><?php e($record->modified_on) ?></td>
                    -->
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