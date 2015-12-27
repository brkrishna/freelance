<?php

$num_columns	= 2;
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class='content'>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class='table table-bordered table-condensed'>
			<caption><h3>Consignments</h3></caption>
			<thead>
				<tr>
					<th>Ref No</th>
					<th>Document</th>
				</tr>
			</thead>
			<tbody>
				<?php
				if ($has_records) :
					$prev_ref_no = '';
					foreach ($records as $record) :
						if ($prev_ref_no != $record->ref_no):
							$prev_ref_no = $record->ref_no;
						?>
						<tr class="success"><td colspan="2"><strong><?php e($record->ref_no); ?></strong></td></tr>
					<?php endif;?>
				<tr><td></td>
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
					<td colspan='<?php echo $num_columns; ?>'><?php echo lang('consignment_documents_records_empty'); ?></td>
				</tr>
				<?php endif; ?>
			</tbody>
		</table>
	<?php
    echo form_close();
    
    ?>
</div>