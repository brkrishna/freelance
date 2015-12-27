<?php

$num_columns	= 6;
$can_delete	= $this->auth->has_permission('Quotes.Content.Delete');
$can_edit		= $this->auth->has_permission('Quotes.Content.Edit');
$can_view		= $this->auth->has_permission('Quotes.Content.View');
$has_records	= isset($records) && is_array($records) && count($records);
if (!$can_view){
	exit;
}

?>
<div class="admin-box">
	<h5>Quotes</h5>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-condensed table-bordered">
			<thead>
				<tr>
					<th>Ref No</th>
					<th>Date</th>
					<th>Vendor</th>
					<th>Product</th>
					<th>Price</th>
					<th>TAT (days)</th>
				</tr>
			</thead>
			<tbody>
				<?php
				if ($has_records) :
					foreach ($records as $record) :
				?>
				<tr>
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/quotes/edit/' . $record->id, '<span class="icon-pencil"></span>' .  $record->ref_no); ?></td>
				<?php else : ?>
					<td><?php e($record->ref_no); ?></td>
				<?php endif; ?>
					<td><?php e($record->quote_dt) ?></td>
					<td><?php e($record->vendor_name) ?></td>
					<td><?php e($record->product_name) ?></td>
					<td><?php e(number_format($record->price, 2)) ?></td>
					<td><?php e($record->tat) ?></td>
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