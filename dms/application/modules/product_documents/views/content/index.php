<?php

$num_columns	= 10;
$can_delete	= $this->auth->has_permission('Product_Documents.Content.Delete');
$can_edit		= $this->auth->has_permission('Product_Documents.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class="admin-box">
	<h3>Product Documents</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>Vendor</th>
					<th>Product</th>
					<th>Document</th>
					<th>Issuing Authority</th>
					<th>Issued on</th>
					<th>Valid Till</th>
					<th>Place of Origin</th>
					<th>Comments</th>
					<th>Attachment</th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('product_documents_delete_confirm'))); ?>')" />
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
                
                <?php
					$doc_type_name = null;
					if (isset($doc_types)):
						foreach($doc_types as $doc_type){
							if($doc_type->id == $record->document_id){
								$doc_type_name = $doc_type->name;		
							}
						}
					endif;

					$product_name = null;
					if (isset($products)):
						foreach($products as $product){
							if($product->id == $record->product_id){
								$product_name = $product->name . ' - ' . $product->desc;
							}
						}
					endif;

					$vendor_name = null;
					if (isset($vendors)):
						foreach($vendors as $vendor){
							if($vendor->id == $record->vendor_id){
								$vendor_name = $vendor->name;
							}
						}
					endif;

                ?>
				<tr>
					<?php if ($can_delete) : ?>
					<td class="column-check"><input type="checkbox" name="checked[]" value="<?php echo $record->id; ?>" /></td>
					<?php endif;?>
					
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/product_documents/edit/' . $record->id, '<span class="icon-pencil"></span>&nbsp;' .  $vendor_name); ?></td>
				<?php else : ?>
					<td><?php e($vendor_name); ?></td>
				<?php endif; ?>
					<td><?php e($product_name) ?></td>
					<td><?php e($doc_type_name) ?></td>
					<td><?php e($record->issue_auth) ?></td>
					<td><?php e($record->issued_on) ?></td>
					<td><?php e($record->valid_till) ?></td>
					<td><?php e($record->place_of_origin) ?></td>
					<td><?php e($record->comments) ?></td>
					<td><?php if(isset($record) && isset($record->attachment) && !empty($record->attachment)) :
							$attachment = unserialize($record->attachment);
						?> 
							<a href="<?php echo base_url() . 'uploads/' . $attachment['file_name'] ?>" target="_blank" >
								<?php echo $attachment['file_name']; ?>
							</a>
						<?php endif; ?>		
                    </td>	
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
    <?php echo $this->pagination->create_links(); ?>
</div>