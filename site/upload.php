<?php
include 'config.php';
if (isset($_POST["message"]))
{
    $message = $_POST["message"];
}
echo $message;
$con= new mysqli($db_server,$db_user,$db_pass,$db_name);

if ($con->connect_error) {
    die("Connection failed: " . $con->connect_error);
    }

$stmt = $con->prepare("INSERT INTO messagelog (message) VALUES (?)");
$stmt->bind_param("s", $message);
if ($stmt->execute(); === TRUE) {
    echo "Success.";
} 
else {
    echo "Error: " . "<br>" . $con->error;
}

$stmt->close();
$conn->close();

$con->close();
?>
