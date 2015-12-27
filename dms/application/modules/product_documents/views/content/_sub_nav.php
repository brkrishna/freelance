<ul class="nav nav-pills">
	<li <?php echo $this->uri->segment(4) == '' ? 'class="active"' : '' ?>>
		<a href="<?php echo site_url(SITE_AREA .'/content/product_documents') ?>" id="list"><?php echo lang('product_documents_list'); ?></a>
	</li>
	<?php if ($this->auth->has_permission('Product_Documents.Content.Create')) : ?>
	<li <?php echo $this->uri->segment(4) == 'create' ? 'class="active"' : '' ?> >
		<a href="<?php echo site_url(SITE_AREA .'/content/product_documents/create') ?>" id="create_new"><?php echo lang('product_documents_new'); ?></a>
	</li>
	<?php endif; ?>
</ul>