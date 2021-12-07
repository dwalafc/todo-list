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

def is_position_valid(task_list_param, position_param):
    isValid = False
    if position_param.isnumeric():
        if int(position_param) > 0 and int(position_param) <= len(task_list_param):
            isValid = True
    
    return isValid
