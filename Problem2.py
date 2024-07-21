<?php

// Function to display a right-angle triangle of ones
function displayRightAngleTriangle() {
    for ($i = 1; $i <= 5; $i++) {
        echo str_repeat("1 ", $i) . "\n";
    }
}

// Function to display a palindromic triangle
function displayPalindromicTriangle() {
    for ($i = 1; $i <= 5; $i++) {
        $row = str_repeat("1 ", $i);
        echo $row . str_repeat("1 ", $i - 1) . "\n";
    }
}

// Function to display the help message
function displayHelp() {
    echo "This program allows you to display different types of triangles:\n";
    echo "1. Display a right-angle triangle of ones\n";
    echo "2. Display a Palindromic Triangle\n";
    echo "3. Help\n";
    echo "4. Exit\n";
}
// Main program loop
while (true) {
    // Display the menu
    echo "\nMenu:\n";
    echo "1. Display a right-angle triangle of ones\n";
    echo "2. Display a Palindromic Triangle\n";
    echo "3. Help\n";
    echo "4. Exit\n";

    // Get user input
    $choice = (int) readline("Enter your choice (1-4): ");

    // Handle the user's choice
    switch ($choice) {
        case 1:
            displayRightAngleTriangle();
            break;
        case 2:
            displayPalindromicTriangle();
            break;
        case 3:
            displayHelp();
            break;
        case 4:
            echo "Exiting the program...\n";
            exit;
        default:
            echo "Invalid choice. Please try again.\n";
            break;
    }
}
