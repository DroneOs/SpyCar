<?php

$hostname="localhost";

$databasename="spy_car";
$id="root";
$pass="";
  
$link=mysql_connect($hostname,$id,$pass)or die ("Error connecting to mysql");


mysql_select_db($databasename);

$result=mysql_query("select * from path",$link);
 



?>

