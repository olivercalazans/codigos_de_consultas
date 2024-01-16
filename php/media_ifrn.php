<?php

echo "1 - Nota do segundo bimestre\n";
echo "2 - Nota da prova final\n";
$notaEscolhida = readline(">>");

if ($notaEscolhida == 1) {
    $notaDoPrimeiroBimestre = readline("Informe a nota do primeiro bimestre: ");
    $notaMinimaDoSegundoBimestre = (300 - (2 * $notaDoPrimeiroBimestre)) / 3;
    echo "Nota necessária para o segundo bimestre: $notaMinimaDoSegundoBimestre";
} else if ($notaEscolhida == 2) { 
    $notaDoPrimeiroBimestre = readline("Informe a nota do 1° bimestre: ");
    $notaDoSegundoBimestre  = readline("Informe a nota do 2° bimestre: ");

    $media = (($notaDoPrimeiroBimestre * 2) + ($notaDoSegundoBimestre * 3)) / 5;
    if ($media >= 60) {
        echo "Você já tem suficiente para passar. Média: $media";
    } else if ($notaDoPrimeiroBimestre > $notaDoSegundoBimestre) { 
        $notaMinimaNaFinal = (300 - (2 * $notaDoPrimeiroBimestre)) / 3;
        echo "Nota mínima na prova final: $notaMinimaNaFinal, substituirá a nota do 2° bimestre";
    } else { 
        $notaMinimaNaFinal = (300 - (3 * $notaDoSegundoBimestre)) / 2;
        echo "Nota mínima na prova final: $notaMinimaNaFinal, substituirá a nota do 1° bimestre";
    };
echo "\n";

};

?>