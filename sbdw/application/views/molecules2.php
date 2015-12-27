<?php defined('BASEPATH') OR exit('No direct script access allowed');

$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');

?>
<script src="<?php echo base_url('public/js/jsme/jsme.nocache.js'); ?>"></script>
<script src="<?php echo base_url('public/js/d3.min.js'); ?>"></script>

<script>
    function jsmeOnLoad(){

    } 
</script>  
<?php
    function tr4jme($inmol) {
        $outmol = $inmol;
        $outmol = str_replace("\r","", $outmol);
        $outmol = strtr($outmol,"\n", "|");
        return($outmol);
    }
?>	
        <hr/>
        <div class="row">
            <div class="col-md-1 col-sm-1"></div>
            <div class="col-md-8 col-sm-8">

                <?php foreach($records->result() as $record) : ?>
                    <?php $jmehitmol = tr4jme($record->cd_structure); ?>
                    <table class="table table-bordered">
                        <caption><h3><?php echo ($record->molecule_name); ?></h3></caption>
                        <tr>
                            <td rowspan="8">
                                <div code="JME.class" name="JME" archive="JME.jar" width="360" height="315" id="JME">
                                    <param name="options" value="oldlook, nopaste, depict">
                                    <param name="mol" value="<?php echo ($jmehitmol) ?>">   
                                    You have to enable JavaScript in your browser to use JSME! 
                                </div>
                            </td>
                            <td class="mol label">Molecular weight</td>
                            <td class="mol label">Formula</td>
                        </tr>
                        <tr>
                            <td class="mol"><?php echo($record->cd_molweight);?></td>
                            <td class="mol"><?php echo($record->cd_formula);?></td>
                        </tr>
                        <tr>
                            <td class="mol label">Molecule Type</td>
                            <td class="mol label">Therapeutic Category</td>
                        </tr>
                        <tr>
                            <td class="mol"><?php echo($record->molecule_type);?></td>
                            <td class="mol"><?php echo($record->therapeutic_category);?></td>
                        </tr>
                        <tr><td colspan="2" class="mol label">Source</td></tr>
                        <tr>
                            <td class="mol label">Type</td>
                            <td class="mol label">Family</td>
                        </tr>
                        <tr>
                            <td class="mol"><?php echo($record->source_type);?></td>
                            <td class="mol"><?php echo($record->source_family);?></td>                                
                        </tr>
                    </table>
                <?php endforeach; ?>
                <?php echo $this->pagination->create_links(); ?>    

            </div>
            
            <div class="col-md-4 col-sm-4 pull-right">
                <div class="section">
                    <div class="col-md-12 col-sm-12">
                        <div class="service-wrapper">
                            <h3>Useful Statistics</h3>
                            <h5><?php echo ($record_count); ?> records in library</h5>
                            
                            </div>                            
                        </div>
                    </div>               
                </div> 
            </div>
        <style>

        .chart rect {
          fill: steelblue;
        }

        .chart text {
          fill: white;
          font: 10px sans-serif;
          text-anchor: end;
        }

        </style>
        <script>

        var data = [4, 8, 15, 16, 23, 42];

        var width = 160,
            height = 250;

        var x = d3.scale.linear().range([0, width]);
            
        var y = d3.scale.linear()
            .domain([0, d3.max(data)])
            .range([height, 0]);
            
        var xAxis = d3.svg.axis().scale(x)
            .orient("bottom").ticks(5);
            
        var chart = d3.select(".chart")
            .attr("width", width)
            .attr("height", height);

        var barWidth = width / data.length;

        var bar = chart.selectAll("g")
            .data(data)
            .enter().append("g")
            .attr("transform", function (d, i) {
            return "translate(" + i * barWidth + ", 0)";
        });

        bar.append("rect")
            .attr("y", function(d) { return y(d); })
            .attr("height", function(d) { return height - y(d); })
            .attr("width", barWidth - 2);

        bar.append("g")         // Add the Y Axis
            .attr("class", "x axis")
            .call(xAxis);

        bar.append("text")
            .attr("x", barWidth / 2)
            .attr("y", 0)
            .transition()
            .delay(750)
            .attr("y", function(d) { return y(d) + 3; })
            .attr("dy", ".75em")
            .text(function(d) { return d; })

        function type(d) {
            d.value = +d.value; // coerce to number
            return d;
        }

        </script>
        </div>            
    </div>
</div>    

<?php
    $this->load->view('/includes/footer');
?>