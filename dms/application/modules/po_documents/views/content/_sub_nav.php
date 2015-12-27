<ul class="nav nav-pills">
	<li <?php echo $this->uri->segment(4) == '' ? 'class="active"' : '' ?>>
		<a href="<?php echo site_url(SITE_AREA .'/content/po_documents') ?>" id="list"><?php echo lang('po_documents_list'); ?></a>
	</li>
	<?php if ($this->auth->has_permission('PO_Documents.Content.Create')) : ?>
	<li <?php echo $this->uri->segment(4) == 'create' ? 'class="active"' : '' ?> >
		<a href="<?php echo site_url(SITE_AREA .'/content/po_documents/create') ?>" id="create_new"><?php echo lang('po_documents_new'); ?></a>
	</li>
	<?php endif; ?>
</ul>