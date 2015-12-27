    <?php defined('BASEPATH') OR exit('No direct script access allowed');

    $this->load->view('/includes/head');

    ?>
          <script src="http://ajax.googleapis.com/ajax/libs/dojo/1.9.1/dojo/dojo.js" type="text/javascript"></script>
          <script src="<?php echo base_url('public/js/Scilligence.JSDraw2.Pro.js') ?>"></script>
          <script type="text/javascript">JSDraw.init();</script>
          <div class="container">
            <div class="row">
                 <div class="col-md-4 col-sm-6" style="padding:5px;">
                    <?php foreach($substrate->result() as $record) : ?>
                        <table class="table table-bordered table-condensed" style="margin-bottom:5px;">
                            <caption><h5><strong>Substrates - </strong><?php echo($record->substrate);?></h5></caption>
                            <tr>
                                <td colspan="4">
                                    <div class='JSDraw' id='div2' style='width: 250px; height: 175px; border:0px solid gray' dataformat='molfile' viewonly showimplicithydrogens="false" data="<?php echo ($record->cd_structure); ?>"></div>
                             </td>
                            </tr>
                            <tr class="info">
                                <th>Mol. Weight</th>
                                <th>Formula</th>
                                <th>Species</th>
                                <th>Half Life</th>
                            </tr>
                            <tr>
                                <td><?php echo($record->cd_molweight);?></td>
                                <td><?php echo($record->cd_formula);?></td>
                                <td><?php echo($record->species);?></td>
                                <td><?php echo($record->half_life);?></td>
                            </tr>
                        </table>
                    <?php endforeach; ?>
					<ul class="pager" style="margin:10px;">
						<li class="<?php echo ($s_offset == 0 ? 'disabled' : ''); ?>"><a href="/staging/index.php/Substrates/substrate/<?php echo intval($s_offset) - 1; ?>"><span class="glyphicon glyphicon-chevron-left"></span></a></li>
						<small><?php echo($s_offset + 1); ?> of <?php echo($substrate_count); ?></small>
						<li class="<?php echo ($s_offset == $substrate_count - 1 ? 'disabled' : ''); ?>"><a href="/staging/index.php/Substrates/substrate/<?php echo intval($s_offset) + 1; ?>"><span class="glyphicon glyphicon-chevron-right"></a></span></li>
					</ul>
                </div>
                <div class="col-md-4 col-sm-6" style="padding:5px;">
                    <?php foreach($biotrans->result() as $record) : ?>
                        <table class="table table-bordered table-condensed" style="margin-bottom:5px;">
                            <caption><h5><strong>Bio Transformations</strong></h5></caption>
                            <tr>
                                <td colspan="4">
                                    <div class='JSDraw' id='div2' style='width: 450px; height: 175px; border:0px solid gray' dataformat='molfile' readonly viewonly showimplicithydrogens="false" data="<?php echo ($record->cd_structure); ?>"></div>
                             </td>
                            </tr>
                            <tr class="info">
                                <th>Reactant</th>
                                <th>Phase</th>
                                <th>Reaction</th>
                                <th>Enzyme</th>
                            </tr>
                            <tr>
                                <td><?php echo($record->reactant);?></td>
                                <td><?php echo($record->phase);?></td>
                                <td><?php echo($record->reaction);?></td>
                                <td><?php echo($record->enzyme);?></td>
                            </tr>
                        </table>
                    <?php endforeach; ?>
                    <nav>
						<ul class="pager" style="margin:10px;">
							<li class="<?php echo ($b_offset == 0 ? 'disabled' : ''); ?>"><a href="/staging/index.php/Substrates/biotrans/<?php echo intval($substrate_id); ?>/<?php echo intval($s_offset); ?>/<?php echo intval($m_offset); ?>/<?php echo intval($b_offset) - 1; ?>"><span class="glyphicon glyphicon-chevron-left"></span></a></li>
							<small><?php echo($b_offset + 1); ?> of <?php echo($biotrans_count); ?></small>
							<li class="<?php echo ($b_offset == $biotrans_count - 1 ? 'disabled' : ''); ?>"><a href="/staging/index.php/Substrates/biotrans/<?php echo intval($substrate_id); ?>/<?php echo intval($s_offset); ?>/<?php echo intval($m_offset); ?>/<?php echo intval($b_offset) + 1; ?>"><span class="glyphicon glyphicon-chevron-right"></a></span></li>
						</ul>
                    </nav>
                </div>
            </div>
            <div class="row">
                <div class="col-md-4 col-sm-6" style="padding:5px;">
                    <?php foreach($metabolite->result() as $record) : ?>
                        <table class="table table-bordered table-condensed" style="margin-bottom:5px;">
                            <caption><h5><strong>Metabolites</strong></h5></caption>
                            <tr>
                                <td colspan="3">
                                    <div class='JSDraw' id='div2' style='width: 250px; height: 175px; border:0px solid gray' dataformat='molfile' viewonly showimplicithydrogens="false" data="<?php echo ($record->cd_structure); ?>"></div>
                                </td>
                            </tr>
                            <tr class="info">
                                <th>Molecular Weight</th>
                                <th>Formula</th>
                                <th>Major</th>
                            </tr>
                            <tr>
                                <td><?php echo($record->cd_molweight);?></td>
                                <td><?php echo($record->cd_formula);?></td>
                                <td><?php echo($record->major == 1 ? 'True' : 'False');?></td>
                            </tr>
                         </table>
                    <?php endforeach; ?>
                    <nav>
						<ul class="pager" style="margin:10px;">
							<li class="<?php echo ($m_offset == 0 ? 'disabled' : ''); ?>"><a href="/staging/index.php/Substrates/metabolite/<?php echo intval($substrate_id); ?>/<?php echo intval($s_offset); ?>/<?php echo intval($m_offset) - 1; ?>"><span class="glyphicon glyphicon-chevron-left"></span></a></li>
							<small><?php echo($m_offset + 1); ?> of <?php echo($metabolites_count); ?></small>
							<li class="<?php echo ($m_offset == $metabolites_count - 1 ? 'disabled' : ''); ?>"><a href="/staging/index.php/Substrates/metabolite/<?php echo intval($substrate_id); ?>/<?php echo intval($s_offset); ?>/<?php echo intval($m_offset) + 1; ?>"><span class="glyphicon glyphicon-chevron-right"></a></span></li>
						</ul>
                    </nav>
				</div>
				<div class="col-md-4 col-sm-6" style="padding:15px;">
					<h3>Useful Statistics</h3>
                    <h5><strong><?php echo ($cd_timestamp_count); ?></strong> new records added on - <strong><?php echo date("d-M-y", strtotime($last_updated_on)); ?></strong></h5>
				</div>
            </div>
        </div>
