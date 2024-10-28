
def print_menu():
    todo_menu = """
    #Todo List Menu#
    1. View Tasks
    2. Add a Task
    3. Remove a Task
    4. Exit
    """
    print(todo_menu)


def get_choice():
    while True:
        choice = input("Enter Your Choice: ")
        valid_choice = ('1', '2', '3', '4')
        if choice not in valid_choice:
            print("Invalid Choice!")
            continue
        else:
            return choice


def display_tasks(tasks):
    if not tasks:
        print("No Task in the list.")
        return
    for index, task in enumerate(tasks, start=1):
        print(f'{index}. {task}')


def add_task(tasks):
    while True:
        task = input("Enter a new task: ").strip()
        if len(task) != 0:
            tasks.append(task)
            break
        else:
            print("Invalid Task!")


def remove_task(tasks):
    display_tasks(tasks)

    while True:
        try:
            task_number = int(input('Enter the task number: '))
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid Task Number!")


def main():
    tasks = []
    while True:
        print_menu()

        choice = get_choice()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        else:
            break


if __name__ == "__main__":
    main()
