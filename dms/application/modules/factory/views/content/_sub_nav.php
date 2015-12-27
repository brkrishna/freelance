<ul class="nav nav-pills">
	<li <?php echo $this->uri->segment(4) == '' ? 'class="active"' : '' ?>>
		<a href="<?php echo site_url(SITE_AREA .'/content/factory') ?>" id="list"><?php echo lang('factory_list'); ?></a>
	</li>
	<?php if ($this->auth->has_permission('Factory.Content.Create')) : ?>
	<li <?php echo $this->uri->segment(4) == 'create' ? 'class="active"' : '' ?> >
		<a href="<?php echo site_url(SITE_AREA .'/content/factory/create') ?>" id="create_new"><?php echo lang('factory_new'); ?></a>
	</li>
	<?php endif; ?>
</ul>