# Fonte 3-12V
 Circuito de uma fonte de 100mA de 3 a 12 volts
 Para executar o código com os cálculos dos valores finais obtidos (listados abaixo), execute:
    python script.py

Valores pré-determinados:
- Tensão máxima e mínima: 12v e 3v
- Queda de tensão entre a base e o emissor do transistor: 0.714547e (medido no falstad)
- Resistência do resistor à direita do potenciômetro: 2k7 (explicação abaixo)
- Ganho do transistor: 200 (explicação abaixo)
- Corrente máxima na base do transistor: 0.497512 mA (valor aproximado pode ser calculado a partir do ganho e da corrente máxima no emissor, de 100mA. Porém, esse valor exato foi o medido no falstad)
- Tensão mínima garantida pelo capacitor: 19v (o mesmo teve sua capacitância escolhida de modo a garantir esse valor)
- Tensão de quebra do diodo zener: 13v (explicação abaixo)

Valores calculados a partir dos definidos acima:
- Resistência máxima do potenciômetro: calculada em 4824.542038208146
- Resistência do resistor à esquerda do potenciômetro (entre o mesmo e o diodo zener): calculada em 132.27265783518087
- Resistência acima do diodo zener: calculada em 2743.1635834358294

# Preços dos Componentes
OBS: Preços atualizados em 20/06/2020
## Resistor à direita do potenciômetro
- 1 resistor 2k7 de 1/4 W (A potência real não passará de 7.5mW): R$0.08 ([loja](https://www.baudaeletronica.com.br/resistor-2k7-5-1-4w.html))
## Resistor à esquerda do potenciômetro
O valor calculado de 132.27265783518087 será aproximado por um resistor de 100R (a diferença na voltagem final é muito pequena)
- 1 resistor 100R de 1/4 W (A potência real não passará de 450uW): R$0.08 ([loja](https://www.baudaeletronica.com.br/resistor-100r-5-1-4w.html))
## Potenciômetro
O valor calculado de 4824.542038208146 será aproximado por um potenciômetro de 5k, que não deve ser rotacionado até o fim para uma tensão de 3V
- 1 Potenciômetro Linear de 5k com potência máxima de 0.2W (A potência real não passará de 17mW): R$ 1,09  ([loja](https://www.baudaeletronica.com.br/potenciometro-linear-de-5k-5000.html))
## Resistor acima do diodo zener
O valor calculado de 2743.1635834358294 será aproximado por um resistor de 2k7
- 1 resistor 2k7 de 1/4 W (A potência real não passará de 45mW): R$0.08 ([loja](https://www.baudaeletronica.com.br/resistor-2k7-5-1-4w.html))
## Capacitor
- 1 capacitor de 220uF e 35V (A tensão real não passará de 25V): R$ 0,38 (([loja](https://www.baudaeletronica.com.br/capacitor-eletrolitico-220uf-35v.html)))
## Diodo zener
- 1 diodo zener 1N4743 [13V / 1W] (A potência real não passará de 30mW): R$ 0,20  ([loja](https://www.baudaeletronica.com.br/diodo-zener-1n4743-13v-1w.html))
## Transformador
- 1 transformador de 127v para 18v, com corrente máxima 3A (A corrente real chegará próxima de 1.3A em cada ciclo ao carregar o capacitor, mas pode ultrapassar 2.6A no primeiro ciclo): R$ 49.99 ([loja](https://produto.mercadolivre.com.br/MLB-1300844398-transformador-1818v-3a-trafo-bivolt-_JM?quantity=1#position=1&type=item&tracking_id=ada41903-7303-418c-9af9-6d00176bfbd2))
## Ponte Retificadora
- 1 ponte retificadora KBPC1510: R$3.13 ([loja](https://www.baudaeletronica.com.br/ponte-retificadora-kbpc1510.html))
## Transistor
- 1 transistor NPN BC546 de ganho 200: R$0.24 ([loja](https://www.baudaeletronica.com.br/transistor-npn-bc546.html))

# O potenciômetro e resistores adjacentes
 No circuito, pode-se ver que existem dois resistores adjacentes ao potenciômetro.
 ## O resistor à direita
 O papel do resistor à direita do potenciômetro é limitar a corrente que passa pelo potenciômetro, reduzindo o gasto de energia.
 Porém, a sua resistência não pode ser muito alta, pois nesse caso a corrente que passa diretamente pelo potenciômetro seria muito pequena em relação à que passa pela base do transistor, o que faria a tensão final da fonte muito sensível a alterações na corrente.
 O seu valor (de 2k7) foi escolhido empiricamente após vários testes. Todos os outros componentes têm seus valores calculados a partir dessa escolha;

 ## O potenciômetro e o resistor à sua esquerda
 É garantido que a tensão em cima do diodo zener será sempre 13v. Assim, as resistências do resistor à esquerda do potenciômetro e do próprio potenciômetro podem ser calculadas para que a tensão de saída da fonte, a partir dos seguintes dados conhecidos:

- Resistência do resistor à direita do potenciômetro (definida em 2k7)
- Tensão do diodo zener (definida em 13v)
- Queda de tensão entre a base e o emissor do transistor (medida no falstad em 0.714547mV)
- Corrente máxima passando pela base do transistor (como o transistor usado tem um ganho de 200x, essa corrente é aproximadamente 1/200 de 100mA, medido no falstad como 497.512uA)

O código para esse cálculo está no arquivo script.py, nas funções get_R e get_Ra, além das linhas 44-48

# O diodo zener e o resistor acima dele
O diodo zener deve possuir uma tensão de quebra de 13v, para permitir produzir 12v na saída após a queda no transistor
O valor do resistor acima dele foi calculado para que a tensão mínima em cima do zener seja sempre 13v, usando as seguintes informações:

- Tensão mínima garantida pelo capacitor (19v no caso)
- Tensão de quebra do diodo zener (13v)
- Corrente passando pelo próprio resistor (calculada com as resistências do potenciômetro e dos resistores adjacentes a ele, valores encontrados anteriormente, além da corrente na base do transistor)

O código para esse cálculo está no arquivo script.py, nas funções get_max_Rz, get_ira e get_irb, além das linhas 50-57

Por não ser ideal, o diodo zener não "quebra" a tensão exatamente em 13v, mas um pouco abaixo, o que faz a tensão de saída oscilar um pouco

# O capacitor e o transformador
Foi escolhido um transformador de 127v para 18v e um capacitor de 220uF. Esses valores foram escolhidos para garantir uma tensão de no mínimo 19v no resistor acima do diodo zener, o qual teve seu valor calculado acima de modo a reduzir esse valor de 19v a um valor de no mínimo 13v (o excedente será absorvido pelo diodo zener).

# O transistor e a corrente de saída
Utilizando os calculos acima, é possível criar um circuito que forneça exatamente as tensões desejadas para a corrente de 100mA pedida. Porém, erros começam a ocorrer quando uma corrente menor que 100mA é fornecida.

Isso porque a corrente na base do transistor, a qual depende da corrente de saída da fonte, foi utilizada nos cálculos de todas as resistências em seu valor máximo.

Dessa forma, para reduzir a variação da tensão para correntes pequenas, foi escolhido um transistor de ganho de 200, de modo a diminuir a corrente de base.
 
