<?php

$num_columns	= 3;
$has_records	= isset($records) && is_array($records) && count($records);
$product_name = '';
if($has_records):
	foreach($records as $record){
		$product_name = $record->prod_name;
	}
endif;	
?>
<div class='content'>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class='table table-bordered'>
			<caption><h3>Product Details - <?php e($product_name); ?></h3></caption>
			<thead>
				<tr>
					<th>Document</th>
					<th>Ingredient</th>
					<th>Comments</th>
				</tr>
			</thead>
			<tbody>
				<?php
				if ($has_records) :
					$party_id = '';	
					foreach ($records as $record) :
						if ($party_id != $record->id):
							$party_id = $record->id;
						?>
							<tr class="success"><td colspan="3"><strong><?php e($record->type . ' - ' . $record->org_name); ?></strong></td></tr>
						<?php endif; ?>		
				<tr>
					<td>
						<?php if(isset($record) && isset($record->doc_file) && !empty($record->doc_file)) :
							$attachment = unserialize($record->doc_file);
						?> 
							<a href="<?php echo base_url() . 'uploads/' . $attachment['file_name'] ?>" target="_blank" >
								<?php e($record->doc_name) ?>
							</a>
						<?php endif; ?>	
					</td>
					<td>
						<?php e($record->ing_name); ?>
					</td>
					<td><?php e($record->comments); ?></td>
				</tr>
				<?php
					endforeach;
				else:
				?>
				<tr>
					<td colspan='<?php echo $num_columns; ?>'><?php echo lang('products_records_empty'); ?></td>
				</tr>
				<?php endif; ?>
			</tbody>
		</table>
	<?php
    echo form_close();
    ?>
</div>