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
    <div ng-app="SristiBio" class="admin-box" ng-controller="TodoCtrl">
            <div>
                <div class="span4">
                    <input type="hidden" ng-model="entityLimit" value="10"/>
                    <div class="controls">
                        Filter: <input class="input-medium search-query" type="text" ng-model="search" ng-change="filter()" placeholder="Filter" />
                    </div>
    <!--                <select ng-model="entryLimit" class="form-control">
                        <option>5</option>
                        <option>10</option>
                        <option>20</option>
                        <option>50</option>
                        <option>100</option>
                    </select>-->
                </div>
                <div class="span6">
                    <h5>Filtered {{ filtered.length }} of {{ totalItems}} total records</h5>
                </div>            
            </div>
            <br/>
            <div>
                 <div class="span11" ng-show="filteredItems > 0">
                     <table class="table table-condensed table-bordered">
                         <thead>
                             <th>List</th>
                             <th>Subject</th>
                             <th>Notes</th>
                             <th>Created By</th>
                             <th>Assigned To</th>
                             <th>Due By</th>
                         </thead>
                         <tbody>
                             <tr ng-repeat="data in filtered = (list | filter:search | orderBy : predicate :reverse) | startFrom:(currentPage-1)*entryLimit | limitTo:entryLimit">
                                 <td>{{data.list_id}}</td>
                                 <td><a href="todo/edit/{{data.id}}">{{data.name}}</a></td>
                                 <td>{{data.notes | limitTo:30}}...</td>
                                 <td>{{data.created_by}}</td>
                                 <td>{{data.assigned_to}}</td>
                                 <td>{{data.due_by | date:'d/MMM'}}</td>
                             </tr>
                         </tbody>
                     </table>
                    <div class="span10" ng-show="filteredItems > 0">    
                        <div class="pagination pagination-small pagniation-centered" pagination="" page="currentPage" on-select-page="setPage(page)" boundary-links="true" total-items="filteredItems" items-per-page="entryLimit" previous-text="&laquo;" next-text="&raquo;"></div>
                    </div>                 
                </div>
            </div>
</div>
<!--
<div class="admin-box">
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-striped table-condensed">
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
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/todo/edit/' . $record->id, $todo_list_name); ?></td>
				<?php else : ?>
					<td><?php e($todo_list_name); ?></td>
				<?php endif; ?>
					<td><?php e($record->name) ?></td>
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
	<?php echo form_close(); ?>
</div>
-->