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
    if get_tasks() != [] and task_id in range(1, get_id()):
        all_tasks = get_tasks()

        # Já está deletando o id corretamente, falta rearranjar os outros ids
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
            