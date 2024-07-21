<?php
// Function to convert decimal to binary
function decimalToBinary($decimal) {
    $binary = "";
    while ($decimal > 0) {
        $remainder = $decimal % 2;
        $binary = $remainder . $binary;
        $decimal = floor($decimal / 2);
    }
    return $binary ?: "0";
}

// Get user input
$decimalInput = (int) readline("Enter a decimal number: ");

// Convert decimal to binary
$binaryOutput = decimalToBinary($decimalInput);

// Display the result
echo "The binary equivalent of $decimalInput is: $binaryOutput\n";
?>
