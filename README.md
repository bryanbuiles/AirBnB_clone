# AirBnB clone

### Table of Contents
1. [Introduction](#introduction)
1. [Installation](#installation)
1. [Features](#features)
1. [Authors](#authors)
1. [Contributing](#contributing)
1. [License](#license)

### Introduction

The Console is one part of the AirBnB Clone Proiect, and consists of the coding in Python language for creation, update and destruction of class instances of different classes. The Console is the base for further activities to complete the main project, all following activities and tasks together, seek the construction of a full web application like AirBnB. All these activities and the final project are part of the curriculum of the Holberton School.

### Installation

Clone the repository from the link below: 

[https://github.com/andresjjn/AirBnB_clone.git](https://github.com/andresjjn/AirBnB_clone.git)

Now, open the directory /AirBnB and execute the console.py file with any version of Python you have in your computer. For example, with the 3.4 version will be: 

```shell
python3.4 console.py
```

### Features

**1. Create:**

The create feature allows you to set up new instances of different classes contained in the console such as **BaseModel, User, State, City, Place and Review**. To use it, just type **create \<class_name\>** Like this:

```python
(hbnb) create User
```

**2. Show:**

It is used to display the different attributes present in a class instance. There are two ways to use this command: 

In the first format you have to type **show \<class_name\>.(\<id\>)**:

```python
(hbnb) show City 6755cf15-ab50-4594-aa12-741a7f62bae6
```
The second one is using the show in this way \<class_name\>.show(\<id\>). For example:

```python
(hbnb) City.show("6755cf15-ab50-4594-aa12-741a7f62bae6")
```
**3. Destroy:**

The destroy method allows the destruction of a class instance. For this, it will only be enough to know the name of the classname and the id of the instance to destroy. 
The way to use this method is like the show feature:

```python
(hbnb) destroy City 6755cf15-ab50-4594-aa12-741a7f62bae6
```
or:

```python
(hbnb) City.destroy("6755cf15-ab50-4594-aa12-741a7f62bae6")
```

**4. All:**

This method allows display all existing classes instances in the data base. Just type in the console:

```python
(hbnb) all
```
In addition, if you want to see more of a specific class intance, you only have to add the name of the class:  all \<classname\>

```python
(hbnb) all User
```
Also you can use \<class_name>.all():

```python
(hbnb) User.all()
```

**5. Update:**

This method is one of the principal features of these console. It allows to actualize a current attribute value in a default instance class. And, if the attribute does not exist, it is created with the assigned value.

**Note** The default attributes **id**, **updated_at** y **created_at** can not be modified.

For example:

To create a new attribute you can use **update \<classname\> \<id\> \<attribute name\> "\<attribute value\>"**

```python
(hbnb) update User ba6b53b4-cfd0-4756-901b-9ef89805110e phone_number 5731225896
```
Also you can use **\<class name\>.update(\<id\>, \<attribute name\>, \<attribute value\>)**

```python
(hbnb) User.update("ba6b53b4-cfd0-4756-901b-9ef89805110e", phone_number, 5731225896)
```

It is possible to use the show command to verify the new attribute created:

```python
(hbnb) show User ba6b53b4-cfd0-4756-901b-9ef89805110e
[User] (ba6b53b4-cfd0-4756-901b-9ef89805110e) {'created_at': datetime.datetime(2020, 6, 30, 21, 45, 23, 306568), phone_number': 5731225896, 'updated_at': datetime.datetime(2020, 6, 30, 21, 45, 23, 306595), 'id': 'ba6b53b4-cfd0-4756-901b-9ef89805110e'}
```
Finally, you can modify the created attribute using one of the previous ways:

```python
(hbnb) User.update("ba6b53b4-cfd0-4756-901b-9ef89805110e", phone_number, 573115896)
```
**6. Count:**

The count feature allows to check the number of the particular class instances staged in the data base **\<classname\>.count()**

```python
(hbnb) User.count()
```

### Authors
1. [Bryan Builes Echavarría](https://github.com/bryanbuiles)
1. [Andrés Felipe Jején Tabares](https://github.com/andresjjn)

### Contributing
Pull requests are welcome. For important changes, please open an issue to discuss the change you would like to improve.

## License
[MIT](https://choosealicense.com/licenses/mit/)
