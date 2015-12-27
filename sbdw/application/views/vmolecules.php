	<?php defined('BASEPATH') OR exit('No direct script access allowed');

	$this->load->view('/includes/head');
	date_default_timezone_set('Asia/Calcutta');
	$mol = '';
	?>
	      <script src="http://ajax.googleapis.com/ajax/libs/dojo/1.9.1/dojo/dojo.js" type="text/javascript"></script>
	      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
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
							<h5><?php echo ('<strong>' . $src_count . '</strong>'); ?> diverse sources</h5>
							<h5><strong><?php echo ($cd_timestamp_count); ?></strong> new records added on - <strong><?php echo date("d-M-y", strtotime($last_updated_on)); ?></strong></h5>
						</span>
						<?php foreach($records->result() as $record) : ?>
							<table class="table table-bordered">
								<caption><h3><?php echo ($record->molecule_name); ?></h3></caption>
								<?php $mol = $record->molecule_name; ?>
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
						<div class="row">
	                    <div class="col-xs-6 col-md-6">
						<?php echo $this->pagination->create_links(); ?>
						</div>
						<div class="col-xs-2 col-md-2"></div>
						<div class="col-xs-4 col-md-4">
						<div>
							<table  id="ncbi" class="table table-condensed table-bordered ncbi">
								<caption><strong>Activity Data</strong></caption>
								<th><small>Activity Name</small></th><th><small>Activity Value(uM)</small></th>
							</table>
						
						</div>
						</div>
						 </div>
					</div>
					
					<script type="text/javascript">
					$("document").ready(function(){
					 	$.getJSON('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/<?php echo $mol; ?>/cids/json',
					 		function(data){
							   		cid = data.IdentifierList.CID[0];
								    $.getJSON('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/' + cid + '/assaysummary/json',
										function(data){
											counter = 0;
											for(i = 0; i < data.Table.Row.length; i++){
												bioactvty_outcome = data.Table.Row[i].Cell[6];
												actvty_nm = data.Table.Row[i].Cell[10];
												actvty_val = data.Table.Row[i].Cell[9];
												$("#ncbi").hide();
												if (bioactvty_outcome == "Active"){
													if (actvty_nm != "" && actvty_val != "" && counter < 3){
														$("#ncbi").show();
														$(".ncbi").append('<tr><td>' + actvty_nm + '</td><td style="text-align:right;">' + actvty_val + '</td></tr>');
														counter += 1;
													}
												}
														
											}
										}
									);
								}
							);
						});
					 </script>
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
