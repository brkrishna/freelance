<?php

$num_columns	= 1;
$can_delete	= $this->auth->has_permission('Botan_Structure.Content.Delete');
$can_edit		= $this->auth->has_permission('Botan_Structure.Content.Edit');
$has_records	= isset($records) && is_array($records) && count($records);

if ($can_delete) {
    $num_columns++;
}
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
	<h3>
		<?php echo lang('botan_structure_area_title'); ?>
	</h3>
	<?php echo form_open($this->uri->uri_string()); ?>
    <?php echo $this->pagination->create_links(); ?>
		<table class='table table-striped'>
			<thead>
				<tr>
					<?php if ($can_delete && $has_records) : ?>
					<th class='column-check'><input class='check-all' type='checkbox' /></th>
					<?php endif;?>
					<th>Mol Id</th>
					<th>Struc</th>
				</tr>
			</thead>
			<?php if ($has_records) : ?>
			<tfoot>
				<?php if ($can_delete) : ?>
				<tr>
					<td colspan='<?php echo $num_columns; ?>'>
						<?php echo lang('bf_with_selected'); ?>
						<input type='submit' name='delete' id='delete-me' class='btn btn-danger' value="<?php echo lang('bf_action_delete'); ?>" onclick="return confirm('<?php e(js_escape(lang('botan_structure_delete_confirm'))); ?>')" />
					</td>
				</tr>
				<?php endif; ?>
			</tfoot>
			<?php endif; ?>
			<tbody>
                <?php
			            function tr4jme($inmol) {
						  $outmol = $inmol;
						  $outmol = str_replace("\r","",$outmol);
						  $outmol = strtr($outmol,"\n","|");
						  return($outmol);
						}

				?>
				<?php
				if ($has_records) :
					foreach ($records as $record) :
				?>
				<tr>
					<?php if ($can_delete) : ?>
					<td class='column-check'><input type='checkbox' name='checked[]' value='<?php echo $record->mol_id; ?>' /></td>
					<?php endif;?>
					
				<?php if ($can_edit) : ?>
					<td><?php echo anchor(SITE_AREA . '/content/botan_structure/edit/' . $record->mol_id, '<span class="icon-pencil"></span> ' .  $record->mol_id); ?></td>
				<?php else : ?>
                    <td><?php e($record->mol_id); ?>
					
				<?php endif; ?>
                        <td><?php 
                         
				       	$mol = $record->struc;
			            $mol = str_replace("\r\n","\n",$mol);
			            $mol = str_replace("\n","\r\n",$mol);

			            $jmehitmol = tr4jme($mol);
                        ?>
                    
			<div class="control-group <?php echo form_error('struc') ? 'error' : ''; ?>">
				<?php echo form_label('Struc'. lang('bf_form_label_required'), 'botan_structure_struc', array('class' => 'control-label') ); ?>
				<div class='controls'>
				<applet code="JME.class" name="JME" archive="/public/JME.jar" width="360" height="315" id="JME">
					<param name="options" value="depict">
					<param name="mol" value="<?php echo ($jmehitmol); ?>" >
                     You have to enable Java and JavaScript in your browser to use JME!
	             </applet>

	            	<input type="hidden" id="botan_structure_struc" name="botan_structure_struc" value="<?php if(isset($_POST['botan_structure_struc'])) { echo $_POST['botan_structure_struc']; } ?>" />	
					<span class='help-inline'><?php echo form_error('struc'); ?></span>
				</div>
			</div>
             </td>
				</tr>
				<?php
					endforeach;
				else:
				?>
				<tr>
					<td colspan='<?php echo $num_columns; ?>'><?php echo lang('botan_structure_records_empty'); ?></td>
				</tr>
				<?php endif; ?>
			</tbody>
		</table>
	<?php
    echo form_close();
    
    ?>
</div>




















