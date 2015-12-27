<?php

$num_columns	= 6;
$has_records	= isset($records) && is_array($records) && count($records);
$ingre_name = '';
if ($has_records):
    foreach($records as $r):
            $ingre_name = $r->ing_name;
    endforeach;
endif;

?>
<div class='content'>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class='table table-bordered table-condensed'>
            <caption><h3><?php e($ingre_name); ?> - Documents</h3></caption>
			<thead>
				<tr>
                    <th><?php echo lang('party_documents_field_party_id'); ?></th>
					<th><?php echo lang('party_documents_field_product_id'); ?></th>
					<th><?php echo lang('party_documents_field_doc_name'); ?></th>
					<th><?php echo lang('party_documents_field_rcvd_on'); ?></th>
					<th><?php echo lang('party_documents_field_comments'); ?></th>
				</tr>
			</thead>
			<tbody>
				<?php
				if ($has_records) :
					foreach ($records as $record) :
				?>
				<tr>
                    <td><?php e($record->org_name); ?></td>
					<td><?php e($record->prod_name); ?></td>
					<td>
        				<?php if(isset($record) && isset($record->doc_file) && !empty($record->doc_file)) :
        					$attachment = unserialize($record->doc_file);
        				?> 
        					<a href="<?php echo base_url() . 'uploads/' . $attachment['file_name'] ?>" target="_blank" >
        						<?php echo $record->doc_name; ?>
        					</a>
        				<?php endif; ?>	
					</td>
					<td><?php e($record->rcvd_on); ?></td>
					<td><?php e($record->comments); ?></td>
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
    
    ?>
</div>