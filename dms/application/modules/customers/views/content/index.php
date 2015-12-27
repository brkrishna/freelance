<?php

$num_columns	= 14;
$can_delete	= $this->auth->has_permission('Customers.Content.Delete');
$can_edit		= $this->auth->has_permission('Customers.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class="admin-box">
	<h3>Customers</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
    
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>Name</th>
					<th>Contact Name</th>
					<th>Contact Phone</th>
					<th>Contact Email</th>
					<th>Address1</th>
					<th>Address2</th>
					<th>City</th>
					<th>Country</th>
					<th>Office Phones</th>
					<th>Website URL</th>
					<th><?php echo lang("customers_column_deleted"); ?></th>
					<th><?php echo lang("customers_column_created"); ?></th>
					<th><?php echo lang("customers_column_modified"); ?></th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('customers_delete_confirm'))); ?>')" />
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
					<td><?php echo anchor(SITE_AREA . '/content/customers/edit/' . $record->id, '<span class="icon-pencil"></span>' .  $record->name); ?></td>
				<?php else : ?>
					<td><?php e($record->name); ?></td>
				<?php endif; ?>
					<td><?php e($record->contact_name) ?></td>
					<td><?php e($record->contact_phone) ?></td>
					<td><?php e($record->contact_email) ?></td>
					<td><?php e($record->address1) ?></td>
					<td><?php e($record->address2) ?></td>
					<td><?php e($record->city) ?></td>
					<td><?php 
							if (isset($countries)):
								foreach($countries as $country){
									if($country->iso == $record->country){
										e($country->name);		
									}
								}
							endif;
						?>
					</td>
					<td><?php e($record->work_phones) ?></td>
					<td><?php e($record->website_url) ?></td>
					<td><?php echo $record->deleted > 0 ? lang('customers_true') : lang('customers_false')?></td>
					<td><?php e($record->created_on) ?></td>
					<td><?php e($record->modified_on) ?></td>
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
	<?php echo form_close(); ?>
    <?php echo $this->pagination->create_links(); ?>
</div>