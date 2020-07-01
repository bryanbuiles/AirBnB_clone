# AirBnB clone

### Table of Contents
1. [Introduction](#introduction)
1. [Installation and usage](#installation_and_usage)
1. [Features](#features)
1. [Authors](#authors)
1. [Contributing](#contributing)
1. [License](#license)

### Introduction

Este proyecto oconsiste en la codificación en lenguaje Python de una consola para la creación, actualización y destrucción de instancias de clase de diferentes clases. Todo esto como base para proximos proyectos, que junto con este, buscan la construcción de una full web application. Este proyecto hace parte del curriculum de la escuela de Holberton School.

### Installation and usage

Clone the repository from the link below: 

[https://github.com/andresjjn/AirBnB_clone.git](https://github.com/andresjjn/AirBnB_clone.git)

Ahora, abra el directorio /AirBnB y ejecute el archivo console.py con la versión de python que disponga en su computador. Por ejemplo, con la versión 3.4: 

```shell
python3.4 console.py
```

### Features

**1.** create:

Esta característica permite crear nuevas instancias de las diferentes clases presentes en la consola como BaseModel, User, State, City, Place and Review. Para utilizarla basta con el commando create mas la clase. Así:

```python
(hbnb) create User
```

**2.** show:

Se utiliza para mostrar los diretentes atributos presentes en una instancia de clase. Exiten dos formas de utilizar este comando: 

La primera consiste en este formato: show <classname> <id>, así:

```python
(hbnb) show City 6755cf15-ab50-4594-aa12-741a7f62bae6
```
También es posible utilizar: <Classname>.show(<id>)

```python
(hbnb) City.show("6755cf15-ab50-4594-aa12-741a7f62bae6")
```
**3.** destroy:

Este metodo permite la destrucción de una instancia de clase. Para esto solo bastará con conocer el nombre de la clase y el id de la instancia a destruir. Las formas de utilizar este método son:

```python
(hbnb) destroy City 6755cf15-ab50-4594-aa12-741a7f62bae6
```
o también:

```python
(hbnb) City.destroy("6755cf15-ab50-4594-aa12-741a7f62bae6")
```

**4.** all:

Este método permite mostrar todas las instanciaciones de clase existentes actualmente en la base de datos. Para esto tecleammos en la consola:

```python
(hbnb) all
```

Además, si se quiere ver todas la instancias de una clase particular, solo basta agregar el nombre de la clase, así: all <classname>

```python
(hbnb) all User
```
o también

```python
(hbnb) User.all()
```

**5.** update:

Este es uno de los principales métodos de esta consola, pues no solo permite actualizar los valores de los attributos presentes en una instancia de clase determinada, sino también, si dicho atributo no existe la crea con el valor asignado. Por ejemplo:

Si utilizamos el commando all y un nombre de clase podremos ver todas las intaccias actuales, esto para escoger una y actualizar o crear atributos, así:

```python
(hbnb) all User
["[User] (ba6b53b4-cfd0-4756-901b-9ef89805110e) {'id': 'ba6b53b4-cfd0-4756-901b-9ef89805110e', 'updated_at': datetime.datetime(2020, 6, 30, 21,
45, 23, 306595), 'created_at': datetime.datetime(2020, 6, 30, 21, 45, 23, 306568)}", "[User] (afbc6c3f-d90c-4421-99c3-86b55f48c98a) {'id': 
'afbc6c3f-d90c-4421-99c3-86b55f48c98a', 'updated_at': datetime.datetime(2020, 7, 1, 2, 20, 35, 944422), 'created_at': datetime.datetime(2020, 
7, 1, 2, 20, 35, 944393)}"]
```
Luego, escogemos una de ellas, por ejemplo:

```python
(hbnb) show User ba6b53b4-cfd0-4756-901b-9ef89805110e
[User] (ba6b53b4-cfd0-4756-901b-9ef89805110e) {'id': 'ba6b53b4-cfd0-4756-901b-9ef89805110e', 'updated_at': datetime.datetime(2020, 6, 30, 21, 45, 23, 306595), 'created_at': datetime.datetime(2020, 6, 30, 21, 45, 23, 306568)}
```
**Nota:** Los atributos **id**, **updated_at** y **created_at** no prodrán ser modificados.

Ya que los atributos iniciales no pueden se modificados, crearemos uno llamado numero de telefono. Para esto sxisten dos métodos, el primero utliza la sintaxis update <classname> <id> <attribute name> "<attribute value>"

```python
(hbnb) update User ba6b53b4-cfd0-4756-901b-9ef89805110e phone_number 5731225896
```
o también de la forma <class name>.update(<id>, <attribute name>, <attribute value>)

```python
(hbnb) User.update("ba6b53b4-cfd0-4756-901b-9ef89805110e", phone_number, 5731225896)
```

De nuevo, es posible utilizar el comando show para verificar la creación del nuevo atributo:

```python
(hbnb) show User ba6b53b4-cfd0-4756-901b-9ef89805110e
[User] (ba6b53b4-cfd0-4756-901b-9ef89805110e) {'created_at': datetime.datetime(2020, 6, 30, 21, 45, 23, 306568), **'phone_number': 5731225896**, 'updated_at': datetime.datetime(2020, 6, 30, 21, 45, 23, 306595), 'id': 'ba6b53b4-cfd0-4756-901b-9ef89805110e'}
```
Finalmente, para modificar, basta con utilizar una de las dos sintaxis y modificar el valor del atributo:

```python
(hbnb) User.update("ba6b53b4-cfd0-4756-901b-9ef89805110e", phone_number, +573115896)
```
**6.** count:

Este método permite contar las intancias de una clase en particular que existen dentro de la base de datos, así: <classname>.count()

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