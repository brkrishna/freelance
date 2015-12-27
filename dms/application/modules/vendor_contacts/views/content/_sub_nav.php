<ul class="nav nav-pills">
	<li <?php echo $this->uri->segment(4) == '' ? 'class="active"' : '' ?>>
		<a href="<?php echo site_url(SITE_AREA .'/content/vendor_contacts') ?>" id="list"><?php echo lang('vendor_contacts_list'); ?></a>
	</li>
	<?php if ($this->auth->has_permission('Vendor_Contacts.Content.Create')) : ?>
	<li <?php echo $this->uri->segment(4) == 'create' ? 'class="active"' : '' ?> >
		<a href="<?php echo site_url(SITE_AREA .'/content/vendor_contacts/create') ?>" id="create_new"><?php echo lang('vendor_contacts_new'); ?></a>
	</li>
	<?php endif; ?>
</ul>