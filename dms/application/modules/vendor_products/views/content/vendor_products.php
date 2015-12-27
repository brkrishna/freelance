<?php

$num_columns	= 2;
$can_delete	= $this->auth->has_permission('Vendor_Products.Content.Delete');
$can_edit		= $this->auth->has_permission('Vendor_Products.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

?>
    <?php if ($has_records) : ?>
        <table class="table table-condensed table-bordered">
            <tr class="info">
                <td><strong>Products</strong></td><td><a class="alert-link" href="content/vendor_products/create"><strong>Add</strong></a></td>    
            </tr>
                <?php foreach ($records as $record) : ?>
                <tr>
                    <td colspan="2"><?php echo anchor(SITE_AREA . '/content/vendor_products/edit/' . $record->id, $record->product_name . ' - ' . $record->product_desc); ?></td>
                </tr>
                <?php endforeach; ?>    
        </table>
    <?php 
        else:
    ?>
        <div class="panel panel-primary">
            <div class="panel-heading">
                Vendor Products
            </div>
            <div class="panel-body">
                <p>No records found that match your selection. <a href="content/vendor_products/create" class="btn btn-primary" name="Create" id="Create">Create</a> </p>
            </div>
        </div>    
    <?php
        endif; 
    ?> 
