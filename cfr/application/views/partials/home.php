<hr/>
<?php
	$perct = 0;

	foreach($pct as $row){
		$perct = round(($row->answers / $row->questions) * 100);
		$perct = ltrim($perct);
	}
?>
<div class="col-md-12">
    <div class="progress">
        <div class="progress-bar" role="progressbar" aria-valuenow="<?php echo $perct; ?>" aria-valuemin="0" aria-valuemax="100" style="width:<?php echo trim($perct) . '%'; ?>";>
            <?php echo $perct; ?>% completed
        </div>
    </div>    
</div>
<div class="col-md-4" style="float:left;">
  <?php echo $this->load->view('partials/left_menus'); ?>
</div>    
<div class="col-md-8" style="float:right;">
  <?php echo $this->load->view('partials/questions'); ?>
</div>    