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

if (isset($po_fulfillment))
{
	$po_fulfillment = (array) $po_fulfillment;
}
$id = isset($po_fulfillment['id']) ? $po_fulfillment['id'] : '';

?>
<div class="admin-box">
	<h3>PO Fulfillment</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-inline"'); ?>
		<fieldset>
            <div class="row">
                <div class="span4">
                    <?php // Change the values in this array to populate your dropdown as required
                        if (is_array($pos_select) && count($pos_select)) :    
                            echo form_dropdown('po_fulfillment_po_no', $pos_select, set_value('po_fulfillment_po_no', isset($po_fulfillment['po_no']) ? $po_fulfillment['po_no'] : ''), 'PO No'. lang('bf_form_label_required'), 'tabindex="1"');
                        endif;
                    ?>

                    <div class="control-group <?php echo form_error('qty') ? 'error' : ''; ?>">
                        <?php echo form_label('Quantity'. lang('bf_form_label_required'), 'po_fulfillment_qty', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <input tabindex="4" id='po_fulfillment_qty' type='text' name='po_fulfillment_qty' maxlength="19" value="<?php echo set_value('po_fulfillment_qty', isset($po_fulfillment['qty']) ? $po_fulfillment['qty'] : ''); ?>" />
                            <span class='help-inline'><?php echo form_error('qty'); ?></span>
                        </div>
                    </div>
                    
                    <?php // Change the values in this array to populate your dropdown as required
                        $options = array(
                            'Drums' => 'Drums',
                            'Totes' => 'Totes'
                        );

                        echo form_dropdown('po_fulfillment_packing_mode', $options, set_value('po_fulfillment_packing_mode', isset($po_fulfillment['packing_mode']) ? $po_fulfillment['packing_mode'] : ''), 'Mode of Packing'. lang('bf_form_label_required'), 'tabindex="7"');
                    ?>
                    
                    <div class="control-group <?php echo form_error('supply_from') ? 'error' : ''; ?>">
                        <?php echo form_label('Supply from'. lang('bf_form_label_required'), 'po_fulfillment_supply_from', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <input tabindex="9" id='po_fulfillment_supply_from' type='text' name='po_fulfillment_supply_from' maxlength="255" value="<?php echo set_value('po_fulfillment_supply_from', isset($po_fulfillment['supply_from']) ? $po_fulfillment['supply_from'] : ''); ?>" />
                            <span class='help-inline'><?php echo form_error('supply_from'); ?></span>
                        </div>
                    </div>

                </div>
                
                <div class="span4">
                        <?php // Change the values in this array to populate your dropdown as required
                            if (is_array($vendors_select) && count($vendors_select)) :    
                                echo form_dropdown('po_fulfillment_vendor_id', $vendors_select, set_value('po_fulfillment_vendor_id', isset($po_fulfillment['vendor_id']) ? $po_fulfillment['vendor_id'] : ''), 'Vendor'. lang('bf_form_label_required'), 'tabindex="2"');
                            endif;
                        ?>
                        <?php // Change the values in this array to populate your dropdown as required
                            if (is_array($uoms_select) && count($uoms_select)) :    
                                echo form_dropdown('po_fulfillment_uom_id', $uoms_select, set_value('po_fulfillment_uom_id', isset($po_fulfillment['uom_id']) ? $po_fulfillment['uom_id'] : ''), 'UOM'. lang('bf_form_label_required'), 'tabindex="5"');
                            endif;
                        ?>
                    
                        <div class="control-group <?php echo form_error('no_of_units') ? 'error' : ''; ?>">
                            <?php echo form_label('No of Units'. lang('bf_form_label_required'), 'po_fulfillment_no_of_units', array('class' => 'control-label') ); ?>
                            <div class='controls'>
                                <input tabindex="8" id='po_fulfillment_no_of_units' type='text' name='po_fulfillment_no_of_units' maxlength="19" value="<?php echo set_value('po_fulfillment_no_of_units', isset($po_fulfillment['no_of_units']) ? $po_fulfillment['no_of_units'] : ''); ?>" />
                                <span class='help-inline'><?php echo form_error('no_of_units'); ?></span>
                            </div>
                        </div>
                    
                        <div class="control-group <?php echo form_error('dest_port') ? 'error' : ''; ?>">
                            <?php echo form_label('Destination Port'. lang('bf_form_label_required'), 'po_fulfillment_dest_port', array('class' => 'control-label') ); ?>
                            <div class='controls'>
                                <input tabindex="10" id='po_fulfillment_dest_port' type='text' name='po_fulfillment_dest_port' maxlength="255" value="<?php echo set_value('po_fulfillment_dest_port', isset($po_fulfillment['dest_port']) ? $po_fulfillment['dest_port'] : ''); ?>" />
                                <span class='help-inline'><?php echo form_error('dest_port'); ?></span>
                            </div>
                        </div>

                </div>
                
                <div class="span4">
                    
                    <?php // Change the values in this array to populate your dropdown as required
                        if (is_array($products_select) && count($products_select)) :    
                            echo form_dropdown('po_fulfillment_product_id', $products_select, set_value('po_fulfillment_product_id', isset($po_fulfillment['product_id']) ? $po_fulfillment['product_id'] : ''), 'Product'. lang('bf_form_label_required'), 'tabindex="3"');
                        endif;
                    ?>
                    
                    <div class="control-group <?php echo form_error('rate') ? 'error' : ''; ?>">
                        <?php echo form_label('Rate'. lang('bf_form_label_required'), 'po_fulfillment_rate', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <input tabindex="6" id='po_fulfillment_rate' type='text' name='po_fulfillment_rate' maxlength="19" value="<?php echo set_value('po_fulfillment_rate', isset($po_fulfillment['rate']) ? $po_fulfillment['rate'] : ''); ?>" />
                            <span class='help-inline'><?php echo form_error('rate'); ?></span>
                        </div>
                    </div>
                    
                </div>
                

            </div>

            <div class="row">
                <div class="form-actions">
                    <input tabindex="11" type="submit" name="save" class="btn btn-primary" value="<?php echo lang('po_fulfillment_action_create'); ?>"  />
                    <?php echo lang('bf_or'); ?>
                    <?php echo anchor(SITE_AREA .'/content/po_fulfillment', lang('po_fulfillment_cancel'), 'class="btn btn-warning"'); ?>
                    <?php echo lang('bf_or'); ?>
                    <?php echo anchor(SITE_AREA .'/content/purchase_orders/po_details/' .  $po_fulfillment['po_no'], 'PO Details', 'class="btn btn-info"'); ?>

                </div>
                
            </div>
		</fieldset>
    <?php echo form_close(); ?>
</div>