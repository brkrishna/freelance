<div class="panel-group" id="accordion">
    <?php

        $first_level = 0;
        $curr_level = 0;

        if ($currentlink == '') { $currentlink = 'home'; }
        if ($left_menus != "") {
           
            foreach($left_menus as $row){
                if ($row->parent_id == $first_level and $curr_level > 0){
                    echo "</small></ul></div></div></div>";    
                }

                if ($row->parent_id == $first_level){

                    if (intval($row->questions) - intval($row->answers) == 0){
                        echo "<div class='panel panel-info'>";        
                    }else{
                        echo "<div class='panel panel-danger'>";        
                    }
                    
                    echo "<div class='panel-heading'>";
                    echo "<h5 class='panel-title'>";
                    echo "<a data-toggle='collapse' data-parent='#accordion' href='#" . $row->parent_id . "_" . $row->id . "'>";
                    echo $row->code . " " . $row->name;
                    echo "</a>";
                    echo "</h5>";
                    echo "</div>";
                    if ($row->id == 1){
                        echo "<div id='" . $row->parent_id . "_" . $row->id . "' class='panel-collapse collapse in'>";
                    }else{
                        echo "<div id='" . $row->parent_id . "_" . $row->id . "' class='panel-collapse collapse'>";
                    }
                }else if ($curr_level != $row->parent_id){

                    $curr_level = $row->parent_id;
                    echo "<div class='list-group'><ul class='list-group'><small>";


                    if ($row->questions - $row->answers == 0){
                        echo "<li class='list-group-item list-group-item-success'><a href=" . base_url('index.php/home/index/') . "/" . $row->id  .">" . $row->name . "</a><span class='badge'>" . ($row->questions - $row->answers) . " / " . $row->questions . "</span></li>";    
                    }else{
                        echo "<li class='list-group-item list-group-item-warning'><a href=" . base_url('index.php/home/index/') . "/" . $row->id  .">" . $row->name . "</a><span class='badge'>" . ($row->questions - $row->answers) . " / " . $row->questions . "</span></li>";    
                    }


                }else{

                    if ($row->questions - $row->answers == 0){
                        echo "<li class='list-group-item list-group-item-success'><a href=" . base_url('index.php/home/index/') . "/" . $row->id  .">" . $row->name . "</a><span class='badge'>" . ($row->questions - $row->answers) . " / " . $row->questions . "</span></li>";    
                    }else{
                        echo "<li class='list-group-item list-group-item-warning'><a href=" . base_url('index.php/home/index/') . "/" . $row->id  .">" . $row->name . "</a><span class='badge'>" . ($row->questions - $row->answers) . " / " . $row->questions . "</span></li>";
                    }

                    
                }       

             }
             echo "</ul></div></div></div>";
         }
    ?>
</div>