<?php
defined('BASEPATH') OR exit('No direct script access allowed');

$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');
?>
    <div class="section">
        <div class="container">
        	<div class="row">
                <div class="col-md-3 col-sm-3"></div>
                <div class="col-md-6 col-sm-6">
                    <div class="service-wrapper">
                     <?php if ($this->session->flashdata('msg') != '') : ?>
                            <div class="alert <?=('Saved' == $this->session->flashdata('msg')) ? 'alert-success' : 'alert-warning'; ?> alert-dismissible" role="alert">
                              <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                              <strong><?=$this->session->flashdata('msg'); ?></strong> 
                            </div>                    
                        <?php endif; ?>
                        <h3>User Registration</h3>
                        <hr/>    
                       <form class="form-inline" method="POST" action="<?php echo base_url('/index.php/Users'); ?>" id="users" name="users">
                            <fieldset>
                                <div class="form-group <?=(null != form_error('name')?'has-error':''); ?>">
                                    <label for="name">Name</label><br/>
                                    <input type="text" name="name" id="name" value="<?php echo set_value('name'); ?>" placeholder="Name..." class="form-control" title="Please enter your name"/>        
                                </div>
                                <br/>
                                <div class="form-group <?=(null != form_error('desg')?'has-error':''); ?>">
                                    <label for="name">Designation</label><br/>
                                    <input type="text" name="desg" id="desg" value="<?php echo set_value('desg'); ?>" placeholder="Designation..." class="form-control" title="Please enter your designation"/>        
                                </div>
                                <br/>
                                <div class="form-group <?=(null != form_error('org')?'has-error':''); ?>">
                                    <label for="name">Organization</label><br/>
                                    <input type="text" name="org" id="org" value="<?php echo set_value('org'); ?>" placeholder="Organization..." class="form-control" title="Please enter your organization"/>        
                                </div>
                                <br/>
                                <div class="form-group <?=(null != form_error('contact_no')?'has-error':''); ?>">
                                    <label for="name">Contact No</label><br/>
                                    <input type="text" name="contact_no" id="contact_no" value="<?php echo set_value('contact_no'); ?>" placeholder="Contact No..." class="form-control" title="Please enter your contact no"/>        
                                </div>
                                <br/>
                                <div class="form-group">
                                    <label for="Email">Email</label><br/>
                                    <input type="text" name="email" id="email" value="<?php echo set_value('email'); ?>" placeholder="Email..." class="form-control"/>    
                                </div>
                                <br/>
                                <div class="form-group">
                                    <label for="Password">Password</label><br/>
                                    <input type="password" name="password" id="password" value="<?php echo set_value('password'); ?>" placeholder="Password..." class="form-control"/>    
                                </div>
                                <br/>
                                <div class="form-group">
                                    <label for="Confirm Password">Confirm Password</label><br/>
                                    <input type="password" name="confirm password" id="confirm password" value="<?php echo set_value('confirm_password'); ?>" placeholder="Confirm Password..." class="form-control"/>    
                                </div>
                                <hr/>
                                <input type="submit" class="btn btn-primary" value="Submit" class="form-control"/>
                                <input type="reset" class="btn btn-primary" name="Reset" value="Reset" class="form-control">
                            </fieldset>
                         </form>
                    </div>
                   <div class="col-md-3 col-sm-3"></div>
                </div>
            </div>
        </div>
     </div>
<?php
    $this->load->view('/includes/footer');
?>