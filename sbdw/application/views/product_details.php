<?php defined('BASEPATH') OR exit('No direct script access allowed');

$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');

?>
<div class="row">
    <div class="col-md-3 col-sm-3"></div>
    <div class="col-md-6 col-sm-6">
        <div class="service">
            <table class="table table-bordered">
                <caption><h3>Product Details</h3><hr/></caption>

                <?php foreach($records->result() as $record) : ?>
                <tr>
                    <td class="mol label">Product Code</td>
                    <td class="mol label">Product Name</td>
                </tr>
                <tr>
                    <td class="mol"><?php echo($record->product_code);?></td>
                    <td class="mol"><?php echo($record->product_name);?></td>
                </tr>
                <tr><td colspan="2" class="mol label">Images</td></tr>
                <tr>
                    <td colspan="2">
                        <div class="row">
                            <div class="col-xs-6 col-md-4">
                                <a href="#" class="thumbnail">
                                    <img src="<?php echo base_url('public/imgs/HMSC-Ad.jpg'); ?>" alt="HCEC-Ad">
                                </a>
                            </div>
                            <div class="col-xs-6 col-md-4">
                                <a href="#" class="thumbnail">
                                    <img src="<?php echo base_url('public/imgs/HMSC-BM.jpg'); ?>" alt="HMSC-BM">
                                </a>
                            </div>
                            <div class="col-xs-6 col-md-4">
                                <a href="#" class="thumbnail">
                                    <img src="<?php echo base_url('public/imgs/HMSC-WJ.jpg'); ?>" alt="HMSC-WJ">
                                </a>
                            </div>

                        </div>
                    </td>

                </tr>
                <tr>
                    <td class="mol label">Category</td>
                    <td class="mol label">PDF Document</td>

                </tr>
                <tr>
                    <td class="mol"><?php echo($record->subcategory);?></td>
                    <td class="mol label"><a href="http://www.lifelinecelltech.com/docs2/spc_hmsc_family_0613_v4_fc-0020_34_57_62-1.pdf">Spec Sheet</a></td>
                </tr>
                <?php endforeach; ?>
            </table>
        </div>
    </div>
</div>
<?php
    $this->load->view('/includes/footer');
?>

