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

if (isset($factory))
{
	$factory = (array) $factory;
}
$id = isset($factory['id']) ? $factory['id'] : '';

?>
<div class="admin-box">
	<h3>Factory</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-inline"'); ?>
		<fieldset>
            <div class="span4">

                <div class="control-group <?php echo form_error('factory_name') ? 'error' : ''; ?>">
                    <?php echo form_label('Name'. lang('bf_form_label_required'), 'factory_name', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="1" id='factory_no_of_emps' type='text' name='factory_name'  value="<?php echo set_value('factory_name', isset($factory['name']) ? $factory['name'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('factory_name'); ?></span>
                    </div>
                </div>

                <div class="control-group <?php echo form_error('factory_cpcty_raw_mtrl') ? 'error' : ''; ?>">
                    <?php echo form_label('Storage Capacity - Raw material (metric tonnes)'. lang('bf_form_label_required'), 'factory_cpcty_raw_mtrl', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="4" id='factory_cpcty_raw_mtrl' type='text' name='factory_cpcty_raw_mtrl' maxlength="19" value="<?php echo set_value('factory_cpcty_raw_mtrl', isset($factory['cpcty_raw_mtrl']) ? $factory['cpcty_raw_mtrl'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('factory_cpcty_raw_mtrl'); ?></span>
                    </div>
                </div>
                
                <div class="control-group <?php echo form_error('factory_near_port') ? 'error' : ''; ?>">
                    <?php echo form_label('Nearest Sea Port'. lang('bf_form_label_required'), 'factory_near_port', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="7"  id='factory_near_port' type='text' name='factory_near_port' maxlength="255" value="<?php echo set_value('factory_near_port', isset($factory['near_port']) ? $factory['near_port'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('factory_near_port'); ?></span>
                    </div>
                </div>
                
                <div class="control-group <?php echo form_error('factory_m_cpcty') ? 'error' : ''; ?>">
                    <?php echo form_label('Capacity per Month'. lang('bf_form_label_required'), 'factory_m_cpcty', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="10" id='factory_m_cpcty' type='text' name='factory_m_cpcty'  value="<?php echo set_value('factory_m_cpcty', isset($factory['m_cpcty']) ? $factory['m_cpcty'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('factory_m_cpcty'); ?></span>
                    </div>
                </div>
                
                <div class="control-group <?php echo form_error('factory_d_cpcty') ? 'error' : ''; ?>">
                    <?php echo form_label('Capacity per Day'. lang('bf_form_label_required'), 'factory_d_cpcty', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="13" id='factory_d_cpcty' type='text' name='factory_d_cpcty'  value="<?php echo set_value('factory_d_cpcty', isset($factory['d_cpcty']) ? $factory['d_cpcty'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('factory_d_cpcty'); ?></span>
                    </div>
                </div>
                
                
                <div class="form-actions">
                    <input tabindex="15" type="submit" name="save" class="btn btn-primary" value="<?php echo lang('factory_action_create'); ?>"  />
                    <?php echo lang('bf_or'); ?>
                    <?php echo anchor(SITE_AREA .'/content/factory', lang('factory_cancel'), 'class="btn btn-warning"'); ?>

                </div>
                
            </div>

            <div class="span4">
                
                <div class="control-group <?php echo form_error('factory_address') ? 'error' : ''; ?>">
                    <?php echo form_label('Address'. lang('bf_form_label_required'), 'factory_address', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="2" id='factory_address' type='text' name='factory_address'  value="<?php echo set_value('factory_address', isset($factory['address']) ? $factory['address'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('factory_address'); ?></span>
                    </div>
                </div>
                
                <div class="control-group <?php echo form_error('factory_cpcty_storage') ? 'error' : ''; ?>">
                    <?php echo form_label('Storage Capacity - Finished material (metric tonnes)'. lang('bf_form_label_required'), 'factory_cpcty_storage', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="5" id='factory_cpcty_storage' type='text' name='factory_cpcty_storage' maxlength="19" value="<?php echo set_value('factory_cpcty_storage', isset($factory['cpcty_storage']) ? $factory['cpcty_storage'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('factory_cpcty_storage'); ?></span>
                    </div>
                </div>
                
                <div class="control-group <?php echo form_error('factory_near_airport') ? 'error' : ''; ?>">
                    <?php echo form_label('Nearest Airport'. lang('bf_form_label_required'), 'factory_near_airport', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="8"  id='factory_near_airport' type='text' name='factory_near_airport' maxlength="255" value="<?php echo set_value('factory_near_airport', isset($factory['near_airport']) ? $factory['near_airport'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('factory_near_airport'); ?></span>
                    </div>
                </div>
                
                <?php // Change the values in this array to populate your dropdown as required
                    if (is_array($uoms_select) && count($uoms_select)) :
                        echo form_dropdown('factory_m_cpcty_uom', $uoms_select, set_value('factory_m_cpcty_uom', isset($factory['m_cpcty_uom']) ? $factory['m_cpcty_uom'] : ''), '', 'tabindex="11"');
                    endif;
                ?>
                
                <?php // Change the values in this array to populate your dropdown as required
                    if (is_array($uoms_select) && count($uoms_select)) :
                        echo form_dropdown('factory_d_cpcty_uom', $uoms_select, set_value('factory_d_cpcty_uom', isset($factory['d_cpcty_uom']) ? $factory['d_cpcty_uom'] : ''), '', 'tabindex="14"');
                    endif;
                ?>
                
            </div>
            
            <div class="span4">
                
                <div class="control-group <?php echo form_error('factory_no_of_emps') ? 'error' : ''; ?>">
                    <?php echo form_label('Employee size'. lang('bf_form_label_required'), 'factory_no_of_emps', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="3" id='factory_no_of_emps' type='text' name='factory_no_of_emps'  value="<?php echo set_value('factory_no_of_emps', isset($factory['no_of_emps']) ? $factory['no_of_emps'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('factory_no_of_emps'); ?></span>
                    </div>
                </div>
                

                <?php // Change the values in this array to populate your dropdown as required
                    $options = array(
                        '-1' => 'Select one',
                        'Road' => 'Road',
                        'Rail' => 'Rail',
                    );

                    echo form_dropdown('factory_transport_opt', $options, set_value('factory_transport_opt', isset($factory['transport_opt']) ? $factory['transport_opt'] : ''), 'Transportation options', 'tabindex="6"');
                ?>
                
                <div class="control-group <?php echo form_error('factory_near_city') ? 'error' : ''; ?>">
                    <?php echo form_label('Nearest Major City'. lang('bf_form_label_required'), 'factory_near_city', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="9" id='factory_near_city' type='text' name='factory_near_city' maxlength="255" value="<?php echo set_value('factory_near_city', isset($factory['near_city']) ? $factory['near_city'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('factory_near_city'); ?></span>
                    </div>
                </div>
                
                <div class="control-group <?php echo form_error('courier_comp') ? 'error' : ''; ?>">
                    <?php echo form_label('Courier Company'. lang('bf_form_label_required'), 'factory_courier_comp', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="12" id='factory_courier_comp' type='text' name='factory_courier_comp' maxlength="255" value="<?php echo set_value('factory_courier_comp', isset($factory['courier_comp']) ? $factory['courier_comp'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('courier_comp'); ?></span>
                    </div>
                </div>
                
                
                
            </div>

            
		</fieldset>
    <?php echo form_close(); ?>
</div>