<?php
    $file = fopen("/tmp/flag.txt", "r") or die("FLAG NOT FOUND");
    $flag = fread($file, filesize("/tmp/flag.txt"));
    fclose($file);
    setcookie("FLAG", $flag);
?>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Hidden</title>
</head>

<body>
    <h2>Hey You, yes you!<br>are you looking for a flag, well it's not here bruh!<br>Try someplace else<h2>
</body>

</html> 
