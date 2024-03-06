<?php

function verificandoValor($frase) {
    while (true) {
        $valor = readline($frase);
        if ($valor == 0) {
            echo 'Informe um número DIFERENTE de zero';
        } else {
            return $valor;
            break;
        };
    };
};

$inicial = verificandoValor("Informe o valor inicial: ");
$razao   = verificandoValor("Informe o valor da razão: ");
$quantidade = verificandoValor("Informe a quantidade de números: ");
$posicao = verificandoValor("Informe a posição do valor que deseja: ");

$quantidade = abs($quantidade);
$contador = 1;
$soma = 0;
$resultado = '';

while ($contador <= $quantidade) {
    $resultado .= $inicial . ', ';
    $soma += $inicial;
    $inicial *= $razao;
    $contador += 1;
    if ($contador == $posicao) {
        $valor = $inicial;
    };
};

if ($razao == 1) { echo "\nProgreção geometrica constante";} 
else if ($inicial > 0 && $razao > 0) { echo "\nProgreção geometrica crescente";} 
else if ($inicial < 0 && $razao > 0) { echo "\nProgreção geometrica decrescente";}
else { echo "\nProgreção geometrica oscilante";};

echo "\nA soma dos valores é $soma";
echo "\nO valor da posição $posicao é $valor";
echo "\n$resultado";

?> 