<ul class="nav nav-pills">
	<li <?php echo $this->uri->segment(4) == '' ? 'class="active"' : '' ?>>
		<a href="<?php echo site_url(SITE_AREA .'/content/vendors') ?>" id="list"><?php echo lang('vendors_list'); ?></a>
	</li>
	<?php if ($this->auth->has_permission('Vendors.Content.Create')) : ?>
	<li <?php echo $this->uri->segment(4) == 'create' ? 'class="active"' : '' ?> >
		<a href="<?php echo site_url(SITE_AREA .'/content/vendors/create') ?>" id="create_new"><?php echo lang('vendors_new'); ?></a>
	</li>
	<?php endif; ?>
</ul>