<?php

$num_columns	= 13;
$can_delete	= $this->auth->has_permission('Purchase_Orders.Content.Delete');
$can_edit		= $this->auth->has_permission('Purchase_Orders.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);
$can_view       = $this->auth->has_permission('Purchase_Orders.Content.View');

if(!$can_view){
    exit;
}
?>
<div class="admin-box">
    <h3><center>PO Dashboard</center></h3>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class="table table-condensed table-bordered">
			<thead>
				<tr>
					<th>PO No</th>
					<th>PO Date</th>
					<th>Product</th>
					<th>Quantity</th>
					<th>Rate</th>
					<th>Mode of Packing</th>
                    <th>Batch No</th>
                    <th>Vessel</th>
                    <th>Container</th>
                    <th>Seal</th>
                    <th>Supply From</th>
                    <th>Destination Port</th>
                    <th>Supplier</th>
					<th>Comments</th>
				</tr>
			</thead>
			<tbody>
				<?php
				if ($has_records) :
					foreach ($records as $record) :
                        $po_dt = date('d/M/y', strtotime($record->po_dt));
				?>
				<tr>
					
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/purchase_orders/edit/' . $record->id, $record->po_no); ?></td>
				<?php else : ?>
					<td><?php e($record->po_no); ?></td>
				<?php endif; ?>
					<td><?php e($po_dt) ?></td>
					<td><?php e($record->prod_name) ?></td>
                    <td><?php e($record->qty . ' ' . $record->uom_name) ?></td>
					<td><?php e($record->rate . ' / ' . $record->uom_name) ?></td>
					<td><?php e($record->no_of_units . ' ' . $record->packing_mode) ?></td>
                    <td><?php e($record->batch_no) ?></td>
                    <td><?php e($record->vessel) ?></td>
                    <td><?php e($record->container) ?></td>
                    <td><?php e($record->seal) ?></td>                    
					<td><?php e($record->supply_from) ?></td>
                    <td><?php e($record->dest_port) ?></td>
                    <td><?php e($record->vendor_name) ?></td>
                    <td><?php e($record->comments) ?></td>
				</tr>
                <tr><td colspan="14">
                    <table class="table table-condensed table-bordered"><tr>
                        <?php 
                            foreach($activity_docs as $ad){
                                $printed = 0;
                                foreach($po_docs as $po_doc){
                                    
                                    if ($po_doc->po_no == $record->id && $po_doc->document_id == $ad->document_id){
                                        
                                        $attachment = NULL;
                                        $attachment = unserialize($po_doc->attachment);
                                        
                                        if ($attachment != NULL && $po_doc->applicable == 'Yes'){
                                            $printed = 1;
                                            echo "<td><a href=" . base_url() . 'uploads/' . $attachment['file_name'] . " target='_blank' ><span class='label label-success'><h6>" . $ad->document_name . "</h6></span></td>";        
                                        }elseif($po_doc->applicable == 'No'){
                                            $printed = 1;
                                            echo "<td><span class='label label-default'><h6>" . $ad->document_name . "</h6></span></td>";        
                                        }else{
                                            $printed = 1;
                                            echo "<td><span class='label label-warning'><h6>" . $ad->document_name . "</h6></span></td>";        
                                        }
                                    }
                                }
                                if ($printed == 0){
                                    echo "<td><span class='label label-warning'><h6>" . $ad->document_name . "</h6></span></td>";        
                                }
                            }
                        ?>
                    </tr></table>
                    <br/>
                </td></tr>
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
        <span class="label label-info"> Items in Orange -> Pending, Gray -> Not applicable, Green -> Uploaded <br/>Click on Green icons do download and view</span>
	<?php echo form_close(); ?>
</div>