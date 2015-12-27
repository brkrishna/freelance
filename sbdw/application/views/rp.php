<?php
defined('BASEPATH') OR exit('No direct script access allowed');

$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');

?>
    <div class="row">
        <div class="col-md-9 col-sm-6">
            <br/>
            <div class="panel panel-default">
                <div class="panel-heading">
                    <h3 class="panel-title">Research Products</h3>
                </div>
                <div class="panel-body">
                    <div class="col-md-12">
                        <div class="panel panel-success">
                            <div class="panel-heading">
                                <h3 class="panel-title"><a href="<?php echo base_url("/index.php/Dd/index/npl"); ?>"><span class="glyphicon glyphicon-list" aria-hidden="true"></span>&nbsp;Natural Products Library</a></h3>        
                            </div>
                            <div class="panel-body">
                                A natural choice for health and nutritional issues
                                <br/><br/>
                                <a href="<?php echo base_url('/index.php/Dd/molecules/botan'); ?>">
                                <div class="col-md-3 prod_list">
                                    <br/>
                                    <span class="glyphicon glyphicon-tag"></span>&nbsp;Botanicule
                                    <hr/>
                                    <p class="text-center">Exploring novelty space in Botanicals</p>
                                </div>
                                </a>
                                <div class="col-md-3 prod_list">
                                    <br/>
                                    <span class="glyphicon glyphicon-tag"></span>&nbsp;<a href="<?php echo base_url('/index.php/Dd/molecules/micro'); ?>">Microbicule</a>
                                    <hr/>
                                    <p class="text-center">Swimming the aquatic chemical diversity space</p>
                                </div>
                                <div class="col-md-4 prod_list">
                                    <br/>
                                    <span class="glyphicon glyphicon-tag"></span>&nbsp;<a href="<?php echo base_url('/index.php/Dd/molecules/marine'); ?>">Marinicule</a>
                                    <hr/>
                                    <p class="text-center">Investigating microbes as production systems and novelty source</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-12">
                        <div class="panel panel-primary">
                            <div class="panel-heading">
                                <h3 class="panel-title"><a href="<?php echo base_url("/index.php/Products/product/cells"); ?>"><span class="glyphicon glyphicon-list" aria-hidden="true"></span>&nbsp;Cell Products</a></h3>        
                            </div>
                            <div class="panel-body">
                                We provide ideal cell systems to establish cell cultures
                                <br/><br/>
                                <div class="col-md-3 prod_list">
                                    <br/>
                                    <span class="glyphicon glyphicon-tag"></span>&nbsp;<a href="<?php echo base_url('/index.php/Products/product/cells'); ?>">Cells</a>
                                </div>
                                <div class="col-md-3 prod_list">
                                    <br/>
                                    <span class="glyphicon glyphicon-tag"></span>&nbsp;<a href="<?php echo base_url('/index.php/Products/product/reagents'); ?>">Reagents</a>
                                </div>
                                <div class="col-md-3 prod_list">
                                    <br/>
                                    <span class="glyphicon glyphicon-tag"></span>&nbsp;<a href="<?php echo base_url('/index.php/Products/product/media'); ?>">Media</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-12">
                        <div class="panel panel-warning">
                            <div class="panel-heading">
                                <h3 class="panel-title"><a href="<?php echo base_url("/index.php/Tissues/tissue/liver"); ?>"><span class="glyphicon glyphicon-list" aria-hidden="true"></span>&nbsp;Micro Tissues</a></h3>        
                            </div>
                            <div class="panel-body">
                                Micro Tissues
                                <br/><br/>
                                <div class="col-md-3 prod_list">
                                    <br/>
                                    <span class="glyphicon glyphicon-tag"></span>&nbsp;<a href="<?php echo base_url('/index.php/Tissues/tissue/liver'); ?>">Liver</a>
                                    <hr/>
                                    <p class="text-center">Human and Rat liver 3D Microtissues</p>
                                </div>
                                <div class="col-md-3 prod_list">
                                    <br/>
                                    <span class="glyphicon glyphicon-tag"></span>&nbsp;<a href="<?php echo base_url('/index.php/Tissues/tissue/tumor'); ?>">Tumor</a>
                                    <hr/>
                                    <p class="text-center">Human Kidney carcinoma Microtissues</p>
                                </div>
                                <div class="col-md-4 prod_list">
                                    <br/>
                                    <span class="glyphicon glyphicon-tag"></span>&nbsp;<a href="<?php echo base_url('/index.php/Tissues/tissue/livertoxicology'); ?>">Liver Toxicology</a>
                                    <hr/>
                                    <p class="text-center">Liver Toxicology Service Packs</p>
                                </div>
                                <div class="col-md-3 prod_list">
                                    <br/>
                                    <span class="glyphicon glyphicon-tag"></span>&nbsp;<a href="<?php echo base_url('/index.php/Tissues/tissue/stemcells'); ?>">Stem Cells</a>
                                    <hr/>
                                    <p class="text-center">Embryonic Stem-Cell Test Service Pack</p>
                                </div>
                                <div class="col-md-3 prod_list">
                                    <br/>
                                    <span class="glyphicon glyphicon-tag"></span>&nbsp;<a href="<?php echo base_url('/index.php/Tissues/tissue/oncology'); ?>">Oncology</a>
                                    <hr/>
                                    <p class="text-center">Oncology Service Packs</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-12">
                        <div class="panel panel-danger">
                            <div class="panel-heading">
                                <h3 class="panel-title"><a href="<?php echo base_url("/index.php/Bioresearch/bio/bonemarrow"); ?>"><span class="glyphicon glyphicon-list" aria-hidden="true"></span>&nbsp;Blood Cells</a></h3>        
                            </div>
                            <div class="panel-body">
                                Blood Cells
                                <br/><br/>
                                <div class="col-md-3 prod_list">
                                    <br/>
                                    <span class="glyphicon glyphicon-tag"></span>&nbsp;<a href="<?php echo base_url('/index.php/Bioresearch/bio/bonemarrow'); ?>">Bone Marrow</a>
                                </div>
                                <div class="col-md-3 prod_list">
                                    <br/>
                                    <span class="glyphicon glyphicon-tag"></span>&nbsp;<a href="<?php echo base_url('/index.php/Bioresearch/bio/cordblood'); ?>">Cord Blood</a>
                                </div>
                                <div class="col-md-3 prod_list">
                                    <br/>
                                    <span class="glyphicon glyphicon-tag"></span>&nbsp;<a href="<?php echo base_url('/index.php/Bioresearch/bio/mobilizedperipheral'); ?>">Mobilized Peripheral</a>
                                </div>
                                <div class="col-md-3 prod_list">
                                    <br/>
                                    <span class="glyphicon glyphicon-tag"></span>&nbsp;<a href="<?php echo base_url('/index.php/Bioresearch/bio/diseasedstate'); ?>">Diseased State</a>
                                </div>
                                <div class="col-md-3 prod_list">
                                    <br/>
                                    <span class="glyphicon glyphicon-tag"></span>&nbsp;<a href="<?php echo base_url('/index.php/Bioresearch/bio/tissueslides'); ?>">Tissue Slides</a>
                                </div>
                                <div class="col-md-3 prod_list">
                                    <br/>
                                    <span class="glyphicon glyphicon-tag"></span>&nbsp;<a href="<?php echo base_url('/index.php/Bioresearch/bio/biopreservationmedia'); ?>">Bio Preservation Media</a>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!--<table class="table table-bordered">
                <tr>
                    <td><a href="<?php echo base_url("/index.php/Dd/index/npl"); ?>"><h3>Natural Products Library</h3></a></td>
                    <td>
                        <p>A natural choice for health and nutritional issues</p>
                        </td>
                </tr>
                <tr>
                    <td><a href="<?php echo base_url("/index.php/Products/product/cells"); ?>">Cell Products</a></td>
                    <td>We provide ideal cell systems to establish cell cultures</td>
                </tr>
                <tr>
                    <td><a href="<?php echo base_url("/index.php/Tissues/tissue/liver"); ?>">Micro Tissues</a></td>
                    <td></td>
                </tr>
                <tr>
                    <td><a href="<?php echo base_url("/index.php/Bioresearch/bio/bonemarrow"); ?>">Blood Cells</a></td>
                    <td></td>
                </tr>
            </table>-->
        </div>
        <div class="col-md-3 pull-right">
            <br/>
            <nav class="leftmenu">
                <ul class="nav nav-pills nav-stacked">
                    <li class=""><a href="<?php echo base_url("/index.php/Dd/index"); ?>">Overview</a></li>
                    <li class=""><a class="" href="<?php echo base_url("/index.php/Dd/index/board"); ?>">Board</a></li>
                    <li class=""><a class="" href="<?php echo base_url("/index.php/Dd/index/ds"); ?>">Discovery Services</a></li>
                    <li class="active"><a class="" href="<?php echo base_url("/index.php/Dd/index/rp"); ?>">Research Products</a></li>
                    <li class=""><a class="" href="<?php echo base_url("/index.php/Dd/index"); ?>">R &amp; D</a></li>
                </ul>
            </nav>
        </div>
        
    </div>
<!--
    <hr/>
    <div class="row">
        <div class="col-md-2 col-sm-6">
            
        </div>
        <div class="col-md-3 col-sm-6">
            <div class="panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title">Natural Products Library</h2>
                </div>
                <div class="panel-body">
                    A natural choice for health and nutritional issues...<a href="<?php echo base_url("/index.php/Dd/index/npl"); ?>">more</a>
                </div>
            </div>
        </div>
        <div class="col-md-3 col-sm-6">
            <div class="panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title">Disease Biology</h2>
                </div>
                <div class="panel-body">
                    Targets with crystalstructure demanding a set of relevant scored...<a href="<?php echo base_url('/index.php/Tissues/tissue/microtissues'); ?>">more</a>
                </div>
            </div>
        </div>
        <div class="col-md-3 col-sm-6">
            <div class="panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title">Cells</h2>
                </div>
                <div class="panel-body">
                    We provide an ideal cell systems to establish cell cultures...<a href="<?php echo base_url("/index.php/Products/product/cells"); ?>">more</a>
                </div>
            </div>
        </div>
        <div class="col-md-1 col-sm-6">
            
        </div>
    </div>
    <div class="row">
        <div class="col-md-2 col-sm-6">
            
        </div>
        <div class="col-md-3 col-sm-6">
            <div class="panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title">Reagents</h2>
                </div>
                <div class="panel-body">
                    A variety of quality cell culture reagents, supplements...<a href="<?php echo base_url("/index.php/Products/product/reagents"); ?>">more</a>
                </div>
            </div>
        </div>
        <div class="col-md-3 col-sm-6">
            <div class="panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title">Micro Tissues</h2>
                </div>
                <div class="panel-body">
                    A variety of quality cell culture reagents, supplements...<a href="<?php echo base_url("/index.php/Tissues/tissue/liver"); ?>">more</a>
                </div>
            </div>
        </div>
        <div class="col-md-3 col-sm-6">
            <div class="panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title">Blood Cells</h2>
                </div>
                <div class="panel-body">
                    A variety of quality cell culture reagents, supplements...<a href="<?php echo base_url("/index.php/Bioresearch/bio/bonemarrow"); ?>">more</a>
                </div>
            </div>
        </div>
        <div class="col-md-1 col-sm-6">
        </div>
    </div>
    <div class="row">
        <div class="col-md-2 col-sm-6">
            
        </div>
        <div class="col-md-3 col-sm-6">
            <div class="panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title">Blooder Cells</h2>
                </div>
                <div class="panel-body">
                    A variety of quality cell culture reagents, supplements...<a href="<?php echo base_url("/index.php/Products/product/reagents"); ?>">more</a>
                </div>
            </div>
        </div>
    </div>
-->
<?php
    $this->load->view('/includes/footer');
?>