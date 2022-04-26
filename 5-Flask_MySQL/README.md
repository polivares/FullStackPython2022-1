# Guía Flask y MySQL
Flask, al ser una biblioteca Python, permite conectarse fácilmente con otras bibliotecas de dicho lenguaje, tales como bibliotecas para MySQL.

## Conexión a BD MySQL con Python
Iniciaremos con la creación de una nueva base de datos. Para ello nos conectaremos a nuestro motor de base de datos usando el usuario y contraseña para root. Recuerda que si estás utilizando otro usuario o contraseña, debes cambiar los comandos según corresponda.

```console
$ mysql -u user -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 14
Server version: 8.0.26-0ubuntu0.20.04.3 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> create database curso;
Query OK, 1 row affected (0.01 sec)

mysql> use curso;
Database changed
mysql> create table grupo (idGrupo int not null auto_increment,
    -> nombre_grupo varchar(45),
    -> descripcion_grupo varchar(1000),
    -> primary key(idGrupo));
Query OK, 0 rows affected (0.02 sec)

mysql> mysql> create table integrantes (idIntegrante int not null auto_increment,
    -> nombre_integrante varchar(45) not null,
    -> apellido_integrante varchar(45) not null,
    -> idGrupo int,
    -> primary key(idIntegrante),
    -> foreign key(idGrupo) references grupo(idGrupo));
Query OK, 0 rows affected (0.04 sec)

mysql> show tables;
+-----------------+
| Tables_in_curso |
+-----------------+
| grupo           |
| integrantes     |
+-----------------+
2 rows in set (0.00 sec)

mysql> desc grupo;
+-------------------+---------------+------+-----+---------+----------------+
| Field             | Type          | Null | Key | Default | Extra          |
+-------------------+---------------+------+-----+---------+----------------+
| idGrupo           | int           | NO   | PRI | NULL    | auto_increment |
| nombre_grupo      | varchar(45)   | YES  |     | NULL    |                |
| descripcion_grupo | varchar(1000) | YES  |     | NULL    |                |
+-------------------+---------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql> desc integrantes;
+---------------------+-------------+------+-----+---------+----------------+
| Field               | Type        | Null | Key | Default | Extra          |
+---------------------+-------------+------+-----+---------+----------------+
| idIntegrante        | int         | NO   | PRI | NULL    | auto_increment |
| nombre_integrante   | varchar(45) | NO   |     | NULL    |                |
| apellido_integrante | varchar(45) | NO   |     | NULL    |                |
| idGrupo             | int         | YES  | MUL | NULL    |                |
+---------------------+-------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

mysql> insert into grupo (nombre_grupo, descripcion_grupo) values ("Primer grupo", "Proyecto hecho en Flask");
Query OK, 1 rows affected (0.03 sec)
Records: 1  Duplicates: 0  Warnings: 0

mysql> select * from grupo;
+---------+---------------+--------------------------+
| idGrupo | nombre_grupo  | descripcion_grupo        |
+---------+---------------+--------------------------+
|       1 | Primer grupo  | Proyecto hecho en Flask  |
+---------+---------------+--------------------------+
1 row in set (0.00 sec)

mysql> insert into integrantes (nombre_integrante, apellido_integrante, idGrupo) values ('Miguel', 'Castillo', 1),
('Patricio', 'Olivares', 1),
('Pedro', 'Carvajal', 1);

Query OK, 3 rows affected (0.01 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from integrantes;
+--------------+-------------------+---------------------+---------+
| idIntegrante | nombre_integrante | apellido_integrante | idGrupo |
+--------------+-------------------+---------------------+---------+
|            1 | Miguel            | Castillo            |       1 |
|            2 | Patricio          | Olivares            |       1 |
|            3 | Pedro             | Carvajal            |       1 |
+--------------+-------------------+---------------------+---------+
3 rows in set (0.00 sec)


```

A continuación, realizaremos consultas sobre las tablas cradas utilizando la biblioteca PyMySQL de Python. Para ello, debemos instalar la biblioteca PyMySQL:

```console
(FlaskVenv)$ pip install PyMySQL
```

También puede ser necesario instalar el paquete cryptography para poder utilizar la biblioteca PyMySQL.

```console
(FlaskVenv)$ pip install cryptography
```

Luego, utilizaremos el código disponible en la carpeta *1-PythonMySQL* para probar su utilización.

## Modelo Vista Controlador (MVC) con Flask
El Modelo Vista Controlador (MVC) es una estructura de programación que permite separar el modelo de la vista y el controlador. Esto es sumamente útil para ahorrar código y mejorar la legibilidad del mismo. En Flask, el modelo es una biblioteca de Python que permite interactuar con la base de datos. La vista es una plantilla de HTML que se utiliza para mostrar los datos en pantalla. El controlador es una biblioteca de Python que permite interactuar con la vista y el modelo. Cada uno de estos componentes se ordena en una carpeta, en la que se encuentra el archivo principal del proyecto. El árbol de carpetas de un proyecto Flask usando MVC es el siguiente:

```console
+-- app
    |-- __init__.py
    |-- server.py
    +-- config
    +-- controllers
    +-- models
    +-- templates
    +-- static

```
donde cada uno de los elementos de la carpeta es una subcarpeta. Veremos un ejemplo de ello en la carpeta *2-FlaskMySQL*.
