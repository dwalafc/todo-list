# CRUD
task_list = []

def show_tasks():
    if len(task_list) == 0:
        print("Não tenho tarefas!")
    else:   
        counter = 1
        for task in task_list:
            print("%d - %s" % (counter, task))
            counter += 1

print("=== OPÇÕES ===")
print("[A]dicionar")
print("[V]isualizar todas")
print("A[t]ualizar")
print("[E]xcluir")
print("[S]air")
print("==============")

while True:
    op = input("Digite uma opção: ")
    if op.upper() == "S":
        break
    
    elif op.upper() == "A":
        task = input("Digite uma tarefa: ")
        task_list.append(task)

    elif op.upper() == "V":
        show_tasks()
    
    elif op.upper() == "T":
        show_tasks()
        position = input("Digite o número da tarefa a ser alterada: ")
        new_task = input("Digite o novo valor da tarefa: ")
        task_list[int(position)-1] = new_task

    elif op.upper() == "E":
        show_tasks()
        position = input("Digite o número da tarefa a ser excluida: ")
        del task_list[int(position)-1]

    else:
        print("Opção inválida!")

print("==============")
print("Saindo...")