<?php

$num_columns	= 6;
$can_delete	= $this->auth->has_permission('Vendor_Contacts.Content.Delete');
$can_edit		= $this->auth->has_permission('Vendor_Contacts.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class="admin-box">
	<h3>Vendor Contacts</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>Vendor Id</th>
					<th>Name</th>
					<th>Designation</th>
					<th>Office Phone</th>
					<th>Cell Phone</th>
					<th>Email</th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('vendor_contacts_delete_confirm'))); ?>')" />
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
				<?php

					$vendor_name = null;
					if (isset($vendors)):
						foreach($vendors as $vendor){
							if($vendor->id == $record->vendor_id){
								$vendor_name = $vendor->name;
							}
						}
					endif;

				?>					
					
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/vendor_contacts/edit/' . $record->id, '<span class="icon-pencil"></span>&nbsp;' .  $vendor_name); ?></td>
				<?php else : ?>
					<td><?php e($vendor_name); ?></td>
				<?php endif; ?>
					<td><?php e($record->name) ?></td>
					<td><?php e($record->dsgn) ?></td>
					<td><?php e($record->work_phone) ?></td>
					<td><?php e($record->cell_phone) ?></td>
					<td><?php e($record->email_id) ?></td>
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
            Click <strong><a class="alert-link" href="factory">Here</a></strong> to continue or click on <strong><a class="alert-link" href="<?php echo site_url(SITE_AREA .'/content') ?>">Home</a></strong> to check overall progress of your registration
        </div>
	<?php echo form_close(); ?>
     <?php echo $this->pagination->create_links(); ?>   
</div>