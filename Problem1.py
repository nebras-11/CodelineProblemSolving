<?php
// Get user input
$username = $_POST['username'];
$password = $_POST['password'];
$email = $_POST['email'];

// Validate Username
if (empty($username) || strlen($username) > 50) {
    echo "Invalid Username";
} else {
    echo "Valid Username";
}

// Validate Password
if (strlen($password) < 8) {
    echo "Password must be at least 8 characters long";
} elseif (!preg_match('/[!@#$%^&*(),.?":{}|<>]/', $password)) {
    echo "Password must contain at least one special symbol";
} elseif (!preg_match('/\d/', $password)) {
    echo "Password must have one or more numbers";
} elseif (!preg_match('/[A-Z]/', $password) || !preg_match('/[a-z]/', $password)) {
    echo "Password must have one or more uppercase and lowercase characters";
} else {
    echo "Valid Password";
}
// Validate Email
if (strpos($email, '@') === false) {
    echo "Email must contain the '@' symbol";
} elseif (!preg_match('/\w+@\w+\.\w+/', $email)) {
    echo "Email must have alphanumeric characters before and after the '@' symbol";
} elseif (substr_count($email, '.') < 1) {
    echo "Email must have letters having a '.' character in between after the '@' symbol";
} else {
    echo "Valid Email";
}
?>
