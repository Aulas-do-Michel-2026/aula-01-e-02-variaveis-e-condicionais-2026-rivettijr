"""
#### Exercício 2

Uma fórmula recomenda 2mg de medicamento por kg de peso do paciente.

Peça o peso de uma pessoa e calcule a dose recomendada.

Exemplo:

Digite o peso do paciente (em kg):
70

Resposta:
Média: 140 mg
"""

peso = int(input('Digite o peso do paciente (Kg):'))
dose_recomendada = 2 * peso

print(f'Média: {dose_recomendada}')
