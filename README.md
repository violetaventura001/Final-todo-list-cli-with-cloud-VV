# Todo List CLI in Sync with the Cloud!

<p align="center"><img src="https://github.com/breatheco-de/todo-list-cli-with-cloud/blob/master/preview.gif" width="500" /></p>
Today you will be building a TODO list using API's to sync it with the cloud.

You will practice:
1. Python lists/arrays
2. Python Dictionaries
3. Using the requests package for API communication
4. HTTP Protocol

We are going to be using [BreatheCode Todo's API](https://assets.breatheco.de/apis/fake/todos/) to upload and download the TODO's, please refer to the HTTP and REST lessons as a quick background research for the project.

- Get todo's by calling: `[GET] /todos/user/<username>`   
- Initilize the todo list: `[POST] /todos/user/<username>`  
- Update your todo list: `[PUT] /todos/user/<username>`  

## 💻 Installation

1. Clone this repository: 

```sh
$ git clone https://github.com/breatheco-de/todo-list-cli-with-cloud
```

2. Install the dependecy packages by typing: 

```sh
$ pipenv install --python 3
```

3. Get inside your virtual environment by typing: 

```sh
$ pipenv shell
```

4. You can run the project by typing: 

```sh
$ python src/app.py
```
5. You can also run the tests for the project: 

```sh
$ python src/test.py
```

## 📝 Instructions

- You app needs to work from the the command line [like this](https://github.com/breatheco-de/todo-list-cli-with-cloud/blob/master/preview.gif).
- The user should be able to add a new tasks.
- The user can add as many tasks as they want.
- The user can delete tasks by specifying the task position in the list.
- The app must be able to save to todo's to the cloud using [BreatheCode Todo's API](https://assets.breatheco.de/apis/fake/todos/)
- The app must be able to download (load) the todo's from the [BreatheCode Todo's API](https://assets.breatheco.de/apis/fake/todos/)


