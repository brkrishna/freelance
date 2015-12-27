<div>
	<h1 class="page-header">PO Documents</h1>
</div>

<br />

<?php if (isset($records) && is_array($records) && count($records)) : ?>
				
	<table class="table table-striped table-bordered">
		<thead>
			<tr>
				
		<th>PO No</th>
		<th>Vendor</th>
		<th>Product</th>
		<th>Applicable</th>
		<th>Document</th>
		<th>Issuing Authority</th>
		<th>Issued on</th>
		<th>Valid Till</th>
		<th>Place of origin</th>
		<th>Attachment</th>
		<th>Comments</th>
		<th>Created By</th>
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
							<?php e(($value > 0) ? lang('po_documents_true') : lang('po_documents_false')); ?>
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