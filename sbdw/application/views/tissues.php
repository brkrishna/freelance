<?php defined('BASEPATH') OR exit('No direct script access allowed');
$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');

?>
<div class="row">
    <div class="col-md-10 col-sm-8">
        <ul class="nav nav-tabs">
            <li class="<?=($category === 'liver') ? 'active':''; ?>"><a href="<?php echo base_url("/index.php/Tissues/tissue/liver"); ?>">Liver</a></li>
            <li class="<?=($category ==='tumor')?'active':''?>"><a href="<?php echo base_url("/index.php/Tissues/tissue/tumor"); ?>">Tumor</a></li>
            <li class="<?=($category ==='fluorescent')?'active':''?>"><a href="<?php echo base_url("/index.php/Tissues/tissue/fluorescent"); ?>">Fluorescent</a></li>
            <li class="<?=($category ==='livertoxicology')?'active':''?>"><a href="<?php echo base_url("/index.php/Tissues/tissue/livertoxicology"); ?>">Liver Toxicology</a></li>
            <li class="<?=($category ==='oncology')?'active':''?>"><a href="<?php echo base_url("/index.php/Tissues/tissue/oncology"); ?>">Oncology</a></li>
            <li class="<?=($category ==='stemcells')?'active':''?>"><a href="<?php echo base_url("/index.php/Tissues/tissue/stemcells"); ?>">Stem Cells</a></li>
        </ul>
        <?php echo $this->pagination->create_links(); ?>
        <table class="table table-bordered table table-condensed">
            <caption><h3>3D Microtissues</h3></caption>
            <thead>
                <th>Category</th>
                <th>Code</th>
                <th>Name</th>
                <th></th>
            </thead>
            <tbody>
                <?php foreach($records->result() as $record){  ?>
                <tr>
                    <td><?php echo ($record->subcategory); ?></td>
                    <td><?php echo ($record->product_code); ?></td>
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


