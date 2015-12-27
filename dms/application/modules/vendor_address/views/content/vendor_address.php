<?php

$num_columns	= 9;
$can_delete	= $this->auth->has_permission('Vendor_Address.Content.Delete');
$can_edit		= $this->auth->has_permission('Vendor_Address.Content.Edit');
$can_view		= $this->auth->has_permission('Vendor_Profile.Content.View');
$has_records	= isset($records) && is_array($records) && count($records);
if (!$can_view){
	exit;
}

?>
<div class="admin-box">
    <?php if ($has_records) : ?>
    <div class="panel panel-primary">
        <div class="panel-heading">
            Vendor Address
        </div>
        <div class="panel-body">
            <table class="table table-condensed table-bordered">
                <tr>
                    <td><strong>Location Type</strong></td><td><strong>Address</strong></td>
                </tr>
                <?php
                    foreach ($records as $record) : ?>
                        <tr>
                            <td><?php echo anchor(SITE_AREA . '/content/vendor_address/edit/' . $record->id, $record->loc_type); ?></td><td><?php e($record->address1 . ', ' . $record->address2) ?></td>
                        </tr>
                <?php endforeach; ?>

            </table>
        </div>
    </div>    
    <?php 
        else:
    ?>
        <div class="panel panel-primary">
            <div class="panel-heading">
                Vendor Address
            </div>
            <div class="panel-body">
                <p>No records found that match your selection. <a href="content/vendor_address/create" class="btn btn-primary" name="Create" id="Create">Create</a> </p>
            </div>
        </div>    
    <?php
        endif; 
    ?> 
</div>


