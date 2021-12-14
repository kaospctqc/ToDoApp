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

## Deployment

## Credits

