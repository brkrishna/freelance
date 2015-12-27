<ul class="nav nav-pills">
	<li <?php echo $this->uri->segment(4) == '' ? 'class="active"' : '' ?>>
		<a href="<?php echo site_url(SITE_AREA .'/reports/sample_documents') ?>" id="list"><?php echo lang('sample_documents_list'); ?></a>
	</li>
	<?php if ($this->auth->has_permission('Sample_Documents.Reports.Create')) : ?>
	<li <?php echo $this->uri->segment(4) == 'create' ? 'class="active"' : '' ?> >
		<a href="<?php echo site_url(SITE_AREA .'/reports/sample_documents/create') ?>" id="create_new"><?php echo lang('sample_documents_new'); ?></a>
	</li>
	<?php endif; ?>
</ul>