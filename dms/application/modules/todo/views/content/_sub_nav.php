<ul class="nav nav-pills">
	<li <?php echo $this->uri->segment(4) == '' ? 'class="active"' : '' ?>>
		<a href="<?php echo site_url(SITE_AREA .'/content/todo') ?>" id="list"><?php echo lang('todo_list'); ?></a>
	</li>
	<?php if ($this->auth->has_permission('Todo.Content.Create')) : ?>
	<li <?php echo $this->uri->segment(4) == 'create' ? 'class="active"' : '' ?> >
		<a href="<?php echo site_url(SITE_AREA .'/content/todo/create') ?>" id="create_new"><?php echo lang('todo_new'); ?></a>
	</li>
	<?php endif; ?>
</ul>