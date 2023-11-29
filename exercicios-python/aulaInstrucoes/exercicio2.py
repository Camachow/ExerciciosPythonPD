""" Altere o programa anterior para a partir dos valores de horas trabahadas 
por semana e salário por horas calcular em duas intruções:
(1) Salario semanal bruto
(2) Salario semanal liquido com todos os descontos
Para a segunda intrução, realize todos os calculos em uma expressão composta.
 """

salario_hora = 20
horas_semanais = 40

salario_bruto = salario_hora * horas_semanais
salario_liquido = salario_bruto - salario_bruto * 0.01 - salario_bruto * 0.05

print("Salário bruto: ", salario_bruto)
print("Salário líquido: ", salario_liquido)

