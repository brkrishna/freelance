<div class='container content'>
    <div class='row'>
       <div class="span12">
           <div class="row-fluid">
                <?php if (isset($current_user->role_id) && $current_user->role_id == 9) : ?>
                    <?php echo Modules::run('vendor_profile/vendor_status'); ?>
               <?php else : ?>
               
                <?php endif; ?>
           </div>
        </div>
    </div>
    <div class="row">
       <div class="span4">
            <div class="row-fluid">
                <?php if (isset($current_user->role_id) && $current_user->role_id <> 9) :
                        $can_view = $this->auth->has_permission('Todo.Content.View');
                        if ($can_view):
                            echo Modules::run('todo/top_todos');
                        endif;
                      else :
                        echo Modules::run('vendor_products/get_vendor_products'); 
                      endif; 
                ?>
            </div>
       </div>
       <div class="span4">
            <div class="row-fluid">
                <?php if (isset($current_user->role_id) && $current_user->role_id <> 9) :
                        $can_view = $this->auth->has_permission('Inquiries.Content.View');
                        if ($can_view):
                            echo Modules::run('inquiries/top_inquiries', 3); 
                        endif;
                      endif;
                ?>
            </div>
       </div>
       <div class="span4">
            <div class="row-fluid">
                <?php if (isset($current_user->role_id) && $current_user->role_id <> 9) : ?>
                    
                <?php else: ?>
                    
                <?php endif; ?>
            </div>
       </div>
	</div>
    <div class='row'>
        <div class='span12'>
            <div class='row-fluid'>
                <?php if (isset($current_user->role_id) && $current_user->role_id <> 9) : ?>
                     <?php echo Modules::run('purchase_orders/po_tracker'); ?>
                <?php else: ?>
                    <?php echo Modules::run('product_documents/get_product_docs_def'); ?>
                <?php endif; ?>
            </div>
       </div>
    </div>
    <div class='row-fluid'>
        <div class='span12'>
            <div class='row-fluid'>
                <?php if (isset($current_user->role_id) && $current_user->role_id <> 9) : ?>                    
                   
                <?php else: ?>
                <?php endif; ?>
            </div>
       </div>
    </div>
</div>
