<ul class="nav nav-pills">
	<li <?php echo $this->uri->segment(4) == '' ? 'class="active"' : '' ?>>
		<a href="<?php echo site_url(SITE_AREA .'/content/activity_type') ?>" id="list"><?php echo lang('activity_type_list'); ?></a>
	</li>
	<?php if ($this->auth->has_permission('Activity_Type.Content.Create')) : ?>
	<li <?php echo $this->uri->segment(4) == 'create' ? 'class="active"' : '' ?> >
		<a href="<?php echo site_url(SITE_AREA .'/content/activity_type/create') ?>" id="create_new"><?php echo lang('activity_type_new'); ?></a>
	</li>
	<?php endif; ?>
</ul>