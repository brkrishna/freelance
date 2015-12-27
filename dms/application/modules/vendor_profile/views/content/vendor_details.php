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
        <caption><h4>Profile</h4></caption>
        <tr class="info">
            <th>Name</th>
            <th>Est Year</th>
            <th>Est Type</th>
            <th>Company</th>
            <th>Website</th>
        </tr>
        <?php 
            $vendor_profile = $records['vendor_profile'];
            if ($vendor_profile != NULL){
                foreach ($vendor_profile as $record) : ?>
                    <tr>
                        <td><?php e($record->name) ?></td>
                        <td><?php e($record->est_start_yr) ?></td>
                        <td><?php e($record->est_type) ?></td>
                        <td><?php e($record->est_const) ?></td>
                        <td><?php e($record->website) ?></td>
                    </tr>
                    <tr>
                        <td colspan="5"><?php e($record->profile) ?></td>
                    </tr>
                <?php endforeach; 
            }
        ?>
    </table>
    <table class="table table-bordered table-condensed">
        <caption><h4>Address</h4></caption>
        <tr>
            <th>Location Type</th>
            <th>Address</th>
            <th>City</th>
            <th>Country</th>
            <th>Office phones</th>
            <th>Office Fax</th>
        </tr>
        <?php 
            $vendor_address = $records['vendor_address'];
            if ($vendor_address != NULL){
                foreach ($vendor_address as $record) : ?>
                    <tr>
                        <td><?php e($record->loc_type) ?></td>
                        <td><?php e($record->address1 . ', ' . $record->address2) ?></td>
                        <td><?php e($record->city) ?></td>
                        <td><?php e($record->country_id) ?></td>
                        <td><?php e($record->office_phones) ?></td>
                        <td><?php e($record->office_fax) ?></td>
                    </tr>
                <?php endforeach; 
            }
        ?>
    </table>
    <table class="table table-bordered table-condensed">
        <caption><h4>Contacts</h4></caption>
        <tr>
            <th>Name</th>
            <th>Designation</th>
            <th>Office Phone</th>
            <th>Cell Phone</th>
            <th>Email</th>
        </tr>
        <?php 
            $vendor_contacts = $records['vendor_contacts'];
            if ($vendor_contacts != NULL){
                foreach ($vendor_contacts as $record) : ?>
                    <tr>
                        <td><?php e($record->name) ?></td>
                        <td><?php e($record->dsgn) ?></td>
                        <td><?php e($record->work_phone) ?></td>
                        <td><?php e($record->cell_phone) ?></td>
                        <td><?php e($record->email_id) ?></td>
                    </tr>
                <?php endforeach; 
            }
        ?>
    </table>
    <table class="table table-bordered table-condensed">
        <caption><h4>Factory / Unit details</h4></caption>
        <tr>
            <th>Name</th>
            <th>Address</th>
            <th>Employee size</th>
            <th>Capacity per Month</th>
            <th>Capacity per Day</th>
            <th>Capacity - Raw material <br/>(Metric tonnes)</th>
            <th>Storage Capacity <br/>(Metric tonnes)</th>
            <th>Nearest Port</th>
            <th>Nearest Airport</th>
            <th>Nearest Major City</th>
            <th>Transportation options</th>
            <th>Courier Company</th>
        </tr>
        <?php 
            $vendor_factory = $records['vendor_factory'];
            $uoms = $records['uoms'];

            if ($vendor_factory != NULL){
                foreach ($vendor_factory as $record) : ?>
                    <tr>
                        <td><?php e($record->name) ?></td>
                        <td><?php e($record->address) ?></td>
                        <td><?php e($record->no_of_emps) ?></td>
                        <td><?php 
                                $uom_name = null;
                                if (isset($uoms)):
                                    foreach($uoms as $uom){
                                        if($uom->id == $record->m_cpcty_uom){
                                            $uom_name = $uom->name;
                                        }
                                    }
                                endif;
                    
                                e($record->m_cpcty . ' ' . $uom_name) 
                                    
                            ?></td>
                        <td><?php 
                                $uom_name = null;
                                if (isset($uoms)):
                                    foreach($uoms as $uom){
                                        if($uom->id == $record->d_cpcty_uom){
                                            $uom_name = $uom->name;
                                        }
                                    }
                                endif;
                    
                                    
                                 e($record->d_cpcty . ' ' . $uom_name) 
                            ?></td>
                        <td><?php e($record->cpcty_raw_mtrl) ?></td>
                        <td><?php e($record->cpcty_storage) ?></td>
                        <td><?php e($record->near_port) ?></td>
                        <td><?php e($record->near_airport) ?></td>
                        <td><?php e($record->near_city) ?></td>
                        <td><?php e($record->transport_opt) ?></td>
                        <td><?php e($record->courier_comp) ?></td>
                    </tr>
                <?php endforeach; 
            }
        ?>
    </table>
    <table class="table table-bordered table-condensed">
        <caption><h4>Bank Details</h4></caption>
        <tr>
            <th>Bank Name</th>
            <th>Address</th>
            <th>Account Type</th>
            <th>Operating Currency</th>
            <th>Accepted Currency</th>
            <th>Swift Code</th>
            <th>MICR</th>
            <th>IFSC</th>
        </tr>
        <?php 
            $vendor_bank = $records['vendor_bank'];
            if ($vendor_bank != NULL){
                foreach ($vendor_bank as $record) : ?>
                    <tr>
                        <td><?php e($record->bank_name . ', ' . $record->branch) ?></td>
                        <td><?php e($record->address) ?></td>
                        <td><?php e($record->account_type) ?></td>
                        <td><?php e($record->oper_curr) ?></td>
                        <td><?php e($record->accept_curr) ?></td>
                        <td><?php e($record->swift_code) ?></td>
                        <td><?php e($record->ifsc) ?></td>
                        <td><?php e($record->micr) ?></td>
                    </tr>
                <?php endforeach; 
            }
        ?>
    </table>
    <table class="table table-bordered table-condensed">
        <caption><h4>Products &amp; Documentation</h4></caption>
        <tr>
            <th colspan="7">Products</th>
        </tr>
        <?php 
            $vendor_product_docs = $records['vendor_product_docs'];
            $docs = $records['docs'];

            if ($vendor_product_docs != NULL){
                    $prod_id = -1;
                    foreach($vendor_product_docs as $record) :
                        if($prod_id != $record->product_id) :
                            if ($prod_id != -1){ echo "</tr>"; }
                            $prod_id = $record->product_id;
                            echo "<tr><td>" . $record->product_name . ' - ' . $record->product_desc . "</td>";
                        endif;
                        
                        $attachment = NULL;

                        if(isset($docs)){
                            foreach($docs as $doc){
                                if($doc->document_id == $record->document_id && $doc->product_id == $record->product_id){
                                    $attachment = unserialize($doc->attachment);
                                }
                            }
                        }

                        if(isset($attachment)) :
                            echo "<td><a href=" . base_url() . 'uploads/' . $attachment['file_name'] . " target='_blank' >" . $record->document_name . "</td>";
                        else:
                            echo "<td>" . $record->document_name . " <small>(pending)</small></td>";
                        endif;

                    endforeach;
                }
            ?>
    </table>
<?php endif; ?> 
