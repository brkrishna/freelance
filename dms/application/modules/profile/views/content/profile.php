<?php

$num_columns	= 2;
$can_view		= $this->auth->has_permission('Profile.Content.View');
$can_edit		= $this->auth->has_permission('Profile.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);
if (!$can_view){
	exit;
}
?>
<div class="admin-box">
    <?php
        if ($has_records) :
            foreach ($records as $record) :
    ?>
        <div class="panel panel-primary">
            <div class="panel-heading">
                Profile
            </div>
            <div class="panel-body">
                <p><?php e($record->profile) ?></p>
            </div>
        </div>    
    <?php 
            endforeach;
        else:
    ?>
        <div class="panel panel-primary">
            <div class="panel-heading">
                Organization
            </div>
            <div class="panel-body">
                <p>No records found that match your selection. <a href="content/profile/create" class="btn btn-primary" name="Create" id="Create">Create</a> </p>
            </div>
        </div>    
    <?php
        endif; 
    ?> 
</div>