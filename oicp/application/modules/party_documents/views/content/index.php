<?php

$num_columns	= 6;
$can_delete	= $this->auth->has_permission('Party_Documents.Content.Delete');
$can_edit		= $this->auth->has_permission('Party_Documents.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);
$num_rows = count($records);
if ($can_delete) {
    $num_columns++;
}
?>
<div class='admin-box'>
	<h3>
		<?php echo lang('party_documents_area_title') . ' - (' . $num_rows . ')'; ?>
	</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class='table table-striped'>
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class='column-check'><input class='check-all' type='checkbox' /></th>
					<?php endif;?>
					<th><?php echo lang('party_documents_field_party_id'); ?></th>
					<th><?php echo lang('party_documents_field_product_id'); ?></th>
					<th><?php echo lang('party_documents_field_ingredient_id'); ?></th>
					<th><?php echo lang('party_documents_field_catg'); ?></th>
					<th><?php echo lang('party_documents_field_cert_type'); ?></th>
					<th><?php echo lang('party_documents_field_doc_name'); ?></th>
					<th><?php echo lang('party_documents_field_doc_file'); ?></th>
					<th><?php echo lang('party_documents_field_rcvd_on'); ?></th>
					<th><?php echo lang('party_documents_field_comments'); ?></th>
					<th><?php echo lang('party_documents_field_archive'); ?></th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan='<?php echo $num_columns; ?>'>
						<?php echo lang('bf_with_selected'); ?>
						<input type='submit' name='delete' id='delete-me' class='btn btn-danger' value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('party_documents_delete_confirm'))); ?>')" />
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
					<?php
					$party_name = null;
					if (isset($party)):
						foreach($party as $p){
							if($p->id == $record->party_id){
								$party_name = $p->org_name;		
							}
						}
					endif;					

					$product_name = null;
					if (isset($products)):
						foreach($products as $p){
							if($p->id == $record->product_id){
								$product_name = $p->name;		
							}
						}
					endif;					

					$ingredient_name = null;
					if (isset($ingredients)):
						foreach($ingredients as $i){
							if($i->id == $record->ingredient_id){
								$ingredient_name = $i->name;		
							}
						}
					endif;					

					?>
					<?php if ($can_delete) : ?>
					<td class='column-check'><input type='checkbox' name='checked[]' value='<?php echo $record->id; ?>' /></td>
					<?php endif;?>
					
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/party_documents/edit/' . $record->id, $party_name); ?></td>
				<?php else : ?>
					<td><?php e($party_name); ?></td>
				<?php endif; ?>
					<td><?php e($product_name); ?></td>
					<td><?php e($ingredient_name); ?></td>
					<td><?php e($record->catg); ?></td>
					<td><?php e($record->cert_type); ?></td>
					<td><?php e($record->doc_name); ?></td>
					<td>
				<?php if(isset($record) && isset($record->doc_file) && !empty($record->doc_file)) :
					$attachment = unserialize($record->doc_file);
				?> 
					<a href="<?php echo base_url() . 'uploads/' . $attachment['file_name'] ?>" target="_blank" >
						<?php echo $attachment['file_name']; ?>
					</a>
				<?php endif; ?>	
					</td>
					<td><?php e($record->rcvd_on); ?></td>
					<td><?php e($record->comments); ?></td>
					<td><?php e($record->archive); ?></td>
				</tr>
				<?php
					endforeach;
				else:
				?>
				<tr>
					<td colspan='<?php echo $num_columns; ?>'><?php echo lang('party_documents_records_empty'); ?></td>
				</tr>
				<?php endif; ?>
			</tbody>
		</table>
	<?php
    echo form_close();
    echo $this->pagination->create_links();
    ?>
</div>