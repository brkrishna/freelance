<?php

$num_columns	= 2;
$has_records	= isset($records) && is_array($records) && count($records);
$num_rows = count($records);
?>
<div class='content'>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class='table table-bordered table-condensed'>
            <caption><h5><div class="alert alert-info">Vendors (<?php e($num_rows); ?>)</div></h5></caption>
			<thead>
				<tr>
					<th><?php echo lang('party_field_org_name'); ?></th>
					<th><?php echo lang('party_field_contact'); ?></th>
				</tr>
			</thead>
			<tbody>
				<?php
				if ($has_records) :
					foreach ($records as $record) :
				?>
				<tr>
					<td><?php echo anchor(SITE_AREA . '/content/party_documents/listing/' . $record->id,  $record->org_name); ?></td>
					<td><?php e($record->contact); ?></td>
				</tr>
				<?php
					endforeach;
				else:
				?>
				<tr>
					<td colspan='<?php echo $num_columns; ?>'><?php echo lang('party_records_empty'); ?></td>
				</tr>
				<?php endif; ?>
			</tbody>
		</table>
	<?php
    echo form_close();
    ?>
</div>