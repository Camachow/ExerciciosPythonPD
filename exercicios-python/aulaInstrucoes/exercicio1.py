salario_hora = 20
horas_semanais = 40

salario_bruto = salario_hora * horas_semanais * 4
desconto_inss = salario_bruto * 0.01
desconto_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - desconto_inss - desconto_sindicato

print("Salário bruto: ", salario_bruto)
print("Desconto INSS: ", desconto_inss)
print("Desconto Sindicato: ", desconto_sindicato)
print("Salário líquido: ", salario_liquido)
