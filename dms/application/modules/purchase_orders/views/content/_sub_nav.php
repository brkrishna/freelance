<ul class="nav nav-pills">
	<li <?php echo $this->uri->segment(4) == '' ? 'class="active"' : '' ?>>
		<a href="<?php echo site_url(SITE_AREA .'/content/purchase_orders') ?>" id="list"><?php echo lang('purchase_orders_list'); ?></a>
	</li>
	<?php if ($this->auth->has_permission('Purchase_Orders.Content.Create')) : ?>
	<li <?php echo $this->uri->segment(4) == 'create' ? 'class="active"' : '' ?> >
		<a href="<?php echo site_url(SITE_AREA .'/content/purchase_orders/create') ?>" id="create_new"><?php echo lang('purchase_orders_new'); ?></a>
	</li>
	<?php endif; ?>
</ul>