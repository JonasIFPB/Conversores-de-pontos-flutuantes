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

    ###########convertendo a parte inteira
    inteiroBinario = ""
    if inteiro == 1:
        inteiroBinario += '1'
    else:
        restoConvertendo = inteiro % 2
        quocienteConvertendo = inteiro // 2

        inteiroBinario += str(restoConvertendo)

        while True:
            if quocienteConvertendo == 1:
                break
            restoConvertendo = quocienteConvertendo % 2

            quocienteConvertendo = quocienteConvertendo // 2

            inteiroBinario += str(restoConvertendo)

        inteiroBinario += str(quocienteConvertendo)  

        inteiroBinario = inteiroBinario[::-1]

    ############convertendo a parte decimal

    decimalBinario = ""

    mult = decimal * 2 

    parte_inteira_decimal = int(mult)

    parte_fracionaria_decimal = (mult) - parte_inteira_decimal

    decimalBinario += str(parte_inteira_decimal)

    mult = parte_fracionaria_decimal * 2 
    
    for i in range(12):
        parte_inteira_decimal = int(mult)

        parte_fracionaria_decimal = (mult) - parte_inteira_decimal

        decimalBinario += str(parte_inteira_decimal)

        mult = parte_fracionaria_decimal * 2
    
    ##formatando a parte decimal 
    #decimalLista = []
    #for i in decimalBinario:
    #    decimalLista.append(int(decimalBinario[int(i)]))
    #
    #ultimoi = decimalLista[0] 
    #
    #for i in range(len(decimalLista)):
    #    if decimalLista[i] == 1:
    #        ultimoi = i + 1




    numeroConvertidoNFormatado = inteiroBinario + ',' + decimalBinario
    numeroConvertido = inteiroBinario + decimalBinario


    if inteiro > 0:
        numeroConvertido = numeroConvertido[0] + ',' + numeroConvertido[1::]


    else:
        for i in range(len(numeroConvertido)):
            if numeroConvertido[i] == '1':
                numeroConvertido = numeroConvertido[i] + ',' + numeroConvertido[i+1::]
                break

    #achando o valor da notação
    if numeroConvertidoNFormatado.find(',') < numeroConvertidoNFormatado.find('1'):
        expoente = (numeroConvertidoNFormatado.find(',') - numeroConvertidoNFormatado.find('1')) 

    else:
        expoente = (numeroConvertidoNFormatado.find(',') - numeroConvertidoNFormatado.find('1')) - 1

    mantissa = numeroConvertido[2::]

    #exposente mais 127

    expoente = int(expoente) + 127

    #convertendo para binário com 8 bits

    inteiroExpoente = ""
    if expoente == 1:
        inteiroExpoente += '1'
    else:
        restoExpoente = expoente % 2
        quocienteExpoente = expoente // 2
        inteiroExpoente += str(restoExpoente)
        while True:
            if quocienteExpoente == 1:
                break
            restoExpoente = quocienteExpoente % 2
            quocienteExpoente = quocienteExpoente // 2
            inteiroExpoente += str(restoExpoente)
        inteiroExpoente += str(quocienteExpoente)  
        inteiroExpoente = inteiroExpoente[::-1]
    print(len(inteiroExpoente))
    print(inteiroExpoente)
    print(len(mantissa))
    print(mantissa)

    if len(inteiroExpoente) < 8:
        for i in range(8 - len(inteiroExpoente)):
            inteiroExpoente += '0'
    
   
    if len(mantissa) < 23:
        for i in range(23 - len(mantissa)):
            mantissa += '0'
  

    
    if sinal == '+':
        sinal = "0"
    else:
        sinal = "1" 

    resultado = sinal + inteiroExpoente + mantissa





print(f'''

Número Convertido :   {resultado}


''')
