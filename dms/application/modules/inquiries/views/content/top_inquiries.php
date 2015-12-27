<?php

$num_columns	= 4;
$can_delete	= $this->auth->has_permission('Inquiries.Content.Delete');
$can_edit		= $this->auth->has_permission('Inquiries.Content.Edit');
$can_view		= $this->auth->has_permission('Inquiries.Content.View');
$has_records	= isset($records) && is_array($records) && count($records);
if (!$can_view){
	exit;
}

?>
<div class="admin-box">
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-condensed table-bordered">
            <caption>
                <strong>Inquiries</strong>
                <?php if ($can_edit) :
                    echo " - " . anchor(SITE_AREA . '/content/inquiries/create/', 'Add New');
                endif; ?>
            </caption>
			<thead>
				<tr>
					<th>Product</th>
					<th>Quantity</th>
					<th>UOM</th>
					<th>Required By</th>
				</tr>
			</thead>
			<tbody>
				<?php
				if ($has_records) :
					foreach ($records as $record) :
				?>
				<tr>
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/inquiries/edit/' . $record->id, '<span class="icon-pencil"></span>' .  $record->product); ?></td>
				<?php else : ?>
					<td><?php e($record->product); ?></td>
				<?php endif; ?>
					<td><?php e($record->quantity) ?></td>
                    <td><?php e($record->uom_name) ?></td>
					<td><?php e($record->required_by) ?></td>
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