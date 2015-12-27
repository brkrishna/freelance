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

if (isset($purchase_orders))
{
	$purchase_orders = (array) $purchase_orders;
}
$id = isset($purchase_orders['id']) ? $purchase_orders['id'] : '';

?>
<div class="admin-box">
	<h3>Purchase Orders</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-inline"'); ?>
		<fieldset>
            <div class="row">
                <div class="span4">
                    <div class="control-group <?php echo form_error('po_no') ? 'error' : ''; ?>">
                        <?php echo form_label('PO No'. lang('bf_form_label_required'), 'purchase_orders_po_no', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <input tabindex="1" id='purchase_orders_po_no' type='text' name='purchase_orders_po_no' maxlength="255" value="<?php echo set_value('purchase_orders_po_no', isset($purchase_orders['po_no']) ? $purchase_orders['po_no'] : ''); ?>" />
                            <span class='help-inline'><?php echo form_error('po_no'); ?></span>
                        </div>
                    </div>

                    <?php // Change the values in this array to populate your dropdown as required
                        if (is_array($products_select) && count($products_select)) :    
                            echo form_dropdown('purchase_orders_product_id', $products_select, set_value('purchase_orders_product_id', isset($purchase_orders['product_id']) ? $purchase_orders['product_id'] : ''), 'Product'. lang('bf_form_label_required'), 'tabindex="4"');
                        endif;
                    ?>

                    <div class="control-group <?php echo form_error('qty') ? 'error' : ''; ?>">
                        <?php echo form_label('Quantity'. lang('bf_form_label_required'), 'purchase_orders_qty', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <input tabindex="7" id='purchase_orders_qty' type='text' name='purchase_orders_qty' maxlength="19" value="<?php echo set_value('purchase_orders_qty', isset($purchase_orders['qty']) ? $purchase_orders['qty'] : ''); ?>" />
                            <span class='help-inline'><?php echo form_error('qty'); ?></span>
                        </div>
                    </div>

                    <?php // Change the values in this array to populate your dropdown as required
                        $options = array(
                            'Active' => 'Active',
                            'Fulfilled' => 'Fulfilled',
                        );

                        echo form_dropdown('purchase_orders_status_id', $options, set_value('purchase_orders_status_id', isset($purchase_orders['status_id']) ? $purchase_orders['status_id'] : ''), 'Status'. lang('bf_form_label_required'), 'tabindex="10"');
                    ?>
                </div>

                <div class="span4">
                    <div class="control-group <?php echo form_error('po_dt') ? 'error' : ''; ?>">
                        <?php echo form_label('PO Date'. lang('bf_form_label_required'), 'purchase_orders_po_dt', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <input tabindex="2" id='purchase_orders_po_dt' type='text' name='purchase_orders_po_dt'  value="<?php echo set_value('purchase_orders_po_dt', isset($purchase_orders['po_dt']) ? $purchase_orders['po_dt'] : ''); ?>" />
                            <span class='help-inline'><?php echo form_error('po_dt'); ?></span>
                        </div>
                    </div>

                    <?php // Change the values in this array to populate your dropdown as required
                        $options = array(
                            'Drums' => 'Drums',
                            'Totes' => 'Totes'
                        );

                        echo form_dropdown('purchase_orders_packing_mode', $options, set_value('purchase_orders_packing_mode', isset($purchase_orders['purchase_orders_packing_mode']) ? $purchase_orders['purchase_orders_packing_mode'] : ''), 'Mode of Packing'. lang('bf_form_label_required'), 'tabindex="5"');
                    ?>

                    <?php // Change the values in this array to populate your dropdown as required
                        if (is_array($uoms_select) && count($uoms_select)) :
                            echo form_dropdown('purchase_orders_uom_id', $uoms_select, set_value('purchase_orders_uom_id', isset($purchase_orders['uom_id']) ? $purchase_orders['uom_id'] : ''), 'UOM'. lang('bf_form_label_required'), 'tabindex="8"');
                        endif;    
                    ?>

                    <div class="control-group <?php echo form_error('comments') ? 'error' : ''; ?>">
                        <?php echo form_label('Comments', 'purchase_orders_comments', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <?php echo form_textarea( array( 'name' => 'purchase_orders_comments', 'id' => 'purchase_orders_comments', 'rows' => '5', 'cols' => '80', 'tabindex' => '11', 'value' => set_value('purchase_orders_comments', isset($purchase_orders['comments']) ? $purchase_orders['comments'] : '') ) ); ?>
                            <span class='help-inline'><?php echo form_error('comments'); ?></span>
                        </div>
                    </div>



                </div>

                <div class="span4">
                    <?php // Change the values in this array to populate your dropdown as required
                        if (is_array($customers_select) && count($customers_select)) :    
                            echo form_dropdown('purchase_orders_customer_id', $customers_select, set_value('purchase_orders_customer_id', isset($purchase_orders['customer_id']) ? $purchase_orders['customer_id'] : ''), 'Customer'. lang('bf_form_label_required'), 'tabindex="3"');
                        endif;
                    ?>

                    <div class="control-group <?php echo form_error('no_of_units') ? 'error' : ''; ?>">
                        <?php echo form_label('No of Units'. lang('bf_form_label_required'), 'purchase_orders_no_of_units', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <input tabindex="6" id='purchase_orders_no_of_units' type='text' name='purchase_orders_no_of_units' maxlength="19" value="<?php echo set_value('purchase_orders_no_of_units', isset($purchase_orders['no_of_units']) ? $purchase_orders['no_of_units'] : ''); ?>" />
                            <span class='help-inline'><?php echo form_error('no_of_units'); ?></span>
                        </div>
                    </div>

                    <div class="control-group <?php echo form_error('rate') ? 'error' : ''; ?>">
                        <?php echo form_label('Rate'. lang('bf_form_label_required'), 'purchase_orders_rate', array('class' => 'control-label') ); ?>
                        <div class='controls'>
                            <input tabindex="9" id='purchase_orders_rate' type='text' name='purchase_orders_rate' maxlength="19" value="<?php echo set_value('purchase_orders_rate', isset($purchase_orders['rate']) ? $purchase_orders['rate'] : ''); ?>" />
                            <span class='help-inline'><?php echo form_error('rate'); ?></span>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="row">
                <div class="span12">
                    <div class="form-actions">
                        <input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('purchase_orders_action_create'); ?>"  />
                        <?php echo lang('bf_or'); ?>
                        <?php echo anchor(SITE_AREA .'/content/purchase_orders', lang('purchase_orders_cancel'), 'class="btn btn-warning"'); ?>

                    </div>
                </div>
            </div>
            

		</fieldset>
    <?php echo form_close(); ?>
</div>