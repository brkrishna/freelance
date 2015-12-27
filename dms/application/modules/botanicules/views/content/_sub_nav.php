<ul class="nav nav-pills">
	<li <?php echo $this->uri->segment(4) == '' ? 'class="active"' : '' ?>>
		<a href="<?php echo site_url(SITE_AREA .'/content/botanicules') ?>" id="list"><?php echo lang('botanicules_list'); ?></a>
	</li>
	<?php if ($this->auth->has_permission('Botanicules.Content.Create')) : ?>
	<li <?php echo $this->uri->segment(4) == 'create' ? 'class="active"' : '' ?> >
		<a href="<?php echo site_url(SITE_AREA .'/content/botanicules/create') ?>" id="create_new"><?php echo lang('botanicules_new'); ?></a>
	</li>
	<?php endif; ?>
</ul>