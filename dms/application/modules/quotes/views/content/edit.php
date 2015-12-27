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

if (isset($quotes))
{
	$quotes = (array) $quotes;
}
$id = isset($quotes['id']) ? $quotes['id'] : '';

?>
<div class="admin-box">
	<h3>Quotes</h3>
	<?php echo form_open_multipart($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<div class="control-group <?php echo form_error('ref_no') ? 'error' : ''; ?>">
				<?php echo form_label('Reference No'. lang('bf_form_label_required'), 'quotes_ref_no', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='quotes_ref_no' type='text' name='quotes_ref_no' maxlength="255" value="<?php echo set_value('quotes_ref_no', isset($quotes['ref_no']) ? $quotes['ref_no'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('ref_no'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('quote_dt') ? 'error' : ''; ?>">
				<?php echo form_label('Date Received'. lang('bf_form_label_required'), 'quotes_quote_dt', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='quotes_quote_dt' type='text' name='quotes_quote_dt'  value="<?php echo set_value('quotes_quote_dt', isset($quotes['quote_dt']) ? $quotes['quote_dt'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('quote_dt'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($vendors_select) && count($vendors_select)) :
				    echo form_dropdown('quotes_vendor_id', $vendors_select, set_value('quotes_vendor_id', isset($quotes['vendor_id']) ? $quotes['vendor_id'] : ''), 'Vendor'. lang('bf_form_label_required')); 
                endif;
			?>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($products_select) && count($products_select)) :
				    echo form_dropdown('quotes_product_id', $products_select, set_value('quotes_product_id', isset($quotes['product_id']) ? $quotes['product_id'] : ''), 'Product'. lang('bf_form_label_required'));
                endif;
			?>

			<div class="control-group <?php echo form_error('price') ? 'error' : ''; ?>">
				<?php echo form_label('Price'. lang('bf_form_label_required'), 'quotes_price', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='quotes_price' type='text' name='quotes_price' maxlength="19" value="<?php echo set_value('quotes_price', isset($quotes['price']) ? $quotes['price'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('price'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('tat') ? 'error' : ''; ?>">
				<?php echo form_label('Turn Around Time (days)'. lang('bf_form_label_required'), 'quotes_tat', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='quotes_tat' type='text' name='quotes_tat'  value="<?php echo set_value('quotes_tat', isset($quotes['tat']) ? $quotes['tat'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('tat'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('quantity') ? 'error' : ''; ?>">
				<?php echo form_label('Quantity'. lang('bf_form_label_required'), 'quotes_quantity', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='quotes_quantity' type='text' name='quotes_quantity' maxlength="19" value="<?php echo set_value('quotes_quantity', isset($quotes['quantity']) ? $quotes['quantity'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('quantity'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($uoms_select) && count($uoms_select)) :
                    echo form_dropdown('quotes_uom_id', $uoms_select, set_value('quotes_uom_id', isset($quotes['uom_id']) ? $quotes['uom_id'] : ''), 'UOM'. lang('bf_form_label_required'));
                endif;
			?>

			<!-- Current Document -->
		<!--	<?php if(isset($quotes) && isset($quotes['attachment']) && !empty($quotes['attachment'])) :
				$attachment = unserialize($quotes['attachment']);
			?>-->

			<!-- Current Document Display -->
		<!--	<div class="control-group">
				<label class="control-label">Attachment</label>
				<div class="controls">
					<ul class="thumbnails">
						<li class="span6">
							<a class="lightbox" href="<?php echo base_url() . 'uploads/' . $attachment['file_name'] ?>" target="_blank" >
								<?php echo $attachment['file_name']; ?>
							</a>
							<p><?php echo anchor(SITE_AREA.'/content/quotes/remove_attachment/'.$quotes['id'],'Remove', 'class="btn btn-small btn-danger"'); ?></p>
							</div>
						</li>
					</ul>
				</div>
			</div>
            <?php else: ?>
                <div class="control-group <?php echo form_error('attachment') ? 'error' : ''; ?>">
                    <?php echo form_label('Attachment', 'attachment', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input id='attachment' name='attachment' type='file' />
                        <span class='help-inline'><?php echo form_error('attachment'); ?></span>
                    </div>
                </div>
			<?php endif; ?>-->

			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('quotes_action_edit'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/quotes', lang('quotes_cancel'), 'class="btn btn-warning"'); ?>
				
			<?php if ($this->auth->has_permission('Quotes.Content.Delete')) : ?>
				or
				<button type="submit" name="delete" class="btn btn-danger" id="delete-me" onclick="return confirm('<?php e(js_escape(lang('quotes_delete_confirm'))); ?>'); ">
					<span class="icon-trash icon-white"></span>&nbsp;<?php echo lang('quotes_delete_record'); ?>
				</button>
			<?php endif; ?>
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>