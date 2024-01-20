# Project: AirBnB clone – The console

## Introduction 

The goal of this project is to simulate [AirBnB website](https://www.airbnb.fr/). We will deploy on our server a simple copy of it. 

**First, what is AirBnB platform?**  
Is a popular online marketplace and hospitality service that allows people to rent or lease short-term lodging, including vacation rentals, apartment rentals, homestays, hostel beds, or hotel rooms (check the link above).  

## Description of the project  

In this project we won’t implement all the features ot this website, only some of them to cover all fundamental concepts of the higher-level programming track.  

The final product is a complete web application that includes:  
- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)  
- A website (the front-end) that shows the final product to everybody: static and dynamic  
- A database or files that store data (data = objects)  
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)  

**Note**: But for now, we will not take care of all the four components above of the final web app. We will start from the first piece of the project by:  
- create a data model  
- manage (create, update, destroy, etc) objects via a console / command interpreter  
- store and persist objects to a file (JSON file)  

## Description of the command interpreter

### How to start it?

The name of the file that starts the command line interpreter is [console.py](https://github.com/malhaouit/AirBnB_clone/blob/master/console.py).  

In your terminal where the file `console.py` exist tap the command `./console.py` to start the program.  

The first thing you will see is a prompt **(hbnb)** waiting the user to enter a command. In the section below you will find some uses and examples.

### How to use it?

This command line works much like a Unix Shell but limited to a specific use-case _(create new object, retrieve an object from a file, do operations on objects, update attributes, destroy an object...)_.  
 
It works both in interactive mode and non interactive mode.  

| Command explanation | Usage |
| --- | --- |
| Display all commands <br/> documented/undocumented  | `(hbnb) help` |
| Display help for a command | `(hbnb) help <command>` |
| Exit the console | `(hbnb) quit` |
| Exit the console (click Ctrl + D) | `(hbnb) Ctrl + D` |
| Create a new Object | `(hbnb) create <class_name>` |
| Prints the string representation <br/> of an instance | `(hbnb) show <class_name> <id>` or <br/> `(hbnb) <class_name>.show(<id>)` |
| Deletes an instance | `destory <class_name> <id>` |
| Prints all string representation <br/> of all instances | `(hbnb) all` |
| Prints all string representation <br/> based on the class | `(hbnb) all <class_name> ` or <br/> `(hbnb) <class_name>.all()` |
| Updates an instance based on <br/> the class name and id | `(hbnb) update <class_name> <id>` <br/> `<attribute_name> "<attribute_value>"` <br/> or `(hbnb) <class>.update(<id>,` <br/> `<attribute_name>, "<attribute value>")` |


### Examples

- **Interactive mode:**  

```
Example 1:  

$ ./console.py  
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help EOF
Exit the console using EOF
(hbnb)
```

```
Example 2:  

(hbnb) create BaseModel
288d1e28-0696-41e5-861f-d0d10bcf73ea
(hbnb)
```

```
Example 3:  

(hbnb) all
["[BaseModel] (288d1e28-0696-41e5-861f-d0d10bcf73ea) {'id': '288d1e28-0696-41e5-861f-d0d10bcf73ea', 'created_at': datetime.datetime(2024, 1, 15, 20, 22, 52, 101730), 'updated_at': datetime.datetime(2024, 1, 15, 20, 22, 52, 102939)}"]
(hbnb)
``` 

- **No-interactive mode:**  

```
Example 1:  

$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)  
$
```

```
Example 2:  

$ echo "show BaseModel 288d1e28-0696-41e5-861f-d0d10bcf73ea" | ./console.py  
(hbnb) [BaseModel] (288d1e28-0696-41e5-861f-d0d10bcf73ea) {'id': '288d1e28-0696-41e5-861f-d0d10bcf73ea', 'created_at': datetime.datetime(2024, 1, 15, 20, 22, 52, 101730), 'updated_at': datetime.datetime(2024, 1, 15, 20, 22, 52, 102939)}
(hbnb)  
$
```
