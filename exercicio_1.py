"""
#### Exercício 1

Receba três notas (números decimais) de um aluno e imprima a média.

Exemplo:

Digite a primeira nota:
8.5
Digite a segunda nota:
7.0
Digite a terceira nota:
9.0

Resposta:
Média: 8.17

Dica: Use inputs para receber os dados! 
Lembre de converter ele para o tipo necessário!
Print na tela com "print"
"""

primeira_nota = float(input("Digite a 1ª nota: "))
segunda_nota = float(input("Digite a 2ª nota: "))
terceira_nota = float(input("Digite a 3ª nota: "))

print(f'Média das notas: {(primeira_nota + segunda_nota + terceira_nota)//3}')
