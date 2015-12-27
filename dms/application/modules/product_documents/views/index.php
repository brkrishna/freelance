<div>
	<h1 class="page-header">Product Documents</h1>
</div>

<br />

<?php if (isset($records) && is_array($records) && count($records)) : ?>
				
	<table class="table table-striped table-bordered">
		<thead>
			<tr>
				
		<th>Vendor</th>
		<th>Activity Type</th>
		<th>Product</th>
		<th>Document</th>
		<th>Issuing Authority</th>
		<th>Issued on</th>
		<th>Valid Till</th>
		<th>Profile Id</th>
		<th>Created by</th>
		<th>Place of Origin</th>
		<th>Comments</th>
		<th>Attachment</th>
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
							<?php e(($value > 0) ? lang('product_documents_true') : lang('product_documents_false')); ?>
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