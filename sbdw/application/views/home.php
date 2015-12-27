<?php
defined('BASEPATH') OR exit('No direct script access allowed');

$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');

?>
    <div class="row">
        <div id="carousel-home" class="carousel slide" data-ride="carousel">
            <!-- Indicators -->
            <ol class="carousel-indicators">
                <li data-target="#carousel-home" data-slide-to="0" class="active"></li>
                <li data-target="#carousel-home" data-slide-to="1"></li>
                <li data-target="#carousel-home" data-slide-to="2"></li>
            </ol>

            <!-- Wrapper for slides -->
            <div class="carousel-inner" role="listbox">
                <div class="item active">
                    <img src="<?php echo base_url('public/imgs/1_dd.jpg'); ?>" alt="Discovery" />
                    <div class="carousel-caption dd">
                        Drug discovery process is often time consuming &amp; incurs steady and significant R&amp;D spending with extremely high failure rates
                    </div>
                </div>
                <div class="item">
                    <img src="<?php echo base_url('public/imgs/1_ch.jpg'); ?>" alt="Consumer Healthcare" />
                    <div class="carousel-caption ch">
                        Consumer healthcare brings in OTC products which are natural formulations from our Discovery journey, helping in bringing healthcare products for everyone
                    </div>
                </div>
                <div class="item">
                    <img src="<?php echo base_url('public/imgs/1_ani.jpg'); ?>" alt="Active Natural Ingredients" />
                    <div class="carousel-caption ani">
                        Natural products offer a vast source of chemical diversity and yield unusual and unexpected lead structures
                    </div>
                </div>
               </div>   

            <!-- Controls -->
            <a class="left carousel-control" href="#carousel-home" role="button" data-slide="prev">
                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="right carousel-control" href="#carousel-home" role="button" data-slide="next">
                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>
        </div>
        <hr/>
    </div>
    <div class="row" style="background-color:#e0e0e0;">
        <br/><br/>
        <div class="col-md-4 col-sm-4">
            <div class="panel panel-default">
                <div class="panel-body">
                    <p class="text-center">
                    <img src="<?php echo base_url('public/imgs/natural_pro.gif'); ?>" alt="Natural Products"></p>
                    <hr/>
                    <p class="text-justify">
                        Plants and marine sources, Compound Libraries for screening, guided library design and synthesis, 
                        natural product formulations, and...
                        <div class="pull-right"><bold><a href="<?php echo base_url("/index.php/NP/index"); ?>">LEARN MORE</a></bold></div>
                    </p>
                </div>
            </div>
        </div>            
        <div class="col-md-4 col-sm-4">
            <div class="panel panel-default">
                <div class="panel-body">
                    <p class="text-center">
                    <img src="<?php echo base_url('public/imgs/discovery_ser.gif'); ?>" alt="Discovery Services"></p>
                    <hr/>
                    <p class="text-justify">
                        Decision Centric Research Intelligence (DCRI), Target Libraries, Virtual Screening, 
                        Medchem Program, data services and...                        
                        <div class="pull-right"><bold><a href="<?php echo base_url("/index.php/DS/index"); ?>">LEARN MORE</a></bold></div>
                    </p>
                </div>
            </div>
        </div>            
        <div class="col-md-4 col-sm-4">
            <div class="panel panel-default">
                <div class="panel-body">
                    <p class="text-center">
                    <img src="<?php echo base_url('public/imgs/cell_pro.gif'); ?>" alt="Cell Therapy"></p>
                    <hr/>
                    <p class="text-justify">
                        Clinical grade human cells for research, cell culture, contract manufacturing, therapeutic development and...
                        <div class="pull-right"><bold><a href="<?php echo base_url("/index.php/CP/index"); ?>">LEARN MORE</a></bold></div>
                    </p>
                </div>
            </div>
        </div>            
    </div>
    <hr/>
    <div class="row" style="background-color:#fff;">
        <br/><br/>
        <div class="col-md-2"></div>
        <div class="col-md-8 col-sm-8">
            <h4 class="text-justify">
                Sristi Biosciences is a next generation healthcare research company that focuses on unmet medical needs.
                <br/><br/>    
                Our research thrust is aimed at accommodating the transition of epidemiology alongside the technological break through for affordable and quality healthcare of common man.
                <br/><br/>
                Our natural product division supply novel compounds in mg for screening. We also support synthesis and scaling up that support drug discovery and development.
                <br/><br/>
                Our formulations division license out phytopharmaceutical, cosmeceutical and food supplements for OTC development of the clients.
                <br/><br/>
                Our Discovery services division provide strategic compound screening support, knowledge support and data management support for pharmaceutical R&D companies.
                <br/><br/>
                Our cell therapy division supply clinical grade cells for research purposes and therapy. We also provide media for cell growth and differentiation, markers and related RNA products. We also supply cell lines for drug screening            
                <br/><br/>
            </h4>
        </div>
        <div class="col-md-2"></div>
    </div>

<?php
    $this->load->view('/includes/footer');
?>