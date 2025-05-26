<?php
    include_once("./dbConn.php");
    include_once("./common.php");

    $_SESSION["id"] = "admin";

    $sql = "SELECT 
                * 
            FROM 
                agency_memberTBL 
            where 
                id = '{$_SESSION["id"]}'
            ";
    $query = mysqli_query($mysqli,$sql);
    $row = mysqli_fetch_array($query);

?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    main{
        width:95%;
        margin:30px auto 0px;
    }
</style>
<body>
    <div id="main">
        <div id="main_top">
            <h3>안녕하세요<?php echo $row["id"] ?> 님 !!! </h3>
            <div class="manu">

            </div>
        </div>
        <div id="main_center"></div>
        <div id="main_bottom"></div>
    </div>
</body>
</html>

<?php 


?>