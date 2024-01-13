<?php

$a = readline('INforme o valor de A: ');
$b = readline('INforme o valor de B: ');
$c = readline('INforme o valor de C: ');

$delta = ($b**2) - (4 * $a * $c);
$x = (($b * -1) + $delta**(1/2)) / 2 * $a;

if ($delta == 0) {
    echo "O delta de A, B e C é zero. Então só existe uma raiz que é $x";
} else if ($delta > 0) {
    $x2 = (($b * -1) - $delta**(1/2)) / 2 * $a;
    echo "As raizes são: $x e $x2";
} else {
    echo 'O delta é menor que zero. Então não existe solução real';
};

echo "\n"

?>