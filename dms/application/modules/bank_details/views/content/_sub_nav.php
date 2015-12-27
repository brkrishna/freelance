<ul class="nav nav-pills">
	<li <?php echo $this->uri->segment(4) == '' ? 'class="active"' : '' ?>>
		<a href="<?php echo site_url(SITE_AREA .'/content/bank_details') ?>" id="list"><?php echo lang('bank_details_list'); ?></a>
	</li>
	<?php if ($this->auth->has_permission('Bank_Details.Content.Create')) : ?>
	<li <?php echo $this->uri->segment(4) == 'create' ? 'class="active"' : '' ?> >
		<a href="<?php echo site_url(SITE_AREA .'/content/bank_details/create') ?>" id="create_new"><?php echo lang('bank_details_new'); ?></a>
	</li>
	<?php endif; ?>
</ul>