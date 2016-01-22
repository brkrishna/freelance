<?php

$can_delete	= $this->auth->has_permission('Product_Documents.Content.Delete');
$can_edit		= $this->auth->has_permission('Product_Documents.Content.Edit');
$can_view		= $this->auth->has_permission('Product_Documents.Content.View');
$has_records	= isset($records) && is_array($records) && count($records);

?>
    <?php if ($has_records) : ?>
        <table class="table table-condensed">
            <tr class="info">
                <td colspan="5"><strong>Products Documents</strong></td><td><a class="alert-link" href="content/product_documents/create"><strong>Upload</strong></a></td>
            </tr>
            <tr>
                <td colspan="7">Lists the status of necessary documentation required against each product. Green indicates that you have uploaded the necessary document</td>
            </tr>
                <?php
                    $prod_id = -1;
                    foreach($records as $record) :
                        if($prod_id != $record->product_id) :
                            if ($prod_id != -1){ echo "</tr>"; }
                            $prod_id = $record->product_id;
                            echo "<tr><td><span style='width:250px;' class='label label-default'><h5>" . $record->product_name . ' - ' . $record->product_desc . "</h5></td>";
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
                                echo "<td><a href=" . base_url() . 'uploads/' . $attachment['file_name'] . " target='_blank' ><span class='label label-success'><h5>" . $record->document_name . "</h5></span></td>";
                            else:
                                echo "<td><span class='label label-warning'><h5>" . $record->document_name . "</h5></span></td>";
                            endif;

                    endforeach;
                ?>
        </table>
    <?php
        else:
    ?>
        <div class="panel panel-primary">
            <div class="panel-heading">
                Product Documents
            </div>
            <div class="panel-body">
                <p>No records found that match your selection. <a href="content/vendor_products/create" class="btn btn-primary" name="Create" id="Create">Create</a> </p>
            </div>
        </div>
    <?php
        endif;
    ?>
