import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ToDoApp')


def show_options():
    """
    Display Sign In and Sign Up options to the user.
    Get users option and return it
    """
    print("Welcome to ToDoApp")
    print("Please choose one of the following options:")
    print("1. Sign Up")
    print("2. Sign In")
    user_choice = input("Option number: ")
    return user_choice


def do_sign_up():
    """
    Register new user using the provided credentials
    """
    print("User registration")
    print("Please choose a username that is not longer than 8 characters\n")
    username = input("Username: ")
    print("\nPlease choose a password that is longer than 8 characters,")
    print("and container a upper and a lower case character,")
    print("and one special character\n")
    password = input("Password: ")
    return [username, password]


def show_todo_list():
    """
    Show current todo list and get user action choice
    """
    todo_list = SHEET.worksheet("todo_list").get_all_values()
    print("ToDo List:")

    for ind in range(1, len(todo_list)):
        print(f"{ind}. {todo_list[ind][1]}")

    get_task_action()

    return todo_list


def get_task_action():
    """
    Get action of user and apply
    """
    print("Please select a action from below:")
    user_choice = input("add[a], delete[d], edit[e], quit[q]: ")
    if user_choice == 'a':
        print('add task')
        add_task()
    elif user_choice == 'd':
        print('delete task')
        remove_task()
    elif user_choice == 'e':
        print('edit')
    elif user_choice == 'q':
        print('Until next time...')
    else:
        print('option not valid')


def add_task():
    """
    Ask user for task and add it to the google sheet
    """
    print("Please input task description")
    task = input("Task: ")
    update_worksheet(['stefan', task], 'todo_list')
    print("Finished updating the task list")
    show_todo_list()


def remove_task():
    """
    Ask user what is the task number of the task to be
    removed and remove that task
    """
    print("Please input the number of the task to be removed")
    task_num = int(input("Task number: "))
    confirmation = input(
            f"Are you sure you wish to remove task number: {task_num}? Y/N: "
        )
    if confirmation.lower() == 'y':
        print("Removing task")
        worksheet_to_update = SHEET.worksheet('todo_list')
        worksheet_to_update.delete_rows(task_num + 1)

    show_todo_list()


def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully.\n")


# update_worksheet(['test_user', 'test_password'], 'users')
# option = show_options()
# print(option)
# new_user = do_sign_up()
# update_worksheet(new_user, 'users')
show_todo_list()
