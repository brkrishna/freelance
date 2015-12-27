<form role="form" method="post" action="<?php echo base_url('index.php/home/save'); ?>">
    <table class="table table-striped table-condensed">
        <thead>
            <th>&nbsp;</th>
            <th>Question</th>
            <th>Answer</th>
        </thead>    
        <tbody>
            <?php       
                
                foreach($questions as $row){
                    echo "<tr>";    
                    echo "<td width='10%'>" . $row->code . "</td>";
                    echo "<td width='75%'>" . $row->short_desc . "</td>";
                    echo "<td width='15%'><select class='form-control input-sm' name=q_" . $row->id . ">";
                    echo "<option value='-2'";
                    echo $row->answer == '-2' ? 'selected' : ''; 
                    echo ">Select one</option>";
                    echo "<option value='1'";
                    echo $row->answer == '1' ? 'selected' : '';
                    echo ">Yes</option>";
                    echo "<option value='-1'";
                    echo $row->answer == '-1' ? 'selected' : '';
                    echo ">No</option>";
                    echo "<option value='0'";
                    echo $row->answer == '0' ? 'selected' : '';
                    echo ">NA</option>";

                    echo "</select></td>";
                    echo "</tr>";
                }
            ?>
        </tbody>                    
    </table>
    <button type="submit" name="b_submit" class="btn btn-default">Save</button>
</form>