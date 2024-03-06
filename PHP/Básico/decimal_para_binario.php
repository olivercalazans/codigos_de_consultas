<?php

$numero   = readline("Informe um número: ");
$auxiliar = $numero;
$binario  = '';

while ($auxiliar > 0) {
    $resto  = $auxiliar % 2;
    $auxiliar = intdiv($auxiliar, 2);
    $binario .= (string)$resto;
};

$binario = strrev($binario);

echo "$numero em binário é $binario";
echo "\n";

?>