
## To-Do: Inicialización de un Backend en Django con un Frontend en Svelte

### 1. **Configuración del Proyecto Django**
   - [ ] Crear un entorno virtual para Python: `python -m venv venv`
   - [ ] Activar el entorno virtual:
     - En Windows: `venv\Scripts\activate`
     - En macOS/Linux: `source venv/bin/activate`
   - [ ] Instalar Django: `pip install django`
   - [ ] Crear un nuevo proyecto Django: `django-admin startproject myproject`
   - [ ] Crear una nueva aplicación Django: `python manage.py startapp myapp`
   - [ ] Configurar la base de datos en `settings.py` (por defecto, se usa SQLite)
   - [ ] Realizar migraciones iniciales: `python manage.py migrate`
   - [ ] Ejecutar el servidor de desarrollo para verificar la instalación: `python manage.py runserver`

### 2. **Configuración del Proyecto Svelte**
   - [ ] Asegurarse de tener Node.js y npm instalados en el sistema
   - [ ] Inicializar un nuevo proyecto Svelte: 
     ```bash
     npx degit sveltejs/template my-svelte-app
     cd my-svelte-app
     ```
   - [ ] Instalar las dependencias: `npm install`
   - [ ] Verificar que el proyecto funciona ejecutando el servidor de desarrollo: `npm run dev`

### 3. **Integración Django-Svelte**
   - [ ] Crear una carpeta `frontend` dentro del directorio del proyecto Django para alojar el proyecto Svelte
   - [ ] Mover el proyecto Svelte a esta carpeta `frontend`
   - [ ] Configurar el `settings.py` de Django para servir los archivos estáticos de Svelte:
     - Agregar `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'frontend/public')]`
   - [ ] Configurar `urls.py` para que Django sirva el frontend Svelte:
     - Crear una vista que sirva el `index.html` de Svelte desde la carpeta `frontend/public`
     - Mapear esta vista en `urls.py` como la ruta raíz (`/`)

### 4. **Construcción y Despliegue**
   - [ ] Configurar el proyecto Svelte para producción: `npm run build`
   - [ ] Verificar que los archivos estáticos generados por Svelte se sirvan correctamente por Django
   - [ ] Desplegar el backend de Django y el frontend de Svelte en el servidor de producción o servicio de hosting adecuado

### 5. **Mejoras y Personalización**
   - [ ] Configurar el manejo de rutas en Svelte usando `svelte-routing` o similar
   - [ ] Integrar Django Rest Framework (DRF) para manejar las API desde el backend
   - [ ] Configurar CORS en Django para permitir las solicitudes desde el frontend Svelte
   - [ ] Crear componentes en Svelte que consuman las APIs de Django

### 6. **Control de Versiones**
   - [ ] Inicializar un repositorio Git en el directorio del proyecto
   - [ ] Crear un `.gitignore` adecuado para excluir archivos innecesarios (ej. `venv/`, `node_modules/`, etc.)
   - [ ] Hacer un primer commit con la estructura básica del proyecto

### 7. **Documentación y Mantenimiento**
   - [ ] Documentar la estructura del proyecto y pasos para iniciar el entorno de desarrollo
   - [ ] Crear instrucciones claras para la configuración y despliegue en producción

Esto debería darte una guía clara para comenzar con la integración de un backend en Django y un frontend en Svelte.





