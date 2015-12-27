<?php
defined('BASEPATH') OR exit('No direct script access allowed');

$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');

?>
<script type="text/javascript">
    $("document").ready(function() {
        $("#unique, #sudhir, #rajendran, #vinuthna, #ramesh, #np, #ct, #cc, #c, #mfg").hide(250);

        $('#overview-trigger').click(function(){
            $("#unique, #overview, #sudhir, #rajendran, #vinuthna, #ramesh, #np, #ct, #cc, #c, #mfg").hide(250);
            $("#overview").show(500);
        });                
        $('#unique-trigger').click(function(){
            $("#unique, #overview, #sudhir, #rajendran, #vinuthna, #ramesh, #np, #ct, #cc, #c, #mfg").hide(250);
            $("#unique").show(500);
        });                
        $('#sudhir-trigger').click(function(){
            $("#unique, #overview, #sudhir, #rajendran, #vinuthna, #ramesh, #np, #ct, #cc, #c, #mfg").hide(250);
            $("#sudhir").show(500);
        });                
        $('#rajendran-trigger').click(function(){
            $("#unique, #overview, #sudhir, #rajendran, #vinuthna, #ramesh, #np, #ct, #cc, #c, #mfg").hide(250);
            $("#rajendran").show(500);
        });                
        $('#vinuthna-trigger').click(function(){
            $("#unique, #overview, #sudhir, #rajendran, #vinuthna, #ramesh, #np, #ct, #cc, #c, #mfg").hide(250);
            $("#vinuthna").show(500);
        });                
        $('#ramesh-trigger').click(function(){
            $("#unique, #overview, #sudhir, #rajendran, #vinuthna, #ramesh, #np, #ct, #cc, #c, #mfg").hide(250);
            $("#ramesh").show(500);
        });                
        $('#np-trigger').click(function(){
            $("#unique, #overview, #sudhir, #rajendran, #vinuthna, #ramesh, #np, #ct, #cc, #c, #mfg").hide(250);
            $("#np").show(500);
        });                
        $('#ct-trigger').click(function(){
            $("#unique, #overview, #sudhir, #rajendran, #vinuthna, #ramesh, #np, #ct, #cc, #c, #mfg").hide(250);
            $("#ct").show(500);
        });                
        $('#cc-trigger').click(function(){
            $("#unique, #overview, #sudhir, #rajendran, #vinuthna, #ramesh, #np, #ct, #cc, #c, #mfg").hide(250);
            $("#cc").show(500);
        });                
        $('#c-trigger').click(function(){
            $("#unique, #overview, #sudhir, #rajendran, #vinuthna, #ramesh, #np, #ct, #cc, #c, #mfg").hide(250);
            $("#c").show(500);
        });                
        $('#mfg-trigger').click(function(){
            $("#unique, #overview, #sudhir, #rajendran, #vinuthna, #ramesh, #np, #ct, #cc, #c, #mfg").hide(250);
            $("#mfg").show(500);
        });                
    });
</script>
    <div class="row">
        <div id="leftmenu" class="col-xs-3 col-md-3 right">
            <br/>
            <nav class="leftmenu">
                <ul class="nav nav-pills nav-stacked">
                    <li id="overview-trigger" class=""><a href="#">Overview</a></li>
                    <li id="unique-trigger" class=""><a href="#">Unique Sristi</a></li>
                    <li class=""><strong>Board</strong>
                        <ul class="nav nav-pills nav-stacked">
                            <li id="sudhir-trigger"><a href="#"><small>Dr. K Sudhir Kumar Reddy</small></a></li>
                            <li id="rajendran-trigger"><a href="#"><small>Dr. A. Rajendran</small></a></li>
                            <li id="vinuthna-trigger"><a href="#"><small>Ms. Vinuthna Reddy</small></a></li>
                            <li id="ramesh-trigger"><a href="#"><small>Mr. G. Ramesh</small></a></li>
                        </ul>
                    </li>                        
                    <li><strong>R &amp; D</strong>
                        <ul class="nav nav-pills nav-stacked">
                            <li id="np-trigger"><a href="#"><small>Natural Products</small></a></li>
                            <li id="ct-trigger"><a href="#"><small>Cell Therapy</small></a></li>
                        </ul>
                     </li>   
                    <li><strong>Facilities</strong>
                        <ul class="nav nav-pills nav-stacked">
                            <li id="cc-trigger"><a href="#"><small>Cell Culture</small></a></li>
                            <li id="c-trigger"><a href="#"><small>Chemistry</small></a></li>
                            <li id="mfg-trigger"><a href="#"><small>Manufacturing</small></a></li>
                        </ul>
                     </li>   
                </ul>
            </nav>
        </div>
        <div id="overview" class="col-xs-9 col-md-9 left" style="height:450px;padding:30px;">
           <br/><br/>
            <h1>Overview</h1>
            <p class="text-justify">
            Sristi Biosciences Private Limited is a next generation biosciences company that focuses on the converging 
            healthcare value chain. The business opportunity of Sristi is mapped out of carefully evolved opportunity 
            selection criteria that consider market transition, size, sustainability and uniqueness.
            <br/><br/>
            Transition of Healthcare industry globally shows a common trend of disease migration form infectious diseases 
            to life style associated conditions. Arthritis, diabetes, cardiac disorders, respiratory problems, cancer and 
            CNS play a major role today as against infectious diseases       
            </p>
        </div>
        <div id="unique" class="col-xs-9 col-md-9 left" style="height:450px;padding:30px;">
            <br/><br/>
            <h1>Unique Sristi</h1>
            <p class="text-justify">
                Sristibio is unique by its approach to healthcare research;
                <ul>
                    <li>We bring together traditional wisdom and technological advancements for adding value to quality of life</li>
                    <li>We believe in the principles of evolution, nature and systems biology that generates sustained healthcare value.</li>
                    <li>Our values drive a medically aware society.</li>
                </ul>
            </p>
        </div>
        <div id="sudhir" class="col-xs-9 col-md-9 left" style="height:450px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <ul>
                    <li><h1>Dr. K Sudhir Kumar Reddy</h1>
                        MBBS (AIIMS), MS Ortho (AIIMS), MCh Orth (UK), FRCS (Edin), FRCSOrth (UK)
                        <br/><br/><strong>Executive Director</strong>
                        <p class="text-justify">
                            Dr Sudhir Reddy is an Orthopaedic Surgeon with special interest in medical applications of Biotechnology, in particular in Tissue Engineering. Dr Reddy was trained in some of the best institutions in India and Europe and has over 15 years of experience in medical field.
                            <br/><br/>                            
                            Dr Reddy spent over 8 years in United Kingdom working as an Orthopaedic Surgeon during which he developed keen interest in Tissue Engineering & Cell therapies and has visited many European countries and institutions to enhance knowledge and skills in these areas. Dr Reddy is a member of International Cartilage Research Society and has a wide network of Pioneers, Institutions and companies which work in Tissue Engineering.
                            <br/><br/>                            
                        </p>                                
                    </li>
                </ul>
            </p>    
        </div>
        <div id="rajendran" class="col-xs-9 col-md-9 left" style="height:450px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <ul>
                    <li><h1>Dr. A. Rajendran</h1>
                        M.Sc., PhD, F.R.H.S., F.I.C., C. Chem, P.G.D.M.M, F.W.S.A.M, M.I.H.M.S
                        <br/><br/><strong>Executive Director</strong>
                        <p class="text-justify">
                            Has been carrying Research and Development activities in various herbal formulations and has developed several formulations of Medicines, Cosmetics, and Nutraceuticals and have more than 75 commercially successful products to his credit.
                            <br/><br/>                            
                            Carries years of experience in the area of Natural Products and formulations. Dr. Rajendran has established & implemented the Aloe vera gel Cold Processing Technology for the first time in India.
                            <br/><br/>                            
                            Has developed more than 170 products based on Aloe vera. He has authored more than 20 publications in various international journals.
                            <br/><br/>                            
                            His credentials include establishment of Phyto Tech Engineering, and he is a Technical Adviser for Sciences and Technology Entrepreneurship development Scheme (STED), Thanjavur (Dept of Science & Technology, Govt of India).
                            <br/><br/>                            
                        </p>                                
                    </li>    
                </ul>
            </p>
        </div>
        <div id="vinuthna" class="col-xs-9 col-md-9 left" style="height:450px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <ul>
                    <li><h1>Ms. Vinuthna Reddy</h1>
                        <strong>Represented by Dr. KRK Reddy as Honorary advisor</strong>
                        <br/>
                        <p class="text-justify">
                            Dr. KRK Reddy as a promoting partner represents his daughter Ms. Vinuthna Reddy in the board of Sristi Biosciences Private Limited. Dr. KRK’s participation in Sristi Biosciences is a strategic intent to expand his business presence beyond agriculture biotechnology to healthcare biotechnology.
                            <br/><br/>                            
                            A seasoned Agricultural Biotechnologist having more than a decade (1994-till date) of experience in manufacturing and marketing of agricultural bio - inputs in Andhra Pradesh. Earlier (1988-1994) he worked as a research scientist in India and abroad. His main area of research was genetic transformations, plant tissue culture and stress metabolism in plants.
                            <br/><br/>                            
                            He published several research papers in national and international referred journals and he is also a life member of several professional bodies dedicated to agricultural research. He became a first generation entrepreneur in the year 1994 and established a state-of-the-art agri biotech laboratory at Hyderabad, one of the earliest biotech centers ever established in Andhra Pradesh in the private sector. Currently he is heading Sri Bio Group, the group engaged in mass production and marketing of biotechnological products for agriculture, aquaculture, poultry and veterinary. The organization is ISO 9001: 500 certified for quality management in production of Biological inputs. He is instrumental in registering six bio pesticides for his group with the Government of India, which is first of its kind in the country.
                            <br/><br/>                            
                            He trained more than 50 M. Sc., Biotechnology and Microbiology post graduates belonging to different Universities in microbial biotechnology with special reference to microbial fermentation and process and guided them in completing their project work for the partial fulfillment of their degrees.
                            <br/><br/>                            
                            He is the man behind getting the awards for his organization viz., Best New Product Innovation award from FAPCCI for the year 2003-2004 and Best Biotechnology award from AIMO for the Year 2002-2003.National award for outstanding research contributions in the field of Agriculture Biotechnology for the year 2005 from Dept, of Scientific and Industrial Research, Ministry of Science and Technology, Govt. of India and Creativity and Innovation award from All India Management Association for the year 2005 (This award was presented by He, Dr . AP J Abdul Kalam, President of India)
                            <br/><br/>                            
                            Currently Dr. Reddy is acting as President, Agricultural Bio-inputs Producers Association of Andhra Pradesh and Founder Member of Bio pesticides Research Consortium (BRC), constituted by ICRISAT. He is on the Advisory board of Kakatiya University and Acharya Nagarjuna University, Andhra Pradesh for Biotechnology. He is also acting as Director of the groups Research and Development Center, the R&D recognized by Department of Scientific and Industrial Research (DSIR), Ministry of Science and Technology, Govt. of India.
                            <br/><br/>                            
                        </p>                                
                    </li>    
                </ul>
            </p>
        </div>
        <div id="ramesh" class="col-xs-9 col-md-9 left" style="height:450px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <ul>
                    <li><h1>Mr. G. Ramesh</h1>
                        <strong>Director</strong>
                        <br/>
                        <p class="text-justify">
                            Mr. G Ramesh is an electrical engineer by qualification and profession. He spent more than 20 years in Pharmaceutical manufacturing with giants like Aurobindo pharma, Hetero drugs, etc. He is instrumental behind establishment of huge bulk and intermediate manufacturing facilities in Andhra Pradesh.
                            <br/><br/>                            
                            His credentials include establishment of Sree Power and Ahlada Pharmaceuticals. He has joined the board of Sristi Biosciences Private limited with a strategic intent of backward integration of Biopharmaceutical industry.
                            <br/><br/>                            
                        </p>                                
                    </li>    
                </ul>
            </p>
        </div>
        <div id="np" class="col-xs-9 col-md-9 left" style="height:450px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Natural Products</h1>
                Our expertise lies in isolation, purification, and structure elucidation of natural products. Our current collection of a variety of pure natural product samples provides a foundation for building natural product based combinatorial libraries, as well as we offer services to identify a minor component in a given sample, whether it is an active compound, a metabolite, or an impurity. Our collection comprises natural compounds isolated from plants, microorganisms, marine species etc.
                <br/><br/>    
                Our research also focus on investigation of herbal medicines, botanicals, dietary supplements, probiotics that have origins in various alternative traditional medical systems. We are specialized in sample acquisition strategies, including isolation sources, microbial strains, and fermentation extracts. We offer bioactive natural product-derived small molecule chemical libraries.            
                <br/><br/>    
            </p>
        </div>
        <div id="ct" class="col-xs-9 col-md-9 left" style="height:450px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Cell Therapy</h1>
                Tissue engineering and cell therapy research focuses on development of therapeutic cells for various disease conditions. Autologous Chondrocyte Implantation is our first therapeutic development, which is at a very late stage, ready for trials.
                <br/><br/>        
                Our extensive research on stem cells/ cell products is aimed at commercializing clinically proven cell therapies which address human diseases. Our service lies in collaborating with commercial partners with which we expect to introduce several new cell therapies for regulatory approval.            </p>
                <br/><br/>    
        </div>
        <div id="cc" class="col-xs-9 col-md-9 left" style="height:450px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Cell Culture</h1>
                Our Cell culture facility is equipped with self-sustained lab with all equipment necessary for cell culture. We also have equipment and facilities for long term storage of cells. The cell culture facility provides investigators with the necessary equipment and environment for development of cell products, and supports maintenance and storage of clinical grade cells. The facility will also manufacture cell products with quicker and more reliable production capacity                
                <br/><br/>
            </p>
        </div>
        <div id="c" class="col-xs-9 col-md-9 left" style="height:450px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Chemistry</h1>
                Our chemistry facility supports extraction, fractionation and isolation of compounds from natural sources. Our analytical facility is equipped with HPLC’s, LCMS and all essential instrumentation to support separation, analysis and elucidation of compounds. Our lab is also highly equipped to enable custom synthesis and natural product formulations. Our infrastructure also includes compound management system that traces back the sources for authentification and availability. We are also enriching our infrastructure to support full fledged medicinal chemistry. Our Chemistry infrastructure includes a well organized informatics infrastructure for end to end management and analysis of structures.                
                <br/><br/>    
            </p>
        </div>
        <div id="mfg" class="col-xs-9 col-md-9 left" style="height:450px;padding:30px;">
            <br/><br/>
            <p class="text-justify">
                <h1>Manufacturing</h1>
                <strong>Sristi</strong> has independent finished-product manufacturing facilities for solid, liquid, semi-solid and dry powder dosage forms in Hyderabad and Chennai. The facility is equipped to manufacture OTC, branded and natural product formulations. The plant produces a multi-product range of generic pharmaceuticals in creams, ointments, liquid and products serving the OTC and herbal dietary supplements. We offer full-service process development, manufacture, and formulation at the cGMP facility in Chennai. We also produce natural product formulations from milligram to several hundred gram quantities
                <br/><br/>    
            </p>
        </div>
    </div>
<?php
    $this->load->view('/includes/footer');
?>