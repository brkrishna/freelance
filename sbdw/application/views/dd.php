<?php
defined('BASEPATH') OR exit('No direct script access allowed');

$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');

?>
    <div class="row">
        <div class="col-xs-9 col-md-9 left">
            <br/>
            <img class="img-thumbnail" src="<?php echo base_url('/public/imgs/dd_overview.jpg'); ?>">         
        </div>
        <div class="col-xs-3 col-md-3 right">
            <br/>
            <nav class="leftmenu">
                <ul class="nav nav-pills nav-stacked">
                    <li class="active"><a href="<?php echo base_url("/index.php/Dd/index"); ?>">Overview</a></li>
                    <li class=""><a class="" href="<?php echo base_url("/index.php/Dd/index/board"); ?>">Board</a></li>
                    <li class=""><a class="" href="<?php echo base_url("/index.php/Dd/index/ds"); ?>">Discovery Services</a></li>
                    <li class=""><a class="" href="<?php echo base_url("/index.php/Dd/index/rp"); ?>">Research Products</a></li>
                    <li class=""><a class="" href="<?php echo base_url("/index.php/Dd/index"); ?>">R &amp; D</a></li>
                </ul>
            </nav>
        </div>
        <div class="col-xs-9 col-md-9 left">
           <br/><br/>
           <h4>
            Drug discovery process is often time consuming & incurs steady and significant R&D spend with extremely high failure rates. 
            The biggest challenge of the industry is to translate the research outcomes into tangible medicines in a cost and 
            time-effective way
            <br/><br/>
            The major advantage of our collaborative discovery services is that it helps clients in choosing the best targets 
            to work on there by accelarating speed and productivity for clients</h4>                  
        </div>
        <div class="col-xs-3 col-md-3 right">
            <div class="panel panel-default">
                <div class="panel-heading">
                    <h3 class="panel-title">Quick Summary</h3>
                </div>
                <div class="panel-body">
                    <ul>
                        <li>15 libraries with over a million small molecules available for subscription</li>
                        <li>Human and Rat liver 3D Microtissues</li>
                        <li>Cells, tissues, growth factors, reagents and media</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
<?php
    $this->load->view('/includes/footer');
?>