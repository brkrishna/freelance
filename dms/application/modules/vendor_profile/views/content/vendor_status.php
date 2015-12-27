<div class="span12 alert alert-info lead">
    Please review the below tracker to identify the progress of your vendor registration process
</div>
<div class="stepwizard">
    <div class="stepwizard-row">
        <div class="stepwizard-step">
        <?php if ($vendor_profile > 0) : ?>
            <button type="button" class="btn btn-success btn-circle">1</button>
        <?php else : ?>
            <button type="button" class="btn btn-warning btn-circle">1</button>
        <?php endif; ?>
        <p><a class="alert-link" href="content/vendor_profile">Profile</a></p>
        </div>
        <div class="stepwizard-step">
            <?php if ($vendor_address > 0) : ?>
                <button type="button" class="btn btn-success btn-circle">2</button>
            <?php else : ?>
                <button type="button" class="btn btn-warning btn-circle">2</button>
            <?php endif; ?>
            <p><a class="alert-link" href="content/vendor_address">Address</a></p>
        </div>
        <div class="stepwizard-step">
            <?php if ($vendor_contacts > 0) : ?>
                <button type="button" class="btn btn-success btn-circle">3</button>
            <?php else : ?>
                <button type="button" class="btn btn-warning btn-circle">3</button>
            <?php endif; ?>
            <p><a class="alert-link" href="content/vendor_contacts">Contacts</a></p>
        </div>
        <div class="stepwizard-step">
            <?php if ($vendor_factory > 0) : ?>
                <button type="button" class="btn btn-success btn-circle">4</button>
            <?php else : ?>
                <button type="button" class="btn btn-warning btn-circle">4</button>
            <?php endif; ?>
            <p><a class="alert-link" href="content/factory">Factory / Units</a></p>
        </div>
        <div class="stepwizard-step">
            <?php if ($vendor_bank > 0) : ?>
                <button type="button" class="btn btn-success btn-circle">5</button>
            <?php else : ?>
                <button type="button" class="btn btn-warning btn-circle">5</button>
            <?php endif; ?>
            <p><a class="alert-link" href="content/bank_details">Bank Details</a></p>
        </div> 
    </div>
</div>
