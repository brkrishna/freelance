<?php

$num_columns	= 13;
$can_delete	= $this->auth->has_permission('Containers.Content.Delete');
$can_edit		= $this->auth->has_permission('Containers.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class="admin-box">
	<h3>Containers</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
    
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>PO Ref</th>
					<th>Container No</th>
					<th>Seal</th>
					<th>Origin</th>
					<th>Batch Numbers</th>
					<th>Product</th>
					<th>Status</th>
					<th>Started on</th>
					<th>Arrived On</th>
					<th><?php echo lang("containers_column_deleted"); ?></th>
					<th><?php echo lang("containers_column_created"); ?></th>
					<th><?php echo lang("containers_column_modified"); ?></th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('containers_delete_confirm'))); ?>')" />
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
					<td><?php echo anchor(SITE_AREA . '/content/containers/edit/' . $record->id, '<span class="icon-pencil"></span>' .  $record->po_ref); ?></td>
				<?php else : ?>
					<td><?php e($record->po_ref); ?></td>
				<?php endif; ?>
					<td><?php e($record->container_no) ?></td>
					<td><?php e($record->seal) ?></td>
					<td><?php 
							if (isset($countries)):
								foreach($countries as $country){
									if($country->iso == $record->origin){
										e($country->name);		
									}
								}
							endif;
						?></td>
					<td><?php e($record->batch_nos) ?></td>
					<td><?php 
							if (isset($products)):
								foreach($products as $product){
									if($product->id == $record->product_id){
										e($product->name);
									}
								}
							endif;
						?></td>
					<td><?php e($record->status) ?></td>
					<td><?php e($record->started_on) ?></td>
					<td><?php e($record->arrived_on) ?></td>
					<td><?php echo $record->deleted > 0 ? lang('containers_true') : lang('containers_false')?></td>
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