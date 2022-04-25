<?php
    echo "<html>";
    echo "<head>";
    echo "<meta http-equiv='Cache-Control' content='no-cache' />";
    echo "<meta http-equiv='Content-Type' content='text/html' />";
    echo "<title>Hello Team IJK</title>";
    echo "</head>";

    echo "<body>";
    echo "<h1 align=center>POST Request Echo</h1>";
    echo "<hr/>";
    echo "<p><b>Message Body:</b></p>";
    echo "<ul>";

    if(empty($_POST)) {

        echo "<li>(null)</li>";

    } else {
        
        foreach ($_POST as $key => $value) {
            
            echo "<li><b>" . $key . ":</b> " . $value . "</li>";
            
        }
    }
  
    echo "</ul>";
    echo "</body>";

    echo "</html>";

?>