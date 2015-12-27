<?php

$num_columns	= 9;
$can_delete	= $this->auth->has_permission('Vendor_Contacts.Content.Delete');
$can_edit		= $this->auth->has_permission('Vendor_Contacts.Content.Edit');
$can_view		= $this->auth->has_permission('Vendor_Contacts.Content.View');
$has_records	= isset($records) && is_array($records) && count($records);
if (!$can_view){
	exit;
}

?>
<div class="admin-box">
    <?php if ($has_records) : ?>
    <div class="panel panel-primary">
        <div class="panel-heading">
            Vendor Contacts
        </div>
        <div class="panel-body">
            <table class="table table-condensed table-bordered">
                <tr>
                    <td><strong>Name</strong></td><td><strong>Office Phone</strong></td><td><strong>Cell Phone</strong></td>
                </tr>
                <?php
                    foreach ($records as $record) : ?>
                        <tr>
                            <td><?php echo anchor(SITE_AREA . '/content/vendor_contacts/edit/' . $record->id, $record->name); ?></td><td><?php e($record->work_phone) ?></td><td><?php e($record->cell_phone) ?></td>
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
                Vendor Contacts
            </div>
            <div class="panel-body">
                <p>No records found that match your selection. <a href="content/vendor_contacts/create" class="btn btn-primary" name="Create" id="Create">Create</a> </p>
            </div>
        </div>    
    <?php
        endif; 
    ?> 
</div>


