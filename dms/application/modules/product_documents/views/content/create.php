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

if (isset($product_documents))
{
	$product_documents = (array) $product_documents;
}
$id = isset($product_documents['id']) ? $product_documents['id'] : '';

?>
<div class="admin-box">
	<h3>Product Documents</h3>
	<?php echo form_open_multipart($this->uri->uri_string(), 'class="form-inline"'); ?>
		<fieldset>
            <div class="row">
                <div class="span4">
                    <?php // Change the values in this array to populate your dropdown as required
                        if (is_array($vendors_select) && count($vendors_select)) :
                            echo form_dropdown('product_documents_vendor_id', $vendors_select, set_value('product_documents_vendor_id', isset($product_documents['vendor_id']) ? $product_documents['vendor_id'] : ''), 'Vendor'. lang('bf_form_label_required'), 'tabindex="1"');
                        endif;
                    ?>

                    <div class="control-group <?php echo form_error('product_documents_issue_auth') ? 'error' : ''; ?>">
                        <?php echo form_label('Issuing Authority'. lang('bf_form_label_required'), 'product_documents_issue_auth', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <input tabindex="4" id='product_documents_issue_auth' type='text' name='product_documents_issue_auth' maxlength="255" value="<?php echo set_value('product_documents_issue_auth', isset($product_documents['issue_auth']) ? $product_documents['issue_auth'] : ''); ?>" />
                            <span class='help-inline'><?php echo form_error('product_documents_issue_auth'); ?></span>
                        </div>
                    </div>

                    <div class="control-group <?php echo form_error('product_documents_place_of_origin') ? 'error' : ''; ?>">
                        <?php echo form_label('Place of Origin'. lang('bf_form_label_required'), 'product_documents_place_of_origin', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <input tabindex="7" id='product_documents_place_of_origin' type='text' name='product_documents_place_of_origin' maxlength="255" value="<?php echo set_value('product_documents_place_of_origin', isset($product_documents['place_of_origin']) ? $product_documents['place_of_origin'] : ''); ?>" />
                            <span class='help-inline'><?php echo form_error('product_documents_place_of_origin'); ?></span>
                        </div>
                    </div>

                </div>

                <div class="span4">
                    <?php // Change the values in this array to populate your dropdown as required
                        if (is_array($products_select) && count($products_select)) :
                            echo form_dropdown('product_documents_product_id', $products_select, set_value('product_documents_product_id', isset($product_documents['product_id']) ? $product_documents['product_id'] : ''), 'Product'. lang('bf_form_label_required'), 'tabindex="2"');
                        endif;
                    ?>

                    <div class="control-group <?php echo form_error('product_documents_issued_on') ? 'error' : ''; ?>">
                        <?php echo form_label('Issued on'. lang('bf_form_label_required'), 'product_documents_issued_on', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <input tabindex="5" id='product_documents_issued_on' type='text' name='product_documents_issued_on'  value="<?php echo set_value('product_documents_issued_on', isset($product_documents['issued_on']) ? $product_documents['issued_on'] : ''); ?>" />
                            <span class='help-inline'><?php echo form_error('product_documents_issued_on'); ?></span>
                        </div>
                    </div>

                    <div class="control-group <?php echo form_error('comments') ? 'error' : ''; ?>">
                        <?php echo form_label('Comments', 'product_documents_comments', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <?php echo form_textarea( array( 'name' => 'product_documents_comments', 'id' => 'product_documents_comments', 'rows' => '5', 'cols' => '80', 'tabindex' => '8', 'value' => set_value('product_documents_comments', isset($product_documents['comments']) ? $product_documents['comments'] : '') ) ); ?>
                            <span class='help-inline'><?php echo form_error('comments'); ?></span>
                        </div>
                    </div>
                </div>

                <div class="span4">
                    <?php // Change the values in this array to populate your dropdown as required
                        if (is_array($doc_types_select) && count($doc_types_select)) :
                            echo form_dropdown('product_documents_document_id', $doc_types_select, set_value('product_documents_document_id', isset($product_documents['document_id']) ? $product_documents['document_id'] : ''), 'Document'. lang('bf_form_label_required'), 'tabindex="3"');
                        endif;    
                    ?>

                    <div class="control-group <?php echo form_error('product_documents_valid_till') ? 'error' : ''; ?>">
                        <?php echo form_label('Valid Till'. lang('bf_form_label_required'), 'product_documents_valid_till', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <input tabindex="6" id='product_documents_valid_till' type='text' name='product_documents_valid_till'  value="<?php echo set_value('product_documents_valid_till', isset($product_documents['valid_till']) ? $product_documents['valid_till'] : ''); ?>" />
                            <span class='help-inline'><?php echo form_error('product_documents_valid_till'); ?></span>
                        </div>
                    </div>

                    <div class="control-group <?php echo form_error('attachment') ? 'error' : ''; ?>">
                        <?php echo form_label('Attachment'. lang('bf_form_label_required'), 'attachment', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <input tabindex="9" id='attachment' type='file' name='attachment'/>
                            <span class='help-inline'><?php echo form_error('attachment'); ?></span>
                        </div>
                    </div>

                </div>                
            </div>
            <div class="row">
                <div class="form-actions">
                    <input tabindex="10" type="submit" name="save" class="btn btn-primary" value="<?php echo lang('product_documents_action_create'); ?>"  />
                    <?php echo lang('bf_or'); ?>
                    <?php echo anchor(SITE_AREA .'/content/product_documents', lang('product_documents_cancel'), 'class="btn btn-warning"'); ?>

                </div>

            </div>



		</fieldset>
    <?php echo form_close(); ?>
</div>