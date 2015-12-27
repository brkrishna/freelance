<ul class="nav nav-pills">
	<li <?php echo $this->uri->segment(4) == '' ? 'class="active"' : '' ?>>
		<a href="<?php echo site_url(SITE_AREA .'/content/activity_documents') ?>" id="list"><?php echo lang('activity_documents_list'); ?></a>
	</li>
	<?php if ($this->auth->has_permission('Activity_Documents.Content.Create')) : ?>
	<li <?php echo $this->uri->segment(4) == 'create' ? 'class="active"' : '' ?> >
		<a href="<?php echo site_url(SITE_AREA .'/content/activity_documents/create') ?>" id="create_new"><?php echo lang('activity_documents_new'); ?></a>
	</li>
	<?php endif; ?>
</ul>