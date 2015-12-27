<?php

$num_columns	= 9;
$can_delete	= $this->auth->has_permission('Product_Documents.Content.Delete');
$can_edit		= $this->auth->has_permission('Product_Documents.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

if ($can_delete) {
    $num_columns++;
}
?>
<div class='admin-box'>
	<h3>
		<?php echo lang('product_documents_area_title'); ?>
	</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class='table table-striped'>
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class='column-check'><input class='check-all' type='checkbox' /></th>
					<?php endif;?>
					
					<th><?php echo lang('product_documents_field_product_id'); ?></th>
					<th><?php echo lang('product_documents_field_doc_name'); ?></th>
					<th><?php echo lang('product_documents_field_doc_file'); ?></th>
					<th><?php echo lang('product_documents_field_rcvd_on'); ?></th>
					<th><?php echo lang('product_documents_field_comments'); ?></th>
					<th><?php echo lang('product_documents_field_archive'); ?></th>
					<th><?php echo lang('product_documents_column_deleted'); ?></th>
					<th><?php echo lang('product_documents_column_created'); ?></th>
					<th><?php echo lang('product_documents_column_modified'); ?></th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan='<?php echo $num_columns; ?>'>
						<?php echo lang('bf_with_selected'); ?>
						<input type='submit' name='delete' id='delete-me' class='btn btn-danger' value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('product_documents_delete_confirm'))); ?>')" />
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
					<td class='column-check'><input type='checkbox' name='checked[]' value='<?php echo $record->id; ?>' /></td>
					<?php endif;?>
					
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/product_documents/edit/' . $record->id, '<span class="icon-pencil"></span> ' .  $record->product_id); ?></td>
				<?php else : ?>
					<td><?php e($record->product_id); ?></td>
				<?php endif; ?>
					<td><?php e($record->doc_name); ?></td>
					<td><?php e($record->doc_file); ?></td>
					<td><?php e($record->rcvd_on); ?></td>
					<td><?php e($record->comments); ?></td>
					<td><?php e($record->archive); ?></td>
					<td><?php echo $record->deleted > 0 ? lang('product_documents_true') : lang('product_documents_false'); ?></td>
					<td><?php e($record->created_on); ?></td>
					<td><?php e($record->modified_on); ?></td>
				</tr>
				<?php
					endforeach;
				else:
				?>
				<tr>
					<td colspan='<?php echo $num_columns; ?>'><?php echo lang('product_documents_records_empty'); ?></td>
				</tr>
				<?php endif; ?>
			</tbody>
		</table>
	<?php
    echo form_close();
    
    echo $this->pagination->create_links();
    ?>
</div>