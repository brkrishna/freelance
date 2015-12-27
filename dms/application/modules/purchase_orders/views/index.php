<div>
	<h1 class="page-header">Purchase Orders</h1>
</div>

<br />

<?php if (isset($records) && is_array($records) && count($records)) : ?>
				
	<table class="table table-striped table-bordered">
		<thead>
			<tr>
				
		<th>PO No</th>
		<th>PO Date</th>
		<th>Product</th>
		<th>Quantity</th>
		<th>UOM</th>
		<th>Rate</th>
		<th>Mode of Packing</th>
		<th>No of Units</th>
		<th>Created By</th>
		<th>Customer</th>
		<th>Status</th>
		<th>Comments</th>
		<th>Deleted</th>
		<th>Created</th>
		<th>Modified</th>
			</tr>
		</thead>
		<tbody>
		
		<?php foreach ($records as $record) : ?>
			<?php $record = (array)$record;?>
			<tr>
			<?php foreach($record as $field => $value) : ?>
				
				<?php if ($field != 'id') : ?>
					<td>
						<?php if ($field == 'deleted'): ?>
							<?php e(($value > 0) ? lang('purchase_orders_true') : lang('purchase_orders_false')); ?>
						<?php else: ?>
							<?php e($value); ?>
						<?php endif ?>
					</td>
				<?php endif; ?>
				
			<?php endforeach; ?>

			</tr>
		<?php endforeach; ?>
		</tbody>
	</table>
<?php endif; ?>