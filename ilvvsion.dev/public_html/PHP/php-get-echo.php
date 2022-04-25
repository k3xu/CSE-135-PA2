<?php
    echo "<html>";
    echo "<head>";
    echo "<meta http-equiv='Cache-Control' content='no-cache' />";
    echo "<meta http-equiv='Content-Type' content='text/html' />";
    echo "<title>Hello Team IJK</title>";
    echo "</head>";

    echo "<body>";
    echo "<h1 align=center>GET Request Echo</h1>";
    echo "<hr/>";
    echo "<p><b>Raw Query String:</b> " . $_SERVER['QUERY_STRING'] . "</p>";
    echo "<p>Formatted Query String:</p>";
    echo "<ul>";

    if (strlen($_SERVER['QUERY_STRING']) > 0){

        $query = proper_parse_str($_SERVER['QUERY_STRING']);

        foreach($query as $key=>$value) {
            echo "<li><b>" . $key . ":</b> " . $value . "</li>\n\n";
        }
    }

    echo "</ul>";
    echo "</body>";

    echo "</html>";

    # https://www.php.net/manual/en/function.parse-str.php#76792
    function proper_parse_str($str) {
        # result array
        $arr = array();
      
        # split on outer delimiter
        $pairs = explode('&', $str);
      
        # loop through each pair
        foreach ($pairs as $i) {
          # split into name and value
          list($name,$value) = explode('=', $i, 2);
         
          # if name already exists
          if( isset($arr[$name]) ) {
            # stick multiple values into an array
            if( is_array($arr[$name]) ) {
              $arr[$name][] = $value;
            }
            else {
              $arr[$name] = array($arr[$name], $value);
            }
          }
          # otherwise, simply stick it in a scalar
          else {
            $arr[$name] = $value;
          }
        }
      
        # return result array
        return $arr;
      }
?>