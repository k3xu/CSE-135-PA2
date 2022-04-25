<?php
    echo "<meta http-equiv='Cache-Control' content='no-cache' />";
    echo "<meta http-equiv='Content-Type' content='text/html' />";

    $myObj->title = "Hello";
    $myObj->heading = "Hello, Team IJK";
    $myObj->message = "This page was generated with the Perl programming language";
    $myObj->time = date("Y-m-d h:i:s");
    $myObj->IP = $_SERVER['REMOTE_ADDR'];
    
    $myJSON = json_encode($myObj, JSON_PRETTY_PRINT);

    echo $myJSON;
?>