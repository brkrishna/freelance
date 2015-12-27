<?php

$validation_errors = validation_errors();

if ($validation_errors) :
?>
<div class="alert alert-block alert-error fade in">
	<a class="close" data-dismiss="alert">&times;</a>
	<h4 class="alert-heading">Please fix the following errors:</h4>
	<?php echo $validation_errors; ?>
</div>
<?php
endif;

if (isset($po_documents))
{
	$po_documents = (array) $po_documents;
}
$id = isset($po_documents['id']) ? $po_documents['id'] : '';

?>
<div class="admin-box">
	<h3>PO Documents</h3>
	<?php echo form_open_multipart($this->uri->uri_string(), 'class="form-inline"'); ?>
		<fieldset>
            <div class="row">
                <div class="span4">
                    <?php
                        if(isset($po_data)):
                            $i_po_no = $po_data->id;
                            $i_po_product = $po_data->product_id;
                        else:
                            $i_po_no = isset($po_documents['po_no']) ? $po_documents['po_no'] : '';
                            $i_po_product = isset($po_documents['product_id']) ? $po_documents['product_id'] : '';
                        endif;
                    ?>
                    <?php // Change the values in this array to populate your dropdown as required
                        if (is_array($pos_select) && count($pos_select)) :    
                            echo form_dropdown('po_documents_po_no', $pos_select, set_value('po_documents_po_no', $i_po_no), 'PO No'. lang('bf_form_label_required'), 'tabindex="1"');
                        endif;
                    ?>
                    
                    <?php // Change the values in this array to populate your dropdown as required
                        if (is_array($doc_types_select) && count($doc_types_select)) :
                            echo form_dropdown('po_documents_document_id', $doc_types_select, set_value('po_documents_document_id', isset($po_documents['document_id']) ? $po_documents['document_id'] : ''), 'Document', 'tabindex="4"');
                        endif;
                    ?>
                    
                    
                    <div class="control-group <?php echo form_error('issue_auth') ? 'error' : ''; ?>">
                        <?php echo form_label('Issuing Authority', 'po_documents_issue_auth', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <input tabindex="6" id='po_documents_issue_auth' type='text' name='po_documents_issue_auth' maxlength="255" value="<?php echo set_value('po_documents_issue_auth', isset($po_documents['issue_auth']) ? $po_documents['issue_auth'] : ''); ?>" />
                            <span class='help-inline'><?php echo form_error('issue_auth'); ?></span>
                        </div>
                    </div>
                    
                    <div class="control-group <?php echo form_error('origin_place') ? 'error' : ''; ?>">
                        <?php echo form_label('Place of origin', 'po_documents_origin_place', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <input tabindex="9" id='po_documents_origin_place' type='text' name='po_documents_origin_place' maxlength="255" value="<?php echo set_value('po_documents_origin_place', isset($po_documents['origin_place']) ? $po_documents['origin_place'] : ''); ?>" />
                            <span class='help-inline'><?php echo form_error('origin_place'); ?></span>
                        </div>
                    </div>
                    

                </div>       
                
                
                
                <div class="span4">
                    <?php // Change the values in this array to populate your dropdown as required
                        if (is_array($vendors_select) && count($vendors_select)) :    
                            echo form_dropdown('po_documents_vendor_id', $vendors_select, set_value('po_documents_vendor_id', isset($po_documents['vendor_id']) ? $po_documents['vendor_id'] : ''), 'Vendor'. lang('bf_form_label_required'), 'tabindex="2"');
                        endif;
                    ?>
                    
                    
                    <?php // Change the values in this array to populate your dropdown as required
                        $options = array(
                            'Yes' => 'Yes',
                            'No' => 'No'
                        );

                        echo form_dropdown('po_documents_applicable', $options, set_value('po_documents_applicable', isset($po_documents['applicable']) ? $po_documents['applicable'] : ''), 'Applicable'. lang('bf_form_label_required'), 'tabindex="5"');
                    ?>

                    <div class="control-group <?php echo form_error('issued_on') ? 'error' : ''; ?>">
                        <?php echo form_label('Issued on', 'po_documents_issued_on', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <input tabindex="7" id='po_documents_issued_on' type='text' name='po_documents_issued_on'  value="<?php echo set_value('po_documents_issued_on', isset($po_documents['issued_on']) ? $po_documents['issued_on'] : ''); ?>" />
                            <span class='help-inline'><?php echo form_error('issued_on'); ?></span>
                        </div>
                    </div>
                    
                    <!-- Current Document -->
                    <?php if(isset($po_documents) && isset($po_documents['attachment']) && !empty($po_documents['attachment'])) : $attachment = unserialize($po_documents['attachment']);
                    ?>

                    <?php if (isset($attachment)) : ?>
                        <!-- Current Document Display -->
                        <div class="control-group">
                            <label class="control-label">Attachment</label>
                            <div class="controls">
                                <ul class="thumbnails">
                                    <li class="span6">
                                        <a class="lightbox" href="<?php echo base_url() . '/uploads/' . $attachment['file_name'] ?>" target="_blank" >
                                            <?php echo $attachment['file_name']; ?>
                                        </a>
                                        <p><?php echo anchor(SITE_AREA.'/content/po_documents/remove_attachment/'.$po_documents['id'],'Remove', 'class="btn btn-small btn-danger"'); ?></p>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <?php endif; ?>
                    <?php else: ?>
                        <div class="control-group <?php echo form_error('attachment') ? 'error' : ''; ?>">
                            <?php echo form_label('Attachment', 'attachment', array('class' => 'control-label') ); ?>
                            <div class='controls'>
                                <input id='attachment' type='file' name='attachment'/>
                                <span class='help-inline'><?php echo form_error('attachment'); ?></span>
                            </div>
                        </div>
                    <?php endif; ?>                
                </div>
                
                <div class="span4">
                    <?php // Change the values in this array to populate your dropdown as required
                        if (is_array($products_select) && count($products_select)) :    
                            echo form_dropdown('po_documents_product_id', $products_select, set_value('po_documents_product_id', $i_po_product), 'Product', 'tabindex="3"');
                        endif;
                    ?>
                    
                    <div class="control-group">
                        <div class="controls">
                            <input type="hidden"/> 
                            <span class='help-inline'><?php echo form_error('valid_till'); ?></span>
                            <br/><br/><br/>
                        </div>
                        
                    </div>
                    
                    <div class="control-group <?php echo form_error('valid_till') ? 'error' : ''; ?>">
                        <?php echo form_label('Valid Till', 'po_documents_valid_till', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <input tabindex="8" id='po_documents_valid_till' type='text' name='po_documents_valid_till'  value="<?php echo set_value('po_documents_valid_till', isset($po_documents['valid_till']) ? $po_documents['valid_till'] : ''); ?>" />
                            <span class='help-inline'><?php echo form_error('valid_till'); ?></span>
                        </div>
                    </div>
                    
                    <div class="control-group <?php echo form_error('comments') ? 'error' : ''; ?>">
                        <?php echo form_label('Comments', 'po_documents_comments', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <?php echo form_textarea( array( 'name' => 'po_documents_comments', 'id' => 'po_documents_comments', 'rows' => '5', 'tabindex'=>'11', 'cols' => '80', 'value' => set_value('po_documents_comments', isset($po_documents['comments']) ? $po_documents['comments'] : '') ) ); ?>
                            <span class='help-inline'><?php echo form_error('comments'); ?></span>
                        </div>
                    </div>
                    
                </div>
            </div>
                <div class="row">
                    <div class="form-actions">
                        <input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('po_documents_action_create'); ?>"  />
                        <?php echo lang('bf_or'); ?>
                        <?php echo anchor(SITE_AREA .'/content/po_documents', lang('po_documents_cancel'), 'class="btn btn-warning"'); ?>

                    </div>
                </div>
		</fieldset>
    <?php echo form_close(); ?>
</div>