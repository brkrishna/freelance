<?php
$can_delete	= $this->auth->has_permission('Vendor_Profile.Content.Delete');
$can_edit		= $this->auth->has_permission('Vendor_Profile.Content.Edit');
$can_view		= $this->auth->has_permission('Vendor_Profile.Content.View');
$has_records	= isset($records) && is_array($records) && count($records);
if (!$can_view){
	exit;
}
?>
<?php if ($has_records) : ?>
    <table class="table table-bordered table-condensed">
        <caption><h4>Vendor Profile</h4></caption>
        <tr class="info">
            <td><strong>Name</strong></td><td>Est Year</td><td>Type</td>
        </tr>
        <?php foreach ($records as $record) : ?>
        <tr>
            <td><?php echo anchor(SITE_AREA . '/content/vendor_profile/edit/' . $record->id, $record->name); ?></td><td><?php e($record->est_start_yr) ?></td><td><?php e($record->est_type) ?></td>
        </tr>
        <?php endforeach; ?>
    </table>
<?php endif; ?> 
