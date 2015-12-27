<?php

$num_columns	= 10;
$can_delete	= $this->auth->has_permission('PO_Transactions.Content.Delete');
$can_edit		= $this->auth->has_permission('PO_Transactions.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class="admin-box">
	<h3>PO Transactions</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
    
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>PO Ref</th>
					<th>Transaction Type</th>
					<th>Date Remitted</th>
					<th>Date Received</th>
					<th>Amount</th>
					<th>Vendor</th>
					<th><?php echo lang("po_transactions_column_deleted"); ?></th>
					<th><?php echo lang("po_transactions_column_created"); ?></th>
					<th><?php echo lang("po_transactions_column_modified"); ?></th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('po_transactions_delete_confirm'))); ?>')" />
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
                      $po_transactions_po_ref = null;
					if (isset($po_transaction)):
						foreach($po_transactions as $po_transaction){
							if($po_transactions->id == $record->po_transactions_id){
								$po_transactions_po_ref = $po_transactions->po_ref;
							}
						}
					endif;
                    ?>
                    
					
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/po_transactions/edit/' . $record->id, '<span class="icon-pencil"></span>' .  $record->po_ref); ?></td>
				<?php else : ?>
					<td><?php e($record->po_ref); ?></td>
				<?php endif; ?>
					<td><?php e($record->trans_type) ?></td>
					<td><?php e($record->remit_date) ?></td>
					<td><?php e($record->rcvd_date) ?></td>
					<td><?php e($record->amount) ?></td>
					<td><?php e($record->vendor_id) ?></td>
					<td><?php echo $record->deleted > 0 ? lang('po_transactions_true') : lang('po_transactions_false')?></td>
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