<?php

$validation_errors = validation_errors();

if ($validation_errors) :
?>
<div class='alert alert-block alert-error fade in'>
	<a class='close' data-dismiss='alert'>&times;</a>
	<h4 class='alert-heading'>
		<?php echo lang('botan_structure_errors_message'); ?>
	</h4>
	<?php echo $validation_errors; ?>
</div>
<?php
endif;

$id = isset($botan_structure->mol_id) ? $botan_structure->mol_id : '';

?>
<script> 
  function check_ss() {
    
    var smiles = document.JME.smiles();
    //var jme = document.JME.jmeFile(); 
    var mol = document.JME.molFile();
    alert("smiles len - " + smiles.length);
    if (smiles.length < 1) {
      alert("No molecule!");
    }
    else {
      //document.form.smiles.value = smiles;
      //document.form.jme.value = jme;
      alert("in else");
      alert(mol);
      document.form2.botan_structure_struc.value = mol;
      alert("mol - " + document.form2.botan_structure_struc.value);
      //document.form.submit();
    }
  }
</script>
<div class='admin-box'>
	<h3>Botan Structure</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal" id="form2" name="form2"'); ?>
		<fieldset>
            <div class="control-group <?php echo form_error('mol_id') ? 'error' : ''; ?>">
				<?php echo form_label('Mol Id'. lang('bf_form_label_required'), 'botan_structure_mol_id', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='botan_structure_mol_id' type='text' name='botan_structure_mol_id' maxlength="255" value="<?php echo set_value('botan_structure_mol_id', isset($botan_structure['mol_id']) ? $botan_structure['mol_id'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('mol_id'); ?></span>
				</div>
			</div>

			 <div class="control-group <?php echo form_error('struc') ? 'error' : ''; ?>">
				<?php echo form_label('Struc'. lang('bf_form_label_required'), 'botan_structure_struc', array('class' => 'control-label') ); ?>
				<div class='controls'>
				<applet code="JME.class" name="JME" archive="/app/public/JME.jar" width="360" height="315" id="JME">
					<param name="jme" value="<?php if(isset($botan_structure['struc'])) { echo ($botan_structure['struc']); } ?>">
                     You have to enable Java and JavaScript in your browser to use JME!
	             </applet>

	            	<input tabindex="1" type="hidden" id="botan_structure_struc" name="botan_structure_struc" value="<?php if(isset($_POST['botan_structure_struc'])) { echo $_POST['botan_structure_struc']; } ?>" />	
					<span class='help-inline'><?php echo form_error('struc'); ?></span>
				</div>
			</div> 
            
            

        </fieldset>
		<fieldset class='form-actions'>
			<input type='submit' name='save' class='btn btn-primary' value="<?php echo lang('botan_structure_action_create'); ?>" onClick="check_ss();" />
			<?php echo lang('bf_or'); ?>
			<?php echo anchor(SITE_AREA . '/content/botan_structure', lang('botan_structure_cancel'), 'class="btn btn-warning"'); ?>
			
		</fieldset>
    <?php echo form_close(); ?>
</div>
























