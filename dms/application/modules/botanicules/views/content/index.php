<?php

$num_columns	= 20;
$can_delete	= $this->auth->has_permission('Botanicules.Content.Delete');
$can_edit		= $this->auth->has_permission('Botanicules.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
<div class="admin-box">
	<h3>Botanicules</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-striped">
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>Molecular Weight</th>
					<th>Structure</th>
					<th>Formula</th>
					<th>Compound Name</th>
					<th>Molecule Name</th>
					<th>Reference</th>
					<th>Source Reference</th>
					<th>Molecule Type</th>
					<th>Therapeutic Category</th>
					<th>IUPAC Name</th>
					<th>Source Type</th>
					<th>Source Family</th>
					<th>QC Status</th>
					<th>PDF Availability</th>
					<th>Parts of Isolation</th>
					<th>User Id</th>
					<th><?php echo lang("botanicules_column_created"); ?></th>
					<th><?php echo lang("botanicules_column_modified"); ?></th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('botanicules_delete_confirm'))); ?>')" />
					</td>
				</tr>
				<?php endif; ?>
			</tfoot>
			<?php endif; ?>
			<tbody>
                
			     <?php
			            function tr4jme($inmol) {
						  $outmol = $inmol;
						  $outmol = str_replace("\r","",$outmol);
						  $outmol = strtr($outmol,"\n","|");
						  return($outmol);
						}

				?>	                
				<?php
				if ($has_records) :
					foreach ($records as $record) :
				?>
				<tr>
					<?php if ($can_delete) : ?>
					<td class="column-check"><input type="checkbox" name="checked[]" value="<?php echo $record->id; ?>" /></td>
					<?php endif;?>
					
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/botanicules/edit/' . $record->id, '<span class="icon-pencil"></span>' .  $record->mol_weight); ?></td>
				<?php else : ?>
					<td><?php e($record->mol_weight) ?></td>
				<?php endif; ?>
                <?php 

                    $mol = $record->structure;
                    $mol = str_replace("\r\n","\n",$mol);
                    $mol = str_replace("\n","\r\n",$mol);

                    $jmehitmol = tr4jme($mol);
                 ?>
                    <td>
						<applet code="JME.class" name="JME" archive="/app/public/JME.jar" width="360" height="315" id="JME">
							<param name="options" value="depict">
							<param name="mol" value="<?php echo ($jmehitmol); ?>" >
		                     You have to enable Java and JavaScript in your browser to use JME!
			             </applet>
                        
                    </td>
					
					<td><?php e($record->formula) ?></td>
					<td><?php e($record->compound_name) ?></td>
					<td><?php e($record->mol_name) ?></td>
					<td><?php e($record->ref) ?></td>
					<td><?php e($record->src_ref) ?></td>
					<td><?php e($record->mol_type) ?></td>
					<td><?php e($record->therapeutic_catg) ?></td>
					<td><?php e($record->iupac_name) ?></td>
					<td><?php e($record->src_type) ?></td>
					<td><?php e($record->src_family) ?></td>
					<td><?php e($record->qc_status) ?></td>
					<td><?php e($record->pdf_avail) ?></td>
					<td><?php e($record->parts_of_isol) ?></td>
					<td><?php e($record->user_id) ?></td>
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
</div>