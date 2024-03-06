<?php

$peso   = readline("Informe seu peso: ");
$altura = readline("Informe sua altura: ");

$imc = $peso / $altura ** 2;

if ($imc >= 40) {
    echo 'Classificação: OBESIDADE GRAU III OU MÓRBIDA.';
} else if ($imc >= 35) {
    echo 'Classificação: OBESIDADE GRAU II';
} else if ($imc >= 30) {
    echo 'Classificação: OBESIDADE GRAU I';
} else if ($imc >= 25) {
    echo 'Classificação: SOBREPESO';
} else if ($imc >= 20) {
    echo 'Classificação: PESO NORMAL';
} else {
    echo 'Classificação: ABAIXO DO PESO';
};

echo "\n";

?>