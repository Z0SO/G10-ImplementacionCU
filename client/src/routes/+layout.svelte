
<script>
  import Navbar from '$lib/components/Navbar.svelte';
</script>

<Navbar />

<main>
  <slot></slot>
</main>

<style>
  main {
    padding: 1rem;
  }
</style>
