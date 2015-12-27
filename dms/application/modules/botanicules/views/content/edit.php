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

if (isset($botanicules))
{
	$botanicules = (array) $botanicules;
}
$id = isset($botanicules['id']) ? $botanicules['id'] : '';

?>
<script> 
  function check_ss() {
    
    var smiles = document.JME.smiles();
    //var jme = document.JME.jmeFile(); 
    var mol = document.JME.molFile();
    //alert("smiles len - " + smiles.length);
    if (smiles.length < 1) {
      alert("No molecule!");
    }
    else {
      //document.form.smiles.value = smiles;
      //document.form.jme.value = jme;
      //alert("in else");
      //alert(mol);
      document.form2.botanicules_structure.value = mol;
      document.form.submit();
    }
  }
</script>

<div class="admin-box">
	<h3>Botanicules</h3>
	<?php echo form_open($this->uri->uri_string(), 'class="form-inline" id="form2" name="form2"'); ?>
		<fieldset>
            <div class="span4">
           <?php
               function tr4jme($inmol) {
                  $outmol = $inmol;
                  $outmol = str_replace("\r","",$outmol);
                  $outmol = strtr($outmol,"\n","|");
                  return($outmol);
                } 

                $mol = $botanicules['structure'];
                $mol = str_replace("\r\n","\n",$mol);
                $mol = str_replace("\n","\r\n",$mol);

                $jmehitmol = tr4jme($mol);
            ?>                
                
                <div class="control-group <?php echo form_error('botanicules_structure') ? 'error' : ''; ?>">
                    <?php echo form_label('Structure'. lang('bf_form_label_required'), 'botanicules_structure', array('class' => 'control-label') ); ?>
                    <div tabindex="1" class='controls'>
                        <applet code="JME.class" name="JME" archive="/app/public/JME.jar" width="360" height="315" id="JME">
                            <param name="mol" value="<?php if(isset($jmehitmol)) { echo ($jmehitmol); } ?>">
                             You have to enable Java and JavaScript in your browser to use JME!
                         </applet>
                        
                        <input type="hidden" id='botanicules_structure' name='botanicules_structure' maxlength="4000" value="<?php echo set_value('botanicules_structure', isset($botanicules['structure']) ? $botanicules['structure'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('botanicules_structure'); ?></span>
                    </div>
                </div>
            </div>
            <div class="span4">
                <div class="control-group <?php echo form_error('compound_name') ? 'error' : ''; ?>">
                    <?php echo form_label('Compound Name', 'botanicules_compound_name', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="2" id='botanicules_compound_name' type='text' name='botanicules_compound_name' maxlength="1000" value="<?php echo set_value('botanicules_compound_name', isset($botanicules['compound_name']) ? $botanicules['compound_name'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('compound_name'); ?></span>
                    </div>
                </div>
                <div class="control-group <?php echo form_error('ref') ? 'error' : ''; ?>">
                    <?php echo form_label('Reference', 'botanicules_ref', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="4" id='botanicules_ref' type='text' name='botanicules_ref' maxlength="1000" value="<?php echo set_value('botanicules_ref', isset($botanicules['ref']) ? $botanicules['ref'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('ref'); ?></span>
                    </div>
                </div>
                
                <div class="control-group <?php echo form_error('mol_weight') ? 'error' : ''; ?>">
                    <?php echo form_label('Molecular Weight', 'botanicules_mol_weight', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="6" id='botanicules_mol_weight' type='text' name='botanicules_mol_weight' maxlength="19" value="<?php echo set_value('botanicules_mol_weight', isset($botanicules['mol_weight']) ? $botanicules['mol_weight'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('mol_weight'); ?></span>
                    </div>
                </div>
                <div class="control-group <?php echo form_error('mol_name') ? 'error' : ''; ?>">
                    <?php echo form_label('Molecule Name', 'botanicules_mol_name', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="8" id='botanicules_mol_name' type='text' name='botanicules_mol_name' maxlength="1000" value="<?php echo set_value('botanicules_mol_name', isset($botanicules['mol_name']) ? $botanicules['mol_name'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('mol_name'); ?></span>
                    </div>
                </div>
                <div class="control-group <?php echo form_error('src_ref') ? 'error' : ''; ?>">
                    <?php echo form_label('Source Reference', 'botanicules_src_ref', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="10" id='botanicules_src_ref' type='text' name='botanicules_src_ref' maxlength="1000" value="<?php echo set_value('botanicules_src_ref', isset($botanicules['src_ref']) ? $botanicules['src_ref'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('src_ref'); ?></span>
                    </div>
                </div>
                <div class="control-group <?php echo form_error('src_type') ? 'error' : ''; ?>">
                    <?php echo form_label('Source Type', 'botanicules_src_type', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="12" id='botanicules_src_type' type='text' name='botanicules_src_type' maxlength="1000" value="<?php echo set_value('botanicules_src_type', isset($botanicules['src_type']) ? $botanicules['src_type'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('src_type'); ?></span>
                    </div>
                </div>
                <?php // Change the values in this array to populate your dropdown as required
                    $options = array(
                        "Available" => "Available",
                        "Not Available" => "Not Available"
                    );

                    echo form_dropdown('botanicules_pdf_avail', $options, set_value('botanicules_pdf_avail', isset($botanicules['pdf_avail']) ? $botanicules['pdf_avail'] : ''), 'PDF Availability', 'tabindex="14"');
                ?>
            </div>
            <div class="span4">
                <div class="control-group <?php echo form_error('iupac_name') ? 'error' : ''; ?>">
                    <?php echo form_label('IUPAC Name', 'botanicules_iupac_name', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="3" id='botanicules_iupac_name' type='text' name='botanicules_iupac_name' maxlength="1000" value="<?php echo set_value('botanicules_iupac_name', isset($botanicules['iupac_name']) ? $botanicules['iupac_name'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('iupac_name'); ?></span>
                    </div>
                </div>
                <div class="control-group <?php echo form_error('parts_of_isol') ? 'error' : ''; ?>">
                    <?php echo form_label('Parts of Isolation', 'botanicules_parts_of_isol', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="5" id='botanicules_parts_of_isol' type='text' name='botanicules_parts_of_isol' maxlength="1000" value="<?php echo set_value('botanicules_parts_of_isol', isset($botanicules['parts_of_isol']) ? $botanicules['parts_of_isol'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('parts_of_isol'); ?></span>
                    </div>
                </div>
                
                <div class="control-group <?php echo form_error('formula') ? 'error' : ''; ?>">
                    <?php echo form_label('Formula', 'botanicules_formula', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="7" id='botanicules_formula' type='text' name='botanicules_formula' maxlength="255" value="<?php echo set_value('botanicules_formula', isset($botanicules['formula']) ? $botanicules['formula'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('formula'); ?></span>
                    </div>
                </div>
                <div class="control-group <?php echo form_error('mol_type') ? 'error' : ''; ?>">
                    <?php echo form_label('Molecule Type', 'botanicules_mol_type', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="9" id='botanicules_mol_type' type='text' name='botanicules_mol_type' maxlength="1000" value="<?php echo set_value('botanicules_mol_type', isset($botanicules['mol_type']) ? $botanicules['mol_type'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('mol_type'); ?></span>
                    </div>
                </div>
                <div class="control-group <?php echo form_error('therapeutic_catg') ? 'error' : ''; ?>">
                    <?php echo form_label('Therapeutic Category', 'botanicules_therapeutic_catg', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="11" id='botanicules_therapeutic_catg' type='text' name='botanicules_therapeutic_catg' maxlength="255" value="<?php echo set_value('botanicules_therapeutic_catg', isset($botanicules['therapeutic_catg']) ? $botanicules['therapeutic_catg'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('therapeutic_catg'); ?></span>
                    </div>
                </div>
                <div class="control-group <?php echo form_error('src_family') ? 'error' : ''; ?>">
                    <?php echo form_label('Source Family', 'botanicules_src_family', array('class' => 'control-label') ); ?>
                    <div class='controls'>
                        <input tabindex="13" id='botanicules_src_family' type='text' name='botanicules_src_family' maxlength="1000" value="<?php echo set_value('botanicules_src_family', isset($botanicules['src_family']) ? $botanicules['src_family'] : ''); ?>" />
                        <span class='help-inline'><?php echo form_error('src_family'); ?></span>
                    </div>
                </div>
                <?php // Change the values in this array to populate your dropdown as required
                    $options = array(
                        "Submitted" => "Submitted",
                        "Approved" => "Approved"
                    );

                    echo form_dropdown('botanicules_qc_status', $options, set_value('botanicules_qc_status', isset($botanicules['qc_status']) ? $botanicules['qc_status'] : ''), 'QC Status', 'tabindex="15"');
                ?>
            </div>
            <div class="span12">
                <div class="form-actions">
                    <input tabindex="16" type="submit" name="save" class="btn btn-primary" value="<?php echo lang('botanicules_action_create'); ?>" onClick="check_ss();" />
                    <?php echo lang('bf_or'); ?>
                    <?php echo anchor(SITE_AREA .'/content/botanicules', lang('botanicules_cancel'), 'class="btn btn-warning"'); ?>

                </div>
            </div>
		</fieldset>
    <?php echo form_close(); ?>
</div>