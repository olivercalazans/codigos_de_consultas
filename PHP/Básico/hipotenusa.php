<?php

$ax = readline('valor de A no eixo X: ');
$ay = readline('valor de A no eixo Y: ');
$bx = readline('valor de B no eixo X: ');
$by = readline('valor de B no eixo Y: ');

$h = (($bx + $ax)**2 + ($by + $ay)**2) ** (1/2);

echo "Adistancia entre os pontos A e B é $h";
echo "\n";

?>