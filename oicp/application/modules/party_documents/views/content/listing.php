<?php

$num_columns	= 3;
$has_records	= isset($records) && is_array($records) && count($records);

$org_name = '';
$address = '';

if ($has_records):
    foreach($records as $r):
            $org_name = $r->org_name;
            $address = $r->address . ', ' . $r->city;
    endforeach;
endif;
?>
<div class='content'>
	<?php echo form_open($this->uri->uri_string()); ?>
		<table class='table table-bordered table-condensed' style="width:50%;">
            <caption><h4><?php e($org_name . ', Address: ' . $address); ?></h4></caption>
			<thead>
				<tr>
					<th><?php echo lang('party_documents_field_doc_name'); ?></th>
					<th><?php echo lang('party_documents_field_comments'); ?></th>
				</tr>
			</thead>
			<tbody>
				<?php
				if ($has_records) :
					foreach ($records as $record) :
                        if ($record->prod_name == 'NA') :
				?>
				<tr>
					<td>
        				<?php if(isset($record) && isset($record->doc_file) && !empty($record->doc_file)) :
        					$attachment = unserialize($record->doc_file);
        				?> 
        					<a href="<?php echo base_url() . 'uploads/' . $attachment['file_name'] ?>" target="_blank" >
        						<?php echo $record->doc_name; ?>
        					</a>
        				<?php endif; ?>	
					</td>
					<td><?php e($record->comments); ?></td>
				</tr>
				<?php
                        endif;
					endforeach;
				else:
				?>
				<tr>
					<td colspan='<?php echo $num_columns; ?>'><?php echo lang('party_documents_records_empty'); ?></td>
				</tr>
				<?php endif; ?>
			</tbody>
		</table>
        <br/>
        <table class='table table-bordered table-condensed'>
            <thead>
                <tr>
                    <th><?php echo lang('party_documents_field_product_id'); ?></th>
                    <th><?php echo lang('party_documents_field_ingredient_id'); ?></th>
                    <th><?php echo lang('party_documents_field_doc_name'); ?></th>
                    <!--<th><?php echo lang('party_documents_field_rcvd_on'); ?></th>-->
                    <th><?php echo lang('party_documents_field_comments'); ?></th>
                </tr>
            </thead>
            <tbody>
                <?php
                if ($has_records) :
                    foreach ($records as $record) :
                        if ($record->prod_name <> 'NA'):
                ?>
                <tr>
                    <td><?php e($record->prod_name); ?></td>
                    <td><?php e($record->ing_name); ?></td>
                    <td>
                        <?php if(isset($record) && isset($record->doc_file) && !empty($record->doc_file)) :
                            $attachment = unserialize($record->doc_file);
                        ?> 
                            <a href="<?php echo base_url() . 'uploads/' . $attachment['file_name'] ?>" target="_blank" >
                                <?php echo $record->doc_name; ?>
                            </a>
                        <?php endif; ?> 
                    </td>
                    <!--<td><?php e($record->rcvd_on); ?></td>-->
                    <td><?php e($record->comments); ?></td>
                </tr>
                <?php
                        endif;
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
    
    ?>
</div>