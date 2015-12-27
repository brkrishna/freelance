<?php
defined('BASEPATH') OR exit('No direct script access allowed');

$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');

?>
<script type="text/javascript">
    $("document").ready(function() {

        $("#cl, #plants, #marine, #screen, #supply, #bb, #cancer, #diabetes, #ai, #phyto, #license, #research, #prod, #draloe").hide("slow");

        $('#overview-trigger').click(function(){
            $("#overview, #cl, #plants, #marine, #screen, #supply, #bb, #cancer, #diabetes, #ai, #phyto, #license, #research, #prod, #draloe").hide("slow");
            $("#overview").show("slow");
        });                
        $('#cl-trigger').click(function(){
            $("#overview, #cl, #plants, #marine, #screen, #supply, #bb, #cancer, #diabetes, #ai, #phyto, #license, #research, #prod, #draloe").hide("slow");
            $("#cl").show("slow");
        });                
        $('#plants-trigger').click(function(){
            $("#overview, #cl, #plants, #marine, #screen, #supply, #bb, #cancer, #diabetes, #ai, #phyto, #license, #research, #prod, #draloe").hide("slow");
            $("#plants").show("slow");
        });                
        $('#marine-trigger').click(function(){
            $("#overview, #cl, #plants, #marine, #screen, #supply, #bb, #cancer, #diabetes, #ai, #phyto, #license, #research, #prod, #draloe").hide("slow");
            $("#marine").show("slow");
        });                
        $('#screen-trigger').click(function(){
            $("#overview, #cl, #plants, #marine, #screen, #supply, #bb, #cancer, #diabetes, #ai, #phyto, #license, #research, #prod, #draloe").hide("slow");
            $("#screen").show("slow");
        });                
        $('#supply-trigger').click(function(){
            $("#overview, #cl, #plants, #marine, #screen, #supply, #bb, #cancer, #diabetes, #ai, #phyto, #license, #research, #prod, #draloe").hide("slow");
            $("#supply").show("slow");
        });                
        $('#bb-trigger').click(function(){
            $("#overview, #cl, #plants, #marine, #screen, #supply, #bb, #cancer, #diabetes, #ai, #phyto, #license, #research, #prod, #draloe").hide("slow");
            $("#bb").show("slow");
        });                
        $('#cancer-trigger').click(function(){
            $("#overview, #cl, #plants, #marine, #screen, #supply, #bb, #cancer, #diabetes, #ai, #phyto, #license, #research, #prod, #draloe").hide("slow");
            $("#cancer").show("slow");
        });                
        $('#diabetes-trigger').click(function(){
            $("#overview, #cl, #plants, #marine, #screen, #supply, #bb, #cancer, #diabetes, #ai, #phyto, #license, #research, #prod, #draloe").hide("slow");
            $("#diabetes").show("slow");
        });                
        $('#ai-trigger').click(function(){
            $("#overview, #cl, #plants, #marine, #screen, #supply, #bb, #cancer, #diabetes, #ai, #phyto, #license, #research, #prod, #draloe").hide("slow");
            $("#ai").show("slow");
        });                
        $('#phyto-trigger').click(function(){
            $("#overview, #cl, #plants, #marine, #screen, #supply, #bb, #cancer, #diabetes, #ai, #phyto, #license, #research, #prod, #draloe").hide("slow");
            $("#phyto").show("slow");
        });                
        $('#license-trigger').click(function(){
            $("#overview, #cl, #plants, #marine, #screen, #supply, #bb, #cancer, #diabetes, #ai, #phyto, #license, #research, #prod, #draloe").hide("slow");
            $("#license").show("slow");
        });                
        $('#research-trigger').click(function(){
            $("#overview, #cl, #plants, #marine, #screen, #supply, #bb, #cancer, #diabetes, #ai, #phyto, #license, #research, #prod, #draloe").hide("slow");
            $("#research").show("slow");
        });                
        $('#prod-trigger').click(function(){
            $("#overview, #cl, #plants, #marine, #screen, #supply, #bb, #cancer, #diabetes, #ai, #phyto, #license, #research, #prod, #draloe").hide("slow");
            $("#prod").show("slow");
        });                
        $('#draloe-trigger').click(function(){
            $("#overview, #cl, #plants, #marine, #screen, #supply, #bb, #cancer, #diabetes, #ai, #phyto, #license, #research, #prod, #draloe").hide("slow");
            $("#draloe").show("slow");
        });                
    });
</script>
    <div class="row">
        <div id="leftmenu" class="col-xs-3 col-md-3 right">
            <br/>
            <nav class="leftmenu">
                <ul class="nav nav-pills nav-stacked">
                    <li id="overview-trigger"><a href="#">Natural Products</a></li>
                    <li id="cl-trigger" class=""><a href="#">Compound Libraries</a></li>
                    <li id="plants-trigger" class="text-justify"><a href="#"><small>Plants</small></a></li>
                    <li id="marine-trigger" class="text-justify"><a href="#"><small>Marine</small></a></li>
                    <li id="screen-trigger" class=""><a href="#">Screening</a></li>
                    <li id="supply-trigger" class="text-justify"><a href="#"><small>Supply</small></a></li>
                    <li id="bb-trigger" class="text-justify"><a href="#"><small>Building Blocks</small></a></li>
                    <li class=""><strong>Focus</strong></li>
                    <li id="cancer-trigger" class="text-justify"><a href="#"><small>Cancer</small></a></li>
                    <li id="diabetes-trigger" class="text-justify"><a href="#"><small>Diabetes</small></a></li>
                    <li id="ai-trigger" class="text-justify"><a href="#"><small>Anti-Infectives</small></a></li>
                    <li class=""><strong>OTC Forumulations</strong></li>
                    <li id="phyto-trigger" class="text-justify"><a href="#"><small>Phytopharmaceuticals</small></a></li>
                    <li class=""><strong>Licensing</strong></li>
                    <li id="license-trigger" class="text-justify"><a href="#"><small>Licensing</small></a></li>
                    <li id="prod-trigger" class="text-justify"><a href="#"><small>Product Development</small></a></li>
                    <li class=""><strong>Brands</strong></li>
                    <li id="draloe-trigger" class="text-justify"><a href="#"><small>Dr. Aloe</small></a></li>
                </ul>
            </nav>
        </div>
        <div id="overview" class="col-xs-9 col-md-9 left text-justify" style="height:600px;padding:30px;">
           <br/><br/>
            <h1>Natural Products</h1>
            Natural products offer a vast source of chemical diversity and yield unusual and unexpected lead structures. As such small 
            molecules produced in this way have been designed by nature to interact with macromolecules (Proteins, DNA etc) and thus 
            modulate the function of such macromolecules. Natural products can derive a wide portfolio of lead structures that shall 
            drive next generation drug discovery. It also provides an opportunity to explore poly herbal formulations that can become 
            potential source for Phytopharmaceuticals, Cosmeceuticals and Food Supplements.
            <br/><br/>    
            <ul>
                <li>Our Natural Products research focuses on two major areas
                    <ul>
                        <li>Natural Products Drug Discovery</li>
                        <li>Formulations Research</li>
                    </ul>
                </li>
            </ul>
            <div class="col-xs-3 col-md-4 text-center">
                <a href="<?php echo base_url('/index.php/NP/molecules/botan'); ?>"><img src="<?php echo base_url('public/imgs/botanicule.jpg'); ?>"/></a><br/><i><strong>Exploring novelty space in botanicals</strong></i>                
            </div>
            <div class="col-xs-3 col-md-4 text-center">
                <a href="<?php echo base_url('/index.php/NP/molecules/marine'); ?>"><img src="<?php echo base_url('public/imgs/marinicule.jpg'); ?>"/></a><br/><i><strong>Swimming the aquatic chemical diversity space</strong></i>
            </div>
            <div class="col-xs-3 col-md-4 text-center">
                <a href="<?php echo base_url('/index.php/NP/molecules/micro'); ?>"><img src="<?php echo base_url('public/imgs/microbicule.jpg'); ?>"/></a><br/><i><strong>investigating microbes as production systems and novetly source</strong></i>                
            </div>
        </div>
        <div id="cl" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <h1>Compound Libraries</h1>
            <p class="text-justify">
                The bioactive compounds are isolated from the raw material by different methods, such as extraction, distillation, separation 
                and analysis. The compounds are isolated and maintained at more than 95% purity. The phytochemical extraction involves 
                homogenization, vaccum filtration, solvent evaporation, lipophilization and involves utilization of various analytical 
                instruments for the same.
                <br/><br/>
                Knowledge in isolation, purification, and structure elucidation of natural products, and our current collection of a variety of 
                pure natural product samples provides a foundation for building natural product based combinatorial libraries, as well as for 
                offering services to identify a minor component in a given sample, whether it is an active compound, a metabolite, or an impurity. 
                Our collection comprises natural compounds isolated from plants, microorganisms, marine species etc.
                <br/><br/>    
                High throughput screening using a 96-well plate is used to generate a large number of low concentration plates for screening. 
                Sristibio has all necessary facilities and equipment to isolate and chemically identify biologically active components. 
                Additionally, identification and chemical synthesis can be provided. In addition we provide
                <ul>
                    <li>Accurate identification of species names</li>
                    <li>Precise information regarding location of samples</li>
                    <li>Resupply with the aid of a large network of collectors</li>
                </ul>
                <br/><br/>            
            </p>
        </div>
        <div id="plants" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Plants</h1>
                Srsiti constructs libraries to target gene families, protein targets, to expand the chemical diversity of the company's 
                compound collection. The database contains approximately 1000 chemical compounds derived from various plant sources including 
                terpenes, saponins, flavonoids, Sterols etc. Our compound libraries from plant sources includes
                <br/><br/>
                Diverse sets of biologically relevant small molecule
                Core scaffold of an individual natural product
                Molecules with high ligand affinity and better specificity to biological targets
                Diversity of scaffolds for the synthesis of natural compound-like libraries
                Molecular diversity of structurally similar analogs
                Valuable pharmacological probes to help target various receptros
                <br/><br/>
            </p>
        </div>
        <div id="marine" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Marine</h1>
                Marine Compounds is a collection of bioactive metabolites of marine microorganisms and invertebrates. The current edition of 
                the library covers more than 700 molecules which include alkaloids, diterpenes, eicosanoids, nucleosides, peptides, polycyclic 
                ethers, toxins, sterols, sesquiterpenes, etc.
                <br/><br/>    
                Marine habitat is considered to be a major source for potential drugs. The library serves as an important source for both 
                biologists and chemists who look for potential pharmaceuticals. The library can be queried using simple &amp; advanced search            
                <br/><br/>
            </p>
        </div>
        <div id="screen" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Screening</h1>
                Screening is an approach to chemical synthesis that enables the creation of large numbers of organic compounds by linking chemical building 
                blocks in all possible combinations, identify novel compounds with therapeutic and preventive efficacy against disease This approach to 
                testing drug candidates is highly dependent on the quality of the initial library of compounds, and the intelligence used to select the 
                initial lead candidates that guide the screening process. Our objective lies in devising computational approaches for testing the binding 
                activity of extensive naturally occurring compound libraries prior to testing activity using ligand-binding approaches and assays.
                <br/><br/>
                We believe our drug discovery and development approach can significantly improve on the industry's existing clinical attrition rates 
                through our use of
                <br/><br/>
                Proprietary cheminformatics databases that relate chemical structure to compound development potential;
                Multiple lead generation strategies including high throughput screening, virtual screening
                A company-wide techniques that enables scientists to collect, analyze and share information across the organization
                <br/><br/>
            </p>
        </div>
        <div id="supply" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Supply</h1>
                We supply compound source plates and assay plates containing compounds in 96-well micro plates for HTS. We plate the compounds in 
                96 well microplating in fixed amounts of DMSO solution for screening. We will also supply compounds in vials based on the request.
                <br/><br/>
                More than 100000 synthetic and natural compounds are available for screening anti-cancer, diabetes and anti-infective. 
                We supply radio-labelled compound at the maximum possible purity. Our approach is to set up a fractionation scheme and to screen 
                the fractions for the presence of bioactive properties. The following are the services offered.
                <ul>
                    <li>Listing of known compounds per plant</li>
                    <li>Listing of previously reported activities</li>
                    <li>Metabolic profiling, or an extensive metabolomic study with identification of known compounds</li>
                    <li>Screening of crude extracts and pre-fractionated extracts</li>
                <ul>                
                <br/><br/>
            </p>
        </div>
        <div id="bb" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Building Blocks</h1>
                Our innovative technology platform and extensive expertise in biocatalysis enable us to build wide range of 
                building block library. Our chemical building block library has been developed to support advanced 
                combinatorial lead generation, lead optimization and medicinal chemistry programs. By developing tailor-made 
                building blocks we can assist clients from early development to commercial stage.
                <br/><br/>
                All of our chemical building blocks undergo extensive quality control, and purity is guaranteed to be over 95%
                <br/><br/>
            </p>
        </div>
        <div id="cancer" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Cancer</h1>
                Our Cancer research is involved in providing an extremely comprehensive review of anticancer plants and 
                natural compounds with an objective to develop strategies that modulate cell cycle regulatory molecules. 
                We maintain repositories of natural sources and compounds available for screening. Additional to that our 
                focus on cancer research provides comprehensive analysis of traditional knowledge in on-going research, 
                safety and efficacy of medical agents from natural sources and on structure diversification.
                <br/><br/>    
                It is a searchable database providing data on small-molecule and its biological therapeutics. 
                Database consists of depicted chemical structures with established anticancer and apoptotic properties
                <br/><br/>
            </p>
        </div>
        <div id="diabetes" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Diabetes</h1>
                We aim at translating discovery into treatment that benefits people with diabetes or those at risk by 
                accumulating molecular libraries. Our team of scientists develop therapeutic molecule database that has 
                the potential to lead the development of better prophylactic and/or therapeutic strategies for preventive 
                diabetes.
                <br/><br/>    
                Our diabetes research provides insights into genetic and molecular mechanisms that likely lead to the 
                identification and development small molecule drugs for the treatment.
                <br/><br/>
                Our analysis and studies on disease pathway provides a better understanding on the mechanisms of gene 
                trafficking, molecular characterization of disease-causing genes, susceptibility genes, and disease-linked 
                genes.
                <br/><br/>    
            </p>
        </div>
        <div id="ai" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Anti-Infectives</h1>
                Our anti-infectives database program is aimed at building small molecule database that constitute the 
                ultimate goal in the search for compounds that can directly block therapeutic targets. Our Anti-infective data 
                library consists of molecules covering natural sources like plants, marine and insects.
                <br/><br/>
            </p>
        </div>
        <div id="phyto" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Phytopharmaceuticals</h1>
                One of the major determinants of the efficacy of a botanical supplement is the manner in which it is 
                formulated. We follow modern techniques in the manufacture of phytopharmaceuticals.
                <br/><br/>
            </p>
        </div>
        <div id="license" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Licensing</h1>
                We share expertise and offer consultancy in :::
                <br/><br/>
                <ul>
                    <li>Good Agriculture practise for reliable source</li>
                    <li>Organic Certification</li>
                    <li>Process Technology with raw material screening and end product analysis</li>
                    <li>GMP standard guidance for manufacturing and Documentation</li>
                    <li>Formulation Technology</li>
                    <li>Technical training for Quality Management and Process</li>
                    <li>Documentation for Drug, Cosmetic and Nutraceuticals Licenses</li>
                    <li>Product registration / Documentation for overseas market</li>
                    <li>Clinical Validation</li>
                    <li>Scientific validation of herbal and the Indian Systems of medicine</li>
                    <li>Exploring new Herbs and Plants</li>
                    <li>Phytochemical and Phyto-pharmacological studies for lead finding in natural products from the great ancient treatise of India</li>
                    <li>Herbal therapeutics - Pharmacokinetics and utilization of Herbal drugs</li>
                    <li>Safety evaluation of Natural products</li>

                </ul>
                <br/><br/>
            </p>
        </div>
        <div id="research" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Research</h1>
                Our Research and Development out fit has been carrying on Research and Development activities in various 
                herbal formulation and has developed several formulations of Medicines, Cosmetic and Nutraceuticals.
                <br/><br/>
                Our mission is to be a primary manufacturer and supplier of active herbal (Indian system of medicines) 
                pharmaceutical ingredients of the highest quality and purity to the traditional pharmaceutical and 
                emerging phytopharmaceutical Industries.
                <br/><br/>
                Isolation, purification and standardization of various formulations derived from plants and other natural 
                sources that can be incorporated into regulated, finished formulations, prescription and OTC products to be 
                sold by clients
                <br/><br/>
            </p>
        </div>
        <div id="prod" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Product Development</h1>
                Our Integrated Product Development service delivery platform for product development helps in
                <ul>
                    <li>Identifying market segments of high value</li>
                    <li>Shortlisting an innovative proposition from either existing licenses or new license development in record time with a clearly marked up USP and offer value</li>
                    <li>Documentation and application of product license in the respective country’s regulatory compliances</li>
                    <li>Process Engineering and development of manufacturing and packaging requirements</li>
                    <li>Documentation of process engineering and packaging standards for compliance</li>
                    <li>Backward integrating supply of raw materials for production</li>
                    <li>Handholding on establishment of the manufacturing unit</li>
                    <li>Continuous handholding in terms of GMP, quality and production planning</li>
                    <li>Marketing Partnerships and support</li>
                </ul>
                <br/><br/>
            </p>
        </div>
        <div id="draloe" class="col-xs-9 col-md-9 left" style="height:600px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Dr. Aloe</h1>
                <strong>Dr.Aloe</strong> as a <strong>Nutritional Supplement</strong> assists the body in performing                
                <ul>
                    <li>The key function of boosting immune system due to the abundant presence of polysaccharides, a property exclusive to this plant.</li>
                    <li>It also contains amino acids, vitamins, minerals and enzymes.</li>
                    <li>It aids digestive system by improving absorption of nutrients.</li>
                    <li>It is a detoxifier and strengthens the nervous system.</li>
                    <li>Dr. Aloe is available in 500 ml. container.</li>
                </ul>
                <br/><br/>
                For more details <a target="_new" href="http://www.draloe.in">Click Here</a> to view Dr.Aloe Home Page
            </p>
        </div>
    </div>
<?php
    $this->load->view('/includes/footer');
?>


