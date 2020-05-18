import json, requests

todos = []

def get_todos():
    return todos

def add_one_task(title):#this is for your local 
    todos.append({'label': title, 'done': False})
    print(todos)

def print_list():
    print(todos)

def delete_task(number_to_delete):
    global todos
    todos.pop(int(number_to_delete)-1)
    print(todos) 

def initialize_todos():
    global todos
    r = requests.get('https://assets.breatheco.de/apis/fake/todos/user/violetaventura001') 
    if(r.status_code == 404):
        print("No previous todos found, starting a new todolist")
        r = requests.post(url = 'https://assets.breatheco.de/apis/fake/todos/user/violetaventura001', data = []) 
        if r.status_code == 200:
            print("Tasks initialized successfully")
    else:
        print("A todo list was found, loading the todos...")
        todos = r.json()
        print(todos)
    
def save_todos():
    global todos
    print(todos)
    r = requests.put('https://assets.breatheco.de/apis/fake/todos/user/violetaventura001', json= todos) 
    print(r.json())
    if r.status_code == 200:
        print("You have saved to the todos.")
    else: r.text

def load_todos():#we want to get the saved todos from the cloud
    global todos
    print(todos)
    response = requests.get('https://assets.breatheco.de/apis/fake/todos/user/violetaventura001') 
    print(response.json())
    if response.status_code == 200:
        todos = response.json() #this will be the new list todos retrived from the API into my my local todos variable 
        print("You have printed the todos from the cloud.")
    else: response.text
    
# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    stop = False
    print("Initializing todos with previous data or creating a new todo's list...")
    initialize_todos()
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Send/Save todo's to API
        5. Retrieve todo's from API
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")