<?php
defined('BASEPATH') OR exit('No direct script access allowed');

$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');

?>
<br/>
<div class="row">
    <div class="col-md-3 col-sm-3">
        <br/>
        <table class="table table-bordered">
            <tr><td><img src="<?php echo base_url('/public/imgs/person.png'); ?>"/></td></tr>
            <tr><td>Jayaraman Packirisamy</td></tr>
            <tr><td>Driving business with technology management expertise</td></tr>
        </table>        
    </div>
    <div class="col-md-3 col-sm-3">
        <br/>
        <table class="table table-bordered">
            <tr><td><img src="<?php echo base_url('/public/imgs/person.png'); ?>"/></td></tr>
            <tr><td>Sudhir Reddy</td></tr>
            <tr><td>Practitioner driving clinical principles</td></tr>
        </table>        
    </div>
    <div class="col-md-3 col-sm-3">
        <br/>
        <table class="table table-condensed table-bordered">
            <tr><td><img src="<?php echo base_url('/public/imgs/person.png'); ?>"/></td></tr>
            <tr><td>Rajendran A</td></tr>
            <tr><td>Exploring chemical diversity space</td></tr>
        </table>        
    </div>
    <div class="col-md-3 pull-right">
        <br/>
        <nav class="leftmenu">
            <ul class="nav nav-pills nav-stacked">
                <li class=""><a href="<?php echo base_url("/index.php/Dd/index"); ?>">Overview</a></li>
                <li class="active"><a class="" href="<?php echo base_url("/index.php/Dd/index/board"); ?>">Board</a></li>
                <li class=""><a class="" href="<?php echo base_url("/index.php/Dd/index/ds"); ?>">Discovery Services</a></li>
                <li class=""><a class="" href="<?php echo base_url("/index.php/Dd/index/rp"); ?>">Research Products</a></li>
                <li class=""><a class="" href="<?php echo base_url("/index.php/Dd/index"); ?>">R &amp; D</a></li>
            </ul>
        </nav>
    </div>
</div>
<div class="row">
    <div class="col-md-3 col-sm-3">
        <br/>
        <table class="table table-condensed table-bordered">
            <tr><td><img src="<?php echo base_url('/public/imgs/person.png'); ?>"/></td></tr>
            <tr><td>K R K Reddy</td></tr>
            <tr><td>Driving microbes as production systems, a manufacturing</td></tr>
        </table>        
    </div>
    <div class="col-md-3 col-sm-3">
        <br/>
        <table class="table table-condensed table-bordered">
            <tr><td><img src="<?php echo base_url('/public/imgs/person.png'); ?>"/></td></tr>
            <tr><td>Seeram Ramakrishna</td></tr>
            <tr><td>Nano delivery and process</td></tr>
        </table>        
    </div>
</div>
<hr/>

<?php
    $this->load->view('/includes/footer');
?>