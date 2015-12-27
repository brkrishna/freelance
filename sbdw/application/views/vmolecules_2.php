<?php defined('BASEPATH') OR exit('No direct script access allowed');

$this->load->view('/includes/head');

?>
      <script src="http://ajax.googleapis.com/ajax/libs/dojo/1.9.1/dojo/dojo.js" type="text/javascript"></script>   
      <script src="<?php echo base_url('public/js/Scilligence.JSDraw2.Pro.js') ?>"></script>
	<body class="background">
		<div class="container">
			<script type="text/javascript">JSDraw.init();</script>
			<div class="row">
				<div class="service">
					<span class="pull-left"><h2><?php echo(strtoupper($table)); ?></h2></span>
					<span class="pull-right">
						<h3>Useful Statistics</h3>
						<h5><?php echo ('<strong>' . $record_count . '</strong>'); ?> records in library. <?php echo ('<strong>' . $src_family_count . '</strong>'); ?> diverse source families</h5>
					</span>
					<?php foreach($records->result() as $record) : ?>
						<table class="table table-bordered">
							<caption><h3><?php echo ($record->molecule_name); ?></h3></caption>
							<tr>
								<td rowspan="8">
									<div class='JSDraw' id='div2' style='width: 350px; height: 325px; border:0px solid gray' dataformat='molfile' viewonly data='" . <?php echo $record->cd_structure; ?> . "'></div>                                
								</td>
								<td><strong>Molecular weight</strong></td>
								<td><?php echo($record->cd_molweight);?></td>
							</tr>
							<tr>
								<td><strong>Formula</strong></td>
								<td><?php echo($record->cd_formula);?></td>
							</tr>
							<tr>
								<td><strong>Molecule Type</strong></td>
								<td><?php echo($record->molecule_type);?></td>
							</tr>
							<tr>
								<td><strong>Therapeutic Category</strong></td>
								<td><?php echo($record->therapeutic_category);?></td>
							</tr>
							<tr>
								<td><strong>Source Name</strong></td>
								<td><?php echo($record->source_name);?></td>
							</tr>
						</table>
					<?php endforeach; ?>
					<?php echo $this->pagination->create_links(); ?>    
				</div>
				<p class="text-justify">
					We would be glad to hear your feedback on our libraries
					<br/>
					<a href="<?php echo base_url('/index.php/Contactus/vinquire'); ?>">Click here</a> to 
					enquire more about these products and subscription options
				</p>
			</div>
			<hr/>
		</div>
	</body>
</html>
