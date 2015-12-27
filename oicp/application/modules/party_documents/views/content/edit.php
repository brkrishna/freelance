<?php

$validation_errors = validation_errors();

if ($validation_errors) :
?>
<div class='alert alert-block alert-error fade in'>
	<a class='close' data-dismiss='alert'>&times;</a>
	<h4 class='alert-heading'>
		<?php echo lang('party_documents_errors_message'); ?>
	</h4>
	<?php echo $validation_errors; ?>
</div>
<?php
endif;

$id = isset($party_documents->id) ? $party_documents->id : '';

?>
<div class='admin-box'>
	<h3>Party Documents</h3>
	<?php echo form_open_multipart($this->uri->uri_string(), 'class="form-horizontal"'); ?>
		<fieldset>
            
			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($party_select) && count($party_select)) :	
				    echo form_dropdown('party_documents_party_id', $party_select, set_value('party_documents_party_id', isset($party_documents->party_id) ? $party_documents->party_id : ''), 'Party'. lang('bf_form_label_required'));
                endif;
			?>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($products_select) && count($products_select)) :	
				    echo form_dropdown('party_documents_product_id', $products_select, set_value('party_documents_product_id', isset($party_documents->product_id) ? $party_documents->product_id : ''), 'Product'. lang('bf_form_label_required'));
                endif;
			?>

			<?php // Change the values in this array to populate your dropdown as required
                if (is_array($ingredients_select) && count($ingredients_select)) :	
				    echo form_dropdown('party_documents_ingredient_id', $ingredients_select, set_value('party_documents_ingredient_id', isset($party_documents->ingredient_id) ? $party_documents->ingredient_id : ''), 'Ingredient');
                endif;
			?>

            <?php // Change the values in this array to populate your dropdown as required
                $options = array(
                    '-1'=>'Select one',
                    'Wild Collection'=>'Wild Collection',
                    'Processing'=>'Processing',
                    'Production' => 'Production',
                    'Trading' => 'Trading',
                    'NA'=>'NA'
                );
                echo form_dropdown(array('name' => 'party_documents_catg', 'required' => 'required'), $options, set_value('party_documents_catg', isset($party_documents->catg) ? $party_documents->catg : ''), 'Category' . lang('bf_form_label_required'));
            ?>

            <?php // Change the values in this array to populate your dropdown as required
                $options = array(
                    '-1'=>'Select one',
                    'NOP'=>'NOP',
                    'NPOP'=>'NPOP',
                    'NOP and NPOP' => 'NOP and NPOP',
                    'NA'=>'NA'
                );
                echo form_dropdown(array('name' => 'party_documents_cert_type', 'required' => 'required'), $options, set_value('party_documents_cert_type', isset($party_documents->cert_type) ? $party_documents->cert_type : ''), 'Certification Type' . lang('bf_form_label_required'));
            ?>

			<div class="control-group<?php echo form_error('doc_name') ? ' error' : ''; ?>">
				<?php echo form_label('Document Name'. lang('bf_form_label_required'), 'doc_name', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='doc_name' type='text' required='required' name='doc_name' maxlength='255' value="<?php echo set_value('doc_name', isset($party_documents->doc_name) ? $party_documents->doc_name : ''); ?>" />
					<span class='help-inline'><?php echo form_error('doc_name'); ?></span>
				</div>
			</div>

			<!--Document -->
            <?php if(isset($party_documents) && isset($party_documents->doc_file) && !empty($party_documents->doc_file)) : $attachment = unserialize($party_documents->doc_file);
            ?>

            <?php if (isset($attachment)) : ?>
                <!-- Current Document Display -->
                <div class="control-group">
                    <label class="control-label">File</label>
                    <div class="controls">
                        <ul class="thumbnails">
                            <li class="span6">
                                <a class="lightbox" href="<?php echo base_url() . '/uploads/' . $attachment['file_name'] ?>" target="_blank" >
                                    <?php echo $attachment['file_name']; ?>
                                </a>
                                <!--<p><?php echo anchor(SITE_AREA.'/content/party_documents/remove_attachment/'.$party_documents->id,'Remove', 'class="btn btn-small btn-danger"'); ?></p>-->
                            </li>
                        </ul>
                        <input id='doc_file' type='hidden' name='doc_file' value=<?php echo($party_documents->doc_file); ?>/>
                    </div>
                </div>
                <?php endif; ?>
            <?php else: ?>
                <div class="control-group <?php echo form_error('doc_file') ? 'error' : ''; ?>">
                    <?php echo form_label('File', 'doc_file', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input id='doc_file' type='file' name='doc_file'/>
                        <span class='help-inline'><?php echo form_error('doc_file'); ?></span>
                    </div>
                </div>
            <?php endif; ?>  

            <div class="control-group<?php echo form_error('rcvd_on') ? ' error' : ''; ?>">
				<?php echo form_label('Received on'. lang('bf_form_label_required'), 'rcvd_on', array('class' => 'control-label')); ?>
				<div class='controls'>
					<input id='rcvd_on' type='text' required='required' name='rcvd_on' maxlength='50' value="<?php echo set_value('rcvd_on', isset($party_documents->rcvd_on) ? $party_documents->rcvd_on : ''); ?>" />
					<span class='help-inline'><?php echo form_error('rcvd_on'); ?></span>
				</div>
			</div>

			<div class="control-group<?php echo form_error('comments') ? ' error' : ''; ?>">
				<?php echo form_label('Comments', 'comments', array('class' => 'control-label')); ?>
				<div class='controls'>
					<?php echo form_textarea(array('name' => 'comments', 'id' => 'comments', 'rows' => '5', 'cols' => '80', 'value' => set_value('comments', isset($party_documents->comments) ? $party_documents->comments : ''))); ?>
					<span class='help-inline'><?php echo form_error('comments'); ?></span>
				</div>
			</div>

			<?php // Change the values in this array to populate your dropdown as required
				$options = array(
					'No'=>'No',
					'Yes'=>'Yes'
				);
				echo form_dropdown(array('name' => 'archive', 'required' => 'required'), $options, set_value('archive', isset($party_documents->archive) ? $party_documents->archive : ''), 'Archive' . lang('bf_form_label_required'));
			?>

        </fieldset>
		<fieldset class='form-actions'>
			<input type='submit' name='save' class='btn btn-primary' value="<?php echo lang('party_documents_action_edit'); ?>" />
			<?php echo lang('bf_or'); ?>
			<?php echo anchor(SITE_AREA . '/content/party_documents', lang('party_documents_cancel'), 'class="btn btn-warning"'); ?>
			
			<?php if ($this->auth->has_permission('Party_Documents.Content.Delete')) : ?>
				<?php echo lang('bf_or'); ?>
				<button type='submit' name='delete' formnovalidate class='btn btn-danger' id='delete-me' onclick="return confirm('<?php e(js_escape(lang('party_documents_delete_confirm'))); ?>');">
					<span class='icon-trash icon-white'></span>&nbsp;<?php echo lang('party_documents_delete_record'); ?>
				</button>
			<?php endif; ?>
		</fieldset>
    <?php echo form_close(); ?>
</div>