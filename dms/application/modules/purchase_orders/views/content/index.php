<?php

$num_columns	= 13;
$can_delete	= $this->auth->has_permission('Purchase_Orders.Content.Delete');
$can_edit		= $this->auth->has_permission('Purchase_Orders.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);
$can_view       = $this->auth->has_permission('Purchase_Orders.Content.View');

if(!$can_view){
    exit;
}
?>
<div class="admin-box">
	<h3>Purchase Orders</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
    
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>PO No</th>
					<th>PO Date</th>
					<th>Product</th>
					<th>Quantity</th>
					<th>Rate</th>
					<th>Mode of Packing</th>
					<th>Customer</th>
					<th>Status</th>
					<th>Comments</th>
                    <th>PO Details</th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('purchase_orders_delete_confirm'))); ?>')" />
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
					<td><?php echo anchor(SITE_AREA . '/content/purchase_orders/edit/' . $record->id, $record->po_no); ?></td>
				<?php else : ?>
					<td><?php e($record->po_no); ?></td>
				<?php endif; ?>
                <?php 
                            $uom_name = NULL;
							if (isset($uoms)):
								foreach($uoms as $uom){
									if($uom->id == $record->uom_id){
										$uom_name = $uom->name;		
									}
								}
							endif;

                            $customer_name = NULL;
							if (isset($customers)):
								foreach($customers as $customer){
									if($customer->id == $record->customer_id){
										$customer_name = $customer->name;		
									}
								}
							endif;

                            $product_name = NULL;
							if (isset($products)):
								foreach($products as $product){
									if($product->id == $record->product_id){
										$product_name = $product->name;		
									}
								}
							endif;

				?>
                    
					<td><?php e($record->po_dt) ?></td>
					<td><?php e($product_name) ?></td>
					<td><?php e($record->qty . ' ' . $uom_name) ?></td>
					<td><?php e($record->rate) ?></td>
					<td><?php e($record->no_of_units . ' ' . $record->packing_mode) ?></td>
					<td><?php e($customer_name) ?></td>
					<td><?php e($record->status_id) ?></td>
					<td><?php e($record->comments) ?></td>
                    <td><?php echo anchor(SITE_AREA . '/content/purchase_orders/po_details/' . $record->id, '<span class="icon-zoom-out"></span>'); ?></td>
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