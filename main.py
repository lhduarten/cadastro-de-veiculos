repositorio = [
    {
        "matricula": 1,
        "modelo": "kwid",
        "cor": "laranja",
        "ano": 2017
    }
]

matriculaAtual = 1
# menu de navegação
while True:
    print('--- BEM VINDO AO MENU ---')
    print('1 - Cadastrar veículo')
    print('2 - Listar todos')
    print('3 - Pesquisar veículo')
    print('4 - Editar veículo')
    print('5 - Excluir veículo')
    opcao = input('Selecione uma opção: ')
    
    if opcao == '6':
        print('Você saiu do sistema...')
        break
    elif opcao == '1':
        matriculaAtual += 1
        modelo = input('Digite o modelo do carro: ')
        cor = input('Digite a cor do carro: ')
        ano = int(input('Digite o ano do carro: '))
        veiculo = {
            "matricula": matriculaAtual,
            "modelo": modelo,
            "cor": cor,
            "ano": ano
        }
        
        repositorio.append(veiculo)
        print('Veículo cadastrado com sucesso!')
    elif opcao == '2':
        print('--- LISTA DE VEÍCULOS ---')
        for veiculo in repositorio:
            print(f"Matricula: {veiculo['matricula']}")
            print(f"Modelo: {veiculo['modelo']}")
            print(f"Cor: {veiculo['cor']}")
            print(f"Ano: {veiculo['ano']}")
            print('-'*50)
            
    elif opcao == '3':
        matricula = int(input('Digite a matricula do veículo: '))
        print('-'*50)
        for veiculo in repositorio:
            if veiculo['matricula'] == matricula:
                print(f"Matricula: {veiculo['matricula']}")
                print(f"Modelo: {veiculo['modelo']}")
                print(f"Cor: {veiculo['cor']}")
                print(f"Ano: {veiculo['ano']}")
                break
        else:
            print('Veículo não encontrado')
    elif opcao == 4:
        matricula = int(input('Digite a matricula do veículo: '))
        print('-'*50)
        for veiculo in repositorio:
            if veiculo['matricula'] == matricula:
                if veiculo['matricula'] == matricula:
                    veiculo['modelo'] = input('Digite o novo modelo do veiculo: ')
                    veiculo['cor'] = input('Digite a nova cor: ')
                    veiculo['ano'] = int(input('Digite o novo ano do veiculo: '))
                    print('Dados alterados com sucesso!')
                    break
                else:
                    print('veiculo não encontrado')
    elif opcao == '5':
        matricula = int(input('Digite a matricula do veiculo: '))
        print('-'*50)
        for veiculo in repositorio:
            if veiculo['matricula'] == matricula:
                repositorio.remove(veiculo)
                print('veiculo removido com sucesso!')
                break
        else:
            print('veiculo não encontrado!')
