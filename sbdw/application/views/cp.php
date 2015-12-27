<?php
defined('BASEPATH') OR exit('No direct script access allowed');

$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');

?>
<script type="text/javascript">
    $("document").ready(function() {
        $("#stem, #embr, #parthe").fadeOut("slow");

        $('#overview-trigger').click(function(){
            $("#overview, #stem, #embr, #parthe").fadeOut("slow");
            $("#overview").fadeIn("slow");
        });                
        $('#stem-trigger').click(function(){
            $("#overview, #stem, #embr, #parthe").fadeOut("slow");
            $("#stem").fadeIn("slow");
        });                
        $('#embr-trigger').click(function(){
            $("#overview, #stem, #embr, #parthe").fadeOut("slow");
            $("#embr").fadeIn("slow");
        });                
        $('#parthe-trigger').click(function(){
            $("#overview, #stem, #embr, #parthe").fadeOut("slow");
            $("#parthe").fadeIn("slow");
        });                
    });
</script>
    <div class="row">
        <div id="leftmenu" class="col-xs-3 col-md-3 right">
            <br/>
            <nav class="leftmenu">
                <ul class="nav nav-pills nav-stacked">
                    <li id="overview-trigger" class=""><a href="#">Overview</a></li>
                    <li id="stem-trigger"><a href="#">Stem Cells</a></li>
                    <li id="embr-trigger"><a href="#">Embryonic</a></li>
                    <li id="parthe-trigger"><a href="#">Parthenogenesis</a></li>
                    <li><a href="<?php echo base_url('/index.php/Products/product/cells'); ?>">Cells</a></li>                        
                    <li><a href="<?php echo base_url('/index.php/Products/product/reagents'); ?>">Reagents</a></li>
                    <li><a href="<?php echo base_url('/index.php/Products/product/media'); ?>">Media</a></li>
                </ul>
            </nav>
        </div>
        <div id="overview" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
           <br/><br/>
            <h1>Overview</h1>
            <p class="text-justify">
                Cell therapy is the innovative and most promising remedy for modern medicine which provides a new clinical approach for restoring function of damaged organs and tissues. Adoptive transfer of stem cell research to therapy seems to offer a promising strategy and a positive potential of stem cell therapies for human disease.
                <br/><br/>
                Our cell therapy division supply clinical grade cells for research purposes and therapy. We also provide media for cell growth and differentiation. We develop and commercialize stem cell-based products with an emphasis on applications in drug discovery, screening and the development of new technologies and tools. Our extensive research on stem cells/ cell products is aimed at commercializing clinically proven cell therapies which address human diseases. Our service lies in collaborating with commercial partners with which we expect to introduce several new cell therapies for regulatory approval.        
                <br/><br/>
        </div>
        <div id="stem" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <h1>Stem Cells</h1>
            <p class="text-justify">
                Stem cell’s regenerative potential and perhaps their ability to undergo differentiation into specific cell lineages 
                are making them a potential therapy for diseases and injuries. Recent research effort has been focused on attempts to 
                improve the survival rates using stem cell lines.
                <br/><br/>
                Sristi sources stem cell products which are manufactured using the highest quality raw materials and incorporates 
                extensive quality assurance in every production run. Our exacting standards and production procedures ensure 
                consistent performance. Our rigorous quality control ensures sterility and performance to standardized testing 
                criteria               
                <br/><br/>            
            </p>
        </div>
        <div id="embr" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Embryonic</h1>
                We source embryonic stem cell lines from our partner Life line Cell Technology. Stem cell lines differentiated from 
                human embryos provides unique in vitro growth characteristics. Our embryonic stem cell line offers consistent and 
                reproducible outcomes.  HES are one of the most pluripotent stem cell that holds a therapeutic promise. The underline 
                property of HES in terms of immortality and pluripotential for differentiation motivates our research for various 
                therapeutic options. We are exploring both manufacture and supply of cells from embryonic sources and using cells 
                for therapeutics           
            </p>
        </div>
        <div id="parthe" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Parthenogenesis</h1>
                We source human parthenogenetic stem (hpSC) cell lines from our partner Life line Cell Techology. hpSc promises to 
                minimize the rejection of transplanted cells by a patient's immune system. This technology, called "parthenogenesis," 
                results in the creation of pluripotent hpSC from unfertilized human eggs. This new methodology offers the potential to 
                create the first true "Stem Cell Bank" and also addresses critical ethical issues by eliminating the need to use fertilized 
                embryos            
            </p>
        </div>
    </div>
<?php
    $this->load->view('/includes/footer');
?>