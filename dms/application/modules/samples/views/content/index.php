<?php

$num_columns	= 9;
$can_delete	= $this->auth->has_permission('Samples.Content.Delete');
$can_edit		= $this->auth->has_permission('Samples.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class="admin-box">
	<h3>Samples</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
        
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
                    
					<th>Internal Ref No</th>
					<th>Product</th>
                    <th>Po No</th>
                    <th>Party Type</th>
                    <th>Trans Type</th>
					<th>Quantity</th>
					<th>UOM</th>
					<th>Party Name</th>
                    <th>Courier</th>
                    <th>Tracking No</th>
					<th>Date Received</th>
					<!--
					<th><?php echo lang("samples_column_deleted"); ?></th>
					<th><?php echo lang("samples_column_created"); ?></th>
					<th><?php echo lang("samples_column_modified"); ?></th>
					-->
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('samples_delete_confirm'))); ?>')" />
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
                    <td><?php e($record->int_ref_num) ?></td>
				<?php
					$product_name = null;
					if (isset($products)):
						foreach($products as $product){
							if($product->id == $record->product_id){
								$product_name = $product->name . ' - ' . $product->desc;
							}
						}
					endif;

					$uom_name = null;
					if (isset($uoms)):
						foreach($uoms as $uom){
							if($uom->id == $record->uom_id){
								$uom_name = $uom->name;
							}
						}
					endif;

                  /*  $party_type = null;
					if (isset($customer)):
						foreach($customer as $customers){
							if($customers->id == $record->customers_id){
								$party_type = $party_type . $party->name;
							}
						}
					endif;
                    */
                    
                   $party_type = null;
                   if(isset($customer)):
                       foreach($customer as $customers){
                          if($customers->id == $record->customers_id){
                              $party_type = $party->type;
                          }    
                       
                   } 
                    endif;

					$party_name = null;
					if (isset($customer)):
						foreach($customer as $customers){
							if($customers->id == $record->customers_id){
								$party_name = $party->name;
							}
						}
					endif;

                    
				?>					
				<?php if ($can_edit) : ?>
                    
					<td><?php echo anchor(SITE_AREA . '/content/samples/edit/' . $record->id, '<span class="icon-pencil"></span>' .  $product_name); ?></td>
				    
                    <?php else : ?>
					<td><?php e($product_name); ?></td>
                    
				<?php endif; ?>
                    <td><?php e($record->po_no) ?></td>
                    <td><?php e($record->party_type) ?></td>
                    <td><?php e($record->trans_type) ?></td>
					<td><?php e($record->quantity) ?></td>
					<td><?php e($uom_name) ?></td>
					<td><?php e($record->party_name) ?></td>
                    <td><?php e($record->courier) ?></td>
                    <td><?php e($record->tracking_no) ?></td>
					<td><?php e($record->date_received) ?></td>
					<!--<td><?php echo $record->deleted > 0 ? lang('samples_true') : lang('samples_false')?></td>
					<td><?php e($record->created_on) ?></td>
					<td><?php e($record->modified_on) ?></td>-->
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