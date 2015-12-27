<?php

$num_columns	= 13;
$can_delete	= $this->auth->has_permission('Factory.Content.Delete');
$can_edit		= $this->auth->has_permission('Factory.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class="admin-box">
	<h3>Factory</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>Name</th>
                    <th>Address</th>
                    <th>Employee size</th>
					<th>Capacity per Month</th>
					<th>Capacity per Day</th>
					<th>Capacity - Raw material <br/>(Metric tonnes)</th>
					<th>Storage Capacity <br/>(Metric tonnes)</th>
					<th>Nearest Port</th>
					<th>Nearest Airport</th>
					<th>Nearest Major City</th>
					<th>Transportation options</th>
					<th>Courier Company</th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('factory_delete_confirm'))); ?>')" />
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
					$m_uom_name = null;
					if (isset($uoms)):
						foreach($uoms as $uom){
							if($uom->id == $record->m_cpcty_uom){
								$m_uom_name = $uom->name;
							}
						}
					endif;

					$d_uom_name = null;
					if (isset($uoms)):
						foreach($uoms as $uom){
							if($uom->id == $record->d_cpcty_uom){
								$d_uom_name = $uom->name;
							}
						}
					endif;


                ?>
				<tr>
					<?php if ($can_delete) : ?>
					<td class="column-check"><input type="checkbox" name="checked[]" value="<?php echo $record->id; ?>" /></td>
					<?php endif;?>
					
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/factory/edit/' . $record->id, '<span class="icon-pencil"></span>&nbsp;' .  $record->name); ?></td>
				<?php else : ?>
					<td><?php e($record->name); ?></td>
				<?php endif; ?>
                    <td><?php e($record->address) ?></td>
                    <td><?php e($record->no_of_emps) ?></td>
					<td><?php e($record->m_cpcty . ' ' . $m_uom_name) ?></td>
					<td><?php e($record->d_cpcty . ' ' . $d_uom_name) ?></td>
					<td><?php e($record->cpcty_raw_mtrl) ?></td>
					<td><?php e($record->cpcty_storage) ?></td>
					<td><?php e($record->near_port) ?></td>
					<td><?php e($record->near_airport) ?></td>
					<td><?php e($record->near_city) ?></td>
					<td><?php e($record->transport_opt) ?></td>
					<td><?php e($record->courier_comp) ?></td>
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
        <hr/>
        <div class="alert alert-warning lead">
            Click <strong><a class="alert-link" href="bank_details">Here</a></strong> to continue or click on <strong><a class="alert-link" href="<?php echo site_url(SITE_AREA .'/content') ?>">Home</a></strong> to check overall progress of your registration
        </div>
    
	<?php echo form_close(); ?>
    <?php echo $this->pagination->create_links(); ?>
</div>