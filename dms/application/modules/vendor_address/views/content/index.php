<?php

$num_columns	= 7;
$can_delete	= $this->auth->has_permission('Vendor_Address.Content.Delete');
$can_edit		= $this->auth->has_permission('Vendor_Address.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class="admin-box">
	<h3>Vendor Address</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>Location Type</th>
					<th>Address1</th>
					<th>Address2</th>
                    <th>City</th>
                    <th>Country</th>
                    <th>Office phones</th>
                    <th>Office Fax</th>
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
				<?php

					$vendor_name = null;
					if (isset($vendors)):
						foreach($vendors as $vendor){
							if($vendor->id == $record->vendor_id){
								$vendor_name = $vendor->name;
							}
						}
					endif;

                    $country_name = NULL;
                    if (isset($countries)):
                        foreach($countries as $country){
                            if($country->iso == $record->country_id){
                                $country_name = $country->name;		
                            }
                        }
                    endif;

				?>					
				<tr>
					<?php if ($can_delete) : ?>
					<td class="column-check"><input type="checkbox" name="checked[]" value="<?php echo $record->id; ?>" /></td>
					<?php endif;?>
					
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/vendor_address/edit/' . $record->id, '<span class="icon-pencil"></span>&nbsp;' .  $record->loc_type); ?></td>
				<?php else : ?>
					<td><?php e($record->loc_type); ?></td>
				<?php endif; ?>
					<td><?php e($record->address1) ?></td>
					<td><?php e($record->address2) ?></td>
					<td><?php e($record->city) ?></td>
                    <td><?php e($country_name) ?></td>
                    <td><?php e($record->office_phones) ?></td>
                    <td><?php e($record->office_fax) ?></td>
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
            Click <strong><a class="alert-link" href="vendor_contacts">Here</a></strong> to continue or click on <strong><a class="alert-link" href="<?php echo site_url(SITE_AREA .'/content') ?>">Home</a></strong> to check overall progress of your registration
        </div>
    
	<?php echo form_close(); ?>
    <?php $this->pagination->create_links(); ?>
</div>