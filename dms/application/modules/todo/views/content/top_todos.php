<?php

$num_columns	= 4;
$can_edit		= $this->auth->has_permission('Todo.Content.Edit');
$can_view		= $this->auth->has_permission('Todo.Content.View');
$has_records	= isset($records) && is_array($records) && count($records);
if(!$can_view){
    exit;
}

?>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-condensed table-bordered">
            <caption>
                <strong>ToDo</strong>
                <?php if ($can_edit) :
                    echo " - " . anchor(SITE_AREA . '/content/todo/create/', 'Add New');
                endif; ?>
            </caption>
			<thead>
				<tr class='bg-info'>
                    <th>&nbsp;</th>                        
					<th>Subject</th>
					<th>Assigned To</th>
					<th>Due By</th>
				</tr>
			</thead>
			<tbody>
				<?php
				if ($has_records) :
                    $prev_list_id = -1;
					foreach ($records as $record) :
                        $due_dt = date('d/M', strtotime($record->due_by));
                        if ($prev_list_id != $record->list_id) :
                            $prev_list_id = $record->list_id;
                            ?>
                                <tr><td colspan="4"><strong><?php e($record->list_name) ?></strong></td></tr>
                            <?php
                        endif;
                            ?>
                                <tr>
                                    <td>&nbsp;</td>                                        
                                    <td><?php echo anchor(SITE_AREA . '/content/todo/edit/' . $record->id, $record->name); ?></td>
                                    <td><?php e($record->assigned_name) ?></td>
                                    <td><?php e($due_dt) ?></td>
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
