# ToDoApp

## Introduction

Welcome to my ToDoApp. It's meant to be a simple way to quickly write down daily tasks and, once completed, to delete them. 
The only possible actions are add, edit and delete and the data is stored on Google Sheets for peristance.

[Live Website](https://todo-app-kaospctqc.herokuapp.com/)

## Table of Contents

1. [Planning](#planning)
2. [Features](#features)
3. [Testing](#testing)
4. [Deployment](#deployment)
5. [Credits](#credits)


## Planning
Diagram:

![website preview](assets/images/todo_diagram.png)

The concept is to design a todo application that is intuitive and requires as little learning from the user as possible. There is a strong emphasis on simplicity and it is not meant to replace more complex, project tracking tools but to have a quick option to write down a task and then, upon completion, to delete and forget it.
The lack of history is a tool used to keep our focus on getting things done rather than keeping things tracked.

Go back to [Table of contents](#table-of-contents)

## Features

- When starting the todo app we have these options
![todo signin signup](assets/images/todo_signin_signup.png)
    - SignUp 
        - for new users
        - requires a username and a password that will be used to identify this user in the future
        - after SignUp is complete, the user will be automatically signed in the application 
    - SignIn 
        - for existing users
        - the user is required to input a username and a password
        - in the event that the password is not correct, the user will not be signed in until he inputs the correct password

- Once Signed in, the user will always have access to the list of tasks
![todo task list](assets/images/todo_task_list.png)
    - The task list is composed of 2 columns
        - ID - this will be used to identify the task when to perform an action
        - Description - here we find the actual content of the task
    - At the end of the task list we find the available actions that are selectable by typing the letter in the square brakets'[]'

- Add will simply ask for the data of a new task
![todo add task](assets/images/todo_add_task.png)

- Delete will ask for the task ID that should be removed
![todo delete task](assets/images/todo_delete_task.png)

- Edit will ask for the task ID that should be edited and, once this has been provided, will request a new Description for the selected task
![todo edit task](assets/images/todo_edit_task.png)

Go back to [Table of contents](#table-of-contents)

## Testing

### Functionality Testing
TEST            | OUTCOME                          | PASS / FAIL  | ScreenShot
--------------- | -------------------------------- | ---------------|---------
SignUp SignIn   | when a user inputs a incorrect option, they should be redirected to the option screen until a valid option is provided| FAIL | ![todo bug001](assets/images/todo_bug001.png)
SignUp used username | when a user wants to use a username that has already been used, they shouldn't be allowed and should be prompted to try another username | PASS | ![todo wrong username](assets/images/todo_username_unavailable.png)
SignUp success  | when a user inputs valid username and password, they should be able perform signup | PASS | ![todo test signup](assets/images/todo_test_signup.png)
SignIn bad password | when a users inputs a incorrect password on signin, they should be asked for the correct password instead of being signed in | PASS | ![todo wrong password](assets/images/todo_wrong_password.png)
SignIn success  | when a user inputs correct username and password, they should be able to perform signin | PASS | ![todo signin](assets/images/todo_signin.png)
Add task        | when a user chooses option [a] and inputs a task description, a task should be created in the task list| PASS | ![todo add task](assets/images/todo_add_task.png)
Delete task     | when a user chooses option [d] and inputs a task ID, the task with that ID should be removed from the task list | PASS | ![todo delete task](assets/images/todo_delete_task.png)
Edit task       | when a user chooses option [e] and inputs a task ID and a task description, the task list should show the edited task | PASS | ![todo edit task](assets/images/todo_edit_task.png)

Go back to [Table of contents](#table-of-contents)

### Syntax Testing

For this test we use the PEP8 validator and we find that we are missing the end tripple double quotes for a multi-line string
![todo pep8 bad](assets/images/todo_pep8_bad.png)

Here we have fixed this issue:
![todo pep8 good](assets/images/todo_pep8_good.png)

## Deployment

## Credits

