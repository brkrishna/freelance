<?php

$num_columns	= 8;
$can_delete	= $this->auth->has_permission('Containers.Content.Delete');
$can_edit		= $this->auth->has_permission('Containers.Content.Edit');
$can_view		= $this->auth->has_permission('Containers.Content.View');
$has_records	= isset($records) && is_array($records) && count($records);
if (!$can_view){
	exit;
}
?>
<div class="admin-box">
	<h5>Containers</h5>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-striped">
			<thead>
				<tr>
					<th>Product</th>
					<th>Origin</th>
                    <th>PO Ref</th>
					<th>Container No</th>
					<th>Seal</th>
					<th>Batch Numbers</th>
					<th>Documents</th>
				</tr>
			</thead>
			<tbody>
				<?php
				if ($has_records) :
					$c_no = null;
					$skip_row = false;					
					foreach ($records as $record) :
						if ($c_no == $record->container_no){
							$skip_row = true;	
						}else{
							$skip_row = false;
							$c_no = $record->container_no;
						}		
				?>
				<tr>
					<td><?php echo $skip_row == true ? '&nbsp;' : e($record->product_name) ?></td>
					<td><?php echo $skip_row == true ? '&nbsp;' : e($record->country_name) ?></td>
                    <td><?php echo $skip_row == true ? '&nbsp;' : e($record->po_ref) ?></td>    
				<?php if ($can_edit) : ?>
					<td><?php echo $skip_row == true ? '&nbsp;' : anchor(SITE_AREA . '/content/containers/edit/' . $record->id, '<span class="icon-pencil"></span>' .  $record->container_no); ?></td>
				<?php else : ?>
					<td><?php echo $skip_row == true ? '&nbsp;' : e($record->container_no); ?></td>
				<?php endif; ?>
					<td><?php echo $skip_row == true ? '&nbsp;' : e($record->seal) ?></td>
					<td><?php echo $skip_row == true ? '&nbsp;' : e($record->batch_nos) ?></td>
					<td><?php if(isset($record) && isset($record->attachments) && !empty($record->attachments)) :
							$attachments = unserialize($record->attachments);
						?> 
							<a href="<?php echo base_url() . '/uploads/' . $attachments['file_name'] ?>" target="_blank" >
								<?php e($record->doc_type_name); ?>
							</a>
						<?php endif; ?></td>							
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
</div>