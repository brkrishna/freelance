<?php

$hiddenFields = array('mol_id',);
?>
<h1 class='page-header'>
    <?php echo lang('botanicules_area_title'); ?>
</h1>
<?php if (isset($records) && is_array($records) && count($records)) : ?>
<table class='table table-striped table-bordered'>
    <thead>
        <tr>
            
            <th>Mol Weight</th>
            <th>Formula</th>
            <th>Compound Name</th>
            <th>Mol Name</th>
            <th>Reference</th>
            <th>Source Reference</th>
            <th>Molecule Type</th>
            <th>Therapeutic Category</th>
            <th>IUPAC Name</th>
            <th>Source Type</th>
            <th>Source Family</th>
            <th>Qc Status</th>
            <th>Pdf Availability</th>
            <th>Part of Isolation</th>
        </tr>
    </thead>
    <tbody>
        <?php
        foreach ($records as $record) :
        ?>
        <tr>
            <?php
            foreach($record as $field => $value) :
                if ( ! in_array($field, $hiddenFields)) :
            ?>
            <td>
                <?php
                if ($field == 'deleted') {
                    e(($value > 0) ? lang('botanicules_true') : lang('botanicules_false'));
                } else {
                    e($value);
                }
                ?>
            </td>
            <?php
                endif;
            endforeach;
            ?>
        </tr>
        <?php endforeach; ?>
    </tbody>
</table>
<?php

endif; ?>