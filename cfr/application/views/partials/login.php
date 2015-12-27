<?php $attr = array('class' => 'form-horizontal',); ?>
<?php echo form_open('login/input', $attr); ?>
<div class="col-md-6">
	<div>
		<fieldset>
			<legend>Login</legend>
			<div class="control-group">
				<label for="title">User name</label>
				<div class="controls">
					<?php echo form_input($results['f_user_name']); ?>
				</div>
			</div>
			<br/>
			<div class="control-group">
				<label for="title">Password</label>
				<div class="controls">
					<?php echo form_password($results['f_password']); ?>
				</div>					
			</div>
			<br/>
			<div class="control-group">
				<div class="controls">
					<?php echo form_button($results['b_submit']);  ?>
				</div>					
			</div>
			<br/>
			<div class="control-group">
				<div class="controls">
					<?php echo anchor(base_url('index.php/fp'), 'Forgot Password') ?>
				</div>					
			</div>
		</fieldset>
	</div>
	<div>
		<br/>
		<?php if ($message != '') { echo '<div class="alert alert-success">' . $message . '</div>'; } ?>
		<br/>
		<?php echo form_close(); ?>
		<br/>
		<?php if (validation_errors() == True) { echo '<div class="alert alert-danger">' . validation_errors() . '</div>'; } ?>
	<div>
	</div>
</div>
	
