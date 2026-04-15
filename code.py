# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress
import json

def get_tasks():
    try:
        with open("db.json", "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        return []

def get_id():
    try:
        with open("db.json", "r", encoding="utf-8") as f:
            for i in json.load(f):
                pass

            return i["id"]

    except FileNotFoundError:
        return 0

def set_new_task(task):
    all_tasks = get_tasks()
    new_id = get_id() + 1

    all_tasks.append({"id": new_id, "task": task, "status": "not done"})

    with open("db.json", "w", encoding="utf-8") as f:
        json.dump(all_tasks, f, indent=4)

def update_task(task_id, task_status="in progress"):
    all_tasks = get_tasks()

    for i in all_tasks:
        if i["id"] == task_id:
            i["status"] = task_status
            break

    all_tasks[task_id-1] = i

    with open("db.json", "w", encoding="utf-8") as f:
        json.dump(all_tasks, f, indent=4)

# A função delete_task deve além de deletar a tarefa com id informado, rearranjar os ids
def delete_task(task_id):
    if get_tasks() != [] and task_id in range(1, get_id()+1):
        all_tasks = get_tasks()

        pre_tasks = []
        post_tasks = []
        
        for i in all_tasks:
            if i["id"] < task_id:
                pre_tasks.append(i)
            
            elif i["id"] > task_id:
                post_tasks.append(i)
                
        for j in post_tasks:
            j["id"] -= 1
            
        all_tasks = pre_tasks + post_tasks
        

        with open("db.json", "w", encoding="utf-8") as f:
            json.dump(all_tasks, f, indent=4)
            
while True:
    user_input = input("")
    commands = user_input.split(" ", 1)
    
    try:
        if commands[1].strip() == "":
            commands.pop()
            
    except IndexError:
        pass
    
    match (commands[0]):
        
        case "add":
            try:
                set_new_task(commands[1])
            
            except IndexError:
                print("Informe a tarefa a ser inserida.")
        
        case "update":
            pass
        
        case "delete":
            try:
                id = int(commands[1])
                delete_task(id)
            
            except ValueError:
                print("Tarefa não encontrada.")
                
            except IndexError:
                print("Informe o ID da tarefa a ser deletada.")
        
        case "list":
            for i in get_tasks():
                print(f"{i["id"]} - {i["task"]}: {i["status"]}")
        
        case "exit":
            break
        
        case _:
            print(f"Comando '{commands[0]}' não encontrado.")