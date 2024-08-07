tipo = input(f'''
-----------------------------------------------------------------------------------------------------------------
             selecione o padrao de Entrada : 
                1 ou 2
            1 -   x,xxxxxxxxxx
            
            2 -   2**x  * 1,xxxxxxxxx
-----------------------------------------------------------------------------------------------------------------             
\n''')

if tipo == '1':
    entrada = input(f'''
-----------------------------------------------------------------------------------------------------------------            
            infome os dados de entrada:
                  padrão :

                  +x,xxxxxx

                  -x,xxxxxx
-----------------------------------------------------------------------------------------------------------------
\n''')
    sinal = entrada[0]
    
    #convertendo para binário
    inteiro, decimal = (entrada).split(',')
    inteiro = int(inteiro[1:])
    decimal = "0." + decimal
    decimal = float(decimal)

    #convertendo a parte inteira
    inteiroBinario = ""

    restoConvertendo = inteiro % 2
    quocienteConvertendo = inteiro // 2

    inteiroBinario += str(restoConvertendo)

    while True:

        restoConvertendo = quocienteConvertendo % 2

        quocienteConvertendo = quocienteConvertendo // 2

        inteiroBinario += str(restoConvertendo)

        if quocienteConvertendo == 0:
            break
    
    #convertendo a parte decimal

    decimalBinario = ""

    mult = decimal * 2 

    parte_inteira_decimal = int(mult)

    parte_fracionaria_decimal = (mult) - parte_inteira_decimal

    decimalBinario += str(parte_inteira_decimal)

    mult = parte_fracionaria_decimal * 2 
    
    for i in range(7):
        parte_inteira_decimal = int(mult)

        parte_fracionaria_decimal = (mult) - parte_inteira_decimal

        decimalBinario += str(parte_inteira_decimal)

        mult = parte_fracionaria_decimal * 2

    #formatando a parte decimal 
    decimalLista = []
    for i in decimalBinario:
        decimalLista.append(int(decimalBinario[int(i)]))

    ultimoi = decimalLista[0] 

    for i in range(len(decimalLista)):
        if decimalLista[i] == 1:
            ultimoi = i + 1




numeroConvertido = inteiroBinario + ',' + decimalBinario[:ultimoi]
print(numeroConvertido)