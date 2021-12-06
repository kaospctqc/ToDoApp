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
option = show_options()
print(option)
