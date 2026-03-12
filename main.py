tarefas = []

while True:
    print('-' *30)
    print('    Gerenciador de tarefas')
    print('-' *30)
    print('1 - Adiconar tarefa')
    print('2 - Ver tarefas')
    print('3 - Remover tarefa')
    print('4 - Sair do sistema')
    op = int(input('Digite o número da opção desejada:'))
    if op > 4 or op < 1:
        print('Erro tente novamente.')
        continue
    if op == 1:
        t = input('Digite a tarefa que deseja adicionar:').strip()
        tarefas.append(t)
    elif op == 2:
        if len(tarefas) == 0:
            print('Sem tarefas adiconadas, tente adicionar.')
            continue
        else:
            for p, v in enumerate(tarefas):
                print(f'{p +1} - {v}')
    elif op == 3:
        rem = int(input('Digite o número da tarefa que deseja remover:'))
        if rem <=0 or rem > len(tarefas):
            print('Erro, este número de tarefa não está na lista tente novamente.')
            continue
        else:
            rem -= 1
            del tarefas[rem]
    elif op == 4:
        print('Encerrando o sistema...')
        break
