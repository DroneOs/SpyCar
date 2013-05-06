<?php
$file1=$_POST['formvar'];
echo "$file1";


include("dbconnect.php"); 
$query="INSERT INTO path (coordinates)
VALUES('$file1')";
mysql_query($query) or die(mysql_error()); 
mysql_close();

?>
