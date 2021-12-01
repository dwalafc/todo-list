def menu():
    print("=== OPÇÕES ===")
    print("[A]dicionar")
    print("[V]isualizar todas")
    print("A[t]ualizar")
    print("[E]xcluir")
    print("[S]air")
    print("==============")

def show_tasks(task_list_param):
    if len(task_list_param) == 0:
        print("Não tenho tarefas!")
    else:   
        counter = 1
        for task in task_list_param:
            print("%d - %s" % (counter, task))
            counter += 1


def exit():
    print("==============")
    print("Saindo...")