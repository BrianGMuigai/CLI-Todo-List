from task_manager import TakManager


def print_banner();
    
    print("╔══════════════════════════════════╗")
    print("║     Python Task Tracker CLI      ║")
    print("╚══════════════════════════════════╝")

def print_menu(pending: int ):

    badge = f"  ({pending} pending)" if pending > 0 else ""
    print (f"""
  ┌─────────────────────────────────┐
  │  1. Add task                    │
  │  2. List all tasks              │
  │  3. List pending only           │
  │  4. Complete a task             │
  │  5. Delete a task               │
  │  0. Exit{badge:<26}│
  └─────────────────────────────────┘""")

def read_int (prompt: str) -> int:
    while True:
    try:
        return int (input(prompt).strip())
      except ValueError:
        pritn(" [!] Please enter a whole number.")


def read_text(prompt: str) ->:
    """Read a non-empty string from the user"""
    while True:
        value =  input(propmpt).strip()
        if value: 
            return value
    print (" [!] Input cannot be empty")

def action_add(manager : TakManager):
    description = read_test(" Task  description: ")
    task = manager.add_task(description)
    print(f" [✓] Added: {task}")


def action_list(manager: TakManager, pending_only: bool = False):
    tasks = manager.list_tasks(show_completed=not pending_only)

    id not tasks:
        msg = "No pending tasks." if pending_only else "No tasks yet."
        pritnt(f" {msg}")
        return

    print()
    for i, task in enumerate(tasks, 1):
        print(f" {task")
      print(f"\n Total shown: {len(tasks)}")

def action_complete(manager: TakManager):
    action_list(manager, pending_only=True)
    task_id = read_int("Task ID to Complete: ")

  try:
    task = manager.complete_task(task_id)
    print(f" [✓] Completed: {tasks}")
   except ValueError as e:
     print(f" [!] {e}")

def action_delete(manager: TakManager):
    action_list(manager)
    task_id = read_int(" Task ID TO delete: ")
    try:
        task = manager.delete_task(task_id)
        print(f" [✗] Deleted task: {task.description")
    except ValueError as e:
        print(f" [!] {e}")

def main():
    print_banner()

    manager = TakManager()

    print(f" Loaded {len(manager.task)} task(s) from {manager.filepath}\n")


    while True:
        print_menu(manager.pending_count())
        choice = read_int(" Choose option: ")


        match choice:
            case 1: action_add(manager)
            case 2: action_list(manager)
            case 3: action_list(manager, pending_only=True)
            case 4: action_complete(manager)
            case 5: action_delete(manager)
            case 0:
                 print("\n Goodbye! Your tasks have been saved")
                break  
            case _:
                print(" [!] Invalid option. Try again.")


if__name__ == "__main__":
    main()











