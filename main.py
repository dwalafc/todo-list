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
            new_task = input("Digite o novo valor da tarefa: ")
            task_list[int(position)-1] = new_task

    elif op.upper() == "E":
        utils.show_tasks(task_list)
        if len(task_list) != 0:
            position = input("Digite o número da tarefa a ser excluida: ")
            del task_list[int(position)-1]

    else:
        print("Opção inválida!")

utils.exit()