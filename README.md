<h1 align="center">AirBnB clone - The console</h1>

## Authors
* **Luis Ortiz** <[luisoh93](https://github.com/luisoh93)>
* **Santiago Echeverri** <[dassantoss](https://github.com/dassantoss)>

<p align="center">
  <img src="https://github.com/dassantoss/holbertonschool-AirBnB_clone/blob/main/assets/logo.png" alt="HBnB logo">
</p>

## Description

HBnB is a comprehensive web application designed to replicate the functionality of AirBnB. It encompasses various components, including database storage, a powerful back-end API, and an intuitive front-end interface. The project aims to provide users with an efficient and user-friendly platform for property rentals, similar to AirBnB.

The current focus of the project is on the development of the back-end console. The console serves as a command-line interface that enables users to manage and manipulate various aspects of the HBnB application. Through the console, users can interact with the underlying database, create and manage instances of different classes (such as users, properties, bookings, etc.), perform operations like searching, updating, and deleting data, and access essential information about the application's functionality.

While the back-end console is currently the primary feature of the project, future updates and enhancements are planned to incorporate the front-end interface, allowing users to interact with HBnB through a graphical user interface (GUI). Additionally, the project will include advanced features like user authentication, property recommendations, secure payment processing, and integration with external services to enrich the user experience.

By leveraging the power of modern web development technologies and implementing best practices, HBnB aims to provide a seamless and reliable platform for property rentals, offering a user experience similar to AirBnB while adding unique features and improvements tailored to the specific needs of its users.

## Built with

Ubuntu 20.04, and Python3 language.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine (Linux distro) for development and testing purposes.

## Installing

You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.

```
git clone https://github.com/dassantoss/holbertonschool-AirBnB_clone
```
After cloning the repository you will have a folder called holbertonschool-AirBnB_clone. 
In here there will be several files that allow the program to work.

> /console.py : The main executable of the project, the command interpreter.
>
> models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes JSON file to instances
> 
> models/__ init __.py:  A unique `FileStorage` instance for the application
> 
> models/base_model.py: Class that defines all common attributes/methods for other classes.
> 
> models/user.py: User class that inherits from BaseModel
> 
>models/state.py: State class that inherits from BaseModel
>
>models/city.py: City class that inherits from BaseModel
>
>models/amenity.py: Amenity class that inherits from BaseModel
>
>models/place.py: Place class that inherits from BaseModel
>
>models/review.py: Review class that inherits from BaseModel


In the tests folders, several test files can be found which serve as unit-tests for the console.

## Classes

HBnB utilizes the following classes:

|     | BaseModel | FileStorage | User | State | City | Amenity | Place | Review |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| **PUBLIC INSTANCE ATTRIBUTES** | `id`<br>`created_at`<br>`updated_at` | | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` |
| **PUBLIC INSTANCE METHODS** | `save`<br>`to_dict` | `all`<br>`new`<br>`save`<br>`reload` | "" | "" | "" | "" | "" | "" |
| **PUBLIC CLASS ATTRIBUTES** | | | `email`<br>`password`<br>`first_name`<br>`last_name`| `name` | `state_id`<br>`name` | `name` | `city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` | 
| **PRIVATE CLASS ATTRIBUTES** | | `file_path`<br>`objects` | | | | | | |

## Storage

The classes mentioned above are managed by the abstracted storage engine implemented in the[FileStorage](./models/engine/file_storage.py) class.

Every time the backend is initialized, HBnB instantiates an instance of 
`FileStorage` called `storage`. The `storage` object is loaded/re-loaded from 
any class instances stored in the JSON file `file.json`. As class instances are 
created, updated, or deleted, the `storage` object is used to register 
corresponding changes in the `file.json`.

## Console

The console is a command line interpreter that permits management of the backend 
of HBnB. It can be used to handle and manipulate all classes utilized by 
the application (achieved by calls on the `storage` object defined above).

### Using the Console

The HBnB console can be run both interactively and non-interactively. 
To run the console in non-interactive mode, pipe any command(s) into an execution 
of the file `console.py` at the command line.

```
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
$
```

Alternatively, to use the HBnB console in interactive mode, run the 
file `console.py` by itself:

```
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb) 
```

To quit the console, enter the command `quit`, or input an EOF signal 
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

### Console Commands

The HBnB console supports the following commands:

* **create**
  * Usage: `create <class>`

Creates a new instance of a given class. The class' ID is printed and 
the instance is saved to the file `file.json`.

```
$ ./console.py
(hbnb) create BaseModel
ad77de3d-71c5-440c-b72d-2a04546be341
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.ad77de3d-71c5-440c-b72d-2a04546be341": {"id": "ad77de3d-71c5-440c-b72d-2a04546be341", "created_at": "2023-07-09T15:31:51.293198", "updated_at": "2023-07-09T15:31:51.293198", "__class__": "BaseModel"}}
```

* **show**
  * Usage: `show <class> <id>` or `<class>.show(<id>)`

Prints the string representation of a class instance based on a given id.

```
$ ./console.py
(hbnb) create User
f3e36d30-3889-4360-a5d3-953a88bd6cc9
(hbnb) show User f3e36d30-3889-4360-a5d3-953a88bd6cc9
[User] (f3e36d30-3889-4360-a5d3-953a88bd6cc9) {'id': 'f3e36d30-3889-4360-a5d3-953a88bd6cc9', 'created_at': datetime.datetime(2023, 7, 9, 15, 48, 40, 423923), 'updated_at': datetime.datetime(2023, 7, 9, 15, 48, 40, 423923)}
(hbnb) User.show(f3e36d30-3889-4360-a5d3-953a88bd6cc9)
[User] (f3e36d30-3889-4360-a5d3-953a88bd6cc9) {'id': 'f3e36d30-3889-4360-a5d3-953a88bd6cc9', 'created_at': datetime.datetime(2023, 7, 9, 15, 48, 40, 423923), 'updated_at': datetime.datetime(2023, 7, 9, 15, 48, 40, 423923)}
(hbnb)
```
* **destroy**
  * Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`

Deletes a class instance based on a given id. The storage file `file.json` 
is updated accordingly.

```
$ ./console.py
(hbnb) create State
7d4b9ec3-51b4-4167-b6f8-cbdb65d2b759
(hbnb) create Place
742524f1-52c1-420a-9cf4-7d980fc07d7b
(hbnb) destroy State 7d4b9ec3-51b4-4167-b6f8-cbdb65d2b759
(hbnb) Place.destroy(742524f1-52c1-420a-9cf4-7d980fc07d7b)
(hbnb) quit
```

* **all**
  * Usage: `all` or `all <class>` or `<class>.all()`

Prints the string representations of all instances of a given class. If no 
class name is provided, the command prints all instances of every class.

```
$ ./console.py
(hbnb) create BaseModel
e070fc62-d455-4af7-95a6-a5d02d8472a6
(hbnb) create User
db58a94b-efc8-4188-9713-8f5ba666875a
(hbnb) create BaseModel
b87112ea-f7f0-48e7-9ed5-c89d077dbf1f
(hbnb) create User
e79c76be-ed0b-4cea-a64b-bcee73d5a2fb
(hbnb) all BaseModel
["[BaseModel] (ad77de3d-71c5-440c-b72d-2a04546be341) {'id': 'ad77de3d-71c5-440c-b72d-2a04546be341', 'created_at': datetime.datetime(2023, 7, 9, 15, 31, 51, 293198), 'updated_at': datetime.datetime(2023, 7, 9, 15, 31, 51, 293198)}", "[BaseModel] (e070fc62-d455-4af7-95a6-a5d02d8472a6) {'id': 'e070fc62-d455-4af7-95a6-a5d02d8472a6', 'created_at': datetime.datetime(2023, 7, 9, 15, 53, 42, 134872), 'updated_at': datetime.datetime(2023, 7, 9, 15, 53, 42, 134872)}", "[BaseModel] (b87112ea-f7f0-48e7-9ed5-c89d077dbf1f) {'id': 'b87112ea-f7f0-48e7-9ed5-c89d077dbf1f', 'created_at': datetime.datetime(2023, 7, 9, 15, 54, 0, 471269), 'updated_at': datetime.datetime(2023, 7, 9, 15, 54, 0, 471269)}"]
(hbnb) User.all
*** Unknown syntax: User.all
(hbnb) User.all()
["[User] (f3e36d30-3889-4360-a5d3-953a88bd6cc9) {'id': 'f3e36d30-3889-4360-a5d3-953a88bd6cc9', 'created_at': datetime.datetime(2023, 7, 9, 15, 48, 40, 423923), 'updated_at': datetime.datetime(2023, 7, 9, 15, 48, 40, 423923)}", "[User] (db58a94b-efc8-4188-9713-8f5ba666875a) {'id': 'db58a94b-efc8-4188-9713-8f5ba666875a', 'created_at': datetime.datetime(2023, 7, 9, 15, 53, 54, 841989), 'updated_at': datetime.datetime(2023, 7, 9, 15, 53, 54, 841989)}", "[User] (e79c76be-ed0b-4cea-a64b-bcee73d5a2fb) {'id': 'e79c76be-ed0b-4cea-a64b-bcee73d5a2fb', 'created_at': datetime.datetime(2023, 7, 9, 15, 54, 4, 872764), 'updated_at': datetime.datetime(2023, 7, 9, 15, 54, 4, 872764)}"]
(hbnb) all
["[BaseModel] (ad77de3d-71c5-440c-b72d-2a04546be341) {'id': 'ad77de3d-71c5-440c-b72d-2a04546be341', 'created_at': datetime.datetime(2023, 7, 9, 15, 31, 51, 293198), 'updated_at': datetime.datetime(2023, 7, 9, 15, 31, 51, 293198)}", "[User] (f3e36d30-3889-4360-a5d3-953a88bd6cc9) {'id': 'f3e36d30-3889-4360-a5d3-953a88bd6cc9', 'created_at': datetime.datetime(2023, 7, 9, 15, 48, 40, 423923), 'updated_at': datetime.datetime(2023, 7, 9, 15, 48, 40, 423923)}", "[BaseModel] (e070fc62-d455-4af7-95a6-a5d02d8472a6) {'id': 'e070fc62-d455-4af7-95a6-a5d02d8472a6', 'created_at': datetime.datetime(2023, 7, 9, 15, 53, 42, 134872), 'updated_at': datetime.datetime(2023, 7, 9, 15, 53, 42, 134872)}", "[User] (db58a94b-efc8-4188-9713-8f5ba666875a) {'id': 'db58a94b-efc8-4188-9713-8f5ba666875a', 'created_at': datetime.datetime(2023, 7, 9, 15, 53, 54, 841989), 'updated_at': datetime.datetime(2023, 7, 9, 15, 53, 54, 841989)}", "[BaseModel] (b87112ea-f7f0-48e7-9ed5-c89d077dbf1f) {'id': 'b87112ea-f7f0-48e7-9ed5-c89d077dbf1f', 'created_at': datetime.datetime(2023, 7, 9, 15, 54, 0, 471269), 'updated_at': datetime.datetime(2023, 7, 9, 15, 54, 0, 471269)}", "[User] (e79c76be-ed0b-4cea-a64b-bcee73d5a2fb) {'id': 'e79c76be-ed0b-4cea-a64b-bcee73d5a2fb', 'created_at': datetime.datetime(2023, 7, 9, 15, 54, 4, 872764), 'updated_at': datetime.datetime(2023, 7, 9, 15, 54, 4, 872764)}"]
(hbnb)
```

* **count**
  * Usage: `count <class>` or `<class>.count()`

Retrieves the number of instances of a given class.

```
$ ./console.py
(hbnb) create Place
7bab2e34-f44b-4769-90f6-9ce4bf4aaa58
(hbnb) create Place
f8ee7f06-772d-4487-8654-9dc16f6dfbca
(hbnb) create City
65f2d975-992a-4b0f-88d9-ed1804dec8af
(hbnb) count Place
2
(hbnb) city.count()
1
(hbnb)
```

* **update**
  * Usage: `update <class> <id> <attribute name> "<attribute value>"` or
`<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(
<id>, <attribute dictionary>)`.

Updates a class instance based on a given id with a given key/value attribute 
pair or dictionary of attribute pairs. If `update` is called with a single 
key/value attribute pair, only "simple" attributes can be updated (ie. not 
`id`, `created_at`, and `updated_at`). However, any attribute can be updated by 
providing a dictionary.

```
$ ./console.py
(hbnb) create User
4018e9ed-f552-4ea7-8824-9d8c66cfbaad
(hbnb) update User 4018e9ed-f552-4ea7-8824-9d8c66cfbaad first_name "Santiago"
(hbnb) show User 4018e9ed-f552-4ea7-8824-9d8c66cfbaad
[User] (4018e9ed-f552-4ea7-8824-9d8c66cfbaad) {'id': '4018e9ed-f552-4ea7-8824-9d8c66cfbaad', 'created_at': datetime.datetime(2023, 7, 9, 15, 58, 22, 598138), 'updated_at': datetime.datetime(2023, 7, 9, 15, 58, 22, 598138), 'first_name': 'Santiago'}
(hbnb) User.update(4018e9ed-f552-4ea7-8824-9d8c66cfbaad, address "Calle 123"
*** Unknown syntax: User.update(4018e9ed-f552-4ea7-8824-9d8c66cfbaad, address "Calle 123"
(hbnb) User.update(4018e9ed-f552-4ea7-8824-9d8c66cfbaad, address, "Calle 123")
(hbnb) User.show(4018e9ed-f552-4ea7-8824-9d8c66cfbaad)
[User] (4018e9ed-f552-4ea7-8824-9d8c66cfbaad) {'id': '4018e9ed-f552-4ea7-8824-9d8c66cfbaad', 'created_at': datetime.datetime(2023, 7, 9, 15, 58, 22, 598138), 'updated_at': datetime.datetime(2023, 7, 9, 15, 58, 22, 598138), 'first_name': 'Santiago', 'address': 'Calle 123'}
(hbnb) User.update(4018e9ed-f552-4ea7-8824-9d8c66cfbaad, {'e-mail': 'santy.e@gmail.com', 'last_name': 'Echeve
rri'})
(hbnb) User.show(4018e9ed-f552-4ea7-8824-9d8c66cfbaad)
[User] (4018e9ed-f552-4ea7-8824-9d8c66cfbaad) {'id': '4018e9ed-f552-4ea7-8824-9d8c66cfbaad', 'created_at': datetime.datetime(2023, 7, 9, 15, 58, 22, 598138), 'updated_at': datetime.datetime(2023, 7, 9, 15, 58, 22, 598138), 'first_name': 'Santiago', 'address': 'Calle 123', 'e-mail': 'santy.e@gmail.com', 'last_name': 'Echeverri'}
(hbnb)
```

## Testing

Unittests for the HBnB project are defined in the [tests](./tests) 
folder. To run the entire test suite simultaneously, execute the following command:

```
$ python3 unittest -m discover tests
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```
