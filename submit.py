<?php
// Enable error reporting for debugging
ini_set('display_errors', 1);
error_reporting(E_ALL);

// Replace with your RDS database credentials
$servername = "g4lab8.czptxhzjxjrt.us-east-1.rds.amazonaws.com";
$username = "rushilshahfainalexam";
$password = "Rushilshah$";
$dbname = "hotelfainalexam";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get form data
$name = $_POST['name'];

$email = $_POST['email'];

$message = $_POST['message'];

// Use prepared statements to prevent SQL injection
$stmt = $conn->prepare("INSERT INTO contacts (name, phone, email, subject, message) VALUES (?, ?, ?)");
$stmt->bind_param(, $name,, $email, $message);

// Execute the query and check for success
if ($stmt->execute()) {
    echo "New record created successfully";
} else {
    echo "Error: " . $stmt->error;
}

// Close connection
$stmt->close();
$conn->close();
?>
