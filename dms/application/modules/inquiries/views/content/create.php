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

if (isset($inquiries))
{
	$inquiries = (array) $inquiries;
}
$id = isset($inquiries['id']) ? $inquiries['id'] : '';

?>
<div class="admin-box">
	<h3>Inquiries</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>

			<div class="control-group <?php echo form_error('product') ? 'error' : ''; ?>">
				<?php echo form_label('Product'. lang('bf_form_label_required'), 'inquiries_product', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='inquiries_product' type='text' name='inquiries_product' maxlength="255" value="<?php echo set_value('inquiries_product', isset($inquiries['product']) ? $inquiries['product'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('product'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('quantity') ? 'error' : ''; ?>">
				<?php echo form_label('Quantity'. lang('bf_form_label_required'), 'inquiries_quantity', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='inquiries_quantity' type='text' name='inquiries_quantity' maxlength="19" value="<?php echo set_value('inquiries_quantity', isset($inquiries['quantity']) ? $inquiries['quantity'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('quantity'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($uoms_select) && count($uoms_select)) :
				    echo form_dropdown('inquiries_uom_id', $uoms_select, set_value('inquiries_uom_id', isset($inquiries['uom_id']) ? $inquiries['uom_id'] : ''), 'UOM'. lang('bf_form_label_required'));
                endif;
			?>

			<div class="control-group <?php echo form_error('required_by') ? 'error' : ''; ?>">
				<?php echo form_label('Required By', 'inquiries_required_by', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='inquiries_required_by' type='text' name='inquiries_required_by'  value="<?php echo set_value('inquiries_required_by', isset($inquiries['required_by']) ? $inquiries['required_by'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('required_by'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('prod_spec') ? 'error' : ''; ?>">
				<?php echo form_label('Product Specifications', 'inquiries_prod_spec', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<?php echo form_textarea( array( 'name' => 'inquiries_prod_spec', 'id' => 'inquiries_prod_spec', 'rows' => '5', 'cols' => '80', 'value' => set_value('inquiries_prod_spec', isset($inquiries['prod_spec']) ? $inquiries['prod_spec'] : '') ) ); ?>
					<span class='help-inline'><?php echo form_error('prod_spec'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('quality_spec') ? 'error' : ''; ?>">
				<?php echo form_label('Quality Specifications', 'inquiries_quality_spec', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<?php echo form_textarea( array( 'name' => 'inquiries_quality_spec', 'id' => 'inquiries_quality_spec', 'rows' => '5', 'cols' => '80', 'value' => set_value('inquiries_quality_spec', isset($inquiries['quality_spec']) ? $inquiries['quality_spec'] : '') ) ); ?>
					<span class='help-inline'><?php echo form_error('quality_spec'); ?></span>
				</div>
			</div>

			<div class="control-group <?php echo form_error('packaging_spec') ? 'error' : ''; ?>">
				<?php echo form_label('Packaging Specifications', 'inquiries_packaging_spec', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<?php echo form_textarea( array( 'name' => 'inquiries_packaging_spec', 'id' => 'inquiries_packaging_spec', 'rows' => '5', 'cols' => '80', 'value' => set_value('inquiries_packaging_spec', isset($inquiries['packaging_spec']) ? $inquiries['packaging_spec'] : '') ) ); ?>
					<span class='help-inline'><?php echo form_error('packaging_spec'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
                    '-1' => 'Select one',
					'1 - High' => '1 - High',
                    '2 - Medium' => '2 - Medium',
                    '3 - Low' => '3 - Low'
				);

				echo form_dropdown('inquiries_priority', $options, set_value('inquiries_priority', isset($inquiries['priority']) ? $inquiries['priority'] : ''), 'Priority'. lang('bf_form_label_required'));
			?>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'Active' => 'Active',
                    'In Progress' => 'In Progress',
                    'Closed' => 'Closed',
				);

				echo form_dropdown('inquiries_status', $options, set_value('inquiries_status', isset($inquiries['status']) ? $inquiries['status'] : ''), 'Status');
			?>

			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('inquiries_action_create'); ?>"  />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/inquiries', lang('inquiries_cancel'), 'class="btn btn-warning"'); ?>
				
			</div>
            
            <?php
            if (isset($comment_form) && !empty($comment_form)) : ?>
                    <!-- COMMENTS -->
                <h3><?php echo lang('nw_article_comments'); ?></h3>
                <?php 
                echo ($comment_form);
            elseif (isset($comment_count) && !empty($comment_count)) :
                echo ('<h4><span class="label">'.$comment_count.'</span> Comments</h4>');
            endif;
            ?>
            
		</fieldset>
    <?php echo form_close(); ?>
</div>