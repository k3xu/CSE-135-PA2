<?php

    echo "<html>";
    echo "<head>";
    echo "<meta http-equiv='Cache-Control' content='no-cache' />";
    echo "<meta http-equiv='Content-Type' content='text/html' />";
    echo "<title>Hello Team IJK</title>";
    echo "</head>";

    echo "<body>";
    echo "<h1 align=center>Environment Variables</h1>";
    echo "<hr/>";

    echo "<h2>Environment Variables</h2>";
    echo "<ul>";

    $env_array = getenv();

    foreach ($env_array as $key=>$value) {
        echo "<li><b>$key</b> : $value</li>";
    };

    echo "</ul>";

    echo "<h2>Server Variables</h2>";
    echo "<ul>";
    $env_array = getenv();

    foreach ($_SERVER as $key=>$value) {
        echo "<li><b>$key:</b> $value</li>";
    };

    echo "</ul>";
    echo "</body>";

    echo "</html>";
?>