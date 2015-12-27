<div>
	<h1 class="page-header">Factory</h1>
</div>

<br />

<?php if (isset($records) && is_array($records) && count($records)) : ?>
				
	<table class="table table-striped table-bordered">
		<thead>
			<tr>
				
		<th>Employee size</th>
		<th>Capacity per Month</th>
		<th>Monthly UOM</th>
		<th>Capacity per Day</th>
		<th>Daily UOM</th>
		<th>Capacity - Raw material</th>
		<th>Storage Capacity</th>
		<th>Nearest Port</th>
		<th>Nearest Airport</th>
		<th>Nearest Major City</th>
		<th>Transportation options</th>
		<th>Courier Company</th>
		<th>Created By</th>
		<th>Profile Id</th>
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
							<?php e(($value > 0) ? lang('factory_true') : lang('factory_false')); ?>
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