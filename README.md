# AirBnB console
![alt text](/media/hbnb_logo.png)

## Description

To summarize, this project is part of a series of projects dedicated to create a prototype version of the popular AirBnB service for learning purposes. Specifically, what recalls in this project is a console which allows the user to create, save, or load classes that already exist and were made for later usage. As said, this will be implemented later on next projects.

## Installation

- Simply clone this repository with ``` git clone https://github.com/Diekkan/AirBnB_clone.git```

- Navigate to root folder and execute ```console.py```

## Usage

The user can create instances from classes with ``` create <classname> ``` command:

```
(hbnb) create BaseModel
731456cb-0f23-4044-9657-ba659780ea82
(hbnb)
```

User can retrieve a specific instance representation with ``` show <classname> <id> ```
command:

```
(hbnb) show BaseModel 731456cb-0f23-4044-9657-ba659780ea82
[BaseModel] (731456cb-0f23-4044-9657-ba659780ea82) {'id': '731456cb-0f23-4044-9657-ba659780ea82', 'created_at': datetime.datetime(2022, 3, 5, 22, 42, 52, 313699), 'updated_at': datetime.datetime(2022, 3, 5, 22, 42, 52, 313699)}
(hbnb)
```

User can retrieve all instances created with ```all``` command, or if specified, all instances of a certain existing class with ```all <classname> ``` command:

```
(hbnb) all
["[BaseModel] (731456cb-0f23-4044-9657-ba659780ea82) {'id': '731456cb-0f23-4044-9657-ba659780ea82', 'created_at': datetime.datetime(2022, 3, 5, 22, 42, 52, 313699), 'updated_at': datetime.datetime(2022, 3, 5, 22, 42, 52, 313699)}"]
(hbnb)
```
```<classname>.all()``` is also valid for retrieving all instances.

User can also update existing attribute, or add new ones from an existing class with ``` update <class name> <id> <attribute name> "<attribute value>" ``` command:
```
(hbnb) update BaseModel 731456cb-0f23-4044-9657-ba659780ea82 newatt 123
(hbnb) show BaseModel 731456cb-0f23-4044-9657-ba659780ea82
[BaseModel] (731456cb-0f23-4044-9657-ba659780ea82) {'id': '731456cb-0f23-4044-9657-ba659780ea82', 'created_at': datetime.datetime(2022, 3, 5, 22, 42, 52, 313699), 'updated_at': datetime.datetime(2022, 3, 5, 22, 42, 52, 313699), 'newatt': '123'}
(hbnb)
```

The user can also wipe out a specific desired instance with ``` destroy <classname> <id> ```

```
(hbnb) destroy BaseModel 731456cb-0f23-4044-9657-ba659780ea82
(hbnb) all      
(hbnb) 
```

## Contributors

This was made by Diego Merentiel and Mateo Victorica from Holberton Uruguay.
- Mateo Victorica ([GitHub](https://github.com/Ual97))
- Diego Merentiel ([GitHub](https://github.com/Diekkan))

## License
No license