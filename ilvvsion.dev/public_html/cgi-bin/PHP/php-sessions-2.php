<?php

    session_start();

    setcookie("SESSID", session_id());

    $_SESSION["username"] = $name;
    

    echo "<html>";
    echo "<head>";
    echo "<meta http-equiv='Cache-Control' content='no-cache' />";
    echo "<meta http-equiv='Content-Type' content='text/html' />";
    echo "<title>Hello Team IJK</title>";
    echo "</head>";

    echo "<body>";
    echo "<h1 align=center>PHP Sessions Page 1</h1>";
    echo "<hr/>";

    if ($name) {
        echo "<p><b>Name:</b> $name";
    } else {
        echo "<p><b>Name:</b> You do not have a name set</p>";
    }

    echo "<br/><br/>";
    print "<a href=\"/cgi-bin/PHP/php-sessions-2.php\">Session Page 2</a><br/>";
    print "<a href=\"/../php-cgiform.html\">PHP CGI Form</a><br />";
    print "<form style=\"margin-top:30px\" action=\"/cgi-bin/PHP/php-destroy-session.php\" method=\"get\">";
    print "<button type=\"submit\">Destroy Session</button>";
    print "</form>";
    echo "</body>";

    echo "</html>";
?>