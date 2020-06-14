# Fonte 3-12V
 Circuito de uma fonte de 100mA de 3 a 12 volts

# O potenciômetro e resistores adjacentes
 No circuito, pode-se ver que existem dois resistores adjacentes ao potenciômetro.
 ## O resistor à direita
 O papelo do resistor à direita do potenciômetro é limitar a corrente que passa pelo potenciômetro, reduzindo o gasto de energia.
 Porém, a sua resistência não pode ser muito alta, pois nesse caso a corrente que passa diretamente pelo potenciômetro seria muito pequena em relação à que passa pela base do transistor, o que faria a tensão final da fonte muito sensível a alterações na corrente.
 O seu valor (de 2k) foi escolhido empiricamente após vários testes. Todos os outros componentes têm seus valores calculados a partir dessa escolha;

 ## O potenciômetro e o resistor à sua esquerda
 É garantido que a tensão em cima do diodo zener será sempre 13v. Assim, as resistências do resistor à esquerda do potenciômetro e do próprio potenciômetro podem ser calculadas para que a tensão de saída da fonte, a partir dos seguintes dados conhecidos:
    - Resistência do resistor à direita do potenciômetro (definida em 2k)
    - Tensão do diodo zener (definida em 13v)
    - Queda de tensão entre a base e o emissor do transistor (medida no falstad em 0.714612mV)
    - Corrente máxima passando pela base do transistor (como o transistor usado tem um ganho de 400x, essa corrente é aproximadamente 1/400 de 100mA, medido no falstad como 249.377uA)
O código para tal cálculo está no arquivo script.py, nas funções get_R e get_Ra, além das linhas 44-48

# O diodo zener e o resistor acima dele
O diodo zener deve possuir uma tensão de quebra de 13v, para permitir produzir 12v na saída após a queda no transistor
O valor do resistor acima dele foi calculado para que a tensão mínima em cima do zener seja sempre 13v, usando as seguintes informações:
    - Tensão mínima garantida pelo capacitor (18v no caso)
    - Tensão de quebra do diodo zener (13v)
    - Corrente passando pelo próprio resistor (calculada com as resistências do potenciômetro e dos resistores adjacentes a ele, valores encontrados anteriormente, além da corrente na base do transistor)
Por não ser ideal, o diodo zener não "quebra" a tensão exatamente em 13v, mas um pouco abaixo, o que faz a tensão de saída oscilar um pouco

# O capacitor e o transformador
Foi escolhido um transformador de razão 0.15 e um capacitor de 150uF. Esses valores foram escolhidos para garantir uma tensão de no mínimo 18v no resistor acima do diodo zener, o qual teve seu valor calculado acima de modo a reduzir esse valor de 18v a um valor de no mínimo 13v (o excedente será absorvido pelo diodo zener).

# O transistor e a corrente de saída
Utilizando os calculos acima, é possível criar um circuito que forneça exatamente as tensões desejadas para a corrente de 100mA pedida. Porém, erros começam a ocorrer quando uma corrente menor que 100mA é fornecida.

Isso porque a corrente na base do transistor, a qual depende da corrente de saída da fonte, foi utilizada nos cálculos de todas as resistências em seu valor máximo.

Dessa forma, para reduzir a variação da tensão para correntes pequenas, foi escolhido um transistor de ganho de 400x, de modo a diminuir a corrente da base do mesmo.
 