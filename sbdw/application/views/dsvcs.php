<?php
defined('BASEPATH') OR exit('No direct script access allowed');

$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');

?>
<script type="text/javascript">
    $("document").ready(function() {
        $("#dcri, #stats, #records").fadeOut("slow");

        $('#overview-trigger').click(function(){
            $("#overview, #dcri, #stats, #records").fadeOut("slow");
            $("#overview").fadeIn("slow");
        });                
        $('#dcri-trigger').click(function(){
            $("#overview, #dcri, #stats, #records").fadeOut("slow");
            $("#dcri").fadeIn("slow");
        });                
        $('#stats-trigger').click(function(){
            $("#overview, #dcri, #stats, #records").fadeOut("slow");
            $("#stats").fadeIn("slow");
        });                
        $('#records-trigger').click(function(){
            $("#overview, #dcri, #stats, #records").fadeOut("slow");
            $("#records").fadeIn("slow");
        });                
    });
</script>
    <div class="row">
        <div id="leftmenu" class="col-xs-3 col-md-3 right">
            <br/>
            <nav class="leftmenu">
                <ul class="nav nav-pills nav-stacked">
                    <li id="overview-trigger" class=""><a href="#">Discovery Services</a></li>
                    <li id="dcri-trigger" class=""><a href="#"><small>DCRI</small></a></li>
                    <li class=""><strong>Clinical Research</strong>
                        <ul class="nav nav-pills nav-stacked">
                            <li id="stats-trigger"><a href="#"><small>Statistical Analysis</small></a></li>
                            <li id="records-trigger"><a href="#"><small>Records Management</small></a></li>
                        </ul>
                    </li>                        
                </ul>
            </nav>
        </div>
        <div id="overview" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
           <br/><br/>
            <h1>Overview</h1>
            <p class="text-justify">
                SristiBio’s cheminformatics service framework aims at providing integrated chemistry solutions to drug discovery & chemical research organizations. The framework enables oragnisations develop, store, manage, analyze &amp; mine chemical data and helps in maximizing the value of their chemical information.
                <br/><br/>    
                The framework facilitates researchers to organize their proprietary chemical data which helps in accelerating the drug discovery process. It also supports database services necessary to help organizations effectively analyze and visualize the valuable knowledge contained in research data            </p>
        </div>
        <div id="dcri" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <h1>Decision Centric Research Intelligence</h1>
            <p class="text-justify">
                DecisionCentric Research Intelligence of Sristi Biosciences Private Limited is drivenby an internal process work bench that enables In Silico Pharmacology happen fordiscovery R&D companies. DCRI services helps clients in multiple forms byharnessing published information in to a knowledge framework that easesresearch decision for clients. Speed and cost are the two major competitiveadvantages DCRI provides its clients.
                <br/><br/>    
                Client may avail DCRI services in multipleforms, which by all means is a research query that may be as broad as a turnkey project leading to lead identification and optimization or as simple as anexercise of compiling small molecules database relevant to target specified. Weorganize access to DCRI services in the following formats.
                <br/><br/>
                Targets with crystalstructure demanding a set of relevant scored small molecules for activity whichare synthesized, synthesizable, natural sources or denovo designed.
                Targets demandingHomology Modeling and protein structure prediction and the resultantidentification and scoring for leads.
                Taking a clue fromexisting binding molecules and tracking similar molecules for activity andreporting.
                Identifying relatedtargets for binding molecules in order to derive clues for small molecules.
                <br/><br/>            
            </p>
        </div>
        <div id="stats" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Statistical Analysis</h1>
                <ul>
                    <li>Statistical Analysis Plan</li>
                    <li>Statistical Analysis
                        <ul>
                            <li>Power / Sample Size Calculation</li>
                            <li>Testing Hypothesis</li>
                            <li>Multiple Regression Analysis</li>
                            <li>Categorical Data Analysis</li>
                            <li>Survival Analysis</li>
                        </ul>
                    </li>
                    <li>Statistical Reporting</li>
                 </ul>
            </p>
        </div>
        <div id="records" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Records Management</h1>
                <ul>
                    <li>Data Management Manual</li>
                    <li>CRF Tracking</li>
                    <li>Database Design</li>
                    <li>Database Design Testing and Validation</li>
                    <li>Double Data Entry</li>
                    <li>Data Comparision and adjudication</li>
                    <li>Query Management</li>
                    <li>Data Validation</li>
                    <li>Data Review</li>
                    <li>Data Cleaning</li>
                    <li>Quality Control</li>
                    <li>Database Lock</li>
                </ul>
            </p>
        </div>
    </div>
<?php
    $this->load->view('/includes/footer');
?>