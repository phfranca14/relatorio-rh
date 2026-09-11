import csv

funcionarios_antigos = []

def calcular_media(funcionarios):
    salarios = 0
    for funcionario in funcionarios:
        salarios += float(funcionario[2])

    return salarios / len(funcionarios)

with open('funcionarios.csv', 'r', encoding='utf-8', newline='') as f:
    leitor = csv.reader(f)
    next(leitor) # pula o cabeçalho
    for linha in leitor:
        if(int(linha[3]) >= 3):
            funcionarios_antigos.append(linha)

media_salarial = calcular_media(funcionarios_antigos)
print(f'R$ {media_salarial:.2f}'.replace(".", ","))

with open('relatorio_rh.csv', 'w', encoding='utf-8', newline='') as f:
    header = ['nome','departamento','salario','anos_empresa','faixa_salarial']
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)

    funcionarios = []

    for funcionario in funcionarios_antigos:
        salario = float(funcionario[-1])
        if salario > media_salarial:
            funcionario.append('Acima da média')
        elif salario < media_salarial:
            funcionario.append('Abaixo da média')
        else:
            funcionario.append('Salário na média...')
        funcionarios.append(funcionario)

    csv_writer.writerows(funcionarios)