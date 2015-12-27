<div>
	<h1 class="page-header">PO Fulfillment</h1>
</div>

<br />

<?php if (isset($records) && is_array($records) && count($records)) : ?>
				
	<table class="table table-striped table-bordered">
		<thead>
			<tr>
				
		<th>PO No</th>
		<th>Vendor</th>
		<th>Product</th>
		<th>Quantity</th>
		<th>UOM</th>
		<th>Rate</th>
		<th>Supply from</th>
		<th>Destination Port</th>
		<th>Mode of Packing</th>
		<th>No of Units</th>
		<th>Created By</th>
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
							<?php e(($value > 0) ? lang('po_fulfillment_true') : lang('po_fulfillment_false')); ?>
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