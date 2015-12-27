<?php

$num_columns	= 10;
$can_delete	= $this->auth->has_permission('Inquiries.Content.Delete');
$can_edit		= $this->auth->has_permission('Inquiries.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class="admin-box">
	<h3>Inquiries</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>Product</th>
					<th>Quantity</th>
					<th>UOM</th>
					<th>Required By</th>
					<th>Product Specifications</th>
					<th>Quality Specifications</th>
					<th>Packaging Specifications</th>
					<th>Priority</th>
					<th>Status</th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('inquiries_delete_confirm'))); ?>')" />
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
					<td><?php echo anchor(SITE_AREA . '/content/inquiries/edit/' . $record->id, '<span class="icon-pencil"></span>' .  $record->product); ?></td>
				<?php else : ?>
					<td><?php e($record->product); ?></td>
				<?php endif; ?>
					<td><?php e($record->quantity) ?></td>
					<td><?php 
							if (isset($uoms)):
								foreach($uoms as $uom){
									if($uom->id == $record->uom_id){
										e($uom->name);		
									}
								}
							endif;
						?></td>
					<td><?php e($record->required_by) ?></td>
					<td><?php e($record->prod_spec) ?></td>
					<td><?php e($record->quality_spec) ?></td>
					<td><?php e($record->packaging_spec) ?></td>
					<td><?php e($record->priority) ?></td>
					<td><?php e($record->status) ?></td>
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