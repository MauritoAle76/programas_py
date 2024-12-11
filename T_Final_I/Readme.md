# CRUD App en Python con SQLite

Esta es una aplicación de ejemplo en Python que utiliza SQLite para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una base de datos.

## Descripción

La aplicación permite gestionar un inventario de productos, proporcionando funciones para agregar nuevos productos, ver la lista de productos, actualizar información de los productos y eliminar productos existentes y sacar reportes de bajo stock.

La primera vez que se ejecuta genera una base de datos llamada `inventario.db` en el directorio actual. Si la base de datos ya existe, se conecta a ella directamente. La aplicación utiliza el módulo `sqlite3` para interactuar con la base de datos. 
Ademas crea la tabla `productos` si no existe. La tabla tiene los siguientes campos: `id`, `nombre`, `descripcion`, `precio`, `cantidad`, `minimo_stock`. 


## Comenzando 🚀

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### Pre-requisitos 📋

Qué necesitas para instalar el software:

- Python 3.x
- SQLite (incluido con Python)
- Librería `colorama` (para colores en la terminal)

### Instalación 🔧

1. Clona este repositorio en tu máquina local:

    git clone https://github.com/MauritoAle76/programas_py/tree/main/T_Final_I


### Instala las dependencias necesarias: 

pip install colorama

# Uso 🔧
Para iniciar la aplicación, ejecuta el archivo principal:

python main.py

### Funciones Principales ⚙️

Crear Producto: Permite agregar un nuevo producto al inventario. Se solicita el nombre, precio y cantidad del producto, como asi tambien el stock minimo

Leer Productos: Muestra todos los productos en el inventario. lo imprime por pantalla.

Actualizar Producto: Permite actualizar la información de un producto existente, la cantidad, el precio y el stock minimo.

Eliminar Producto: Permite eliminar un producto del inventario, llamando por el ID del producto.

Buscar por ID: permite buscar un producto por ID. 

Reporte de bajo Stock: Muestra los productos con stock menor a indicado en el campo minimo_stock de la base de datos.



# Construido con 🛠️

Python - El lenguaje de programación utilizado.

SQLite - Base de datos utilizada.

Colorama - Librería para colores en la terminal.


## Autores ✒️
Mauro Alesini - Trabajo Inicial para Talento TEch - 


## Agradecimientos 🎁

Agradecimientos especiales a todos los que contribuyeron al desarrollo de esta aplicación.

Talento tech
El Profe Juan Pablo Rigotti
La secre Augsutina Digiesi