<?php

$num_columns	= 12;
$can_delete	= $this->auth->has_permission('Drums.Content.Delete');
$can_edit		= $this->auth->has_permission('Drums.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class="admin-box">
	<h3>Drums</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>PO No</th>
					<th>Container No</th>
					<th>Seal No</th>
					<th>Drum No</th>
					<th>Product</th>
					<th>Quantity</th>
					<th>UOM</th>
					<th>Status</th>
					<th><?php echo lang("drums_column_deleted"); ?></th>
					<th><?php echo lang("drums_column_created"); ?></th>
					<th><?php echo lang("drums_column_modified"); ?></th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('drums_delete_confirm'))); ?>')" />
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

                ?>
                    
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/drums/edit/' . $record->id, '<span class="icon-pencil"></span>' .  $record->po_no); ?></td>
				<?php else : ?>
					<td><?php e($record->po_no); ?></td>
				<?php endif; ?>
					<td><?php e($record->container_no) ?></td>
					<td><?php e($record->seal) ?></td>
					<td><?php e($record->drum_no) ?></td>
					<td><?php e($product_name) ?></td>
					<td><?php e($record->qty) ?></td>
					<td><?php e($uom_name) ?></td>
					<td><?php e($record->status) ?></td>
					<td><?php echo $record->deleted > 0 ? lang('drums_true') : lang('drums_false')?></td>
					<td><?php e($record->created_on) ?></td>
					<td><?php e($record->modified_on) ?></td>
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