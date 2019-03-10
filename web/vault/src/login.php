<?php
if (isset($_POST["submit"])) {
    $log_inned = false;
    if (isset($_POST["username"]) && $_POST["password"]) {
        $username = $_POST["username"];
        $password = $_POST["password"];
        $conn = new mysqli("database", "root", "password", "vault");
        $statement = "SELECT * FROM users WHERE username='". $username ."' AND password='".$password."'";
        if ($conn->connect_error) {
            die("Challenge is dead please contact admin");
        }
        $result = $conn->query($statement);
        if ($result->num_rows > 0) {
            $log_inned = true;
            $flagFd = fopen("/tmp/flag.txt","r") or die("challenge is dead please contact admin");
            $flag = fread($flagFd,filesize("/tmp/flag.txt"));
            setcookie("SESSIONID",base64_encode($flag));
        }
    } else {
        die("ACCESS DENIED");
    }
}
?>

<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Login</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="css/main.css">
</head>

<body>
    <div class="main">
        <h1 class="heading">
            <?php
                if($log_inned===true) {
                    echo "ACCESS GRANTED<br>";
                    echo "<img src=\"/flag.png\" alt=\"flag\"/>";
                } else {
                    echo "ACCESS DENIED";
                }
            ?>
        </h1>
    </div>
</body>
</html>