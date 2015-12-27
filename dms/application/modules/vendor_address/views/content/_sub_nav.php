<ul class="nav nav-pills">
	<li <?php echo $this->uri->segment(4) == '' ? 'class="active"' : '' ?>>
		<a href="<?php echo site_url(SITE_AREA .'/content/vendor_address') ?>" id="list"><?php echo lang('vendor_address_list'); ?></a>
	</li>
	<?php if ($this->auth->has_permission('Vendor_Address.Content.Create')) : ?>
	<li <?php echo $this->uri->segment(4) == 'create' ? 'class="active"' : '' ?> >
		<a href="<?php echo site_url(SITE_AREA .'/content/vendor_address/create') ?>" id="create_new"><?php echo lang('vendor_address_new'); ?></a>
	</li>
	<?php endif; ?>
</ul>