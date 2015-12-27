<?php

$num_columns	= 9;
$can_delete	= $this->auth->has_permission('PO_Fulfillment.Content.Delete');
$can_edit		= $this->auth->has_permission('PO_Fulfillment.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class="admin-box">
	<h3>PO Fulfillment</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>PO No</th>
					<th>Vendor</th>
					<th>Product</th>
					<th>Quantity</th>
					<th>Rate</th>
					<th>Supply from</th>
					<th>Destination Port</th>
					<th>Mode of Packing</th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('po_fulfillment_delete_confirm'))); ?>')" />
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
                            $po_no = NULL;
							if (isset($pos)):
								foreach($pos as $po){
									if($po->id == $record->po_no){
										$po_no = $po->po_no;		
									}
								}
							endif;

                            $uom_name = NULL;
							if (isset($uoms)):
								foreach($uoms as $uom){
									if($uom->id == $record->uom_id){
										$uom_name = $uom->name;		
									}
								}
							endif;

                            $vendor_name = NULL;
							if (isset($vendors)):
								foreach($vendors as $vendor){
									if($vendor->id == $record->vendor_id){
										$vendor_name = $vendor->name;		
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
				<tr>
					<?php if ($can_delete) : ?>
					<td class="column-check"><input type="checkbox" name="checked[]" value="<?php echo $record->id; ?>" /></td>
					<?php endif;?>
					
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/po_fulfillment/edit/' . $record->id,  $po_no); ?></td>
				<?php else : ?>
					<td><?php e($po_no); ?></td>
				<?php endif; ?>
					<td><?php e($vendor_name) ?></td>
					<td><?php e($product_name) ?></td>
					<td><?php e($record->qty . ' ' . $uom_name) ?></td>
					<td><?php e($record->rate) ?></td>
					<td><?php e($record->supply_from) ?></td>
					<td><?php e($record->dest_port) ?></td>
					<td><?php e($record->no_of_units . ' ' . $record->packing_mode) ?></td>
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
</div>