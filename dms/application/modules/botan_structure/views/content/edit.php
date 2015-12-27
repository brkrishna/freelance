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

if (isset($botan_structure))
{
	$botan_structure = (array) $botan_structure;
}
$id = isset($botan_structure['mol_id']) ? $botan_structure['mol_id'] : '';

?>
<script type="text/JavaScript"> 
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
      //alert(document.form.molstruct_struc.value);
      document.form.submit();
    }
  }
 </script>

<div class="admin-box">
	<h3>botan structure</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-horizontal" id="form2" name="form2"'); ?>
		<fieldset>
             <div class="control-group <?php echo form_error('mol_id') ? 'error' : ''; ?>">
				<?php echo form_label('Mol Id'. lang('bf_form_label_required'), 'botan_structure_mol_id', array('class' => 'control-label') ); ?>
				<div class='controls'>
					<input id='botan_structure_mol_id' type='text' name='botan_structure_mol_id' maxlength="255" value="<?php echo set_value('botan_structure_mol_id', isset($botan_structure['mol_id']) ? $botan_structure['mol_id'] : ''); ?>" />
					<span class='help-inline'><?php echo form_error('mol_id'); ?></span>
				</div>
			</div>

           <?php
            $mol = $botan_structure['struc'];
            $mol = str_replace("\r\n","\n",$mol);
            $mol = str_replace("\n","\r\n",$mol);

            $jmehitmol = tr4jme($mol);
            function tr4jme($inmol) {
			  $outmol = $inmol;
			  $outmol = str_replace("\r","",$outmol);
			  $outmol = strtr($outmol,"\n","|");
			  return($outmol);
			}
             ?>


			<div class="control-group <?php echo form_error('struc') ? 'error' : ''; ?>">
				<?php echo form_label('Struc'. lang('bf_form_label_required'), 'botan_structure_struc', array('class' => 'control-label') ); ?>
				<div class='controls'>
				<applet code="JME.class" name="JME" archive="/app/public/JME.jar" width="360" height="315" id="JME">
					<param name="mol" value="<?php echo ($jmehitmol); ?>" >
                     You have to enable Java and JavaScript in your browser to use JME!
	             </applet>

	            	<input type="hidden" id="botan_structure_struc" name="botan_structure_struc" value="<?php if(isset($_POST['botan_structure_struc'])) { echo $_POST['botan_structure_struc']; } ?>" />	
					<span class='help-inline'><?php echo form_error('struc'); ?></span>
				</div>
			</div>

			<div class="form-actions">
				<input type="submit" name="save" class="btn btn-primary" value="<?php echo lang('botan_structure_action_edit'); ?>" onClick="check_ss();" />
				<?php echo lang('bf_or'); ?>
				<?php echo anchor(SITE_AREA .'/content/botan_structure', lang('botan_structure_cancel'), 'class="btn btn-warning"'); ?>
				
			<?php if ($this->auth->has_permission('Botan_Structure.Content.Delete')) : ?>
				or
				<button type="submit" name="delete" class="btn btn-danger" id="delete-me" onclick="return confirm('<?php e(js_escape(lang('botan_structure_delete_confirm'))); ?>'); ">
					<span class="icon-trash icon-white"></span>&nbsp;<?php echo lang('botan_structure_delete_record'); ?>
				</button>
			<?php endif; ?>
			</div>
		</fieldset>
    <?php echo form_close(); ?>
</div>















