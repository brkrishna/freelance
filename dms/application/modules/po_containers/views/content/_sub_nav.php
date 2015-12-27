<ul class="nav nav-pills">
	<li <?php echo $this->uri->segment(4) == '' ? 'class="active"' : '' ?>>
		<a href="<?php echo site_url(SITE_AREA .'/content/po_containers') ?>" id="list"><?php echo lang('po_containers_list'); ?></a>
	</li>
	<?php if ($this->auth->has_permission('PO_Containers.Content.Create')) : ?>
	<li <?php echo $this->uri->segment(4) == 'create' ? 'class="active"' : '' ?> >
		<a href="<?php echo site_url(SITE_AREA .'/content/po_containers/create') ?>" id="create_new"><?php echo lang('po_containers_new'); ?></a>
	</li>
	<?php endif; ?>
</ul>