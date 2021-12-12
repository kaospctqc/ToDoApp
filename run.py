import gspread
from google.oauth2.service_account import Credentials
from getpass import getpass

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
    user_choice = input("Option number:\n")
    return user_choice


def check_username(username):
    """
    Verify if provided user is in the user list
    """
    user_list = SHEET.worksheet("users").col_values(1)
    if username in user_list:
        return True


def check_password(username):
    """
    Verify password for the provided user
    """
    return


def get_username():
    """
    Get username from user input
    """
    print("Please choose a username that is not longer than 8 characters\n")
    username = input("Username:\n")

    return username


def get_password():
    """
    Get password form user input
    """
    print("\nPlease choose a password that is longer than 8 characters,")
    print("and container a upper and a lower case character,")
    print("and one special character\n")
    password = getpass("Password:\n")
    return password


def do_sign_up():
    """
    Register new user using the provided credentials
    """
    print("User registration")
    username = get_username()
    while check_username(username):
        print(f"\nThe '{username}' username is not available!")
        print("Please try a different option\n")
        username = get_username()

    password = get_password()
    update_worksheet([username, password], 'users')

    return username


def do_sign_in():
    """
    Sign in existing user using the provided credentials
    """
    print("User sign in")
    username = get_username()
    password = get_password()
    while check_password(password):
        password = get_password()

    return username


def show_todo_list(username):
    """
    Show current todo list and get user action choice
    """
    todo_list = SHEET.worksheet("todo_list").get_all_values()
    print("ToDo List:\n")
    print("ID Description")

    for ind in range(1, len(todo_list)):
        if todo_list[ind][0] == username:
            print(f"{ind}. '{todo_list[ind][1]}'")

    get_task_action(username)

    return todo_list


def get_task_action(username):
    """
    Get action of user and apply
    """
    print("Please select a action from below:")
    user_choice = input("add[a], delete[d], edit[e], quit[q]:\n")
    if user_choice == 'a':
        print('add task')
        add_task(username)
    elif user_choice == 'd':
        print('delete task')
        remove_task(username)
    elif user_choice == 'e':
        print('edit')
    elif user_choice == 'q':
        print('Until next time...')
    else:
        print('option not valid')


def add_task(username):
    """
    Ask user for task and add it to the google sheet
    """
    print("Please input task description")
    task = input("Task:\n")
    update_worksheet([username, task], 'todo_list')
    print("Finished updating the task list")
    show_todo_list(username)


def remove_task(username):
    """
    Ask user what is the task ID of the task to be
    removed and remove that task
    """
    print("Please input the ID of the task to be removed")
    task_num = int(input("Task ID: "))
    confirmation = input(
            f"Are you sure you wish to remove task ID: {task_num}? Y/N:\n"
        )
    if confirmation.lower() == 'y':
        print(f"Removing task ID {task_num}\n")
        worksheet_to_update = SHEET.worksheet('todo_list')
        worksheet_to_update.delete_rows(task_num + 1)

    show_todo_list(username)


def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully.\n")


def main():
    """
    Run all program functions
    """
    option = show_options()
    if option == '1':
        username = do_sign_up()
    elif option == '2':
        username = do_sign_in()
    else:
        print('Invalid option')
        return

    show_todo_list(username)


main()
