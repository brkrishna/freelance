<ul class="nav nav-pills">
	<li <?php echo $this->uri->segment(4) == '' ? 'class="active"' : '' ?>>
		<a href="<?php echo site_url(SITE_AREA .'/content/po_fulfillment') ?>" id="list"><?php echo lang('po_fulfillment_list'); ?></a>
	</li>
	<?php if ($this->auth->has_permission('PO_Fulfillment.Content.Create')) : ?>
	<li <?php echo $this->uri->segment(4) == 'create' ? 'class="active"' : '' ?> >
		<a href="<?php echo site_url(SITE_AREA .'/content/po_fulfillment/create') ?>" id="create_new"><?php echo lang('po_fulfillment_new'); ?></a>
	</li>
	<?php endif; ?>
</ul>