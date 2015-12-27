<?php

$can_delete	= $this->auth->has_permission('Purchase_Orders.Content.Delete');
$can_edit		= $this->auth->has_permission('Purchase_Orders.Content.Edit');
$can_edit_fulfillment	= $this->auth->has_permission('PO_Fulfillment.Content.Edit');
$can_edit_containers	= $this->auth->has_permission('PO_Containers.Content.Edit');
$can_edit_docs	= $this->auth->has_permission('PO_Documents.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);
$can_view       = $this->auth->has_permission('Purchase_Orders.Content.View');

if(!$can_view){
    exit;
}
?>
<?php if ($has_records) : ?>
		<table class="table table-condensed table-bordered">
            <caption>Purchase Order</caption>
			<thead>
				<tr>
					<th>PO No</th>
					<th>PO Date</th>
					<th>Product</th>
					<th>Quantity</th>
					<th>Rate</th>
					<th>Mode of Packing</th>
					<th>Customer</th>
					<th>Status</th>
					<th>Comments</th>
				</tr>
			</thead>
			<tbody>
                
                <?php 
                    $uom_name = NULL;
                    $customer_name = NULL;
                    $product_name = NULL;

                    $po_details = $records['po_details'];

                    if ($po_details != NULL) :
                        foreach($po_details as $record){
                         ?>
                            <tr>
                                <?php if ($can_edit) : ?>
                                    <td><?php echo anchor(SITE_AREA . '/content/purchase_orders/edit/' . $record->id, $record->po_no); ?></td>
                                <?php else : ?>
                                    <td><?php e($record->po_no); ?></td>
                                <?php endif; ?>
                                <td><?php e($record->po_dt) ?></td>
                                <td><?php e($record->prod_name) ?></td>
                                <td><?php e($record->qty . ' ' . $record->uom_name) ?></td>
                                <td><?php e($record->rate) ?></td>
                                <td><?php e($record->no_of_units . ' ' . $record->packing_mode) ?></td>
                                <td><?php e($record->cust_name) ?></td>
                                <td><?php e($record->status_id) ?></td>
                                <td><?php e($record->comments) ?></td>
                            </tr>
                    <?php
                        }
                    endif;
				?>
			</tbody>
		</table>
        <table class="table table-condensed table-bordered">
            <caption>Fulfillment Details - <?php echo anchor(SITE_AREA . '/content/po_fulfillment/create/' . $record->id, 'Add New'); ?></caption>
			<thead>
                <tr>
                    <th>Vendor</th>
                    <th>Product</th>
                    <th>Quantity</th>
                    <th>Rate</th>
                    <th>Mode of Packing</th>                
                    <th>Supply from</th>
                    <th>Destination Port</th>
                </tr>            
            </thead>
            <tbody>
                <?php   
                    if ($po_details != NULL) :
                        foreach($po_details as $record){ ?>
                            <tr>
                                <?php if ($can_edit_fulfillment) : ?>
                                    <td><?php echo anchor(SITE_AREA . '/content/po_fulfillment/edit/' . $record->fulfillment_id, $record->vendor_name); ?></td>
                                <?php else : ?>
                                    <td><?php e($record->vendor_name); ?></td>
                                <?php endif; ?>
                                
                                <td><?php e($record->prod_name) ?></td>    
                                <td><?php e($record->qty . ' ' . $record->uom_name) ?></td>
                                <td><?php e($record->rate) ?></td>
                                <td><?php e($record->no_of_units . ' ' . $record->packing_mode) ?></td>
                                <td><?php e($record->supply_from) ?></td>
                                <td><?php e($record->dest_port) ?></td>
                            </tr>
                        <?php }
                    endif;
                 ?>
            </tbody>
        </table>
        <table class="table table-condensed table-bordered">
            <caption>Container Details - <?php echo anchor(SITE_AREA . '/content/po_containers/create/' . $record->id, 'Add New'); ?></caption>
			<thead>
                <tr>
					<th>Batch No</th>
					<th>Vessel</th>
					<th>Container</th>
					<th>Seal</th>
                </tr>            
            </thead>
            <tbody>
                <?php   
                    if ($po_details != NULL) :
                        foreach($po_details as $record){ ?>
                            <tr>
                                <?php if ($can_edit_containers) : ?>
                                    <td><?php echo anchor(SITE_AREA . '/content/po_containers/edit/' . $record->container_id, $record->batch_no); ?></td>
                                <?php else : ?>
                                    <td><?php e($record->batch_no); ?></td>
                                <?php endif; ?>
                                <td><?php e($record->vessel) ?></td>    
                                <td><?php e($record->container) ?></td>
                                <td><?php e($record->seal) ?></td>
                            </tr>
                        <?php }
                    endif;
                 ?>
            </tbody>
        </table>
        <table class="table table-condensed table-bordered">
            <caption>Documents - <?php echo anchor(SITE_AREA . '/content/po_documents/create/' . $record->id, 'Add New'); ?></caption>
			<thead>
                <tr>
					<th>Document Name</th>
					<th>Applicable</th>
					<th>Attachment</th>
                </tr>            
            </thead>
            <tbody>
                <?php   
                    $po_docs = $records['po_docs'];    
                    if ($po_docs != NULL) :
                        foreach($po_docs as $record){ ?>
                            <tr>
                                <?php if ($can_edit_docs) : ?>
                                    <td><?php echo anchor(SITE_AREA . '/content/po_documents/edit/' . $record->id, $record->document_name); ?></td>
                                <?php else : ?>
                                    <td><?php e($record->document_name); ?></td>
                                <?php endif; ?>
                                <td><?php e($record->applicable) ?></td>
                                <?php 
                                        $attachment = NULL;
                                        $attachment = unserialize($record->attachment);
                                        
                                        if ($attachment != NULL){
                                            echo "<td><a href=" . base_url() . 'uploads/' . $attachment['file_name'] . " target='_blank' >" . $attachment['file_name'] . "</td>";        
                                        }else{
                                            echo "<td>&nbsp;</td>";
                                        }                                                
                                ?>
                            </tr>
                        <?php }
                    endif;
                 ?>
            </tbody>
        </table>        
<?php endif; ?>