<?php defined('BASEPATH') OR exit('No direct script access allowed');
$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');

?>
<div class="row">
    <div id="leftmenu" class="col-xs-3 col-md-3 right">
        <br/>
        <nav class="leftmenu">
            <ul class="nav nav-pills nav-stacked">
                <li><a href="<?php echo base_url('/index.php/CP/index'); ?>"><small>Back to Cell Products</small></a></li>
                <li><a href="<?php echo base_url('/index.php/Products/product/cells'); ?>">Cells</a></li>                        
                <li><a href="<?php echo base_url('/index.php/Products/product/reagents'); ?>">Reagents</a></li>
                <li><a href="<?php echo base_url('/index.php/Products/product/media'); ?>">Media</a></li>
            </ul>
        </nav>
    </div>
    <div class="col-xs-9 col-md-9 left">
        <br/><br/>
        <?php if ($category == 'cells') : ?>
            <p class="text-justify">
                <h1>Cells</h1>
                We provide an ideal cell systems to establish cell cultures or as a model for the study and exploitation of cell cultures 
                in fundamental and applied research. Our cell types are quality tested and are suitable for use as feeder layers for human 
                embryonic stem cell cultures and other cell culture applications requiring feeder layers. 
                <br/>
                All the cell types are extensively tested and guaranteed for quality and optimal performance.            
            </p>
        <?php elseif($category == 'media') : ?>
            <p class="text-justify">
                <h1>Media</h1>
                Sristi sources traditional supplements; that are needed, or recommended, to achieve optimal cell performance. 
                The products we offer allow researchers to prepare fresh medium in the laboratory, extending shelf life and enhancing 
                performance. The products offer guaranteed consistency and reproducible results. They help researchers to tailor the 
                culture system to provide the desired outcome. 
                <br/>
                Growth media products we offer initiate the culture, differentiation, expansion and maintenance of desired cell culture systems.                <br/>
            </p>
        <?php endif; ?>
        <ul class="nav nav-tabs">
            <li class="<?=$category === 'cells' ? 'active':''; ?>"><a href="<?php echo base_url("/index.php/Products/product/cells"); ?>">Cells</a></li>
            <li class="<?=($category ==='reagents')?'active':''?>"><a href="<?php echo base_url("/index.php/Products/product/reagents"); ?>">Reagents</a></li>
            <li class="<?=($category ==='media')?'active':''?>"><a href="<?php echo base_url("/index.php/Products/product/media"); ?>">Media</a></li>
        </ul>

        <?php echo $this->pagination->create_links(); ?>
        <br/>
        <table class="table table-striped">
            <tr>
                <th>Code</th>
                <th>Name</th>
                <th></th>
                <th>Specification Sheet</th>
                <th></th>
            </tr>
            <tbody>
                <?php foreach($records->result() as $record){  ?>
                <tr>
                    <td><?php echo ($record->product_code); ?></td>
                    <td><?php echo ($record->product_name); ?></td>
                    <td><img style="border-radius:15px;width:200px;height:200px;" src="<?php echo ($record->img_url); ?>" alt="<?=$record->product_name; ?>" /></td>
                    <?php if ($record->pdf_url != ''){  ?>
                        <td><a href="<?php echo ($record->pdf_url); ?>" target='_blank'>Spec Sheet</a></td>
                    <?php }else{ ?>
                        <td></td>
                    <?php } ?>
                    <td><a href="<?php echo base_url('/index.php/Contactus/inquire/' . $record->product_code); ?>">Inquire</a></td>
                </tr>
                <?php }
                ?>
            </tbody>
        </table>   
    </div>
</div>
<br/><br/>
<?php
    $this->load->view('/includes/footer');
?>