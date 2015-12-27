<?php
defined('BASEPATH') OR exit('No direct script access allowed');

$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');

?>
    <div class="row">
        <div class="col-md-9 col-sm-6">
            <br/>
            <table class="table table-bordered">
                <tr>
                    <td><h4>Research Analytics Services</h4></td>
                    <td></td>
                </tr>
                <tr>
                    <td><h4>Analytical Services</h4></td>
                    <td></td>
                </tr>
                <tr>
                    <td><h4>Extract to Leads</h4></td>
                    <td></td>
                </tr>
                <tr>
                    <td><h4>Screening Services</h4></td>
                    <td></td>
                </tr>
            </table>
        </div>
        <div class="col-md-3 pull-right">
            <br/>
            <nav class="leftmenu">
                <ul class="nav nav-pills nav-stacked">
                    <li class=""><a href="<?php echo base_url("/index.php/Dd/index"); ?>">Overview</a></li>
                    <li class=""><a class="" href="<?php echo base_url("/index.php/Dd/index/board"); ?>">Board</a></li>
                    <li class="active"><a class="" href="<?php echo base_url("/index.php/Dd/index/ds"); ?>">Discovery Services</a></li>
                    <li class=""><a class="" href="<?php echo base_url("/index.php/Dd/index/rp"); ?>">Research Products</a></li>
                    <li class=""><a class="" href="<?php echo base_url("/index.php/Dd/index"); ?>">R &amp; D</a></li>
                </ul>
            </nav>
        </div>
    </div>
    <!--
    <hr/>
    <div class="row">
        <div class="col-md-4 col-sm-6">
            <div class="panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title">Decision Centric Research Intelligence</h2>
                </div>
                <div class="panel-body">
                    A platform to enable faster decisions by mining data for <strong>Information</strong> which helps in taking decions...<a href="#">more</a>
                </div>
            </div>
        </div>
        <div class="col-md-4 col-sm-6">
            <div class="panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title">Screening</h2>
                </div>
                <div class="panel-body">
                    Screening is an approach to chemical synthesis that enables the creation of large numbers of organic compounds by linking chemical...<a href="#">more</a>
                </div>
            </div>
        </div>
        <div class="col-md-4 col-sm-6">
            <div class="panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title">Discovery Biology</h2>
                </div>
                <div class="panel-body">
                    We aim at translating discovery into treatment that benefits people with diabetes or those at risk by accumulating molecular libraries...<a href="#">more</a>
                </div>
            </div>
        </div>
        <div class="col-md-4 col-sm-6">
            <div class="panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title">Program Management</h2>
                </div>
                <div class="panel-body">
                    We aim at translating discovery into treatment that benefits people with diabetes or those at risk by accumulating molecular libraries...<a href="#">more</a>
                </div>
            </div>
        </div>
    </div>-->
    
<?php
    $this->load->view('/includes/footer');
?>