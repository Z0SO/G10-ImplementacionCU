
<script>
  import { onMount } from 'svelte';

  let isOpen = false;
  let isDarkMode = false;

  function toggleSidebar() {
    isOpen = !isOpen;
  }

  function toggleTheme() {
    const htmlElement = document.documentElement;
    
    if (htmlElement.classList.contains('dark')) {
      htmlElement.classList.remove('dark');
      htmlElement.classList.add('light');
      localStorage.setItem('theme', 'light');
    } else {
      htmlElement.classList.add('dark');
      htmlElement.classList.remove('light');
      localStorage.setItem('theme', 'dark');
    }
    isDarkMode = !isDarkMode;
  }


  // cuando se monta el componente, esta funcion se encargara de verificar si el usuario tiene el tema oscuro activado
  onMount(() => {
    if (localStorage.getItem('theme') === 'dark' || 
        (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      isDarkMode = true;
      document.documentElement.classList.add('dark');
    } else {
      isDarkMode = false;
      document.documentElement.classList.remove('dark');
    }
  });
</script>

<style>
  .drawer {
    transition: transform 0.3s ease;
  }
  .drawer-open {
    transform: translateX(0);
  }
  .drawer-closed {
    transform: translateX(-100%);
  }





</style>

<!-- Sidebar -->
<div
  class={`fixed top-0 left-0 z-40 w-64 h-screen p-4 overflow-y-auto bg-white dark:bg-gray-800 drawer ${isOpen ? 'drawer-open' : 'drawer-closed'}`}
  tabindex="-1"
  aria-labelledby="drawer-navigation-label"
>
  <h5 id="drawer-navigation-label" class="text-base font-semibold text-gray-500 uppercase dark:text-gray-400">Menu</h5>
  <button
    type="button"
    on:click={toggleSidebar}
    aria-controls="drawer-navigation"
    class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 absolute top-2.5 right-2.5 inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
  >
    <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
      <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
    </svg>
    <span class="sr-only">Close menu</span>
  </button>
  <div class="py-4 overflow-y-auto">
    <ul class="space-y-2 font-medium">
      <li>
        <a href="/" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
          <svg class="w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 21">
            <path d="M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z"/>
            <path d="M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z"/>
          </svg>
          <span class="ml-3">Dashboard</span>
        </a>
      </li>
      <!-- Agregar más ítems del menú aquí -->
      <li>
        <button
          on:click={toggleTheme}
          class="w-full text-left p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
        >
          {isDarkMode ? 'Modo Claro' : 'Modo Oscuro'}
        </button>
      </li>
    </ul>
  </div>
</div>

<!-- Navbar -->
<nav class="border-gray-400 bg-gray-200 dark:bg-gray-800 dark:border-gray-700 mb-20">
  <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
    <a href="/" class="flex items-center space-x-3 rtl:space-x-reverse">
      <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Sistema</span>
    </a>
    <div class="hidden w-full md:block md:w-auto" id="navbar-solid-bg">
      <ul class="flex flex-col font-medium mt-4 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-transparent dark:bg-gray-800 md:dark:bg-transparent dark:border-gray-700">
        <li>
          <a href="/" class="block py-2 px-3 md:p-0 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:dark:text-blue-500 dark:bg-blue-600 md:dark:bg-transparent" aria-current="page">Home</a>
        </li>
        <li>
          <a href="/turnos" class="block py-2 px-3 md:p-0 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">Turnos</a>
        </li>
      </ul>
    </div>
    <!-- Button to open the sidebar -->
    <button
      type="button"
      on:click={toggleSidebar}
      aria-controls="drawer-navigation"
      class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
    >
      <span class="sr-only">Open sidebar</span>
      <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 17 14">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 1h15M1 7h15M1 13h15"/>
      </svg>
    </button>
  </div>
</nav>
