import utils

task_list = []

utils.menu()

while True:
    op = input("Digite uma opção: ")
    if op.upper() == "S":
        break
    
    elif op.upper() == "A":
        task = input("Digite uma tarefa: ")
        task_list.append(task)

    elif op.upper() == "V":
        utils.show_tasks(task_list)
    
    elif op.upper() == "T":
        utils.show_tasks(task_list)
        if len(task_list) != 0:
            position = input("Digite o número da tarefa a ser alterada: ")
            if utils.is_position_valid(task_list, position):
                new_task = input("Digite o novo valor da tarefa: ")
                task_list[int(position)-1] = new_task
            else:
                print("Não foi possível atualizar a lista de tarefas!")

    elif op.upper() == "E":
        utils.show_tasks(task_list)
        if len(task_list) != 0:
            position = input("Digite o número da tarefa a ser excluida: ")
            if utils.is_position_valid(task_list, position):
                del task_list[int(position)-1]
            else:
                print("Não foi possível excluir a tarefa!")

    else:
        print("Opção inválida!")

utils.exit()