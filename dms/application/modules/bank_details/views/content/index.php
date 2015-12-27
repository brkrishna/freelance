<?php

$num_columns	= 10;
$can_delete	= $this->auth->has_permission('Bank_Details.Content.Delete');
$can_edit		= $this->auth->has_permission('Bank_Details.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class="admin-box">
	<h3>Bank Details</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
   
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>Bank Name</th>
                    <th>Branch</th>
					<th>Address</th>
					<th>Account Type</th>
					<th>Operating Currency</th>
					<th>Accepted Currency</th>
					<th>Swift Code</th>
					<th>MICR</th>
					<th>IFSC</th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('bank_details_delete_confirm'))); ?>')" />
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
					<td><?php echo anchor(SITE_AREA . '/content/bank_details/edit/' . $record->id, '<span class="icon-pencil"></span>&nbsp;' .  $record->bank_name); ?></td>
				<?php else : ?>
					<td><?php e($record->bank_name); ?></td>
				<?php endif; ?>
                    <td><?php e($record->branch) ?></td>
					<td><?php e($record->address) ?></td>
					<td><?php e($record->account_type) ?></td>
					<td><?php e($record->oper_curr) ?></td>
					<td><?php e($record->accept_curr) ?></td>
					<td><?php e($record->swift_code) ?></td>
					<td><?php e($record->micr) ?></td>
					<td><?php e($record->ifsc) ?></td>
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
        <hr/>
        <div class="alert alert-warning lead">
            Click <strong><a class="alert-link" href="<?php echo site_url(SITE_AREA .'/content') ?>">Home</a></strong> to check overall progress of your registration
        </div>
	<?php echo form_close(); ?>
     <?php echo $this->pagination->create_links(); ?>
</div>