<div>
	<h1 class="page-header">Inquiries</h1>
</div>

<br />

<?php if (isset($records) && is_array($records) && count($records)) : ?>
				
	<table class="table table-striped table-bordered">
		<thead>
			<tr>
				
		<th>Product</th>
		<th>Quantity</th>
		<th>UOM</th>
		<th>Required By</th>
		<th>Product Specifications</th>
		<th>Quality Specifications</th>
		<th>Packaging Specifications</th>
		<th>Priority</th>
		<th>Status</th>
		<th>Comments</th>
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
							<?php e(($value > 0) ? lang('inquiries_true') : lang('inquiries_false')); ?>
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