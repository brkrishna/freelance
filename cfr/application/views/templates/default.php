<?php $this->load->view('include/header'); ?>
<div class="container-fluid">
	<div class="header">
		<div class="row-fluid">
			<div class="col-md-2 col-xm-2">
				<img class="logo" src="<?php echo base_url('assets/imgs/logo.png'); ?>" alt="Sristi Bio-sciences" title="Sristi Bio-sciences" />	
			</div>
			<div class="col-md-10 col-xm-10">	
				<ul class="nav nav-pills pull-right">
				  <li <?php if($this->data['currentlink'] == 'home') { echo ' class="active"'; }?>><a href="<?php echo base_url('index.php/home'); ?>">Home</a></li>
				</ul>				
			</div>	
		</div>
	</div>
	<div class="row-fluid">
		<div class="col-md-12 col-xm-12">
			<?php $this->load->view('partials/' . $content); ?>
		</div>
	</div>
</div>
<?php $this->load->view('include/footer'); ?>
