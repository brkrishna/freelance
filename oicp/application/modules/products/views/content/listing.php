<?php

$num_columns	= 3;
$has_records	= isset($records) && is_array($records) && count($records);
$num_rows = count($records);
?>
<div class='content'>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class='table table-bordered table-condensed'>
			<caption><h5><div class="alert alert-info">Product Portfolio (<?php e($num_rows); ?>)</div></h5></caption>
			<thead>
				<tr>
					<th><?php echo lang('products_field_name'); ?></th>
					<th><?php echo lang('products_field_desc'); ?></th>
					<th><?php echo lang('products_field_class'); ?></th>
				</tr>
			</thead>
			<tbody>
				<?php
				if ($has_records) :
					$prev_catg = '';	
					foreach ($records as $record) :
						if ($prev_catg != $record->catg):
							$prev_catg = $record->catg;
						?>
							<tr class="success"><td colspan="3"><strong><?php e($record->catg); ?></strong></tr>
						<?php endif; ?>		
				<tr>
					<td><?php echo anchor(SITE_AREA . '/content/products/details/' . $record->id, $record->name); ?></td>
					<td><?php e($record->desc); ?></td>
					<td><?php e($record->class); ?></td>
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