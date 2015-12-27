<?php defined('BASEPATH') OR exit('No direct script access allowed');

$this->load->view('/includes/head');
$this->load->view('/includes/topmenu');

?>
<div class="section">
    <div class="container">
        <div class="row">
            <div class="col-md-6 col-sm-6">
                <div class="service-wrapper">
                   <table class="table table-bordered">
                    <caption><h3>3D Microtissues Details</h3><hr/></caption>
                      
                <?php foreach($records->result() as $record) : ?>
                       <tr>
                            <td class="mol label">Product Code</td>
                            <td class="mol label">Product Name</td>
                        </tr>
                        <tr>
                            <td class="mol"><?php echo($record->product_code);?></td>
                            <td class="mol"><?php echo($record->product_name);?></td>
                        </tr>
                        <tr>
                            <td class="mol label">Category</td>
                            <td class="mol label">PDF Document</td>
                            
                        </tr>
                        <tr>
                            <td class="mol"><?php echo($record->subcategory);?></td>
                             <td class="mol label"><a href="http://www.insphero.com/images/LiverMT_Product_Guide_FinalLR.PDF">Spec Sheet</a></td>
                        </tr>
                       <?php endforeach; ?>
                     </table>
                </div>
            </div>
         </div>
      </div>
   </div>            
<?php
    $this->load->view('/includes/footer');
?>

