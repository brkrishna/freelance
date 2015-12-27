<div>
	<div class="col-md-4">
		<form role="form">
		  <div class="form-group">
		    <label for="name">Name&nbsp;*</label>
		    <input type="text" class="form-control" id="name" placeholder="Enter Name">
		  </div>	
		  <div class="form-group">
		    <label for="email">Email address</label>
		    <input type="email" class="form-control" id="email" placeholder="Enter email">
		  </div>	  
		  <div class="form-group">
		    <label for="org">Organization</label>
		    <textarea type="text" rows="3" class="form-control" id="org" placeholder="Enter Organization"></textarea>
		  </div>	
		  <button type="submit" class="btn btn-default">Start</button>
		</form>
		<br/>
		<?php if ($message != '') { echo '<div class="alert alert-success">' . $message . '</div>'; } ?>
		<br/>
		<?php echo form_close(); ?>
		<br/>
		<?php if (validation_errors() == True) { echo '<div class="alert alert-danger">' . validation_errors() . '</div>'; } ?></h4>
	</div>
</div>