<?php

$num_columns	= 3;
$can_delete	= $this->auth->has_permission('Standards_Documents.Content.Delete');
$can_edit		= $this->auth->has_permission('Standards_Documents.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

if ($can_delete) {
    $num_columns++;
}
?>
<div class='admin-box'>
	<h3>
		<?php echo lang('standards_documents_area_title'); ?>
	</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class='table table-striped'>
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class='column-check'><input class='check-all' type='checkbox' /></th>
					<?php endif;?>
					
					<th><?php echo lang('standards_documents_field_doc_name'); ?></th>
					<th><?php echo lang('standards_documents_field_doc_file'); ?></th>
					<th><?php echo lang('standards_documents_field_archive'); ?></th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan='<?php echo $num_columns; ?>'>
						<?php echo lang('bf_with_selected'); ?>
						<input type='submit' name='delete' id='delete-me' class='btn btn-danger' value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('standards_documents_delete_confirm'))); ?>')" />
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
					<td><?php echo anchor(SITE_AREA . '/content/standards_documents/edit/' . $record->id, '<span class="icon-pencil"></span> ' .  $record->doc_name); ?></td>
				<?php else : ?>
					<td><?php e($record->doc_name); ?></td>
				<?php endif; ?>
					<td>
						<?php if(isset($record) && isset($record->doc_file) && !empty($record->doc_file)) :
							$attachment = unserialize($record->doc_file);
						?> 
							<a href="<?php echo base_url() . 'uploads/' . $attachment['file_name'] ?>" target="_blank" >
								<?php echo $attachment['file_name']; ?>
							</a>
						<?php endif; ?>	
					</td>
					<td><?php e($record->archive); ?></td>
				</tr>
				<?php
					endforeach;
				else:
				?>
				<tr>
					<td colspan='<?php echo $num_columns; ?>'><?php echo lang('standards_documents_records_empty'); ?></td>
				</tr>
				<?php endif; ?>
			</tbody>
		</table>
	<?php
    echo form_close();
    echo $this->pagination->create_links();
    ?>
</div>