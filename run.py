# External package used to enhance the program
import gspread
# External package used to enhance the program
from google.oauth2.service_account import Credentials
# External package used to enhance the program
from getpass import getpass

# Code from Code Institute Love Sandwiches project
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
    print(
        """
        It's meant to be a simple way to quickly write down daily
        tasks and, once completed, to delete them. The only possible
        actions are add, edit and delete and the data is stored on
        Google Sheets for peristance.
        """
    )
    print("Please choose one of the following options:")
    print("1. Sign Up")
    print("2. Sign In")
    user_choice = input("Option number:\n")
    while True:  # Input validation loop
        if user_choice in ["1", "2"]:
            break
        print("Invalid input, please choose from the options")
        user_choice = input("Option number:\n")
    return user_choice


def check_username(username):
    """
    Verify if provided user is in the user list
    """
    user_list = SHEET.worksheet("users").col_values(1)
    if username in user_list:
        return True


def check_password(username, password):
    """
    Verify password for the provided user
    """
    backend = SHEET.worksheet("users")

    username_row = backend.find(username).row
    password_from_backend = backend.cell(username_row, 2).value

    if password == password_from_backend:
        return True


def get_username():
    """
    Get username from user input
    """
    print("Please choose a username that is not longer than 8 characters\n")
    username = input("Username:\n")

    return username


def get_password(type_of_password):
    """
    Get password form user input
    """
    if type_of_password == "sign_up":  # Only happens on user SignUp
        print("\nPlease choose a password that is longer than 8 characters,")
        print("and container a upper and a lower case character,")
        print("and one special character\n")

    password1 = getpass("Password:\n")
    if type_of_password == "sign_up":  # Ask to confirm password on SignUp
        password2 = getpass("Confirm password:\n")
        while password1 != password2:
            print("Passwords do not match, please try again\n")
            password1 = getpass("Password:\n")
            password2 = getpass("Confirm password:\n")
    return password1


def do_sign_up():
    """
    Register new user using the provided credentials
    """
    print("User registration")
    username = get_username()
    while check_username(username):  # Make sure to have only unique usernames
        print(f"\nThe '{username}' username is not available!")
        print("Please try a different option\n")
        username = get_username()

    password = get_password("sign_up")
    update_worksheet([username, password], 'users')

    return username


def do_sign_in():
    """
    Sign in existing user using the provided credentials
    """
    print("User sign in")
    username = get_username()
    password = get_password("sign_in")
    while not check_password(username, password):  # Only allow correct pass
        print("Wrong password, please try again")
        password = get_password("sign_in")

    return username


def show_todo_list(username):
    """
    Show current todo list and get user action choice
    """
    todo_list = SHEET.worksheet("todo_list").get_all_values()
    print("ToDo List:\n")
    print("ID Description")

    task_list_count = 0
    for ind in range(1, len(todo_list)):  # Show task list
        if todo_list[ind][0] == username:
            task_list_count += 1
            print(f"{ind}. '{todo_list[ind][1]}'")

    if task_list_count == 0:  # show message if task list is empty
        print("\nThere are currently no tasks in the list.")
        print("Please use the add action to create tasks.\n")

    get_task_action(username)

    return todo_list


def get_task_action(username):
    """
    Get action of user and apply
    """
    print("\nPlease select a action from below:")
    user_choice = input("add[a], delete[d], edit[e], quit[q]:\n")
    while True:  # Input validation loop
        if user_choice in ["a", "d", "e", "q"]:
            break
        print("Invalid input, please choose from the options")
        user_choice = input("add[a], delete[d], edit[e], quit[q]:\n")

    if user_choice == 'a':  # Add new task
        print('add task')
        add_task(username)
    elif user_choice == 'd':  # Delete task
        print('delete task')
        remove_task(username)
    elif user_choice == 'e':  # Edit task
        print('edit')
        edit_task(username)
    elif user_choice == 'q':  # Exit program
        print(
            """
            If you wish to restart the application,
            please use the "Run program" from above
            """
        )
        print('Until next time...')


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
    task_id = get_task_id(username)

    confirmation = input(
        f"Are you sure you wish to remove task ID: {task_id}? Y/N:\n"
    )

    while True:  # Input validation loop
        if confirmation.lower() in ["y", "n"]:
            break
        print("Invalid input, please enter a valid option")
        confirmation = input(
            f"Are you sure you wish to remove task ID: {task_id}? Y/N:\n"
        )

    if confirmation.lower() == 'y':
        print(f"Removing task ID {task_id}\n")
        worksheet_to_update = SHEET.worksheet('todo_list')
        worksheet_to_update.delete_rows(task_id + 1)

    show_todo_list(username)


def edit_task(username):
    """
    Ask user for task ID to edit and allow user to
    overwrite specific task
    """
    print("Please input the ID of the task to be edited")
    task_id = get_task_id(username)

    confirmation = input(
        f"Are you sure you wish to edit task ID: {task_id}? Y/N:\n"
    )

    while True:  # Input validation loop
        if confirmation.lower() in ["y", "n"]:
            break
        print("Invalid input, please enter a valid option")
        confirmation = input(
            f"Are you sure you wish to edit task ID: {task_id}? Y/N:\n"
        )

    if confirmation.lower() == 'y':
        print(f"EDIT: {task_id}")
        task = input()

        worksheet_to_update = SHEET.worksheet('todo_list')
        worksheet_to_update.update_cell(task_id + 1, 2, task)

        print("Finished editing the task")

    show_todo_list(username)


def get_task_id(username):
    """
    Get task id from user and check if user and owner match
    """
    while True:  # Input validation loop
        try:
            task_id = int(input("Task ID: "))
            while task_id >= 985:
                print("Please choose a ID value of less than 985")
                task_id = int(input("Task ID: "))
            break
        except ValueError as ve:
            print("Invalid ID, please enter a valid ID")
            continue

    owner = SHEET.worksheet('todo_list').cell(task_id + 1, 1).value
    while username != owner:  # Only return tasks that belong to user
        print("Selected task has a different owner")
        print("Please choose again")
        task_id = int(input("Task ID: "))
        owner = SHEET.worksheet('todo_list').cell(task_id + 1, 1).value

    return task_id


# Code from Code Institute Love Sandwiches project
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

    show_todo_list(username)


main()
