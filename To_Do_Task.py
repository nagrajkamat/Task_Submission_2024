tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully.")

def delete_task(task):
    task_index = find_task_index(task)
    if task_index is not None:
        del tasks[task_index]
        print(f"Task '{task}' deleted successfully.")
    else:
        print(f"Task '{task}' not found.")

def mark_completed(task):
    task_index = find_task_index(task)
    if task_index is not None:
        tasks[task_index]["completed"] = True
        print(f"Task '{task}' marked as completed.")
    else:
        print(f"Task '{task}' not found.")

def update_completed_task(task, new_task):
    task_index = find_task_index(task)
    if task_index is not None and tasks[task_index]["completed"]:
        tasks[task_index]["task"] = new_task
        print(f"Task '{task}' updated to '{new_task}'.")
    elif task_index is not None and not tasks[task_index]["completed"]:
        print(f"Task '{task}' is not completed yet. Complete the task before updating.")
    else:
        print(f"Task '{task}' not found.")

def find_task_index(task):
    for index, t in enumerate(tasks):
        if t["task"] == task:
            return index
    return None

def display_tasks():
    if tasks:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{idx}. {task['task']} - {status}")
    else:
        print("No tasks found.")

# Adding 10 tasks
add_task("Buy groceries")
add_task("Finish coding assignment")
add_task("Read a book")
add_task("Exercise for 30 minutes")
add_task("Call a friend")
add_task("Write a blog post")
add_task("Learn a new programming language")
add_task("Watch a movie")
add_task("Clean the house")
add_task("Plan the weekend")

# Displaying tasks
display_tasks()

# Marking a task as completed
mark_completed("Read a book")

# Updating a completed task
update_completed_task("Read a book", "Read two chapters of a book")

# Deleting a task
delete_task("Exercise for 30 minutes")

# Displaying tasks after modifications
display_tasks()
