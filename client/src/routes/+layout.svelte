
<script>
  
  import Navbar from '../components/layout/Navbar.svelte';

</script>

<div 
  class=" sombra-div-nav-light dark:sombra-div-nav"
>
  <Navbar />
</div>

<main
>
  <slot></slot>
</main>

<style>
  .sombra-div-nav-light {
    box-shadow: 0 0px 20px 0px rgba(0, 0, 0, 0.2);
  }

  .sombra-div-nav {
    box-shadow: 0 4px 20px;
  }

</style>

