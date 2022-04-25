<?php 
    echo "<html>";
    echo "<head>";
    echo "<meta http-equiv='Cache-Control' content='no-cache' />";
    echo "<meta http-equiv='Content-Type' content='text/html' />";
    echo "<title>Hello Team IJK</title>";
    echo "</head>";

    echo "<body>";
    echo "<h1 align=center>Hello Team IJK</h1>";
    echo "<hr/>";
    echo "<p>Hello Team IJK</p>";
    echo "<p>This page was generated with the PHP programming language</p>";
    echo "<p>This program was run at: " . date("Y/m/d") . "</p>";
    echo "<p>Your current IP address is: " . $_SERVER['REMOTE_ADDR'] . "</p>";
    echo "</body>";
    
    echo "</html>";
?>