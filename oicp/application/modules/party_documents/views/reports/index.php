<?php

$has_records    = isset($records) && is_array($records) && count($records);
$num_rows = count($records);
?>
<div class='admin-box'>
    <h3>
        Product - Ingredients - Scope certificate mapping
    </h3>
    <?php echo form_open($this->uri->uri_string()); ?>
        <table class='table table-bordered table-condensed'>
            <thead>
                <tr>
                    <th>&nbsp;</th>
                    <th><?php echo lang('party_documents_field_ingredient_id'); ?></th>
                    <th><?php echo lang('party_documents_field_party_id'); ?></th>
                    <th><?php echo lang('party_documents_field_catg'); ?></th>
                    <th><?php echo lang('party_documents_field_cert_type'); ?></th>
                    <th><?php echo lang('party_documents_field_doc_name'); ?></th>
                </tr>
            </thead>
            <tbody>
                <?php
                $prev_prod = '';
                if ($has_records) :
                    foreach ($records as $record) :
                        if($prev_prod != $record->prod_name):
                            $prev_prod = $record->prod_name;
                            ?>
                                <tr class="info"><td colspan="6"><strong><?php e($record->prod_name); ?></strong></td></tr>
                        <?php endif; ?>        
                <tr>    
                    <td><?php e($record->classification); ?></td>
                    <td><?php e($record->ing_name); ?></td>
                    <td><?php e($record->org_name); ?></td>
                    <td><?php e($record->catg); ?></td>
                    <td><?php e($record->cert_type); ?></td>
                    <td>
                        <?php if(isset($record) && isset($record->doc_file) && !empty($record->doc_file)) :
                            $attachment = unserialize($record->doc_file);
                        ?> 
                            <a href="<?php echo base_url() . 'uploads/' . $attachment['file_name'] ?>" target="_blank" >
                                <?php e($record->doc_name);   ?>
                            </a>
                        <?php endif; ?> 
                    </td>
                </tr>
                <?php
                    endforeach;
                else:
                ?>
                <tr>
                    <td colspan='<?php echo $num_columns; ?>'><?php echo lang('party_documents_records_empty'); ?></td>
                </tr>
                <?php endif; ?>
            </tbody>
        </table>
    <?php
    echo form_close();
    //echo $this->pagination->create_links();
    ?>
</div>