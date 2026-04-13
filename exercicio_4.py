"""
#### Exercício 3 - Identificar se a variante está no gene BRCA1 - Versão 1.

Receba 2 inputs do usuário:
1) O cromossomo de uma variante. Ele virá escrito como texto e da seguinte forma "chr1", "chr2", etc.
2) A posição dessa variante. Será um número inteiro.

Responde:
"Sim" se ela estiver no BRCA1.
"Não" se ela não estiver.

Considere que a variante está no gene BRCA1 se estiver no cromossomo 17 (chr17), e se a posição estiver no intevalo de 41196312 a 41277500.

Obs: Tirei a localização daqui: https://grch37.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012048;r=17:41196312-41277500.

Exemplos:

----------------------------------

Digite o cromossomo: chrM
Digite a posição: 41196390
Resposta:
Não

----------------------------------

Digite o cromossomo: chr17
Digite a posição: 99
Resposta:
Não

----------------------------------

Digite o cromossomo: chr17
Digite a posição: 41196313
Resposta:
Sim

"""

# Receber a descrição do cromossomo da variante
cromossomo_variante = str(input("Digite o cromossomo: "))

# Receber a descrição do cromossomo da variante
posicao = int(input("Digite a posição: "))

#Limites gene BRCA1
inicio_brca1 = 41196312
fim_brca1 = 41277500

# Calculo sim x nao
if cromossomo_variante == "chr17" and inicio_brca1 <= posicao <= fim_brca1:
    print("Resultado: SIM")
else:
    print("Resultado: NÃO")
