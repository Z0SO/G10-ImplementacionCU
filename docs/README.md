
### 1. Estructura Básica de la Carpeta `client`

```
client/
├── public/
│   ├── index.html
│   └── global.css
├── src/
│   ├── api/
│   │   └── turnos.js
│   ├── components/
│   │   ├── TurnoList.svelte
│   │   ├── TurnoForm.svelte
│   │   └── Navbar.svelte
│   ├── routes/
│   │   ├── Home.svelte
│   │   └── Turnos.svelte
│   ├── store/
│   │   └── turnos.js
│   ├── App.svelte
│   └── main.js
├── package.json
└── svelte.config.js
```

### 2. Descripción de Cada Carpeta y Archivo

- **`public/`**: Archivos estáticos que se sirven directamente, como `index.html` y estilos globales (`global.css`).

- **`src/`**: Contiene el código fuente de tu aplicación.

  - **`api/`**: Aquí puedes definir los módulos que interactúan con tu API. Por ejemplo, `turnos.js` manejará todas las solicitudes relacionadas con los "turnos" (usando Axios).

  - **`components/`**: Aquí se ubican los componentes reutilizables de la interfaz. Algunos ejemplos son:
    - `TurnoList.svelte`: Componente que muestra la lista de turnos.
    - `TurnoForm.svelte`: Componente que maneja la creación y edición de turnos.
    - `Navbar.svelte`: Barra de navegación de la aplicación.

  - **`routes/`**: Componentes que representan diferentes páginas o rutas de la aplicación.
    - `Home.svelte`: La página principal.
    - `Turnos.svelte`: Página que muestra la lista de turnos y permite interactuar con ellos.

  - **`store/`**: Aquí se pueden definir los "stores" de Svelte para manejar el estado compartido. Por ejemplo, `turnos.js` puede manejar el estado global de los turnos (lista, selección, etc.).

  - **`App.svelte`**: El componente raíz de la aplicación.

  - **`main.js`**: El punto de entrada de la aplicación, donde se inicializa Svelte.
``
