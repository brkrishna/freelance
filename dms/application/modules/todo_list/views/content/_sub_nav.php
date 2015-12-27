<ul class="nav nav-pills">
	<li <?php echo $this->uri->segment(4) == '' ? 'class="active"' : '' ?>>
		<a href="<?php echo site_url(SITE_AREA .'/content/todo_list') ?>" id="list"><?php echo lang('todo_list_list'); ?></a>
	</li>
	<?php if ($this->auth->has_permission('Todo_List.Content.Create')) : ?>
	<li <?php echo $this->uri->segment(4) == 'create' ? 'class="active"' : '' ?> >
		<a href="<?php echo site_url(SITE_AREA .'/content/todo_list/create') ?>" id="create_new"><?php echo lang('todo_list_new'); ?></a>
	</li>
	<?php endif; ?>
</ul>