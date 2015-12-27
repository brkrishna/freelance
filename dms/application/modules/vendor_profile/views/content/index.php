<?php

$num_columns	= 7;
$can_delete	= $this->auth->has_permission('Vendor_Profile.Content.Delete');
$can_edit		= $this->auth->has_permission('Vendor_Profile.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class="admin-box">
	<h3>Vendor Profile</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>Name</th>
					<th>Establishment Type</th>
					<th>Constitution of Company</th>
					<th>Year of Establishment</th>
                    <th>Website</th>
                    <th>Profile</th>
                    <th>Full Profile</th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('vendor_profile_delete_confirm'))); ?>')" />
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
					<?php if ($can_delete) : ?>
					<td class="column-check"><input type="checkbox" name="checked[]" value="<?php echo $record->id; ?>" /></td>
					<?php endif;?>
					
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/vendor_profile/edit/' . $record->id, '<span class="icon-pencil"></span>&nbsp;' .  $record->name); ?></td>
				<?php else : ?>
					<td><?php e($record->name); ?></td>
				<?php endif; ?>
					<td><?php e($record->est_type) ?></td>
					<td><?php e($record->est_const) ?></td>
					<td><?php e($record->est_start_yr) ?></td>
                    <td><?php e($record->website) ?></td>
                    <td><?php e(substr($record->profile, 0, 50) . '...') ?></td>
                    <td><?php echo anchor(SITE_AREA . '/content/vendor_profile/vendor_details/' . $record->id, '<span class="icon-zoom-out"></span>'); ?></td>
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
            Click <strong><a class="alert-link" href="vendor_address">Here</a></strong> to continue or click on <strong><a class="alert-link" href="<?php echo site_url(SITE_AREA .'/content') ?>">Home</a></strong> to check overall progress of your registration
        </div>
        
	<?php echo form_close(); ?>
    <?php echo $this->pagination->create_links(); ?>
</div>