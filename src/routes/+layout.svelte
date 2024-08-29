
<script>  
  import Navbar from '../components/layout/Navbar.svelte';
</script>

<div class="bg-white dark:bg-gray-800 shadow-md">
  <Navbar />
</div>

<main class="p-4 max-w-7xl mx-auto">
  <slot></slot>
</main>
