<?php defined('BASEPATH') OR exit('No direct script access allowed');
$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');

?>
<div class="row">
    <div class="col-md-12 col-sm-12">
        <?php 
$uri_segment_1 = '';
$uri_segment_3 = '';
if($this->uri->segment(1) != ''){
    $uri_segment_1 = $this->uri->segment(1); 
}
if($this->uri->segment(3) != ''){
    $uri_segment_3 = $this->uri->segment(3);
} 

        ?>
        <ul class="nav nav-pills">
            <li class="<?=$uri_segment_1 === 'bonemarrow' ? 'top_menu_active':''; ?>"><a href="<?php echo base_url("/index.php/Bioresearch/bio/bonemarrow"); ?>">Bone Marrow</a></li>
            <?php if($uri_segment_1 !='Liver' && $uri_segment_1 !='Tumor' && $uri_segment_1 !='Fluorescent') : ?>
            <li class="<?=($uri_segment_1 ==='cordblood')?'top_menu_active':''?>"><a href="<?php echo base_url("/index.php/Bioresearch/bio/cordblood"); ?>">Cord Blood</a></li>
            <li class="<?=($uri_segment_1 ==='mobilizedperipheralblood')?'top_menu_active':''?>"><a href="<?php echo base_url("/index.php/Bioresearch/bio/mobilizedperipheralblood"); ?>">Mobilized Peripheral</a></li>
            <li class="<?=($uri_segment_1 ==='peripheralblood')?'top_menu_active':''?>"><a href="<?php echo base_url("/index.php/Bioresearch/bio/peripheralblood"); ?>">Peripheral</a></li>
            <li class="<?=($uri_segment_1 ==='diseasestate')?'top_menu_active':''?>"><a href="<?php echo base_url("/index.php/Bioresearch/bio/diseasestate"); ?>">Disease State</a></li>
            <li class="<?=($uri_segment_1 ==='tissueslides')?'top_menu_active':''?>"><a href="<?php echo base_url("/index.php/Bioresearch/bio/tissueslides"); ?>">Tissue Slides</a></li>
            <li class="<?=($uri_segment_1 ==='biopreservationmedia')?'top_menu_active':''?>"><a href="<?php echo base_url("/index.php/Bioresearch/bio/biopreservationmedia"); ?>">BioPreservation Media</a></li>
            <?php endif; ?>                                
        </ul>

        <?php echo $this->pagination->create_links(); ?>
        <table class="table table-bordered table table-condensed">
            <caption><h3>Human Bioresearch Products</h3></caption>
            <thead>
                <th>Category</th>
                <th>Code</th>
                <th>Source</th>
                <th>Cell Type</th>
                <th>Format</th>
                <th>State</th>
                <th>Quantity</th>
                <th>Name</th>
            </thead>
            <tbody>
                <?php foreach($records->result() as $record){  ?>
                <tr>
                    <td><?php echo ($record->subcategory); ?></td>
                    <td><?php echo ($record->product_code); ?></td>
                    <td><?php echo ($record->source); ?></td>
                    <td><?php echo ($record->cell_type); ?></td>
                    <td><?php echo ($record->format); ?></td>
                    <td><?php echo ($record->state); ?></td>
                    <td><?php echo ($record->quantity); ?></td>
                    <td><?php echo ($record->product_name); ?></td>
                </tr>
                <?php }
                ?>
            </tbody>
        </table>   

    </div>
</div>
<?php
    $this->load->view('/includes/footer');
?>


