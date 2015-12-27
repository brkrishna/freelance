<?php

$num_columns	= 8;
$can_delete	= $this->auth->has_permission('Todo.Content.Delete');
$can_edit		= $this->auth->has_permission('Todo.Content.Edit');
$can_view		= $this->auth->has_permission('Todo.Content.View');
$has_records	= isset($records) && is_array($records) && count($records);
if(!$can_view){
    exit;
}

?>
<div class="admin-box">
	<?php echo form_open($this->uri->uri_string()); ?>
<<<<<<< HEAD
            <ul class="nav nav-tabs">
                <li <?php echo $filter == 'status' ? 'class="dropdown active"' : ''; ?> class="dropdown"> 
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                        By Status <?php echo isset($filter_status) ? ": $filter_status" : ''; ?>
                        <b class="caret light-caret"></b>
                    </a>            
                    <ul class="dropdown-menu">
                        <?php if (isset($statuses) && is_array($statuses) && count($statuses)) : 
                                foreach($statuses as $status) : ?>
                                    <li>
                                        <a href="<?php echo $current_url . '?filter=status&status=' . $status ?>">
                                            <?php echo $status; ?>
                                        </a>
                                    </li>                                
                                <?php 
                                endforeach; 
                              endif; 
                        ?>
                    </ul>
                </li>
                <li <?php echo $filter == 'list' ? 'class="dropdown active"' : ''; ?> class="dropdown"> 
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                        By List <?php echo isset($filter_list) ? ": $filter_list" : ''; ?>
                        <b class="caret light-caret"></b>
                    </a>            
                    <ul class="dropdown-menu">
                        <?php if (isset($lists) && is_array($lists) && count($lists)) : 
                                foreach($lists as $list) : ?>
                                    <li>
                                        <a href="<?php echo $current_url . '?filter=list&list=' . $list->id; ?>">
                                            <?php echo $list->name; ?>
                                        </a>
                                    </li>                                
                                <?php 
                                endforeach; 
                              endif; 
                        ?>
                    </ul>
                </li>
                <!--<li>
                    <div class="input-append">
                        <input class="span2" id="appendedInputButton" name="appendedInputButton" type="text">
                        <button class="btn" type="submit">Go!</button>
                    </div>                    
                </li>-->
                
            </ul>
		<table class="table table-striped table-condensed">
=======
   
		<table class="table table-striped">
>>>>>>> f19371064a9ba4d3faff72c86b6ae2805aa04588
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class="column-check"><input class="check-all" type="checkbox" /></th>
					<?php endif;?>
					
					<th>List</th>
					<th>Subject</th>
					<th>Notes</th>
					<th>Created By</th>
					<th>Assigned To</th>
					<th>Due By</th>
                    <th>Status</th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan="<?php echo $num_columns; ?>">
						<?php echo lang('bf_with_selected'); ?>
						<input type="submit" name="delete" id="delete-me" class="btn btn-danger" value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('todo_delete_confirm'))); ?>')" />
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
					$todo_list_name = null;
					if (isset($todo_lists)):
						foreach($todo_lists as $todo_list){
							if($todo_list->id == $record->list_id){
								$todo_list_name = $todo_list->name;
							}
						}
					endif;

					$created_name = null;
					if (isset($users)):
						foreach($users as $user){
							if($user->id == $record->created_by){
								$created_name = $user->display_name;
							}
						}
					endif;

					$assigned_name = null;
					if (isset($users)):
						foreach($users as $user){
							if($user->id == $record->assigned_to){
								$assigned_name = $user->display_name;
							}
						}
					endif;
                    $due_dt = date('d/M', strtotime($record->due_by));
                ?>  
                    <td><?php e($todo_list_name) ?></td>
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/todo/edit/' . $record->id, $record->name); ?></td>
				<?php else : ?>
					<td><?php e($record->name); ?></td>
				<?php endif; ?>
					<td><?php e($record->notes) ?></td>
					<td><?php e($created_name) ?></td>
					<td><?php e($assigned_name) ?></td>
					<td><?php e($due_dt) ?></td>
                    <td><?php e($record->status) ?></td>
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
        <?php echo $this->pagination->create_links(); ?>   
	<?php echo form_close(); ?>
<<<<<<< HEAD
</div>
=======
     <?php echo $this->pagination->create_links(); ?>
</div>
>>>>>>> f19371064a9ba4d3faff72c86b6ae2805aa04588
