<?php

$numero = readline("Informe um número: ");

if ($numero % 2 == 0) {
    $imparOuPar = 'par';
} else {
    $imparOuPar = 'impar';
};

if ($numero == 0) {
    echo "O número nulo";
} else if ($numero >= 1) {
    echo "O número é positivo e $imparOuPar ";
} else if ($numero <= -1) {
    echo "O número é negativo e $imparOuPar";
};
echo "\n";

?>