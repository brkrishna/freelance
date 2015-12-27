<?php

$num_columns	= 3;
$can_edit		= $this->auth->has_permission('Samples.Content.Edit');
$can_view		= $this->auth->has_permission('Samples.Content.View');
$has_records	= isset($records) && is_array($records) && count($records);
if (!$can_view){
	exit;
}
?>
<div class="admin-box">
	<h5>Samples</h5>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-condensed table-bordered">
			<thead>
				<tr>
					<th>Date Received</th>
					<th>Product</th>
					<th>Vendor</th>
				</tr>
			</thead>
			<tbody>
				<?php
				if ($has_records) :
					foreach ($records as $record) :
				?>
				<tr>
					<td><?php e($record->date_received) ?></td>
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/samples/edit/' . $record->id, '<span class="icon-pencil"></span>' .  $record->product_name . ' - ' . $record->product_desc); ?></td>
				<?php else : ?>
					<td><?php e($record->product_name . ' - ' . $record->product_desc); ?></td>
				<?php endif; ?>
					<td><?php e($record->vendor_name) ?></td>
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