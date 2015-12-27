<div class='container'>
    <div class="row">
      
      <div class="span12"> 
        <ul class="nav nav-tabs pull-left">
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Product Development<b class="caret"></b></a>
                  <ul class="dropdown-menu">
                      <li><a href="#">Type</a></li>
                      <li><a href="#">Ingredients Evaluation</a></li>
                      <li><a href="#">Process Evaluation</a></li>
                      <li class="divider"></li>
                      <li><a href="#">Sampling</a></li>
                  </ul>
          </li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Approvals<b class="caret"></b></a>
              <ul class="dropdown-menu">
                    <li><a href="#">Certificate of Analysis</a></li>
                    <li><a href="#">Material Safety Data Sheet</a></li>
                    <li><a href="#">Hazard Analysis and Critical Control Points</a></li>
                    <li class="divider"></li>
                    <li><a href="#">GMP</a></li>
                    <li><a href="#">Organic Control Points</a></li>
                    <li class="divider"></li>
                    <li><a href="#">Submissions</a></li>
                    <li><a href="#">Audit facilitation</a></li>
                  </ul>
          </li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Maintenance<b class="caret"></b></a>
              <ul class="dropdown-menu">
                    <li><a href="#">Asset Log</a></li>
                    <li><a href="#">Preventive Maintenance</a></li>
                    <li><a href="#">Sanitation / Pest Management</a></li>
                    <li class="divider"></li>
                    <li><a href="#">Water Quality</a></li>
                    <li><a href="#">Air Quality</a></li>
                    <li class="divider"></li>
                    <li><a href="#">Resource Log</a></li>
                    <li><a href="#">Waste Disposal</a></li>
              </ul>
          </li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown"><span class="glyphicon glyphicon-book"></span>&nbsp;Processing/Handling<b class="caret"></b></a>
              <ul class="dropdown-menu">
                    <li><a href="#">Vendor Approvals</a></li>
                    <li><a href="#">Procurement</a></li>
                    <li><a href="#">Batch Planning</a></li>
                    <li class="divider"></li>
                    <li><a href="#">Floor Monitoring</a></li>
                    <li><a href="#">Store Monitoring</a></li>
                    <li class="divider"></li>
                    <li><a href="#">End Product Evaluation</a></li>
                    <li><a href="#">Maintenance</a></li>
                    <li><a href="#">Packing</a></li>
                    <li><a href="#">Transport</a></li>
                  </ul>
          </li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown"><span class="glyphicon glyphicon-list-alt"></span>&nbsp;Consignment<b class="caret"></b></a>
              <ul class="dropdown-menu">
                    <li><a href="#">Purchase Order</a></li>
                    <li><a href="#">Proforma Invoice</a></li>
                    <li><a href="#">Material Resource Planning</a></li>
                    <li class="divider"></li>
                    <li><a href="#">Packing List</a></li>
                    <li><a href="#">Commercial Invoice</a></li>
                    <li><a href="#">Bill of Lading</a></li>
                    <li class="divider"></li>
                    <li><a href="#">Origin Certificate</a></li>
                    <li><a href="#">Organic Transfer Certificate</a></li>
                    <li><a href="#">Phytosanitary Certificate</a></li>
                    <li><a href="#">Export Inspection Certificate</a></li>
                    <li><a href="#">Lab Report / Certificate of Analysis</a></li>
                  </ul>
          </li>
        </ul> 
        <h2 class="success"><i><center>Sristi Bio - Organic Integrity Flow</center></i></h2>      
      </div>
       <div class="span3">
           <?php echo Modules::run('standards_documents/listing'); ?>
        </div> 
       <div class="span4">
           <?php echo Modules::run('products/listing'); ?>
        </div> 
       <div class="span4">
           <?php echo Modules::run('ingredients/listing'); ?>
        </div> 
       <div class="span4">
           <?php echo Modules::run('labels/listing'); ?>
        </div> 
       <div class="span4">
           <?php echo Modules::run('party/units'); ?>
        </div> 
       <div class="span4">
           <?php echo Modules::run('party/vendors'); ?>
        </div> 
       <div class="span4">
           <?php echo Modules::run('consignment_documents/listing'); ?>
        </div> 
    </div>  
    <div class="row">
    </div>
    <div class="row">
    </div>
</div>