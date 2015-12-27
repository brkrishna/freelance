<div class="jumbotron" text-align="center">
	<h1>Sristi's Organic Handling Program</h1>

	<p class="lead">A Sristi Biosciences Internal Initiative</p>

	<?php if (isset($current_user->email)) : ?>
		<a href="<?php echo site_url(SITE_AREA) ?>" class="btn btn-large btn-success">Go to the Admin area</a>
	<?php else :?>
		<a href="<?php echo site_url(LOGIN_URL); ?>" class="btn btn-large btn-primary"><?php echo lang('bf_action_login'); ?></a>
	<?php endif;?>
</div>

<hr />

<div class="row-fluid">

	<div class="span6">
		<h4>Highlights</h4>

		<p>This portal helps Sristi track its vendors, products, organic certificates and acts as a single window repository</p>

	</div>

	<div class="span6">
		<h4>Role based access</h4>

		<p>We have configured this system to provide information, on need basis to various stakeholders</p>

	</div>
</div>

