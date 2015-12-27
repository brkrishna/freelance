<div class="jumbotron" text-align="center">
	<h1>Document Management System</h1>
	<br/>
	<?php if (isset($current_user->email)) : ?>
		<a href="<?php echo site_url(SITE_AREA) ?>" class="btn btn-large btn-success">Go to Dashboard</a>
	<?php else :?>
		<a href="<?php echo site_url(LOGIN_URL); ?>" class="btn btn-large btn-primary"><?php echo lang('bf_action_login'); ?></a>
	<?php endif;?>

</div>

<hr />

<div class="row-fluid">

	<div class="span6">
		<h4>Documents</h4>

		<p>Helps in keeping track of documents related to Products</p>

	</div>

	<div class="span6">
	</div>
</div>

