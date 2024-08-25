
# GRUPO 10 - Diseño de Sistemas

## Super Importante antes de empezar

Para agregar alguna colaboracion al proyec  debes seguir los siguientes pasos:

Siempre que vayas a trabajar en una nueva funcionalidad, debes crear una nueva rama con el nombre de la funcionalidad que vas a implementar, por ejemplo:

> suponiendo que tienes clonado el repositorio y estas en la rama `master`

```bash
git checkout -b <integrante>-<nombre_de_la_funcionalidad>
```
reemplazando `<integrante>` por tu nombre y `<nombre_de_la_funcionalidad>` por el nombre de la funcionalidad que vas a implementar.

ejemplo:

```bash
git checkout -b lautaro-pagina_de_turnos
```

Listo, ahora puedes empezar a trabajar en tu funcionalidad.

----


## Caso de Uso a implementar: Asignar Turno a Mecanico

##### Aca te dejo las rutas accesibles desde el backend

> Obviamente teniendo en cuenta que estas en http://localhost:8000

- Para registrar usuario (te dara un token) -> ``/accounts/api/register/``

- Para obtener un token -> ``/accounts/api/token/``

- Para refrescar el token -> ``/accounts/api/token/refresh/``

- Para ver el json de los mecanicos -> ``/api/mecanicos/``

- Para ver el json de los turnos -> ``/api/turnos/``

- para ver el json de los vehiculos -> ``/api/vehiculos/``


### Backend: Ejecutar el proyecto en Local

1. Clonar el repositorio


2. Crear un entorno virtual

- Para crear un entorno virtual en Windows, ejecute el siguiente comando:

```bash
python -m venv venv
```

Luego de crear el entorno virtual, actívelo con el siguiente comando:

```bash
venv\Scripts\activate
```

Una vez en el entorno virtual (debería ver el prefijo `(venv)` en la terminal), continúe con el paso 3.


3. Instalar las dependencias

- Para instalar las dependencias del proyecto deje un requeriments.txt en la carpeta raíz del proyecto, ejecute el siguiente comando:

```bash
pip install -r requirements.txt
```

4. Realizar las migraciones

- Para realizar las migraciones, ejecute el siguiente comando:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Ejecutar el proyecto

- Para ejecutar el proyecto, ejecute el siguiente comando:

```bash
python manage.py runserver
```

Luego ingresas a la URL que por lo general es el localhost:8000


### Frontend: Ejecutar el proyecto en Local

Si ya clonaste el repositorio y estas en la carpeta del proyecto, sigue los siguientes pasos:

dirigete a la carpeta `client`  con `cd client` y ejecutas el siguiente comando:

```bash
npm install
```

Luego de que termine de instalar las dependencias, ejecutas el siguiente comando:

```bash
npm run dev
```
