<?php

$num_columns	= 6;
$can_delete	= $this->auth->has_permission('PO_Containers.Content.Delete');
$can_edit		= $this->auth->has_permission('PO_Containers.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class="admin-box">
	<h3>PO Containers</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>PO No</th>
					<th>Batch No</th>
					<th>Vessel</th>
					<th>Container</th>
					<th>Seal</th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('po_containers_delete_confirm'))); ?>')" />
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

                ?>
				<tr>
					<?php if ($can_delete) : ?>
					<td class="column-check"><input type="checkbox" name="checked[]" value="<?php echo $record->id; ?>" /></td>
					<?php endif;?>
					
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/po_containers/edit/' . $record->id, $po_no); ?></td>
				<?php else : ?>
					<td><?php e($po_no); ?></td>
				<?php endif; ?>
					<td><?php e($record->batch_no) ?></td>
					<td><?php e($record->vessel) ?></td>
					<td><?php e($record->container) ?></td>
					<td><?php e($record->seal) ?></td>
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