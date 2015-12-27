<?php

$num_columns	= 3;
$has_records	= isset($records) && is_array($records) && count($records);
?>
<div class='content'>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class='table table-bordered table-condensed'>
			<caption><h3>Labels</h3></caption>
			<thead>
				<tr>
					<th><?php echo lang('labels_field_product_id'); ?></th>
					<th><?php echo lang('labels_field_label'); ?></th>
					<th><?php echo lang('labels_field_doc_name'); ?></th>
				</tr>
			</thead>
			<tbody>
				<?php
				if ($has_records) :
					foreach ($records as $record) :
				?>
				<tr>
					<td><?php e($record->prod_name); ?></td>
					<td><?php e($record->label); ?></td>
					<td>
						<?php if(isset($record) && isset($record->doc_file) && !empty($record->doc_file)) :
							$attachment = unserialize($record->doc_file);
						?> 
							<a href="<?php echo base_url() . 'uploads/' . $attachment['file_name'] ?>" target="_blank" >
								<?php echo $record->doc_name; ?>
							</a>
						<?php endif; ?>	
					</td>
				</tr>
				<?php
					endforeach;
				else:
				?>
				<tr>
					<td colspan='<?php echo $num_columns; ?>'><?php echo lang('labels_records_empty'); ?></td>
				</tr>
				<?php endif; ?>
			</tbody>
		</table>
	<?php
    echo form_close();
    ?>
</div>