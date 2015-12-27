<?php

$num_columns    = 1;
$has_records    = isset($records) && is_array($records) && count($records);
$num_rows = count($records);
?>
<div class='content'>
    <?php echo form_open($this->uri->uri_string()); ?>
        <table class='table table-bordered table-condensed'>
            <caption><h5><div class="alert alert-info">Active Primary Ingredients</div></h5></caption>
            <thead>
                <tr>
                    <th><?php echo lang('ingredients_field_name'); ?></th>
                </tr>
            </thead>
            <tbody>
                <?php
                if ($has_records) :
                    foreach ($records as $record) :
                        if ($record->doc_name == 'Scope Certificate' || is_null($record->doc_name)):
                ?>
                <tr>
                    <td><?php echo anchor(SITE_AREA . '/content/party_documents/ingre_listing/' . $record->id, $record->name); ?></td>
                    <td>
                        <?php if(isset($record) && isset($record->doc_file) && !empty($record->doc_file)) :
                            $attachment = unserialize($record->doc_file);
                        ?> 
                            <a href="<?php echo base_url() . 'uploads/' . $attachment['file_name'] ?>" target="_blank" >
                                <?php echo $record->doc_name; ?>
                            </a>
                        <?php endif; ?> 
                    </td>
                </tr>
                <?php            
                        endif;
                    endforeach;
                else:
                ?>
                <tr>
                    <td colspan='<?php echo $num_columns; ?>'><?php echo lang('ingredients_records_empty'); ?></td>
                </tr>
                <?php endif; ?>
            </tbody>
        </table>
    <?php
    echo form_close();
    ?>
</div>