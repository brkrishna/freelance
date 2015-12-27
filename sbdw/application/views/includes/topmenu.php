<?php
defined('BASEPATH') OR exit('No direct script access allowed');
?>
    <?php 
        $uri_segment = 'Home';
        if($this->uri->segment(1) != ''){
            $uri_segment = $this->uri->segment(1); 
        }
    ?>
<body class="background">
    <div class="container-fluid">
        <div class="row">
            <nav class="navbar navbar-default navbar-custom">
                <div class="container">
                    <div class="row">
                        <div class="col-md-3">
                            <div class="navbar-header">
                                <a href="<?php echo base_url("/index.php/Home/index"); ?>"><img src="<?php echo base_url('public/imgs/sristibio.png'); ?>" alt="Sristi Biosciences"></a>
                            </div>
                        </div>
                        <div class="col-md-9">
                            <ul class="nav navbar-nav pull-right">
                                <li class="<?=$uri_segment === 'Home' ? 'active':''; ?>"><a href="<?php echo base_url("/index.php/Home/index"); ?>"><span class="glyphicon glyphicon-home">&nbsp;</span>Home</a></li>
                                <li class="<?=$uri_segment === 'AboutUs' ? 'active':''; ?>"><a href="<?php echo base_url("/index.php/AboutUs/index"); ?>">About Us</a></li>
                                <li class="<?=$uri_segment === 'NP' ? 'active':''; ?>"><a href="<?php echo base_url("/index.php/NP/index"); ?>">Natural Products</a></li>
                                <li class="<?=$uri_segment === 'DS' ? 'active':''; ?>"><a href="<?php echo base_url("/index.php/DS/index"); ?>">Discovery Services</a></li>
                                <li class="<?=$uri_segment === 'CP' ? 'active':''; ?>"><a href="<?php echo base_url("/index.php/CP/index"); ?>">Cell Products</a></li>
                                <li class="<?=$uri_segment === 'Contactus' ? 'active':''; ?>"><a href="<?php echo base_url('/index.php/Contactus/index'); ?>"><span class="glyphicon glyphicon-envelope"></span>&nbsp;Contact Us</a></li>
                            </ul>                     
                        </div>
                    </div>
                </div>
            </nav>
        </div>





