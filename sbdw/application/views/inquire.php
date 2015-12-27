<?php
defined('BASEPATH') OR exit('No direct script access allowed');

$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');

?>
<div class="row">
    <div class="col-md-6 col-sm-8">
        <div class="service">
            <?php if ($this->session->flashdata('msg') != '') : ?>
            <div class="alert alert-info alert-dismissible" role="alert">
                <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <strong><?=$this->session->flashdata('msg'); ?></strong> 
            </div>                    
            <?php endif; ?>
            <h3>Product / Service Inquiry</h3>
            <p class="text-justify">
                Please drop us a line indicating the products you are interested in and we will get back to you shortly
            </p>
            <hr/>    
            <form class="form-inline" method="POST" action="<?php echo base_url('/index.php/Contactus/inquire'); ?>" id="contactus" name="contactus">
                <div class="form-group <?=(null != form_error('c_name')?'has-error':''); ?>">
                    <input type="text" name="c_name" id="c_name" placeholder="Name..." class="form-control" title="Please enter your name"/>        
                </div>
                <br/><br/>
                <div class="form-group <?=(null != form_error('c_email')?'has-error':''); ?>">
                    <input type="text" name="c_email" id="c_email" placeholder="Email..." class="form-control" title="Please enter your email address"/>    
                </div>
                <br/><br/>
                <div class="form-group">
                    <input type="text" name="c_phone" id="c_phone" placeholder="Phone..." class="form-control" title="Please enter your contact number"/>    
                </div>
                <br/><br/>
                <div class="form-group">
                    <label>Subject</label>
                    <input type="text" name="c_subject" id="c_subject" placeholder="Subject..." class="form-control" style="width:150%;" title="Please enter the subject" value="Interested in <?php echo set_value('c_subject', isset($subject) ? $subject : 'General inquiry'); ?>" />    
                </div>
                <hr/>
                <div class="form-group <?=(null != form_error('c_notes')?'has-error':''); ?>">
                    <textarea name="c_notes" id="c_notes" placeholder="Notes..." class="form-control" rows="8" cols="40" title="Please enter your comments / queries / feedback / questions..."></textarea>
                </div>
                <hr/>
                <input type="submit" class="btn btn-primary" value="Submit" class="form-control"/>
            </form>
        </div>
    </div>
     <div class="col-md-6 col-sm-8">
        <p class="text-center" style="margin-top:200px;">
            <address>
              <strong><h1>Sristi Biosciences Private Limited</h1></strong><br>
              104, Susthiralok Complex, <br>
              Kothapet, Hyderabad - 500 060<br>
              <abbr title="Phone">P:</abbr> +91-40-6579 4668, 2404 5551
              <abbr title="Fax">F:</abbr> +91-40-2404 5552
            </address>
        </p>
     </div>
</div>

<?php
    $this->load->view('/includes/footer');
?>