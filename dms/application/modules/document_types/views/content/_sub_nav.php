<ul class="nav nav-pills">
	<li <?php echo $this->uri->segment(4) == '' ? 'class="active"' : '' ?>>
		<a href="<?php echo site_url(SITE_AREA .'/content/document_types') ?>" id="list"><?php echo lang('document_types_list'); ?></a>
	</li>
	<?php if ($this->auth->has_permission('Document_Types.Content.Create')) : ?>
	<li <?php echo $this->uri->segment(4) == 'create' ? 'class="active"' : '' ?> >
		<a href="<?php echo site_url(SITE_AREA .'/content/document_types/create') ?>" id="create_new"><?php echo lang('document_types_new'); ?></a>
	</li>
	<?php endif; ?>
</ul>