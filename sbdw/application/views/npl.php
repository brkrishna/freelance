<?php
defined('BASEPATH') OR exit('No direct script access allowed');

$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');
?>
<!--
<style>
    .decades rect {
        fill: steelblue;
    }

    .decades text {
        fill: #000;
        font: 10px sans-serif;
        text-anchor: end;
    }
    .axis text {
      font: 10px sans-serif;
    }

    .axis path,
    .axis line {
      fill: none;
      stroke: #000;
      shape-rendering: crispEdges;
    }    
</style>
<script type='text/javascript'>
    
    $(document).ready(function(){
        $.ajax({
            'url': '../decade_count',
            'type': 'GET',
            'success': function(data){
                if(data){
                    data = JSON.parse(data)
                    
                    var margin = {top: 20, right: 30, bottom: 30, left: 40},
                        width = 420 -  margin.left - margin.right,
                        height = 250 - margin.top - margin.bottom;

                    //var x = d3.scale.linear().range([0, width]);
                    var x = d3.scale.ordinal()
                        .domain(data.map(function(d){ return d.year;}))
                        .rangeRoundBands([0, width], .1);
                    
                    var y = d3.scale.linear()
                        .domain([0, d3.max(data, function(d) { return d.articles; })])
                        .range([height, 0]);

                    var xAxis = d3.svg.axis().scale(x)
                        .orient("bottom");
                    
                    var yAxis = d3.svg.axis().scale(y)
                        .orient("left");

                    var chart = d3.select(".decades")
                        .attr("width", width + margin.left + margin.right)
                        .attr("height", height + margin.top + margin.bottom)
                        .append("g")
                        .attr("transform", "translate(" + margin.left + ", " + margin.top + ")");
                    
                    chart.append("g")
                        .attr("class", "x axis")
                        .attr("transform", "translate(0, " + height + ")")
                        .call(xAxis)
                        .append("text")
                            .attr("x", width / 2)
                            .attr("y")
                            .text("Years");
                    
                    chart.append("g")
                        .attr("class", "y axis")
                        .call(yAxis)
                        .append("text")
                            .attr("transform", "rotate(-90)")
                            .attr("y", 6)
                            .attr("dy", ".71em")
                            .style("text-anchor", "end")
                            .text("Articles");
                    
                    var barWidth = width / data.length;
                    
                    chart.selectAll(".bar")
                        .data(data)
                        .enter().append("rect")
                        .attr("class", "bar")
                        .attr("x", function(d) { return x(d.year); })
                        .attr("y", function(d) { return y(d.articles); })
                        .attr("height", function(d) { return height - y(d.articles); }) 
                        .attr("width", x.rangeBand());
                    
                    /*
                    var bar = chart.append("g")
                        .data(data)
                        .enter().append("g")
                        .attr("transform", function (d) {
                        return "translate(" + x(d.year) + ", 0)";
                    });
                    
                    bar.append("rect")
                        .attr("y", function(d) { return y(d.articles); })
                        .attr("height", function(d) { return height - y(d.articles); })
                        .attr("width", x.rangeBand());
                    
                   bar.append("text")
                        .attr("x", x.rangeBand() /1.5)
                        .attr("y", function(d) { return y(d.articles) + 3; })
                        .attr("dy", ".50em")
                        .text(function(d) { return d.articles + '0'; });                    
                   */
                    
                }
            }
        });
    });   
    
    
</script>

    <div class="section">
        <div class="container">
        	<div class="row">
        		<div class="col-md-5 col-sm-5">
                    <div class="service-wrapper">
                        <h3>Articles on JNP</h3>
                        <svg class="decades">
                        </svg>
                    </div>
                </div>
            </div>
        </div>
    </div>
-->
    <?php if (isset($terms) && isset($family_plants) && isset($family_top)) : ?>
        	<div class="row">
                <div class="col-md-1"></div>
                <div class="col-md-10">
                    <table class="table">
                        <tr>
                            <td width="35%">
                                <h3>Botanicule</h3>
                                <p>Exploring novelty space in Botanicals</p>
                                <a href="<?php echo base_url('/index.php/Dd/molecules/botan'); ?>">more</a>
                            </td>
                            <td rowspan="3">
                                <div class="service-wrapper">
                                    <h3>Diversity of Natural Products - Source families</h3>
                                    <hr/>
                                    <div id="tags">
                                        <ul>
                                            <?php 
                                            // start looping through the tags
                                                foreach ($terms as $term):
                                                    // determine the popularity of this term as a percentage
                                                    $percent = floor(($term['counter'] / $maximum) * 100);


                                                    // determine the class for this term based on the percentage
                                                    if ($percent < 20):
                                                        $class = 'tag1';
                                                    elseif ($percent >= 20 and $percent < 40):
                                                        $class = 'tag2';
                                                    elseif ($percent >= 40 and $percent < 60):
                                                        $class = 'tag3';
                                                    elseif ($percent >= 60 and $percent < 80):
                                                        $class = 'tag4';
                                                    else:
                                                        $class = 'tag5';
                                                    endif;
                                                ?>
                                                <li class="<?php echo $class; ?>">
                                                    <a href="search.php?search=<?php echo urlencode($term['term']); ?>"><?php echo $term['term']; ?></a>
                                                </li>
                                            <?php endforeach; ?>

                                        </ul>    
                                    </div> 
                                </div>
                            </td>
                        </tr>
                        <tr><td>
                            <h3>Microbicule</h3>
                            <p>Investigating microbes as production systems and novelty source</p>
                            <a href="#">more</a>
                        </td></tr>
                        <tr><td>
                            <h3>Marinicule</h3>
                            <p>Swimming the aquatic chemical diversity space</p>
                            <a href="#">more</a>
                        </td></tr>
                    </table>                    
                </div>
            </div>
    <br/><br/>
    <?php endif; ?>
<?php
    $this->load->view('/includes/footer');
?>